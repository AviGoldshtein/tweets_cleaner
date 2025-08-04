import pandas as pd

class DataCleaner:
    def __init__(self):
        pass

    def drop_unnecessary_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        remaining_columns = ['Biased', 'Text']
        columns_to_drop = []
        for column in df.columns:
            if column not in remaining_columns:
                columns_to_drop.append(column)
        return df.drop(columns=columns_to_drop)

    def remove_punctuation_marks(self, df: pd.DataFrame) -> pd.DataFrame:
        df['Text'] = df['Text'].apply(DataCleaner._replace_punctuation_and_dots_marks)
        return df

    @staticmethod
    def _replace_punctuation_and_dots_marks(text: str):
        text = text.replace(",", "")
        text = text.replace(".", "")
        return text