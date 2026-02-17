from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog

class PDFEditor(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.label = QLabel("No PDF Loaded. Secure Kernel PDF Engine Active.")
        btn = QPushButton("Open PDF for Annotation")
        btn.clicked.connect(self.load_pdf)
        layout.addWidget(self.label)
        layout.addWidget(btn)

    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.label.setText(f"Editing: {os.path.basename(file_path)}")