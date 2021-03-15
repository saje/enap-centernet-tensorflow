import tensorflow as tf
from tqdm import tqdm
'''
raw_dataset = tf.data.TFRecordDataset("annotations/test.record")

for raw_record in raw_dataset.take(1):
    example = tf.train.Example()
    example.ParseFromString(raw_record.numpy())
    print(example)


'''
from os import listdir
from PIL import Image
   
for filename in listdir('./images/train'):
  if filename.endswith('.png'):
    try:
      img = Image.open('./'+filename) # open the image file
      img.verify() # verify that it is, in fact an image
    except (IOError, SyntaxError) as e:
      print('Bad file:', filename) 