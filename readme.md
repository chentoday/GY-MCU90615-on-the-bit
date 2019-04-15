# Document

- 前提准备：[第一次使用必看](https://github.com/aJantes/Initialize-the-board/blob/master/readme.md)
- 硬件介绍：
1. [BPI:bit(ESP32)](https://github.com/aJantes/introduce-bpi-bit/blob/master/readme.md)
2. [GY-MCU90615V2](https://github.com/aJantes/GY-MCU90615/blob/master/GY-MCU90615.pdf)
3. 底座
4. 杜邦线
- 编程工具：[pycharm](https://github.com/aJantes/use-pycharm/blob/master/readme.md)

## 对GY-MCU90615的应用

硬件连接
1. 将模块上的RX连接到bpi:bit上的P9(TX)
2. 将模块上的TX连接到bpi:bit上的P8(RX)
3. 将模块上的GND连接到bpi:bit上的GND
4. 将模块上的VIN连接到bpi:bit上的3.3V
5. SIM,RST悬空，不需要连接
![](album/BIT.JPG)
![](album/GY-MCU90615.JPG)
- 注意杜邦线颜色对应


示例代码
- [serial.py](https://github.com/aJantes/GY-MCU90615/blob/master/serial.py)

运行效果如下图：
![](album/temp.png)

通过[串口通信原理(百度百科)](https://baike.baidu.com/item/%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1/3775296?fr=aladdin)向 GY-MCU90615 传输命令，GY-MCU90615 接收到命令后返回数据