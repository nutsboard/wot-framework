#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import nuts_gpio as nuts

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/gpio", methods=['GET' , 'POST'])
def gpio():

    if request.method == 'POST':
        name = request.form['action']
        if name == "GPIO_5V1":
            num=0
        elif name == "GPIO_5V2":
            num=1
        elif name == "GPIO_5V3":
            num=2
        elif name == "GPIO_5V4":
            num=3
        elif name == "HP_DET":
            num=4
        elif name == "I2C_EXP_PWR":
            num=5
        elif name == "TOUCH_SEL":
            num=6

        val = request.form.get('value')
        val_ret = False
        if val == "None":
            val_ret = False
        elif val == "on":
            val_ret = True

        dir = request.form.get('direction')
        dir_ret = 0
        if dir == "None":
            dir_ret = 0
        elif dir == "on":
            dir_ret = 1

       nuts.write_GPIO(num, dir_ret, val_ret)

    name, direction, value = nuts.read_GPIOLIST()
    info = zip(name, direction, value)

    templateData = {
        'info' : info,
    }

    return render_template('gpio.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
