import pandas as pd
import os
import json

class DataLoader:
    def __init__(self):
        pass

    def load_data(self, path: str) -> pd.DataFrame | None:
        if os.path.exists(path):
            return pd.read_csv(path)
        return None

    def dump_to_json(self, path: str, data: dict) -> None:
        with open(path, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def dump_to_csv(self, path: str, data: pd.DataFrame) -> None:
        print(data.head())
        data.to_csv(path)