from src.managers.controller import Controller
from src.core.data_cleaner import DataCleaner
from src.core.data_analyzer import DataAnalyzer
from src.core.data_loader import DataLoader

if __name__ == "__main__":
    data_cleaner = DataCleaner()
    data_analyzer = DataAnalyzer()
    data_loader = DataLoader()
    controller = Controller(data_cleaner, data_analyzer, data_loader)

    controller.run()
