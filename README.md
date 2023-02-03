# Dockerize python application to generate Newick tree using FlaskAPI


## Hierarchical Clustering 
**Hierarchical Clustering** is an unsupervised clustering algorithm which involves creating clusters that have predominant ordering from top to bottom. The endpoint is a set of clusters or groups, where each cluster is distinct from each other cluster, and the objects within each cluster are broadly similar to each other. 
**Agglomerative clustering** is a type of hierarchical clustering which follows a bottom up approach where each observation starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy. 
A **dendrogram** is a type of tree diagram showing hierarchical relationships between different sets of data. Just by looking at a dendrogram one is able to visualise how a cluster is formed. 
Hierarchical clustering can be used to generate phylogenetic trees. **Phylogenetic trees** represent the evolutionary relationships among organisms and can be used to trace the origin of pathogens.

## Hierarchical_Clustering.ipynb

Modules and Libraries used
For data pre-processing: Pandas, Numpy

For building the model: ScikitLearn

For data visualization: Matplotlib

This notebook shows the clustering on Immunotherapy dataset for binary classification with visualisations using dendrogram and radial tree. Also included is dendrogram_highlight which displays highlighted clusters at the leaf level.


To visualize the dendrogram along with the labels for each instance:
```
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 7))  
plt.title("Dendrograms")  
dend = shc.dendrogram(shc.linkage(df1, method='ward'), labels = df.index)
```

## Newick File
Newick is a standard format for representing tree-like structures in computational biology and phylogenetics. In a Newick tree, each node is represented by a set of nested parentheses, with branch lengths appearing between the parentheses and node labels following the closing parenthesis.
[output.txt](https://github.com/n9mr9t9/python-flask-docker/blob/main/output.txt) represents the newick tree output. This can be visualized further as a phylogentic tree using [iTOL](https://itol.embl.de/)

## Docker
Docker is a platform that enables developers to easily create, deploy, and run applications by using containers. Containers are isolated environments that package an application and its dependencies together, making it easier to manage and deploy.

Build the container image:
```
docker build -t phylo . 
```

where 'phylo' is the name of the image

Starting the docker container:
```
docker run -p 5000:5000 phylo
```


index.html:

<img width="347" alt="image" src="https://user-images.githubusercontent.com/98946943/216527203-11fe0411-acd2-445e-9b2e-0694eca9ce74.png">

index2.html:

<img width="367" alt="image" src="https://user-images.githubusercontent.com/98946943/216527277-8e8223cf-76de-4b52-9d3a-c8787bb33fb6.png">

visualizing the radial tree using output.txt on iTOL:

<img width="365" alt="image" src="https://user-images.githubusercontent.com/98946943/216527565-0648e04d-35e5-46a1-8325-782946b576ae.png">


