import pytorch_lightning as pl
from torch.utils.data import DataLoader
from dataset import CustomDataset

class CustomDataModule(pl.LightningDataModule):
    def __init__(self, train_data, val_data, batch_size: int):
        super().__init__()
        self.train_data = train_data
        self.val_data = val_data
        self.batch_size = batch_size

    def setup(self, stage=None):
        self.train_dataset = CustomDataset(self.train_data)
        self.val_dataset = CustomDataset(self.val_data)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)
    
    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)
