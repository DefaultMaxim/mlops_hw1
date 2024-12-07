import torch
from torch.utils.data import Dataset
import _vector_standardization  # биндинги из ДЗ-1

class CustomDataset(Dataset):
    def __init__(self, data):
        # data - список массивов или список чисел, заданный в конфиге
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        vector = self.data[idx]
        # Предполагаем, что vector - это обычный список чисел.
        # Применяем C++ стандартизацию:
        standardized =_vector_standardization.standardize(vector)
        # Преобразуем в тензор
        return torch.tensor(standardized, dtype=torch.float32)
