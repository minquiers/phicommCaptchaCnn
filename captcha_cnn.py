# coding:utf-8
import tensorflow as tf
import os
from cnn_train import cnn_graph
from captcha_gen import gen_captcha_text_and_image,read_dir_image,read_dir_image_for_position, IMAGE_TEST_PATH, RESTORE_PATH
from util import vec2text, convert2gray, CAPTCHA_LIST, CAPTCHA_WIDTH, CAPTCHA_HEIGHT, CAPTCHA_LEN




def image2text(image , height=CAPTCHA_HEIGHT, width=CAPTCHA_WIDTH):
    pre_text = '1111'
    tf.reset_default_graph()
    x = tf.placeholder(tf.float32, [None, height * width])
    keep_prob = tf.placeholder(tf.float32)
    y_conv = cnn_graph(x, keep_prob, (height, width))
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, RESTORE_PATH)
        image = convert2gray(image)
        image = image.flatten() / 255
        image = [image]
        predict = tf.argmax(tf.reshape(y_conv, [-1, CAPTCHA_LEN, len(CAPTCHA_LIST)]), 2)
        vector_list = sess.run(predict, feed_dict={x: image, keep_prob: 1})
        vector_list = vector_list.tolist()
        pre_text = [vec2text(vector) for vector in vector_list]
    return pre_text


def captcha2text(height=CAPTCHA_HEIGHT, width=CAPTCHA_WIDTH):
    '''
    验证码图片转化为文本
    :param image_list:
    :param height:
    :param width:
    :return:
    '''
    x = tf.placeholder(tf.float32, [None, height * width])
    keep_prob = tf.placeholder(tf.float32)
    y_conv = cnn_graph(x, keep_prob, (height, width))
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, RESTORE_PATH)
        success = 0
        error = 0
        for num in range(0, len(os.listdir(IMAGE_TEST_PATH))):
            text, image = read_dir_image_for_position(num,IMAGE_TEST_PATH)
            image = convert2gray(image)
            image = image.flatten() / 255
            image = [image]
            predict = tf.argmax(tf.reshape(y_conv, [-1, CAPTCHA_LEN, len(CAPTCHA_LIST)]), 2)
            vector_list = sess.run(predict, feed_dict={x: image, keep_prob: 1})
            vector_list = vector_list.tolist()
            pre_text = [vec2text(vector) for vector in vector_list]
            if (text == ''.join(pre_text)):
                success += 1
            else:
                error += 1
            print('Label:', text, ' Predict:', pre_text)
        print('total:', success + error, ',success:', success, ',error:', error)


       # return text_list

if __name__ == '__main__':
    #text, image = gen_captcha_text_and_image()
    #text, image = read_dir_image("C:/Users/Administrator/Desktop/tensorflow/captcha/testImages/")
    #image = convert2gray(image)
    #image = image.flatten() / 255
    #pre_text = captcha2text([image])
    #print('Label:', text, ' Predict:', pre_text)
    captcha2text()
