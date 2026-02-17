from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class SpreadsheetEditor(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.table = QTableWidget(50, 26)
        
        # Initialize Column Headers A-Z
        headers = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.table.setHorizontalHeaderLabels(headers)
        
        layout.addWidget(self.table)