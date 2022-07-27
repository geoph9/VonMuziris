# Project VonMuziris

The purpose of the project is to create customized solution for a startup that in the jewelry retail industry. The idea is to find a way to allow jewelry sellers bulk upload their products in the startup's online platform. Currently, sellers have to either upload their products one by one (very time consuming), or use a very strict bulk upload format. Sellers with no programming background find it very hard to transform their data sets into this standardized format and this project tries to find a way to dynamically adapt to each seller's way of storing the data. In particular, we focus on the most difficult task which is to map a single product (a title, for example) to a sequence of images (since each jelewry entry is characterized by many images, e.g. taken from different angles). 

This work focuses on creating a neural network architecture that can find correct mappings between products and images, assuming that the input data set is not given into any specific format. The combined solution of two neural networks is built for working with images of jewelry and texts, characterizing them. The relevant repository files are:

- `Model.ipynb`: definition of classes for the model and the training pipeline.
- `Training.py`: Mostly used as a playground.
- `Preprocessing.py`: preprcosseing of the data from the original resources.
- `download_dropbox_imgs.py`: A script that downloads the dropbox images of our data set using `wget` (only works on linux machines).
