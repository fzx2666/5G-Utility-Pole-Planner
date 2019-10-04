#=====================================================================
# Function : Define CNN
# Author : Yanyu Zhang
# Date : 10/04/2019
# Copyright 2019 Yanyu Zhang zhangya@bu.edu
#=====================================================================
from keras import layers
from keras import models
from keras import optimizers

def model_Sequential():
  model = models.Sequential()
# 输入的图形尺寸为150*150,channel为3
# filter尺寸为3*3，深度为32
# 该层的输出为：148*148*32
# 参数数量为：3*3*3*32+32=896
  model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
# 该层输出为：74*74*32
  model.add(layers.MaxPool2D(2,2))
# filter尺寸为3*3，深度为64
# 该层的输出为：72*72*64
# 参数的数量为：3*3*32*64+64=18496
  model.add(layers.Conv2D(64,(3,3),activation='relu'))
# 该层的输出为：36*36*64
  model.add(layers.MaxPool2D(2,2))
# filter尺寸为3*3，深度为128
# 该层的输出为：34*34*128
# 参数的数量为：3*3*64*128+128=73856
  model.add(layers.Conv2D(128,(3,3),activation='relu'))
# 该层的输出为：17*17*128
  model.add(layers.MaxPool2D(2,2))
# filter尺寸为3*3，深度为128
# 该层的输出为：15*15*128
# 参数的数量为：3*3*128*128+128=147584
  model.add(layers.Conv2D(128,(3,3),activation='relu'))
# 该层的输出为：7*7*128
  model.add(layers.MaxPool2D(2,2))
  model.add(layers.Flatten())
# 全连接层，参数的数量为：7*7*128*512+512 = 321176
  model.add(layers.Dense(512,activation='relu'))
# 由于是二分类问题，最后一层只有一个激活函数为sigmoid的神经元
  model.add(layers.Dense(1,activation='sigmoid'))

  model.compile(loss='binary_crossentropy',
                optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])
  return model


