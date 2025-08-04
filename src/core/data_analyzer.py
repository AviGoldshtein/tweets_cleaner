class DataAnalyzer:
    def __init__(self):
        pass

    def tweet_amount_by_category(self, df) -> dict:
        amounts = {"total_tweets": {"total": 0}}
        value_counts = df.value_counts("semitic_category")
        for category in value_counts.index:
            amount_of_category = value_counts[category]
            amounts['total_tweets'][category] = amount_of_category
            amounts['total_tweets']['total'] += amount_of_category
        return amounts

    def categorize_to_semitic(self, df):
        df['semitic_category'] = df['Biased'].map(lambda x: "antisemitic" if x == 1 else "non_antisemitic").astype("category")
        return df
