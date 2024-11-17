from PyQt6.QtCore import Qt, pyqtSlot, pyqtSignal, QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QFileDialog,
    QFrame,
    QPushButton,
    QVBoxLayout,
)


class UploadWidget(QFrame):
    uploaded = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        icon = QIcon("icons/material-symbols--upload.svg")
        upload_button = QPushButton(icon, "Upload Image")
        upload_button.setIconSize(QSize(30, 30))
        upload_button.setObjectName("mangobold")
        upload_button.clicked.connect(self.uploadH)
        layout.addWidget(upload_button, 0, Qt.AlignmentFlag.AlignCenter)
        self.setObjectName("mango")

    @pyqtSlot()
    def uploadH(self):
        path = QFileDialog.getOpenFileName(
            filter="JPEG (*.jpg *.jpeg);; TIFF (*.tif);; All files (*.*)"
        )[0]
        self.uploaded.emit(path)
