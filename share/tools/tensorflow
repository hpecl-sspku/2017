Tensorflow简介
TensorFlow是谷歌基于DistBelief进行研发的第二代人工智能学习系统，其命名来源于本身的运行原理。Tensor（张量）意味着N维数组，Flow（流）意味着基于数据流图的计算，TensorFlow为张量从流图的一端流动到另一端计算过程。TensorFlow是将复杂的数据结构传输至人工智能神经网中进行分析和处理过程的系统。
TensorFlow可被用于语音识别或图像识别等多项机器学习和深度学习领域，对2011年开发的深度学习基础架构DistBelief进行了各方面的改进，它可在小到一部智能手机、大到数千台数据中心服务器的各种设备上运行。TensorFlow将完全开源，任何人都可以用。

Tensorflow安装
官方提供了5种安装tensorflow的方法:
1.Pip install: Install TensorFlow on your machine, possibly upgrading previously installed Python packages. May impact existing Python programs on your machine.
2.Virtualenv install: Install TensorFlow in its own directory, not impacting any existing Python programs on your machine.
3.Anaconda install: Install TensorFlow in its own environment for those running the Anaconda Python distribution. Does not impact existing Python programs on your machine.
4.Docker install: Run TensorFlow in a Docker container isolated from all other programs on your machine.
5.Installing from sources: Install TensorFlow by building a pip wheel that you then install using pip.
这里分别提供一种linux和window环境下的安装方法
linux下安装TensorFlow(centos)
一、python安装
　　centos自带python2.7.5，这一步可以省略掉。
二、python-pip
　　pip--python index package,累世linux的yum，安装管理python软件包用的。
   yum install  python-pip python-devel
三、安装tensorflow
　　安装基于linux和python2.7的tensorflow 0.9
pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl
　　其他操作系统版本可以参照下表：
# Ubuntu/Linux 64-bit, CPU only, Python 2.7
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl
# Ubuntu/Linux 64-bit, GPU enabled, Python 2.7
# Requires CUDA toolkit 7.5 and CuDNN v4. For other versions, see "Install from sources" below.
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl
# Mac OS X, CPU only, Python 2.7:
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py2-none-any.whl
# Ubuntu/Linux 64-bit, CPU only, Python 3.4
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl
# Ubuntu/Linux 64-bit, GPU enabled, Python 3.4
# Requires CUDA toolkit 7.5 and CuDNN v4. For other versions, see "Install from sources" below.
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl
# Ubuntu/Linux 64-bit, CPU only, Python 3.5
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl
# Ubuntu/Linux 64-bit, GPU enabled, Python 3.5
# Requires CUDA toolkit 7.5 and CuDNN v4. For other versions, see "Install from sources" below.
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl
# Mac OS X, CPU only, Python 3.4 or 3.5:
 export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/tensorflow-0.9.0-py3-none-any。whl
 
 Win10+CPU+python+pycharm下安装tensorflow
 这里教程较长，提供链接，win里面安装tensorflow可以一定程度上解决虚拟机配置不足的问题
 windows+pycharm+tensorflow
安装windows的tensorflowhttp://blog.csdn.net/whu_gcoder_2017/article/details/61920211

最后给由于不同版本的tensorflow内部代码有一定的区别，所以提供一套自动升级代码的教程，适应于将1.0以前的版本代码升级的1.0以后。
升级代码到1.0以上https://juejin.im/post/5a2675ecf265da431d3c89ba通过DOS进入tf_update.py的文件目录下然后按照上面的教程进行文件的升级。
