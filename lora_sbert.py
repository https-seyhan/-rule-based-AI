pip install transformers sentence-transformers peft torch

data = [
    {"sentence1": "Text A", "sentence2": "Text B", "label": 1},
    {"sentence1": "Text C", "sentence2": "Text D", "label": 0},
    ...
]
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
from peft import LoraConfig, get_peft_model
import torch

# Define the LoRA configuration
lora_config = LoraConfig(
    r=8,          # Low-rank dimension
    lora_alpha=16,  # LoRA scaling factor
    lora_dropout=0.1,  # Dropout for regularization
    target_modules=["transformer.h.11.mlp"],  # Layers to apply LoRA
    bias="none"
)

# Wrap the model with LoRA configuration
model = get_peft_model(model, lora_config)
from sentence_transformers import InputExample
from torch.utils.data import DataLoader

# Convert data into InputExample format
train_samples = [InputExample(texts=[d["sentence1"], d["sentence2"]], label=d["label"]) for d in data]

# Create a DataLoader for batching
train_dataloader = DataLoader(train_samples, shuffle=True, batch_size=16)
from sentence_transformers import losses

# Using Binary Cross-Entropy Loss for binary classification
train_loss = losses.SoftmaxLoss(model=model, sentence_embedding_dimension=model.get_sentence_embedding_dimension(), num_labels=2)
num_epochs = 3
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=num_epochs,
    warmup_steps=100,
    output_path="output/lora-sbert"
)
model.save("output/lora-sbert")

