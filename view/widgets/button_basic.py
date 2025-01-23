from PySide6.QtWidgets import QPushButton


class ButtonBasic(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                font-family: Outfit;
                font-size: 18px;
                font-weight: bold;
                color: #FFFFFF;
                background-color: #815B5B; 
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: #A67878;
            }
            QPushButton:pressed {
                background-color: #5A3D3D; 
            }
        """)
