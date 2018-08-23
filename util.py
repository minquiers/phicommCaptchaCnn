# coding:utf-8
import numpy as np
import base64
import io
from captcha_gen import gen_captcha_text_and_image,read_dir_image
from captcha_gen import CAPTCHA_LIST, CAPTCHA_LEN, CAPTCHA_HEIGHT, CAPTCHA_WIDTH
from PIL import Image



def convert2gray(img):
    '''
    图片转为黑白，3维转1维
    :param img:
    :return:
    '''
    if len(img.shape) > 2:
        img = np.mean(img, -1)
    return img


def text2vec(text, captcha_len=CAPTCHA_LEN, captcha_list=CAPTCHA_LIST):
    '''
    验证码文本转为向量
    :param text:
    :param captcha_len:
    :param captcha_list:
    :return:
    '''
    text_len = len(text)
    if text_len > captcha_len:
        raise ValueError('验证码最长4个字符')
    vector = np.zeros(captcha_len * len(captcha_list))
    for i in range(text_len): vector[captcha_list.index(text[i])+i*len(captcha_list)] = 1
    return vector


def vec2text(vec, captcha_list=CAPTCHA_LIST, size=CAPTCHA_LEN):
    '''
    验证码向量转为文本
    :param vec:
    :param captcha_list:
    :param size:
    :return:
    '''
    # if np.size(np.shape(vec)) is not 1:
    #     raise ValueError('向量限定为1维')
    # vec = np.reshape(vec, (size, -1))
    # vec_idx = np.argmax(vec, 1)
    vec_idx = vec
    text_list = [captcha_list[v] for v in vec_idx]
    return ''.join(text_list)


def wrap_gen_captcha_text_and_image(shape=(60, 160, 3)):
    '''
    返回特定shape图片
    :param shape:
    :return:
    '''
    while True:
        t, im = gen_captcha_text_and_image()
        if im.shape == shape: return t, im


def next_batch(batch_count=60, width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT):
    '''
    获取训练图片组
    :param batch_count:
    :param width:
    :param height:
    :return:
    '''
    batch_x = np.zeros([batch_count, width * height])
    batch_y = np.zeros([batch_count, CAPTCHA_LEN * len(CAPTCHA_LIST)])
    for i in range(batch_count):
        #text, image = wrap_gen_captcha_text_and_image()
        text, image = read_dir_image()
        image = convert2gray(image)
        # 将图片数组一维化 同时将文本也对应在两个二维组的同一行
        batch_x[i, :] = image.flatten() / 255
        batch_y[i, :] = text2vec(text)
    # 返回该训练批次
    return batch_x, batch_y

def base64CoverImage(base64Str, width=CAPTCHA_WIDTH, height=CAPTCHA_HEIGHT):
    parseByte = base64.b64decode(base64Str)
    imgdata = Image.open(io.BytesIO(parseByte))
    imgdata = imgdata.resize((CAPTCHA_WIDTH, CAPTCHA_HEIGHT), Image.ANTIALIAS)
    imgdata = np.array(imgdata)
    #file = open('1231231231.jpg', 'wb')
    #file.write(parseByte)
    #file.close()
    return imgdata

if __name__ == '__main__':
    #x, y = next_batch(batch_count=1)
    #print(x, y)
    image = base64CoverImage('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')
    print(image)


