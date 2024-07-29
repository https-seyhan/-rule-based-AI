import vaex

# Load large datasets
df1 = vaex.open('large_file1.hdf5')
df2 = vaex.open('large_file2.hdf5')

# Perform the merge
merged_df = df1.join(df2, on='key')

# Save the result
merged_df.export('merged_file.hdf5')
