import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
 
data = fetch_california_housing(as_frame=True)
df = data.frame

print(df.head())        
print(df.describe())    

features = ["MedInc", "HouseAge", "AveRooms", "MedHouseVal"]
df_selected = df[features]

df_selected.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df["MedInc"], df["MedHouseVal"])
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Income vs House Value")
plt.show()

plt.figure()
plt.scatter(df["AveRooms"], df["MedHouseVal"])
plt.xlabel("Average Rooms")
plt.ylabel("Median House Value")
plt.title("Correlation: Rooms vs House Value")
plt.savefig("correlation.png")  
plt.show()
