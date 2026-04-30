import torch
from torch import nn
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader


class CNN(nn.Module):
    def __init__(self, conv_layers:  torch.nn.modules.container.Sequential, dense_layers:  torch.nn.modules.container.Sequential):
        super().__init__()

        self.conv_layers = conv_layers
        self.dense_layers = dense_layers

    def forward(self, X):
        X = self.conv_layers(X)
        X = X.flatten(start_dim=1)
        return self.dense_layers(X)

    def predict(self, X):
        self.eval()
        return self(X)

    def train_network(self, X, y, epochs, loss_fn, optimizer):
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5)

        train_dataset = TensorDataset(X_train, y_train)
        val_dataset = TensorDataset(X_val, y_val)

        train_loader = DataLoader(train_dataset, shuffle=True, batch_size=64)
        val_loader = DataLoader(val_dataset, batch_size=64)

        for epoch in range(epochs):
            self.train()

            for X_batch, y_batch in train_loader:
                optimizer.zero_grad()

                output = self(X_batch)
                loss = loss_fn(output, y_batch)
                loss.backward()
                optimizer.step()
            self.eval()

            with torch.no_grad():
                val_loss = sum(loss_fn(self(X_b), y_b).item() for X_b, y_b in val_loader) / len(val_loader)
                train_loss = sum(loss_fn(self(X_b), y_b).item() for X_b, y_b in train_loader) / len(train_loader)

            print(f"Epoch {epoch + 1}/{epochs} | Train Loss: {train_loss:.6f} | Val Loss: {val_loss:.6f}")
        self.evaluate(X_test, y_test)

    def evaluate(self, X, y):
        self.eval()

        with torch.no_grad():
            pred = self(X)
            accuracy = torch.mean((torch.argmax(pred, dim=1) == y).float()) * 100

            print(f"Accuracy: {accuracy:.2f}%")

    def save(self, path: str):
        torch.save(self.state_dict(), path)

    def load(self, path: str, is_eval: bool):
        self.load_state_dict(torch.load(path))

        if is_eval:
            self.eval()

