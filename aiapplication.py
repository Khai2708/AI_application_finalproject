# -*- coding: utf-8 -*-
"""Aiapplication.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/177NSuIjhI_D6kyOaBmcJeoD2glzavhE8
"""

!pip install kaggle

!mkdir -p ~/.kaggle

!cp kaggle.json ~/.kaggle/

import pandas as pd
from google.colab import files
files.upload()

!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d zalando-research/fashionmnist

!unzip fashionmnist.zip && rm fashionmnist.zip

df = pd.read_csv('/content/fashion-mnist_test.csv')
df.head()

!pwd

!mkdir my_project

def state(b):
  x = 5*b+4
  print(x)

state(8)
