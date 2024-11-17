import os
from pathlib import Path
import time
from PyQt6.QtCore import pyqtSlot, QDir
from PyQt6.QtWidgets import (
    QLabel,
    QStackedLayout,
    QWidget,
    QApplication,
    QVBoxLayout,
)

from custom_widgets.upload_widget import UploadWidget
from custom_widgets.define_widget import DefineWidget
from dictionary_types import class_filter, clothing_items
from mangoCNN import MangoNet
import torch
from torch.utils.data import Dataset
from torchvision.io import read_image
from PIL import Image
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os
from torchvision import transforms
import time


class MangoLoco(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.image_path = ""
        self.result: dict = {}
        self.item_class: str = list(clothing_items.keys())[0]

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.content_widget = QWidget()
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
        self.define_widget.set_item_class.connect(self.set_item_class)
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

    @pyqtSlot(str)
    def set_item_class(self, item_class: str):
        print("item class: " + item_class)
        self.item_class = item_class

    @pyqtSlot()
    def compute_tags(self): 
        
        self.img_labels = pd.read_csv('clean_data.csv')
        self.label_encoders = {}
        for col in self.img_labels:
            le = LabelEncoder()
            self.img_labels[col] = le.fit_transform(self.img_labels[col])  # Codifiquem les etiquetes
            self.label_encoders[col] = le  # Guardem l'encoder per a futures prediccions

        model = MangoNet(num_channels=11*(33+1),drop=0.5)
        model.load_state_dict(torch.load('params4b2',map_location=torch.device('cpu')))
        self.image_path
        image = read_image(self.image_path).type(torch.float32)
        image = torch.unsqueeze(image, 0)
        output = model(image)
        output = output.detach().numpy()
        pred_labels = np.argmax(output, axis=1)

        tags = self.label_encoders.keys()

        d = {}
        for i, t in enumerate(tags):
            if i >= pred_labels.shape[1]: continue
            encoder = self.label_encoders[t]
         
            label_for_tag = pred_labels[0, i]  # Assuming pred_labels has shape (1, 11)

            # Use inverse_transform with the scalar label
            
            try:
                d[t] = encoder.inverse_transform([label_for_tag])[0]
            except:
                d[t] = 'INVALID'
            if d[t] == 'INVALID': d.pop(t)
                

        print(d)
        self.result = class_filter(d, self.item_class)
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
