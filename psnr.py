import numpy
from skimage import io
import tensorflow as tf
from PIL import Image
import os, sys, glob
from itertools import combinations
from functools import reduce

def log10(x):
    numerator = tf.log(x)
    denominator = tf.log(tf.constant(10, dtype=numerator.dtype))
    return numerator / denominator


def psnr(im1, im2):
    im1 = Image.open(im1)
    im2 = Image.open(im2)
    img_arr1 = numpy.array(im1).astype('double')
    img_arr2 = numpy.array(im2).astype('double')
    mse = tf.reduce_mean(tf.squared_difference(img_arr1, img_arr2))
    psnr = tf.constant(255**2, dtype=tf.double)/mse
    result = tf.constant(10, dtype=tf.double)*log10(psnr)
    with tf.Session():
        result = result.eval()
    return result

def msssim(im1, im2):
    im1 = Image.open(im1)
    im2 = Image.open(im2)
    img_arr1 = numpy.array(im1).astype('double')
    img_arr2 = numpy.array(im2).astype('double')
    img_arr1 = tf.convert_to_tensor(img_arr1)
    img_arr2 = tf.convert_to_tensor(img_arr2)
    with tf.Session():
        result = tf.image.ssim_multiscale(img_arr1, img_arr2, max_val=255)
        result = result.eval()
    return result

def Average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst) 

def calculate_metrics():
    mydir = os.getcwd()
    os.chdir(str(mydir)+'/samples/' + 'relu/test_processed')
    idx=0
    m_list = []
    filelist =  glob.glob('*.png')
    combs = combinations(filelist, 2)
    for combination in combinations(filelist, 2):
        print(combination)
        m_list.append(psnr(str(combination[0]),str(combination[1])))
        print(m_list)
        # print('average ms-ssim score:')
        # print(Average(m_list))
        # print('iter:')
        # print(len(m_list))
    return m_list




calculate_metrics()

