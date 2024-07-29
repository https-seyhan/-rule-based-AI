import dask.dataframe as dd

# Read data into a Dask DataFrame
ddf = dd.read_csv('large_file.csv')

# Perform merge operation
merged_ddf = ddf.merge(ddf2, on='key')

# Compute the result
result = merged_ddf.compute()
