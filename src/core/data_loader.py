import pandas as pd
import os

class DataLoader:
    def __init__(self):
        pass

    def load_data(self, path: str) -> pd.DataFrame | None:
        if os.path.exists(path):
            return pd.read_csv(path)
        return None
