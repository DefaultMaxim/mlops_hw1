import hydra
from omegaconf import DictConfig
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger
from datamodule import CustomDataModule
from model import SimpleModel

@hydra.main(version_base=None, config_path="configs", config_name="config")
def main(cfg: DictConfig):
    # Инициализируем TensorBoard Logger
    logger = TensorBoardLogger(
        save_dir="logs",               # Каталог для сохранения логов
        name="training_logs",          # Имя подкаталога для конкретного запуска
        log_graph=True                 # Логирование графа модели (опционально)
    )

    # Инициализируем модель
    model = SimpleModel(input_dim=cfg.model.input_dim, lr=cfg.model.lr)
    
    # Инициализируем DataModule
    dm = CustomDataModule(
        train_data=cfg.data.train_data, 
        val_data=cfg.data.val_data, 
        batch_size=cfg.data.batch_size
    )
    dm.setup()

    # Инициализируем трейнер с TensorBoard Logger
    trainer = pl.Trainer(
        max_epochs=cfg.trainer.max_epochs,
        accelerator=cfg.trainer.accelerator,  # Используем accelerator
        devices=cfg.trainer.devices,         # Используем devices
        logger=logger,                       # Добавляем TensorBoard Logger
        log_every_n_steps=1                  # Логировать на каждом шаге (можно настроить)
    )

    # Запускаем обучение
    trainer.fit(model, dm)

if __name__ == "__main__":
    main()
