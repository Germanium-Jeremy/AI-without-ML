# FACE RECOGNITION SYSTEM AND TRACKER – “Every AI is not ML”

## Installation

```bash
# Create virtual environment
python -m venv .venv

# Windows
./.venv/Scripts/activate 

# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python 01_train.py
python 02_recognize.py
python 03_track_face.py
python 04_track_face.py
python 05_track_face.py
```

## Explanation

### 01_create_dataset.py
Take images of faces and train the model as datasets. Make sure you are not in motion while taking images and there is no light changes. Too much light or dark changes can cause the model to be unstable. Take as many pictures as you can (Minimum 200 images).

### 02_review_dataset.py
Review the dataset and remove any images that are not clear or not of good quality. Make sure to review all the captured images.

### 03_train_model.py
Train the model using the dataset.

### 04_predict.py
Predict the face using the model. 

### 05_track_face.py
Track the face using the model.

## License
MIT