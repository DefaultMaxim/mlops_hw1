# MLops Homework 1, 2: Python bindings, Python packaging, Docker, Hydra, DVC, Lightning

## Описание

Этот проект является результатом выполнения домашнего задания по курсу MLops. Основной целью является интеграция Python bindings, Python packaging, Docker Hydra, DVC и PyTorch Lightning для построения и автоматизации цикла обучения. Проект состоит из:
- Python модуля с C++ биндингами (`_vector_standardization`).
- PyTorch Lightning DataModule и модели, использующей биндинги для стандартизации данных.
- Конфигурационного управления с помощью Hydra.
- Трекинга данных и артефактов с использованием DVC.

## Структура проекта
```
mlops/
  ├─ src/
  │   ├─ VectorStandardization.cpp
  │   ├─ VectorStandardization.h
  │   ├─ bindings.cpp
  ├─ configs/
  │   ├─ config.yaml
  │   ├─ model/
  │   │   └─ model.yaml
  │   ├─ data/
  │   │   └─ data.yaml
  │   ├─ trainer/
  │   │   └─ trainer.yaml
  ├─ data/
      ├─ .gitignore
      ├─ raw_data.csv.dvc
  ├─ Makefile
  ├─ Dockerfile
  ├─ pyproject.toml
  ├─ setup.py
  ├─ test.py
  ├─ test.ipynb
  ├─ dataset.py
  ├─ datamodule.py
  ├─ model.py
  ├─ train.py
  ├─ dvc.yaml
  └─ README.md
```

### Основные компоненты

1. **C++ биндинги**  
   Используются для стандартизации входных данных. Метод `standardize` стандартизирует вектор чисел, возвращая значения с нулевым средним и стандартным отклонением 1.

2. **Hydra**  
   Управление конфигурацией проекта. Все параметры модели, данных, тренировки и логирования вынесены в yaml-файлы в директории `configs/`.

3. **PyTorch Lightning**  
   Модель и DataModule реализованы в `model.py` и `datamodule.py`. DataModule использует биндинги для предобработки данных.

4. **DVC**  
   Используется для трекинга данных и артефактов. Пример: трекинг исходного датасета.

## Установка

### 1. Установка Python окружения

1. Клонируйте репозиторий:
     ```bash
     git clone https://github.com/DefaultMaxim/mlops_hw1.git
     cd https://github.com/DefaultMaxim/mlops_hw1.git
     ```
2. Создайте виртуальное окружение и установите зависимости:
      ```python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      ```
3. Собирите модуль С++ с биндингами:
     ```python3 -m build
     pip install dist/vector_standardization-0.1-*.whl
     ```
   
## Инициализация DVC
1. Инициализируйте dvc:
     ```bash
     dvc init
     ```
2. Добавьте данные для трекинга:
    ```bash
    dvc add data/raw_data.csv
    git add data/raw_data.csv.dvc .dvc/ .dvcignore
    git commit -m "Add raw data to DVC"
    ```
3. Настройте remote для хранения данных:
    ```bash
    dvc remote add -d myremote s3://mybucket/path/to/storage
    dvc push
    ```
   
## Использование

### 1. Запуск обучения

Запустите train.py для обучения модели:
  ```bash
  python train.py
  ```
Hydra создаст рабочую директорию в outputs/<дата_и_время>, где будут сохранены конфиги и логи.

### 2. Изменение параметров
Для изменения параметров обучения используйте либо конфиги в configs/, либо командную строку. Пример:
  ```bash
  python train.py trainer.max_epochs=10 data.batch_size=32
  ```

### 3. Восстановление данных с помощью DVC
Для восстановления данных выполните:
  ```bash
  dvc pull
  ```

### 4. Проверка DVC статуса
Проверить статус трекаемых данных:
  ```bash
  dvc status
  ```

## Тестирование
1. Проверьте, что датасет возвращает стандартизированные данные:
   ```bash
   python -c "from dataset import CustomDataset; print(CustomDataset([[1.0,2.0,3.0]]).__getitem__(0))"
    ```
2. Запустите обучение и убедитесь, что (_train_loss_ и _val_loss_) логируются.
