from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QLabel
from typing import Optional
from PyQt6.QtGui import QResizeEvent, QPixmap


class ImageViewer(QLabel):
    def __init__(self):
        super().__init__()
        self.path = ""

    def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
        h = self.height()
        if self.path != "":
            self.setPixmap(QPixmap(self.path).scaledToHeight(h))

    def setPath(self, path: str) -> None:
        self.path = path
        h = self.height()
        return super().setPixmap(QPixmap(self.path).scaledToHeight(h))

    def sizeHint(self) -> QSize:
        if self.path != "":
            return super().sizeHint()
        return QSize(2024, 2024)
