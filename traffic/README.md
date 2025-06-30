# Traffic Sign Classification with TensorFlow

This project is a deep learning-based image classification model that recognizes German traffic signs using the [GTSRB dataset](https://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset). The model is built using TensorFlow and OpenCV.

## 📁 Dataset

The dataset contains more than 50,000 images categorized into **43 different types of traffic signs**, stored in folders named `0` through `42`. Each image varies in size and must be resized to a fixed size of `30x30` pixels to be used in the neural network.

## 🚀 Setup

1. Clone or download the project files.
2. Download the GTSRB dataset and place it inside your project directory:
   ```
   traffic/
   ├── gtsrb/
   │   ├── 0/
   │   ├── 1/
   │   └── ...
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the model:
   ```bash
   python traffic.py gtsrb model.h5
   ```

## 🧠 Model Architecture

The model is a Convolutional Neural Network (CNN) built with TensorFlow Keras:

- **Input Layer**: (30, 30, 3) RGB image
- **Conv2D + MaxPooling**: Extracts features with 32 filters
- **Conv2D + MaxPooling**: Adds deeper feature maps with 64 filters
- **Flatten**: Prepares for classification
- **Dense + Dropout**: Fully connected layer with 128 units and dropout for regularization
- **Output Layer**: Dense layer with 43 units (one for each traffic sign), using `softmax` activation

## 📊 Training Configuration

- **Epochs**: 10  
- **Train/Test Split**: 60/40  
- **Loss Function**: Categorical Crossentropy  
- **Optimizer**: Adam  
- **Metrics**: Accuracy  

## 🧪 Experimentation Process

### ✅ What Worked Well

- Using two convolutional layers followed by max pooling effectively extracted spatial features.
- Dropout reduced overfitting and helped improve test accuracy.
- Training on all 43 categories with resized (30x30) images was computationally efficient while retaining accuracy.

### ❌ What Didn’t Work Well

- Using only one convolutional layer resulted in poor accuracy (~60%) on test data.
- Increasing the model depth without dropout led to overfitting, where training accuracy reached ~98% but test accuracy stagnated around 70–75%.
- Using higher-resolution input images (e.g., 64x64) increased computation time without significant accuracy gains.

### 📈 Final Results

After tuning:
- Training accuracy reached ~95%
- Test accuracy stabilized around **88–92%** depending on random seed and exact split.

## 📦 Files

- `traffic.py`: Main script to load data, define the model, train, evaluate, and save.
- `requirements.txt`: Lists required packages (`tensorflow`, `opencv-python`, `scikit-learn`)
- `model.h5`: Saved trained model (if specified).
- `README.md`: Documentation for the project.

## 📝 Notes

- You can modify the number of epochs, image dimensions, and layers to experiment with different results.
- To visualize model performance, consider adding a confusion matrix or per-category accuracy breakdown.

## 📚 References

- [TensorFlow Keras Documentation](https://www.tensorflow.org/api_docs/python/tf/keras)
- [OpenCV Python Docs](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [GTSRB Dataset Info](https://benchmark.ini.rub.de/?section=gtsrb&subsection=news)
