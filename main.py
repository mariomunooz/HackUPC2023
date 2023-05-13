import pandas as pd
# set the max_columns option to None
pd.options.display.max_columns = None

df = pd.read_json('data/hackupc2023_restbai__dataset_sample.json')

df = df.transpose()

print(df.head(2))
