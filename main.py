import sys
from PyQt6.QtWidgets import QApplication
from forge_office.core.engine import ForgeOfficeMain

def main():
    # Security Check: Standard User Compliance
    app = QApplication(sys.argv)
    app.setApplicationName("LinuxForge Office")
    window = ForgeOfficeMain()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()