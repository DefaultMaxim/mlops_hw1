import hydra
from omegaconf import DictConfig
import pytorch_lightning as pl
from datamodule import CustomDataModule
from model import SimpleModel
import os

@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig):
    # Инициализируем модель
    model = SimpleModel(input_dim=cfg.model.input_dim, lr=cfg.model.lr)
    
    # Инициализируем DataModule
    dm = CustomDataModule(train_data=cfg.data.train_data, val_data=cfg.data.val_data, batch_size=cfg.data.batch_size)
    dm.setup()

    # Инициализируем трейнер
    trainer = pl.Trainer(
    max_epochs=cfg.trainer.max_epochs,
    accelerator=cfg.trainer.accelerator,  # Замените gpus на accelerator
    devices=cfg.trainer.devices           # Укажите devices вместо gpus
)


    # Запускаем обучение
    trainer.fit(model, dm)

if __name__ == "__main__":
    main()
