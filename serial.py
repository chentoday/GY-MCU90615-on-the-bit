from  machine import UART


uart=UART(2)
uart.init(9600, bits=8, parity=None, stop=1)
b1=b'\xA5\xAE\x53'     # 配置 9600 波特率
b2=b'\xA5\xAF\x54'     # 配置 115200 波特率(默认)
b3=b'\xA5\x15\xBA'     # 查询输出
b4=b'\xA5\x45\xEA'     # 连续输出
uart.write(b4)
while True:
    if uart.any():
        t=bytes(uart.read())
        print("The target temperature is %d"%((t[4]*256+t[5])/100))  #计算出目标温度
        print("---------------------")
        print("The environment temperature is %d"%((t[6]*256+t[7])/100))    #计算出环境温度
        print("---------------------")

# 每次重新配置波特率后都需要断电重起bpi:bit