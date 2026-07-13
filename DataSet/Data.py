import panda as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("ajithdari/lung-cancer-genomic-and-clinical-dataset")

print("Path to dataset files:", path)