import os
from pathlib import Path
import time
from PyQt6.QtCore import pyqtSlot, QDir
from PyQt6.QtWidgets import (
    QLabel,
    QMenuBar,
    QStackedLayout,
    QWidget,
    QFrame,
    QApplication,
    QVBoxLayout,
)

from custom_widgets.upload_widget import UploadWidget
from custom_widgets.define_widget import DefineWidget


class MangoLoco(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.image_path = ""
        self.result: dict = {}

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.content_widget = QFrame()
        self.topbar = QLabel("Mango Loco")
        self.topbar.setObjectName("title")
        self.main_layout.addWidget(self.topbar)
        self.main_layout.addWidget(self.content_widget)

        self.my_layout = QStackedLayout()
        self.content_widget.setLayout(self.my_layout)
        self.upload_widget = UploadWidget()
        self.upload_widget.uploaded.connect(self.set_define_view)
        self.define_widget = DefineWidget()
        self.define_widget.compute.connect(self.compute_tags)
        self.define_widget.change_image.connect(self.set_upload_view)
        self.define_widget.save_result.connect(self.saveResult)
        self.my_layout.addWidget(self.upload_widget)
        self.my_layout.addWidget(self.define_widget)

    @pyqtSlot(str)
    def set_define_view(self, path):
        self.my_layout.setCurrentWidget(self.define_widget)
        self.image_path = path
        self.define_widget.set_image(path)

    @pyqtSlot()
    def set_upload_view(self):
        self.my_layout.setCurrentWidget(self.upload_widget)

    @pyqtSlot()
    def compute_tags(self):
        time.sleep(2)  # Aqui va la funció dels majetes!
        self.result = {"Coll": "LLarg", "Llargada": "Curt", "Estil": "Guai"}
        self.define_widget.showResult(self.result)

    @pyqtSlot()
    def saveResult(self):
        name = Path(self.image_path).stem
        with open(f"{name}_attributes.csv", "w") as f:
            for key, value in self.result.items():
                f.write(key + "," + value + "\n")


def main():
    qapp = QApplication([])

    # use script directory as root
    root = os.path.dirname(os.path.abspath(__file__))
    QDir.addSearchPath("icons", os.path.join(root, "icons"))

    with open("style/style.qss", "r") as f:
        qapp.setStyleSheet(f.read())

    mango_app = MangoLoco()
    mango_app.show()
    qapp.exec()


if __name__ == "__main__":
    main()
