# CutMixImageDataGenerator (Keras)

![Python-v3.7.3](https://img.shields.io/badge/Python-v3.7.3-blue)
![Keras-v2.2.4](https://img.shields.io/badge/Keras-v2.2.4-brightgreen)

**Version 0.1 (Beta)**  

<br>

```python
class CutMixImageDataGenerator():
    def __init__(self, generator1, generator2, img_size, batch_size):
        self.batch_index = 0
        self.samples = generator1.samples
        self.class_indices = generator1.class_indices
        self.generator1 = generator1
        self.generator2 = generator2
        . . .
```

- `generator1`, `generator2` need same generator applied `flow` method

<br>

- `generator1`, `generator2` need `shuffle=True`  
If `shuffle=False`, This generator cutmix with same images.  
So there would no augmentation

<br>

- Why are there two same generators? (`generator1`, `generator2`)  
\-\-\> To Solve Reference Problem  

<br>

## Using Example

```python
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
