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

    def get_average_length_tweets(self, df) -> dict:
        total = df['Text'].map(lambda x: len(x.split())).mean()

        mask = df['semitic_category'] == "antisemitic"
        antisemitic = df[mask]['Text'].map(lambda x: len(x.split())).mean()

        mask = df['semitic_category'] == "non_antisemitic"
        non_antisemitic = df[mask]['Text'].map(lambda x: len(x.split())).mean()

        average_lengths = {
            "average_length": {
                "total": total,
                "antisemitic": antisemitic,
                "non_antisemitic": non_antisemitic
            }
        }
        return average_lengths

    def three_longest_tweets_by_category(self, df) -> dict:
        df['count_chars_of_text'] = df['Text'].map(lambda x: len(x))
        df = df.sort_values(by=['count_chars_of_text'], ascending=False)

        three_longest_tweets_for_category = {"longest_3_tweets": {}}
        for category in df['semitic_category'].unique():
            df_with_category = df[df["semitic_category"] == category]
            three_longest_tweets = list(df_with_category['Text'].head(3))
            three_longest_tweets_for_category['longest_3_tweets'][category] = three_longest_tweets

        return three_longest_tweets_for_category

    def ten_most_common_words(self, df) -> dict:
        pass

    def uppercase_words_amount(self, df) -> dict:
        pass