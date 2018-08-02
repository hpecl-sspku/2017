# 使用说明
    文档参考
    * 1701210388-颜崎展-综合实践技术报告

### 使用说明 ###

   Part1.
       步骤1.修改网络配置文件
          - # sudo vim /etc/network/interfaces
          把这个文件修改成如下：
             auto lo
             iface lo inet loopback
             iface eth0 inet dhcp
             auto wlan0              ---------这个地方wlan0是设置wlan，也就是无线，eth0设置的有线
             allow-hotplug wlan0      ---------wlan0可以热插拔
             iface wlan0 inet dhcp    ---------表示用dhcp获取wifi的ip地址
             wpa-ssid “你的wifi名称”  ---------双引号内改掉
             wpa-psk “你的wifi密码”  ---------双引号内改掉
             
       步驟2. 重新开启网络连接
          - # sudo /etc/init.d/networking restart
          注意：可以重启一下（sudo reboot），注意：不要直接插拔电源，会损害SD卡，也就是系统。
           
       步驟3. 使用 ifconfig 查看ip地址
          树莓派有三段信息:
             第一段是 eth0，网线，有固定的ip
             第二段是lo，具体信息可以自行了解
             第三段是 wlan0，也就是wifi信号了，在这里查看我们的wifi的ip地址

   Part2.
       Python PubClient，SubClient获取（镜像中已安装好 MQTT Server）
       通过git下载代码到本地
       - # git clone https://github.com/hpecl-sspku/2017/smarthome/src/MQTT_Server_Client.git

   Part3.
       启动并查看 MQTT Server 服务运行状态
       在树莓派终端执行
       - # sudo service mosquitto start
       - # sudo service mosquitto status
       - # netstat -an | grep 1883
          備註：
             停止MQTT服务：
             - # sudo service mosquitto stop
             1. localhost为服务器的ip地址，若为远端连接则改成该服务器的ip地址即可，-h 之后接的是服务器地址
             2. –t 之后接的是消息的主题
             3. –i 之后接的是消息的发布端
             4. –m 之后接的是消息的内容

       
   Part4.
       使用python编写程序进行测试MQTT的发布和订阅功能要安装
       - # sudo pip3 install paho-mqtt
       
   Part5.
       在RaspberryPi终端上执行.py程序文件
       mqttpubclient.py与mqttsubclient.py都执行
       若是使用Arduino作为节点测试，订阅端程序改成执行mqttsubclient_nogateway.py
       ex.
          - # python3 mqttpubclient.py
       
   Part6.
       使用Arduino测试方案：（使用PC进行）
            下载Arduino IDE
            接上Arduino UNO板
            选择好硬件版本与串口
            烧入testnode2.ino
            可使用IDE提供的串口监控来查看运行状态
