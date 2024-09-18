# https://machinelearningmastery.com/save-load-keras-deep-learning-models/

import numpy as np

from keras.datasets import mnist

import keras

import gc

import os

 

from keras.models import Sequential, Model

from keras.layers import Input, Dense, Dropout, Flatten

from keras.layers.convolutional import Conv2D, MaxPooling2D

from keras.models import model_from_json

from keras.models import load_model

import cv2

 

 

#Load a trained model. Note, make sure your Keras version can not be lower than the Keras version used to save the model

 

 

loaded_model=load_model('keras_mnist1.h5')

print("Loaded keras_mnist1 from disk")

 

 

#Load a MNIST image in JPG format, MNIST data set in JPG can be downloaded from https://www.kaggle.com/scolianni/mnistasjpg

#It is 28x28x3, meaning depth is 3, that needs to make it grey scale only with depth 1, following is the code

 

from skimage import transform,io

grey = io.imread("3.jpg")

small_grey = transform.resize(grey, (28,28), mode='symmetric', preserve_range=True)

im=small_grey

height, width  = im.shape

print(height)

print(width)

 

#It will predict the image in JPG and tell what it is

 

pr = loaded_model.predict_classes(im.reshape(1, height, width,1))

print(pr)