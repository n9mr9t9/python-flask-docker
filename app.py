import pandas as pd
from joblib import load
from flask import Flask, request,render_template, session, send_file, Response
import os
from werkzeug.utils import secure_filename
from fastcluster import linkage
from scipy.cluster.hierarchy import to_tree, ClusterNode
from typing import List
from io import BytesIO


UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'csv'}

flask_app = Flask(__name__)
flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
flask_app.config['SECRET_KEY'] = 'the random string'

@flask_app.route('/')
def home():
    return render_template('index.html')


@flask_app.route('/',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # Upload file flask
        uploaded_file = request.files['file']
        if not uploaded_file:
            return "No file selected"
        # Extracting uploaded data file name
        filename = secure_filename(uploaded_file.filename)
        # Upload file to database (defined uploaded folder in static path)
        uploaded_file.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], filename))
        # Storing uploaded file path in flask session
        session['uploaded_file_path'] = os.path.join(flask_app.config['UPLOAD_FOLDER'], filename)

        return render_template('index2.html')

@flask_app.route('/result')
def result():
    file_path = session.get('uploaded_file_path', None)
    df_test=pd.read_csv(file_path)
    df_test = df_test.set_index('ID')
    df_test.drop(['Result_of_Treatment'], axis=1)
    Z = linkage(df_test, method="complete")
    T = to_tree(Z, rd=False)
    def _scipy_tree_to_newick_list(node: ClusterNode, newick: List[str], parentdist: float, leaf_names: List[str]) -> List[str]:
        if node.is_leaf():
            return newick + [f'{leaf_names[node.id]}:{parentdist - node.dist}']

        if len(newick) > 0:
            newick.append(f'):{parentdist - node.dist}')
        else:
            newick.append(');')
        newick = _scipy_tree_to_newick_list(node.get_left(), newick, node.dist, leaf_names)
        newick.append(',')
        newick = _scipy_tree_to_newick_list(node.get_right(), newick, node.dist, leaf_names)
        newick.append('(')
        return newick

    def to_newick(tree: ClusterNode, leaf_names: List[str]) -> str:
        newick_list = _scipy_tree_to_newick_list(tree, [], tree.dist, leaf_names)
        return ''.join(newick_list[::-1])

    newick_file = to_newick(T, df_test.index)

    response = Response(newick_file, content_type="text/plain")
    response.headers["Content-Disposition"] = "attachment; filename=output.txt"
    return response

if __name__=='__main__':
    flask_app.run(host='0.0.0.0')
