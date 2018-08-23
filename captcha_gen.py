# coding:utf-8
import os
import random
import numpy as np
from PIL import Image
from captcha.image import ImageCaptcha


NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOW_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
UP_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
CAPTCHA_LIST = NUMBER + LOW_CASE + UP_CASE
CAPTCHA_LEN = 4
CAPTCHA_HEIGHT = 20
CAPTCHA_WIDTH = 65
#测试图片存储路径
IMAGE_TEST_PATH = 'E:/SVN/eclipseWorkSpace/phicomm/src/main/java/tensorflow/captcha/testImages/'
#训练文件存储路径
#RESTORE_PATH = 'E:\\SVN\\eclipseWorkSpace\\phicomm\\src\\main\\java\\tensorflow\\captchaCnn\\1.0captcha.model-30000'
RESTORE_PATH = 'E:/SVN/eclipseWorkSpace/phicomm/src/main/java/tensorflow/captchaCnn/1.0captcha.model-30000'
#训练图片存储路径
IMAGE_PATH = 'E:/SVN/eclipseWorkSpace/phicomm/src/main/java/tensorflow/captcha/images/'


def random_captcha_text(char_set=CAPTCHA_LIST, captcha_size=CAPTCHA_LEN):
    '''
    随机生成验证码文本
    :param char_set:
    :param captcha_size:
    :return:
    '''
    captcha_text = [random.choice(char_set) for _ in range(captcha_size)]
    return ''.join(captcha_text)


def gen_captcha_text_and_image(width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT,save=None):
    '''
    生成随机验证码
    :param width:
    :param height:
    :param save:
    :return: np数组
    '''
    image = ImageCaptcha(width=width, height=height)
    # 验证码文本
    captcha_text = random_captcha_text()
    captcha = image.generate(captcha_text)
    # 保存
    if save: image.write(captcha_text, captcha_text + '.jpg')
    captcha_image = Image.open(captcha)
    # 转化为np数组
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image


def read_dir_image(path=IMAGE_PATH):
    list = os.listdir(path)
    fileName = ''.join(list[random.randint(0, list.__len__() - 1)])
    fileFullPath = path + fileName
    captcha_image = Image.open(fileFullPath)
    captcha_image = captcha_image.resize((CAPTCHA_WIDTH, CAPTCHA_HEIGHT), Image.ANTIALIAS)
    captcha_image = np.array(captcha_image)
    captcha_text = fileName.split('.')[0]
    if(len(captcha_text) > CAPTCHA_LEN):
        captcha_text = captcha_text[0:CAPTCHA_LEN]
    #print('old',fileName,'new',captcha_text)
    return captcha_text, captcha_image

def read_dir_image_for_position(position,path=IMAGE_PATH):
    list = os.listdir(path)
    fileName = ''.join(list[position])
    fileFullPath = path + fileName
    captcha_image = Image.open(fileFullPath)
    captcha_image = captcha_image.resize((CAPTCHA_WIDTH, CAPTCHA_HEIGHT), Image.ANTIALIAS)
    captcha_image = np.array(captcha_image)
    captcha_text = fileName.split('.')[0]
    if (len(captcha_text) > CAPTCHA_LEN):
        captcha_text = captcha_text[0:CAPTCHA_LEN]
    return captcha_text, captcha_image

if __name__ == '__main__':
    #t, im = gen_captcha_text_and_image(save=True)
    t, im = read_dir_image()
    print(t, im)



