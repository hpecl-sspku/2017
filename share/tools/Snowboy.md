# Snowboy
该部分内容译自[Snowboy官网][1]
## 1.概述
Snowboy 是一款高度可定制的唤醒词检测引擎，它可以用于实时嵌入式系统，并且始终处于监听状态（即使离线）。当前，它可以运行在 Raspberry Pi、（Ubuntu）Linux 和 Mac OS X 系统上。

当前，有这些热门的唤醒词：Amazon Echo 上的“Alexa”、Android 设备上的“OK Google” 和 iPhone 上的“Hey Siri”。这些唤醒词用于发起一个完整的语音交互界面。除此之外，唤醒词还可以用于其他用途，比如执行简单的命令和控制动作。

在一个简单的解决方案中，可以通过运行语音识别（ASR，Automatic Speech Recognition）来进行唤醒词检测。在这种情况下，设备将监视语音识别转录中的特定唤醒词。此外，当您使用基于云的解决方案时，您的隐私将不会受到保护。幸运的是，Snowboy 可以解决这些问题！

## 2.特点
Snowboy 具有以下特性：

*   **高度可定制**。让您自由定义自己的唤醒词，如（但不限于）“open sesame”、“garage door open”、或者“hello dreamhouse"。你能想到的，你就能定制它。
*   **一直监听，但是保护您的隐私**。因为 Snowboy 没有连接到网络，因此不需要将你的声音上传到任何地方。
*   **轻量级、可嵌入**。您可以在 Raspberry Pi 上运行Snowboy。同时，Snowboy在最小的Pi（单核700M Hz ARMv6）上仅占用少于10％的CPU。
*   **Apache 协议**

现在，Snowboy还提供唤醒词服务。 您可以通过编程方式使用Snowboy的RESTful API Calls以3个简单步骤来训练唤醒词模型。
*  首先选择一个唤醒词。
*  在您的设备上录音3次
*  通过Snowboy的RESTful API Calls提交音频文件，模型将被训练并返回。

完成后，设备可以立即执行唤醒词检测。

## 3.支持
当前，Snowboy 可以支持：

*   所有版本的 Raspberry Pi (搭载 Debian Jessie 8.0)
*   64位 Mac OS X
*   64bit Ubuntu (12.04 和 14.04)
*   iOS
*   Android （ARMv7 CPU）
*   Pine 64，搭载 Debian Jessie 8.5 (内核版本 3.10.102)
*   Intel Edison，搭载 Ubilinux (Debian Wheezy 7.8)

## 4.更多内容
关于Snowboy的使用和更多内容，请点击Snowboy的[官方文档][2]进行查看


  [1]: http://docs.kitt.ai/snowboy/#introduction
  [2]: http://docs.kitt.ai/snowboy/