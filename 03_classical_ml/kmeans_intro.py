import pandas as pd 
from sklearn.cluster import KMeans

data = {
    'owns_car': [1,1,1,1,0,0,0,0],
    'high_credit': [1,1,0,0,1,1,0,0]
}
df = pd.DataFrame(data)

model = KMeans(n_clusters= 2, random_state= 42, n_init= 10)
model.fit(df)

labels = model.labels_
print("Cluster labels: ", labels)
print("Cluster centers:\n", model.cluster_centers_)