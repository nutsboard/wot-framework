# -*- coding: utf-8 -*-
from periphery import GPIO

# This is for Pistachio series
GPIO_name_list = ["GPIO_5V1","GPIO_5V2","GPIO_5V3","GPIO_5V4","HP_DET","I2C_EXP_PWR","TOUCH_SEL"]
GPIO_num_list = [203,51,132,204,200,85,52]
GPIO_directon_list = [0, 0, 0, 0, 0, 0, 0]
GPIO_value_list = [0, 0, 0, 0, 0, 0, 0]


def read_GPIOLIST():
    for num in range(7):
        gpio_in = GPIO(GPIO_num_list[num])
        GPIO_directon_list[num] = gpio_in.direction
        GPIO_value_list[num] = gpio_in.read()
        gpio_in.close()

    return GPIO_name_list, GPIO_directon_list, GPIO_value_list


def write_GPIO(num, direction, val):

    # 1 == OUT, 0 == IN
    if direction == 1:
        gpio_out = GPIO(GPIO_num_list[num], "out")
        gpio_out.write(val)
        gpio_out.close()
    elif direction == 0:
        gpio_in = GPIO(GPIO_num_list[num], "in")
        gpio_in.close()
    else:
        gpio_in = GPIO(GPIO_num_list[num], "in")
        gpio_in.close()
