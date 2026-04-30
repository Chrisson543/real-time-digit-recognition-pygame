# Real-Time Digit Recognition

Draw a digit on the pixel grid and watch the model predict it in real time. Built with Pygame for the interface and a CNN trained on MNIST for the predictions.

---

## How it works

- 28x28 drawable grid maps directly to MNIST input format
- CNN runs inference every 500ms and displays the prediction live
- Press **C** to clear the grid

## Stack

- Python, Pygame
- PyTorch (CNN)
- MNIST dataset

## Run it

```bash
pip install pygame torch
python main.py
```

## Model

Two layer CNN — Conv2d → ReLU → MaxPool → Linear → output. Trained on the standard MNIST dataset.
