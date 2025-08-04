class Controller:
    def __init__(self, cleaner, data_analyzer, data_loader, file_path):
        self.file_path = file_path
        self.cleaner = cleaner
        self.data_analyzer = data_analyzer
        self.data_loader = data_loader

    def run(self):
        df = self.data_loader.load_data(self.file_path)
        results = {}
        if not df.empty:
            tweet_amount_by_category = self.data_analyzer.tweet_amount_by_category(df)
            results.update(tweet_amount_by_category)

        print(results)