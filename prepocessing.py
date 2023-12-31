import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Import dataset
dataset = pd.read_csv('dataset.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# Menghilangkan missing value NaN
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

# Encoding data kategori (Atribut)
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# Encoding data kategori (class)
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

# membagi dataset ke dalam training set dan test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train)

print(X_test)

print(y_train)
print(y_test)

# Feature Scaling
sc = StandardScaler()
X_train[:, 1:] = sc.fit_transform(X_train[:, 1:]) 
X_test[:, 1:] = sc.fit_transform(X_test[:, 1:]) 

print(X_train)
print(X_test)