import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("materials.csv")
X = df.drop("name", axis=1)
scaler = StandardScaler().fit(X)
X_scaled = scaler.transform(X)
