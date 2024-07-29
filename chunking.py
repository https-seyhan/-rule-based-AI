import pandas as pd

# Define chunk size
chunk_size = 100000  # Adjust based on your system's memory

# Read and process data in chunks
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Perform necessary processing on each chunk
    chunks.append(chunk)

# Concatenate all chunks after processing
df = pd.concat(chunks)
