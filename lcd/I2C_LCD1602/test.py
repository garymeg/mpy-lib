'''
    I2C LCD1602 demo

    Author: shaoziyang
    Date:   2018.2

    http://www.micropython.org.cn

'''
from machine import I2C, Pin
from mp_i2c_lcd1602 import LCD1602
from time import sleep_ms

sda = Pin(0)
scl = Pin(1)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)

LCD = LCD1602(i2c)

LCD.puts("I2C LCD1602")
n = 0
while 1:
    LCD.puts(n, 0, 1)
    n += 1
    sleep_ms(1000)

