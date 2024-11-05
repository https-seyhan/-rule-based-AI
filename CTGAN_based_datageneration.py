import pandas as pd
from ctgan import CTGAN

# Load your existing dataset
# Replace 'your_dataset.csv' with your dataset file path
df_original = pd.read_csv('your_dataset.csv')

# Inspect the dataset and set categorical and continuous columns
# Define which columns are categorical
categorical_columns = ['task_code', 'actv_code_name', 'wbs_name', 'PH_phase', 'DI_discipline', 'ME_method']

# Train a CTGAN model on the original dataset
ctgan = CTGAN()
ctgan.fit(df_original, discrete_columns=categorical_columns)

# Generate synthetic data with the same number of rows as the original dataset
num_samples = len(df_original)
df_synthetic = ctgan.sample(num_samples)

# Display a sample of the synthetic data
print(df_synthetic.head())

