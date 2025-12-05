import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score


df = pd.read_csv('combind.csv')

print(df.head())