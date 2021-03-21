from PySide2.QtWidgets import QWidget
from src.ui.spentEditor_ui import Ui_spentEditor

class SpentEditor(QWidget):
    def __init__(self, new_spent_function):
        super().__init__()
        self.ui = Ui_spentEditor()
        self.ui.setupUi(self)

        self.__new_spent_function = new_spent_function

        self.ui.btn_new.clicked.connect(self.new_spent)
        # TODO: mudar tela para ter um resumo de gastos?

    def new_spent(self):
        self.__new_spent_function()
   