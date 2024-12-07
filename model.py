import torch
import pytorch_lightning as pl
from torch import nn

class SimpleModel(pl.LightningModule):
    def __init__(self, input_dim: int, lr: float):
        super().__init__()
        self.save_hyperparameters()
        self.layer = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.layer(x).squeeze(-1)

    def training_step(self, batch, batch_idx):
        y_pred = self(batch)
        # Предположим, что у нас задача предсказания среднего (просто пример)
        y_true = torch.zeros_like(y_pred)
        loss = torch.mean((y_pred - y_true)**2)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        y_pred = self(batch)
        y_true = torch.zeros_like(y_pred)
        loss = torch.mean((y_pred - y_true)**2)
        self.log("val_loss", loss)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.hparams.lr)
