import matplotlib.pyplot as plt
from matplotlib import use
use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from src.dao.spentcategory import SpentCategory


class CategoryPieChart(FigureCanvas):
    def __init__(self, categories : list, parent, title = ""):
        self.fig, self.ax = plt.subplots(figsize=(2, 2))
        super().__init__(self.fig)
        self.setParent(parent)

        self.labels = []
        for category in categories:
            self.labels.append(category.name)
        
        self.title = title
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        if title != "":
            self.ax.set_title(title)

    def plot(self, spent_values_list : list, show_absolute_value = False):
        # just plot values larger than zero:
        spent_values_larger_than_zero = []
        spent_categories_labels_larger_than_zero = []
        for i, value in enumerate(spent_values_list):
            if value > 0:
                spent_values_larger_than_zero.append(spent_values_list[i])
                spent_categories_labels_larger_than_zero.append(self.labels[i])

        self.ax.clear()
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        if self.title != "":
            self.ax.set_title(self.title)

        if (len(spent_values_larger_than_zero) > 0): #tirar esse if? o fundo fica branco, porém da msg de erro
            if show_absolute_value:
                self.ax.pie(spent_values_larger_than_zero, labels=spent_categories_labels_larger_than_zero, 
                        autopct=self.__make_autopct(spent_values_larger_than_zero), shadow=True, startangle=90)
            else:
                self.ax.pie(spent_values_larger_than_zero, labels=spent_categories_labels_larger_than_zero, 
                        autopct='%1.1f%%', shadow=True, startangle=90)
            self.fig.canvas.draw()

    def update_category_labels(self, labels_list):
        self.labels = labels_list

    def update_title(self, title):
        self.title = title

    def __make_autopct(self, values):
        """Show absolute value in chart"""
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{v:d}  ({p:.2f}%)'.format(p=pct,v=val)
        return my_autopct
        