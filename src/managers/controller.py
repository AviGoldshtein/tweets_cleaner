class Controller:
    def __init__(self, cleaner, data_analyzer, data_loader, file_path):
        self.file_path = file_path
        self.cleaner = cleaner
        self.data_analyzer = data_analyzer
        self.data_loader = data_loader

    def run(self):
        df = self.data_loader.load_data(self.file_path)
        self.data_analyzer.categorize_to_semitic(df)
        results = {}
        if not df.empty:
            tweet_amount_by_category = self.data_analyzer.tweet_amount_by_category(df)
            average_length_tweets = self.data_analyzer.get_average_length_tweets(df)
            three_longest_tweets_by_category = self.data_analyzer.three_longest_tweets_by_category(df)
            ten_most_common_words = self.data_analyzer.ten_most_common_words(df)
            uppercase_words_amount = self.data_analyzer.uppercase_words_amount(df)



            results.update(tweet_amount_by_category)
            results.update(average_length_tweets)
            results.update(three_longest_tweets_by_category)
            results.update(ten_most_common_words)
            results.update(uppercase_words_amount)

        print(results)