class DataAnalyzer:
    def __init__(self):
        pass

    def tweet_amount_by_category(self, df) -> dict:
        amounts = {"total_tweets": {}}
        value_counts = df.value_counts("Biased")
        for category in value_counts.index:
            if category == 0:
                amounts['total_tweets']['non_antisemitic'] = value_counts[category]
            elif category == 1:
                amounts['total_tweets']['antisemitic'] = value_counts[category]
        return amounts