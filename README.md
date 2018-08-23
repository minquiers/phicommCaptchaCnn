# 简介
基于CNN的验证码识别模块
# 快速开始
* 训练模型

  python cnn_train.py

* 模型测试

  python captcha_cnn.py
  
* 提供API接口

  python captchaCnnAPI.py
  
 # 部署:
 0.安装python3 https://www.python.org/downloads/ <br />
 1.安装tensorflow https://www.tensorflow.org/install/install_linux?hl=zh-cn <br />
 2.安装Flask  <br />
 3.启动 captchaCnnAPI.py <br />
 x.模型已经训练好(1.0captcha.model-30000.data-00000-of-00001 文件),斐讯图片验证码识别在99.95% <br />
 x.接口地址 http://localhost:5000/vcode <br />
 
