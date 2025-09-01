# Handwritten Digit Recognition (MNIST)

This project demonstrates a simple model for recognizing handwritten
digits using **TensorFlow** and the **MNIST dataset**.\
The model is based on **softmax regression** (logistic regression for
multiple classes).

## 📂 Project Structure

-   `main.py` -- main script for training and testing the model\
-   `test1.png` -- custom test image of a digit\
-   `README.md` -- this file\
-   (optional) `requirements.txt` -- list of required libraries

## 🚀 How to Run

1.  Clone the repository:

    ``` bash
    git clone https://github.com/username/mnist-digit-recognition.git
    cd mnist-digit-recognition
    ```

2.  Install the required packages:

    ``` bash
    pip install -r requirements.txt
    ```

3.  Run the script:

    ``` bash
    python main.py
    ```

## 📊 Results

-   The model achieves around **92--93% accuracy on the test set**
    (simple softmax model).\
-   Visualization of some training samples:

![samples](https://github.com/bakirbecicRI/Handwritten-Digit-Recognition-/blob/b00dfd7d63e3ca0f601af2ca400fdb92ae56c09e/samples.PNG)

-   Example prediction on a custom image (`test1.png`):

![test1](https://github.com/bakirbecicRI/Handwritten-Digit-Recognition-/blob/d2ef70532b7677d7834518d1718a2d86cf116c13/test1.png)

    Model predicts digit: 1

## 🛠️ Used Libraries

-   TensorFlow / Keras\
-   NumPy\
-   Matplotlib\
-   Pillow (PIL)

------------------------------------------------------------------------


