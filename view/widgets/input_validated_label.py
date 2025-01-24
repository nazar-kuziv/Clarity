from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QLineEdit


class InputValidatedLabel(QWidget):
    def __init__(self, label_text: str, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)
        self.label_text = QLabel(label_text)
        self.label_text.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #222222;
                font-size: 20px;
            }
        """)
        # noinspection PyUnresolvedReferences
        self.label_text.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.main_layout.addWidget(self.label_text)
        self.input = QLineEdit()
        font = self.input.font()
        font.setPointSize(16)
        self.input.setFont(font)
        # noinspection PyUnresolvedReferences
        self.input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.input.setStyleSheet("""
            QLineEdit {
                border: 1px solid rgba(34, 34, 34, 0.15);
                border-radius: 5px;
                background-color: #FCFDFF;
            }
        """)
        self.input.textChanged.connect(lambda: self.set_valid_style(True))
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input)

    def set_valid_style(self, is_valid: bool):
        if is_valid:
            self.input.setStyleSheet("""
                    QLineEdit {
                        border: 1px solid rgba(34, 34, 34, 0.15);
                        border-radius: 5px;
                        background-color: #FCFDFF;
                    }
            """)
        else:
            self.input.setStyleSheet("""
                    QLineEdit {
                        border: 1px solid rgb(170, 74, 68);
                        border-radius: 5px;
                        background-color: rgba(170, 74, 68, 0.5);
                    }
            """)

    def get_text(self) -> str:
        return self.input.text()

    def set_password_mode(self):
        # noinspection PyUnresolvedReferences
        self.input.setEchoMode(QLineEdit.Password)
