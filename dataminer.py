import numpy as np # linear algebra
import pandas as pd # data processing, for CSV
import random as rd
import matplotlib.pyplot as plt
from math import sqrt       
    
data = pd.read_csv("superbowl.csv")
data.head()

winnerInfo = data["Winner Dist"]
loserInfo = data["Loser Dist"]
pointDiff = data["Winner Pts"] - data["Loser Pts"]

# Visualize data point
plt.scatter(winnerInfo, pointDiff, c="blue")
plt.scatter(loserInfo, pointDiff, c="green")
plt.ylabel("Point Differential")
plt.xlabel("Distance")
plt.legend(['Winner', 'Loser'])
plt.show()

# number of centriod
K=2

items = data["Loser Dist"].tolist()
for i in data["Winner Dist"]:
    items.append(i)

pointDiff = pointDiff.tolist()
pointDiff = pointDiff + pointDiff

d = {"pointDiff" : pointDiff, "distance" : items}
data2 = pd.DataFrame(data = d)

print(data2)


# select random observation as a centriod 
Centroids = (data2.sample(n=K))
print(Centroids)
#Centroids2 = (Y.sample(n=K))
plt.scatter(data2["distance"], data2["pointDiff"], c="blue")
plt.scatter(Centroids["distance"], Centroids["pointDiff"], c="red")

#plt.scatter(Y["Loser Pts"], Y["Loser Dist"], c="green")
#plt.scatter(Centroids2["Loser Pts"], Centroids2["Loser Dist"], c="purple")

plt.xlabel("Distance")
plt.ylabel("Points")
plt.show()

diff = 1
j=0

# k-Means Clustering
while(diff!=0):
    XD=data2
    i=1
    for index1, row_c in Centroids.iterrows():
        ED=[]
        for index2, row_d in XD.iterrows():
            d1 = (row_c["pointDiff"]-row_d["pointDiff"])**2
            d2 = (row_c["distance"]-row_d["distance"])**2
            d = sqrt(d1+d2)
            ED.append(d)
        data2[i] = ED
        i = i+1
    
    C = []
    for index, row in data2.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos = i+1
        C.append(pos)
    data2["Cluster"]=C
    Centroids_new = data2.groupby(["Cluster"]).mean()[["distance", "pointDiff"]]
    if j == 0:
        diff = 1
        j = j+1
    else:
        diff = (Centroids_new['distance'] - Centroids['distance']).sum() + (Centroids_new['pointDiff'] - Centroids['pointDiff']).sum()
        print(diff.sum())
    Centroids = data2.groupby(["Cluster"]).mean()[["distance","pointDiff"]]
 
color=['purple','green','blue']
for k in range(K):
    print(k)
    data=data2[data2["Cluster"]==k+1]
    plt.scatter(data["distance"],data["pointDiff"],c=color[k])

#Visualize Clustered Data
plt.scatter(Centroids["distance"],Centroids["pointDiff"],c='red')
plt.ylabel('Point Differential')
plt.xlabel('Distance')
plt.legend(['Clustering Group A', 'Clustering Group B', 'Centroids'])
plt.show()
