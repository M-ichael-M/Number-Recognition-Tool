# Number Recognition Tool v1.0.0
## Requirements
The program works on images with dimensions of 28x28 px.
The location of the image files (training and test data) must be in the same folder as the main.py program or its subfolders.
In the program folder where the main.py file is located, the following items should be present:

- weight.py file
- folder with test data
- folder with training data
- The data should be saved in the following formats: EPS, GIF, ICO, JPEG, PNG, PSD, EMF, ICNS, IM, MSP, PCX, PPM, SGI, SPIDER, TGA, WebP, XBM, BLP, CUR, DCX, DDS, FLI, FPX, FTEX, GBR, GD, IMT, MCIDAS, MIC, MPO, PCD, PIXAR, WAL, XPM

The training data should be properly sorted and verified to avoid errors during input, as this will result in incorrect model operation. The weight.py file contains the weights that the program retrieves at the beginning.

## About the Program
The program is a supervised learning-based neural network model. The neural network model was built without the use of any libraries. The program analyzes each image by extracting the RGB pixel values and converting them to grayscale. The Pillow library is responsible for this task. The program then converts the data into binary form. The network consists of 4 layers, including the input layer.

## How to Use
At the beginning, the program prompts you to choose from the available options:
1 - Train: This should be done initially upon launching the program. The program then asks for the path to an example (it should be in the program's folder or subfolder). In the next step, you enter the label for the image, i.e., what is depicted in it (an integer from 0 to 9). The program analyzes the image and modifies the neural network weights, thus learning the pattern. The more examples we provide for each digit, the more accurate our model will be.

2 - Use: After training the model, we can proceed to use and test it. The program asks for the path to a test image file. After analyzing and passing it through the model, the program outputs the result. The result is displayed in the form of an array. Each element represents the probability percentage (0-100) that the given test example is the number 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9. In the case where the array looks like this: [5.05454, 45.48, 44.44, 78.55, 98.66, 33.33, 65.25, 78.56, 42.35, 69.69], the highest value is at index 4, which corresponds to the digit 4. From the program's operation, it can be inferred that the test example displayed the digit 4.

3 - Print Weights: The program prints the weights for the digits it has learned. This allows us to save what the program has learned so that we can start from it next time. We can also try to detect any errors that may have occurred during the learning process. If the weights for two digits are very similar, it may indicate that data from one digit has been used to train another.

Upon closing the program, all weights are reset, which means losing the learning progress. The learning process will have to be repeated the next time. Alternatively, we can save the weights from the previous learning and paste them into the weight.py file instead of resetting them to zero.

## Tips for Training the Network
Training the model is a very difficult and time-consuming process, which is why we have prepared a small dataset of 10 examples for each digit. You can use it during the training process. When using your own data, it is essential to verify its correctness. Data engineering is too complex to describe the best methods for selecting data. If you want to achieve the most optimal model, we recommend taking a Data Science course.

## Author
Michał Małeczek