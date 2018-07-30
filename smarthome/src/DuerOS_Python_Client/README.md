# 使用说明
文档参考
* [《Step by Step带你玩转DuerOS - Python DuerOS SDK[树莓派平台] (3)》](https://dueros.baidu.com/didp/forum/topic/show?topicId=244796)

## 使用说明

### Python SDK的获取（镜像中已安装好SDK）
通过git下载代码到本地

    # git clone https://github.com/MyDuerOS/DuerOS-Python-Client.git

### 认证授权（认证授权需打开网页，故需在远程桌面或其他vnc下进行）
在DuerOS-Python-Client目录下执行
 
    # ./auth.sh

### 通过[Enter]键触发唤醒状态
在DuerOS-Python-Client目录下执行

    # ./enter_trigger_start.sh

然后，每次单击[Enter]键后进行语音输入
### 通过[小度小度]触发唤醒状态
在DuerOS-Python-Client目录下执行

    # ./wakeup_trigger_start.sh
然后，每次通过[小度小度]进行唤醒，然后，进行语音输入

 
### 代码替换

使用Filezilla直接将文件上传至以下目录进行代码文件替换，或使用其他方法进行替换

*DuerOS-Python-Client/app:应用目录*
* DuerOS-Python-Client/app/wakeup_tirgger_main.py:[小度小度]触发唤醒实现模块

*DuerOS-Python-Client/sdk:dueros sdk目录*

* DuerOS-Python-Client/sdk/dueros_core.py:dueros交互实现
