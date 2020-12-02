import pandas as pd

synthetic = pd.read_csv('synthetic.txt', sep="    ", header=None)
synthetic.columns = ["a", "b"]

thyroid = pd.read_csv('thyroid.txt', sep="   ", header=None)
thyroid.columns = ["a", "b",'c','d','e']

thyroid