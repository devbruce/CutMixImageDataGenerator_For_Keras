from setuptools import setup
import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(ROOT_DIR, 'README.md')

setup(
    name='cutmix-keras',
    author='devbruce',
    author_email='bruce93k@gmail.com',
    description='CutMuxImageDataGenerator For Keras',
    long_description=open(README_PATH, encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    version='1.0.0',
    url='https://github.com/DevBruce/CutMixImageDataGenerator_For_Keras',
    py_modules=['cutmix_keras'],
    keywords=['cutmix', 'keras'],
    # install_requires=['keras'],
)
