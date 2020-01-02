# CutMixImageDataGenerator (Keras)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/DevBruce/CutMixImageDataGenerator_For_Keras)

> Paper: [CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features](https://arxiv.org/abs/1905.04899)

<br>

## Install

```bash
$ pip install cutmix-keras
```

<br>

## How To Use

```python
# (some codes) ...
from cutmix_keras import CutMixImageDataGenerator  # Import CutMix


train_datagen = ImageDataGenerator(
    rescale=1./255,
)

train_generator1 = train_datagen.flow_from_dataframe(
    dataframe=X_train,
    directory=IMG_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    x_col='X_Column',
    y_col='Y_Column',
    color_mode='rgb',
    class_mode='categorical',
    batch_size=BATCH_SIZE,
    shuffle=True,  # Required
)

train_generator2 = train_datagen.flow_from_dataframe(
    dataframe=X_train,
    directory=IMG_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    x_col='X_Column',
    y_col='Y_Column',
    color_mode='rgb',
    class_mode='categorical',
    batch_size=BATCH_SIZE,
    shuffle=True,  # Required
)

# CutMixImageDataGenerator
train_generator = CutMixImageDataGenerator(
    generator1=train_generator1,
    generator2=train_generator2,
    img_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
)
```

- `generator1`, `generator2` need same generator applied `flow` method

<br>

- `generator1`, `generator2` need `shuffle=True`  
If `shuffle=False`, This generator cutmix with same images.  
So there would no augmentation

<br>

- Why are there two same generators? (`generator1`, `generator2`)  
\-\-\> To Solve Reference Problem  
