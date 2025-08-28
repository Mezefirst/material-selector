import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load material data
df = pd.read_csv("materials.csv")

# Drop the 'Material' column to get feature matrix X
X = df.drop("Material", axis=1)

# Fit the scaler on features
scaler = StandardScaler().fit(X)
X_scaled = scaler.transform(X)
