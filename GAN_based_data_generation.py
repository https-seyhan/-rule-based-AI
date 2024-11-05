from sdv.tabular import GaussianCopula

# Train a synthetic data generator model
model = GaussianCopula()
model.fit(df)  # Train on your original dataset

# Generate synthetic data
synthetic_df = model.sample(num_rows=100)

# Display the synthetic data
print(synthetic_df.head())

