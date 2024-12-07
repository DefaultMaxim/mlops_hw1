from dataset import CustomDataset
ds = CustomDataset([[1.0,2.0,3.0,4.0,5.0]])
sample = ds[0]
print("Sample from dataset:", sample)
