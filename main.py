#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import nuts_gpio as nuts

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/gpio")
def gpio():
    name, direction, value = nuts.read_GPIOLIST()
    info = zip(name, direction, value)

    templateData = {
        'info' : info,
    }

    return render_template('gpio.html', **templateData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
