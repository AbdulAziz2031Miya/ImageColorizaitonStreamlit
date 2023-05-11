
import tensorflow as tf
from skimage.transform import resize
from skimage.io import imsave, imshow
import numpy as np
import keras
from keras.utils import img_to_array,load_img
from skimage.color import rgb2lab, lab2rgb


model = tf.keras.models.load_model('./final.h5',
                                   custom_objects=None,
                                   compile=True)
def colorize_image(img_path):
            img1_color=[]

            img1=img_to_array(img_path)
            img1 = resize(img1 ,(256,256))
            img1_color.append(img1)

            img1_color = np.array(img1_color, dtype=float)
            img1_color = rgb2lab(1.0/255*img1_color)[:,:,:,0]
            img1_color = img1_color.reshape(img1_color.shape+(1,))

            output1 = model.predict(img1_color)
            output1 = output1*128

            result = np.zeros((256, 256, 3))
            result[:,:,0] = img1_color[0][:,:,0]
            result[:,:,1:] = output1[0]
            result2=lab2rgb(result)
            return (result2)