import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QStatusBar
from PyQt6.QtGui import QIcon
from .editors.word_processor import WordProcessor
from .editors.spreadsheet import SpreadsheetEditor
from .editors.pdf_viewer import PDFEditor

class ForgeOfficeMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LinuxForge Productivity Suite - Military-Grade Precision")
        self.resize(1200, 800)
        
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Initialize Modules
        self.word_tab = WordProcessor()
        self.sheet_tab = SpreadsheetEditor()
        self.pdf_tab = PDFEditor()
        
        self.tabs.addTab(self.word_tab, "Word Processor")
        self.tabs.addTab(self.sheet_tab, "Spreadsheet")
        self.tabs.addTab(self.pdf_tab, "PDF / Annotations")
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("System Ready - Offline Priority Mode Enforced")

    def closeEvent(self, event):
        # Autosave logic
        self.word_tab.autosave()
        event.accept()