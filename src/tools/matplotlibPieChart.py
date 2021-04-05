import matplotlib.pyplot as plt
from matplotlib import use
use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from src.dao.spentcategory import SpentCategory


class CategoryPieChart(FigureCanvas):
    def __init__(self, categories : list, parent):
        fig, self.ax = plt.subplots(figsize=(2, 2))
        super().__init__(fig)
        self.setParent(parent)

        self.labels = []
        for category in categories:
            self.labels.append(category.name)
        
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    def plot(self, spent_values_list : list):
        self.ax.pie(spent_values_list, labels=self.labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
