import matplotlib.pyplot as plt
from matplotlib import use
use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from src.dao.spentcategory import SpentCategory


class CategoryPieChart(FigureCanvas):
    def __init__(self, categories : list, parent):
        self.fig, self.ax = plt.subplots(figsize=(2, 2))
        super().__init__(self.fig)
        self.setParent(parent)

        self.labels = []
        for category in categories:
            self.labels.append(category.name)
        
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    def plot(self, spent_values_list : list):
        # just plot values larger than zero:
        spent_values_larger_than_zero = []
        spent_categories_labels_larger_than_zero = []
        for i, value in enumerate(spent_values_list):
            if value > 0:
                spent_values_larger_than_zero.append(spent_values_list[i])
                spent_categories_labels_larger_than_zero.append(self.labels[i])

        self.ax.clear()
        if (len(spent_values_larger_than_zero) > 0): #tirar esse if? o fundo fica branco, porém da msg de erro
            self.ax.pie(spent_values_larger_than_zero, labels=spent_categories_labels_larger_than_zero, 
                        autopct='%1.1f%%', shadow=True, startangle=90)
            self.fig.canvas.draw()
