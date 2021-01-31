# STUautoHealthreport
## 汕头大学自动健康打卡 
该程序需要一直运行，推荐使用腾讯云或者阿里云的学生机远程运行

使用时运行main文件，将user修改为自己的用户名和密码，自己设定几时运行

## 需要额外安装的依赖
selenuim  
schedule

另外需要额外下载[chromedriver程序](https://chromedriver.chromium.org/)放在anaconda和chrome的文件夹中


# main.py
主程序,用户在该文件中修改user为自己的账户密码以及设定时间

# healthreport_auto.py 
负责获取cookies和实现POST的操作，打卡内容变动后可自行修改data中的内容
# healthreport_gui.py
一个小的GUI，已弃用

