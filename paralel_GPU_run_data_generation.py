import deepspeed
import torch
from torch.utils.data import DataLoader, Dataset
from ctgan import CTGAN
import pandas as pd
import os

# Load your existing dataset and define categories
df = pd.read_csv("your_dataset.csv")
categorical_columns = ['task_code', 'actv_code_name', 'wbs_name', 'PH_phase', 'DI_discipline', 'ME_method']

# Define custom dataset loader for DataLoader
class TabularDataset(Dataset):
    def __init__(self, dataframe):
        self.data = dataframe
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data.iloc[index]

# Initialize distributed model
def setup_deepspeed_ctgan():
    model = CTGAN()
    model.to(torch.device("cuda"))  # Ensure model on GPU
    return model

# Training function with DeepSpeed
def train_ctgan_distributed(model, train_loader, config):
    model, optimizer, _, _ = deepspeed.initialize(config=config, model=model)
    model.train()
    
    for epoch in range(config['training']['epochs']):
        for data in train_loader:
            # Your training step with CTGAN - replace with specific CTGAN usage if needed
            model.fit(data)  # CTGAN fit on mini-batches
        
        print(f"Epoch {epoch + 1}/{config['training']['epochs']} complete.")
    
    # Save or use model for synthetic data generation
    synthetic_data = model.sample(len(df))
    return synthetic_data

# DeepSpeed configuration
ds_config = {
    "train_micro_batch_size_per_gpu": 4,  # Adjust per GPU capacity
    "gradient_accumulation_steps": 2,
    "optimizer": {
        "type": "Adam",
        "params": {
            "lr": 0.001,
            "weight_decay": 1e-5
        }
    },
    "fp16": {
        "enabled": True
    },
    "training": {
        "epochs": 10
    }
}

# DataLoader for distributed training
train_data = TabularDataset(df)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True, num_workers=4)

# Set up distributed CTGAN and start training
if __name__ == "__main__":
    deepspeed.init_distributed()  # Initialize distributed processing with DeepSpeed
    model = setup_deepspeed_ctgan()
    synthetic_data = train_ctgan_distributed(model, train_loader, ds_config)

    # Save synthetic data to CSV
    synthetic_data.to_csv("synthetic_data.csv", index=False)
    print("Synthetic data generated and saved.")

