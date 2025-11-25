"""
Train a simple binary classifier using PyTorch.
This script demonstrates model definition, device handling,
a proper training loop, and clean code structure.
"""

import torch
import torch.nn as nn
import torch.optim as optim


class SimpleClassifier(nn.Module):
    """A small neural network for binary classification."""

    def __init__(self) -> None:
        super().__init__()
        self.layer1 = nn.Linear(3, 50)
        self.layer2 = nn.Linear(50, 1)
        self.activation = nn.ReLU()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.activation(self.layer1(x))
        return torch.sigmoid(self.layer2(x))


def train_model() -> None:
    """Create data, train a model, and print predictions."""

    # ---------------------------
    # Device setup
    # ---------------------------
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # ---------------------------
    # Fake dataset
    # ---------------------------
    data = torch.randn(100, 3).to(device)
    labels = torch.randint(0, 2, (100,)).float().unsqueeze(1).to(device)

    # ---------------------------
    # Model, optimizer, loss
    # ---------------------------
    model = SimpleClassifier().to(device)
    optimizer = optim.SGD(model.parameters(), lr=0.1)
    loss_fn = nn.BCELoss()

    model.train()
    epochs = 5

    for epoch in range(epochs):
        optimizer.zero_grad()

        outputs = model(data)
        loss = loss_fn(outputs, labels)

        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item():.4f}")

    # ---------------------------
    # Evaluation
    # ---------------------------
    model.eval()
    with torch.no_grad():
        predictions = model(data)[:10]

    print("\nFirst 10 predictions:")
    print(predictions)


if __name__ == "__main__":
    train_model()
