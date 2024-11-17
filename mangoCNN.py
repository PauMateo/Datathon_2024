# Definim la classe MangoNet que hereta d'EfficientNet
import torch
import torch.nn as nn
import pandas as pd
import random
import numpy as np
from efficientnet_pytorch import EfficientNet

class MangoNet(nn.Module):
    def __init__(self, num_channels=11*(33+1),drop=0.5):
        # Carrega EfficientNet-B1 preentrenat
        super(MangoNet, self).__init__()
        # Carrega el model EfficientNet-B1 amb pesos preentrenats
        efficient_net = EfficientNet.from_pretrained('efficientnet-b2')

        # Obté el nombre d'entrades de l'última capa fully connected original
        self.features = nn.Sequential(
            efficient_net._conv_stem,
            efficient_net._bn0,
            *efficient_net._blocks,
            efficient_net._conv_head,
            efficient_net._bn1,
        )
        in_features = efficient_net._fc.in_features

        # Substitueix l'última capa amb una nova capa Conv2d per tenir la sortida amb els canals desitjats
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Sequential(
            nn.Dropout(p=drop, inplace=True),
            nn.Linear(in_features, num_channels),
        )


    def forward(self, x):
        # Passa l'entrada a través de les capes de features d'EfficientNet
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        # Aplica la nostra capa Conv2d personalitzada per obtenir la sortida desitjada
        x = self.classifier(x)
        x = torch.reshape(x, [-1,34,11])
        return x
