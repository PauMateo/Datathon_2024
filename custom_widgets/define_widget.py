from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot, QSize
from PyQt6.QtWidgets import (
    QComboBox,
    QFrame,
    QGridLayout,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from custom_widgets.image_viewer import ImageViewer
import dictionary_types as dic_types


class DefineWidget(QFrame):
    compute = pyqtSignal()
    change_image = pyqtSignal()
    save_result = pyqtSignal()
    set_item_class = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        self.setObjectName("mango")

        self.compute_bttn = QPushButton("Compute")
        self.compute_bttn.setObjectName("mango")

        self.compute_bttn.clicked.connect(self.computeStart)
        self.image = ImageViewer()
        change_image = QPushButton("Change Image")
        change_image.setObjectName("mango")

        change_image.clicked.connect(self.changeImageH)
        self.options = QComboBox()
        self.options.addItems(dic_types.clothing_items.keys())
        self.options.setObjectName("mango")
        self.options.currentTextChanged.connect(self.change_item_class)
        self.result = QTableWidget()
        self.result.horizontalHeader().hide()  # type: ignore
        self.result.setObjectName("mango")

        self.result.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        self.save_bttn = QPushButton("Save Results (csv)")
        self.save_bttn.setObjectName("mango")
        self.save_bttn.clicked.connect(self.saveResult)

        right_layout = QVBoxLayout()
        left_layout = QVBoxLayout()
        layout.addLayout(left_layout, 0, 0)
        layout.addLayout(right_layout, 0, 1)

        right_layout.addWidget(self.options)
        right_layout.addWidget(self.compute_bttn)
        right_layout.addWidget(self.result, 1, alignment=Qt.AlignmentFlag.AlignTop)
        right_layout.addWidget(self.save_bttn)

        left_layout.addWidget(self.image, 1, Qt.AlignmentFlag.AlignCenter)
        left_layout.addWidget(change_image, 0)

    @pyqtSlot(str)
    def set_image(self, path):
        self.image.setPath(path)

    @pyqtSlot()
    def computeStart(self):
        self.compute_bttn.setDisabled(True)
        self.compute.emit()

    @pyqtSlot(dict)
    def showResult(self, result: dict):
        self.compute_bttn.setDisabled(False)
        self.result.setRowCount(len(result))
        self.result.setColumnCount(1)
        i = 0
        self.result.setVerticalHeaderLabels(result.keys())
        
        for key, value in result.items():
            item = QTableWidgetItem(value)
            item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.result.setItem(i, 0, item)
            self.result.setColumnWidth(0, 200)
            i += 1

    @pyqtSlot()
    def changeImageH(self):
        self.change_image.emit()

    @pyqtSlot()
    def saveResult(self):
        self.save_result.emit()

    @pyqtSlot(str)
    def change_item_class(self, item_class: str):
        self.set_item_class.emit(item_class)
