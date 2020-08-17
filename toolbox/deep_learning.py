# Copyright (C) 2020 Aron Sarosi

from os.path import split
import pandas as pd
from matplotlib.pyplot import plt


# Building a Sequential DL model with dropout
def build_model_with_dropout():
    model = Sequential()

    model.add(Conv2D(32, (5, 5), padding='same', input_shape=(32, 32, 3), activation='relu'))
    model.add(Dropout(0.1)) # randomly sets 10% of the previous layer's output
    # to zero -> prevents overfitting
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
    model.add(Dropout(0.1))
    model.add(MaxPooling2D(pool_size=(3, 3)))

    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Dropout(0.1))
    model.add(MaxPooling2D(pool_size=(3, 3)))

    model.add(Flatten())
    model.add(Dense(40, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    return model
