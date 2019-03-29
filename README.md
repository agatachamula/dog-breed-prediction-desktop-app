# Dog breed prediction desktop app

Application in Python with user interface in Kivy that predicts dog breed based on image provided by user.

p align="center">
  <img width="150" height="150" src="https://github.com/agatachamula/dog-breed-prediction-desktop-app/blob/master/resources/dog.png?raw=true">
</p>


## Prerequisites

List of used packages for running the prediction app:
* os
* sys
* csv
* tensorflow
* kivi and its dependencies (instruction how to install [here](https://kivy.org/doc/stable/installation/installation-windows.html))

## Dataset

Dataset for training and testing is adapted from Stanford Dog dataset available [here](http://vision.stanford.edu/aditya86/ImageNetDogs/).
This dataset consists of 120 dogs breeds with about 100 images for training for each breed.

## Data training

Data was trained with CNN using [VGG-16 bottleneck features](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogVGG16Data.npz). 
This greatly improves accuracy and shortens training time of the model.
After training and testing is performed model is exported to be used in desktop app.

## Desktop App

User Interface for the application was prepared with Kivy package. App consists of three main screens.

Welcome screen:

![alt text](https://github.com/agatachamula/dog-breed-prediction-desktop-app/blob/master/App%20screens/1.PNG?raw=true)


After clicking button on the bottom user is redirected to the new screen with file explorer:

![alt text](https://github.com/agatachamula/dog-breed-prediction-desktop-app/blob/master/App%20screens/2.PNG?raw=true)


User chooses file with image of the dog and clicks the button. After a second prediction is made and user is redirected to new screen:

![alt text](https://github.com/agatachamula/dog-breed-prediction-desktop-app/blob/master/App%20screens/3.PNG?raw=true)


User image is displayed. Below result of prediction and two similar looking breeds are displayed. With all the breeds example images are also presented.

## Resources

All dog images are from Stanford dataset.
Dog logo is provided for free by [FlatIcon](https://www.flaticon.com/)
