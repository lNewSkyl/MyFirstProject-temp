import sys
from collections import Counter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt, QTimer, QTime
import sqlite3
import time
import datetime
import random
from random import randint
from pyowm import OWM
import requests
from bs4 import BeautifulSoup
from tkinter import *
import calendar
import platform
import os
import sys, time, threading
import vlc

# conn = sqlite3.connect(r'C:\Users\r80\YandexDisk\Курсы Python\7урок\orders.db')
conn = sqlite3.connect(r'C:\Users\NewSky\YandexDisk\Курсы Python\7урок\orders.db')
cursor = conn.cursor()


class Main(QMainWindow):  # ОКНО АВТОРИЗАЦИИ

    def __init__(self):
        super().__init__()
        self.initUI()  # передали функцию.

    def initUI(self):
        self.setFixedSize(450, 480)  # размеры окна
        self.setWindowTitle('Лучшая программа в мире')

        self.setWindowIcon(QIcon('1.ico'))

        font_Serif1 = QFont()
        font_Serif1.setFamily(u"MS Serif")
        font_Serif1.setPointSize(14)
        font_Serif1.setBold(True)

        font_Serif2_bold = QFont()
        font_Serif2_bold.setFamily(u'Comic Sans MS')
        font_Serif2_bold.setPointSize(20)
        font_Serif2_bold.setBold(True)
        font_Serif2_bold.setItalic(True)

        hbox = QHBoxLayout(self)
        pixmap1 = QPixmap('22.png')
        lbl = QLabel(self)
        lbl.setPixmap(pixmap1)
        lbl.setGeometry(310, 5, 150, 10)
        hbox.addWidget(lbl)

        self.label_morda = QLabel(self)
        self.label_morda.setGeometry(20, 10, 400, 200)
        self.label_morda.setFont(font_Serif2_bold)
        self.label_morda.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.label_morda.setText('Да это же лучшая про-\nграмма в мире!!1!')

        self.btn_kalk = QPushButton("Калькулятор", self)  # кнопка входа
        self.btn_kalk.setGeometry(5, 200, 440, 30)
        self.btn_kalk.setFont(font_Serif1)
        self.btn_kalk.clicked.connect(self.btn_kalk_func)

        # self.ugadaichislo = QPushButton("Угадай число", self)  # кнопка входа
        # self.ugadaichislo.setGeometry(5, 235, 440, 30)
        # self.ugadaichislo.setFont(font_Serif1)
        # self.ugadaichislo.clicked.connect(self.ugadaichislo_func)

        self.btn_notes = QPushButton("Заметки", self)  # кнопка входа
        self.btn_notes.setGeometry(5, 270, 440, 30)
        self.btn_notes.setFont(font_Serif1)
        self.btn_notes.clicked.connect(self.btn_notes_func)

        self.btn_weather = QPushButton("Погода", self)  # кнопка входа
        self.btn_weather.setGeometry(5, 305, 440, 30)
        self.btn_weather.setFont(font_Serif1)
        self.btn_weather.clicked.connect(self.btn_weather_func)

        self.btn_radio = QPushButton("Радио", self)  # кнопка входа
        self.btn_radio.setGeometry(5, 340, 440, 30)
        self.btn_radio.setFont(font_Serif1)
        self.btn_radio.clicked.connect(self.btn_radio_func)

        self.btn_news = QPushButton("Новости", self)  # кнопка входа
        self.btn_news.setGeometry(5, 375, 440, 30)
        self.btn_news.setFont(font_Serif1)
        self.btn_news.clicked.connect(self.btn_news_func)

        self.btn_calendar = QPushButton("Календарь", self)  # кнопка входа
        self.btn_calendar.setGeometry(5, 410, 440, 30)
        self.btn_calendar.setFont(font_Serif1)
        self.btn_calendar.clicked.connect(self.btn_calendar_func)

        self.btn_clock = QPushButton("Часы", self)  # кнопка входа
        self.btn_clock.setGeometry(5, 235, 440, 30)
        self.btn_clock.setFont(font_Serif1)
        self.btn_clock.clicked.connect(self.btn_clock_func)

    def btn_kalk_func(self):
        self.hide()
        self.a = Calculon()
        self.a.show()

    # def ugadaichislo_func(self):
    #     self.hide()
    #     self.a = Ugadaichislo()
    #     self.a.show()

    def btn_notes_func(self):
        self.hide()
        self.a = Zametki()
        self.a.show()

    def btn_weather_func(self):
        self.hide()
        self.a = Weather()
        self.a.show()

    def btn_radio_func(self):
        self.hide()
        self.a = Radio()
        self.a.show()

    def btn_news_func(self):
        self.hide()
        self.a = News()
        self.a.show()

    def btn_calendar_func(self):
        self.hide()
        self.a = Calendar()
        self.a.show()

    def btn_clock_func(self):
        self.hide()
        self.a = Clock()
        self.a.show()


# class Ugadaichislo(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Угадай число")
#         self.initUI()  # передали функцию.
#         self.setWindowIcon(QIcon('wopros.png'))
#
#     def initUI(self):
#
#         self.setFixedSize(350, 580)  # размеры окна
#         self.font = QFont()  # создаём объект шрифта
#         self.font.setPointSize(15)
#
#         self.labeltop = QLabel(self)
#         self.labeltop.setFont(self.font)
#         self.labeltop.setGeometry(20, 50, 325, 200)
#         self.labeltop.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
#
#         self.strokawwoda = QLineEdit(self)
#         self.strokawwoda.setGeometry(10, 10, 100, 35)
#         self.strokawwoda.move(125, 300)  # перенос строки
#         self.strokawwoda.setText("")
#         self.strokawwoda.hide()
#
#         self.glavnoeokno()
#
#     def glavnoeokno(self):
#
#         self.number_popytka = 1
#         self.labeltop.setText("Компьютер загадал число \nот 0 до 100. \nУгадайте его за 7 попыток ")
#         self.labeltop.setWordWrap(True)
#
#         self.btn_vvod = QPushButton('Старт', self)
#         self.btn_vvod.resize(200, 100)
#         self.btn_vvod.move(75, 400)
#
#         self.btn_vvod.clicked.connect(self.igra_func)
#         self.number_to_gues = random.randint(0, 100)
#
#     def igra_func(self):
#         self.btn_vvod.clicked.connect(self.proverka)
#         self.strokawwoda.show()
#         self.wwod = self.strokawwoda.text()
#         self.btn_vvod.setText('Проверить')
#
#     def konec(self):
#         self.btn_vvod.clicked.connect(self.initUI)
#         self.labeltop.setText(f'Вы исчерпали попытки. \nGame over.\nБыло загадано {self.number_to_gues}')
#         self.labeltop.setWordWrap(True)
#         self.btn_vvod.setText('Заново')
#
#     def proverka(self):
#
#         if self.wwod.isdigit():
#             if int(self.wwod) < self.number_to_gues:
#                 self.btn_vvod.clicked.connect(self.igra_func)
#                 self.labeltop.setText('Загаданное число \nбольше, \nвведите другое \nчисло ')
#                 self.labeltop.setWordWrap(True)
#                 self.number_popytka += 1
#                 if self.number_popytka == 20:
#                     self.konec()
#
#             if int(self.wwod) > self.number_to_gues:
#                 self.btn_vvod.clicked.connect(self.igra_func)
#                 self.labeltop.setText("Загаданное число \nменьше, \nвведите другое \nчисло ")
#                 self.labeltop.setWordWrap(True)
#                 self.number_popytka += 1
#                 if self.number_popytka == 20:
#                     self.konec()
#
#             if int(self.wwod) == self.number_to_gues:
#                 self.labeltop.setText("Угадал")
#                 self.btn_vvod.setText('Заново')
#                 self.btn_vvod.clicked.connect(self.glavnoeokno)


class Clock(QLCDNumber):

    def __init__(self):
        super().__init__()
        top = 400
        left = 400
        width = 900
        height = 600
        self.setWindowTitle("Гадзiннiк")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon('clock.png'))
        self.initUI()  # передали функцию.

    def initUI(self):
        palete = self.palette()
        palete.setColor(palete.WindowText, QColor(204, 204, 0))
        self.setPalette(palete)

        palete.setColor(palete.Light, QColor(255, 0, 0))
        self.setSegmentStyle(QLCDNumber.Filled)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]
        self.display(text)


class Calculon(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кал")
        self.initUI()  # передали функцию.
        app.setStyleSheet("QLabel{font-size: 25pt;} {bold}")
        self.setWindowIcon(QIcon('calc.png'))

    def initUI(self):

        self.strokavivoda = ''
        self.history = []
        self.pustoispisok = ''
        self.proverkatruefalse = True

        self.setFixedSize(325, 580)  # размеры окна
        self.formula = "0"
        self.font = QFont()  # создаём объект шрифта
        self.font.setPointSize(20)

        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setGeometry(15, 5, 325, 95)
        self.label2 = QLabel(self)
        self.label2.hide()
        self.label2.setGeometry(15, 20, 300, 550)
        style_1 = 'border:3px solid black;'  # разукрасили рамку
        self.label2.setStyleSheet(style_1)
        self.label2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label2.setStyleSheet("QLabel{font-size: 12pt;} {bold}")

        self.btn_history = QPushButton('History', self)
        self.btn_history.resize(50, 20)
        self.btn_history.move(275, 0)
        self.btn_history.clicked.connect(self.f_istoria)

        self.btn_clear_history = QPushButton('Clear Hist', self)
        self.btn_clear_history.hide()
        self.btn_clear_history.resize(60, 20)
        self.btn_clear_history.move(0, 0)
        self.btn_clear_history.clicked.connect(self.f_clear_istoria)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(75, 75)
        self.num_1.move(5, 340)
        self.num_1.clicked.connect(self.vvod)
        self.num_1.setStyleSheet("background-color: snow")
        self.num_1.setFont(self.font)
        self.num_1.setShortcut('1')

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(75, 75)
        self.num_2.move(85, 340)
        self.num_2.clicked.connect(self.vvod)
        self.num_2.setStyleSheet("background-color: snow")
        self.num_2.setFont(self.font)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(75, 75)
        self.num_3.move(165, 340)
        self.num_3.clicked.connect(self.vvod)
        self.num_3.setStyleSheet("background-color: snow")
        self.num_3.setFont(self.font)

        self.num_div = QPushButton('/', self)
        self.num_div.resize(75, 75)
        self.num_div.move(245, 180)
        self.num_div.clicked.connect(self.vvod)
        self.num_div.setFont(self.font)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(75, 75)
        self.num_4.move(5, 260)
        self.num_4.clicked.connect(self.vvod)
        self.num_4.setStyleSheet("background-color: snow")
        self.num_4.setFont(self.font)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(75, 75)
        self.num_5.move(85, 260)
        self.num_5.clicked.connect(self.vvod)
        self.num_5.setStyleSheet("background-color: snow")
        self.num_5.setFont(self.font)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(75, 75)
        self.num_6.move(165, 260)
        self.num_6.clicked.connect(self.vvod)
        self.num_6.setStyleSheet("background-color: snow")
        self.num_6.setFont(self.font)

        self.num_mul = QPushButton('*', self)
        self.num_mul.resize(75, 75)
        self.num_mul.move(245, 260)
        self.num_mul.setFont(self.font)
        self.num_mul.clicked.connect(self.vvod)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(75, 75)
        self.num_7.move(5, 180)
        self.num_7.clicked.connect(self.vvod)
        self.num_7.setStyleSheet("background-color: snow")
        self.num_7.setFont(self.font)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(75, 75)
        self.num_8.move(85, 180)
        self.num_8.clicked.connect(self.vvod)
        self.num_8.setStyleSheet("background-color: snow")
        self.num_8.setFont(self.font)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(75, 75)
        self.num_9.move(165, 180)
        self.num_9.clicked.connect(self.vvod)
        self.num_9.setStyleSheet("background-color: snow")
        self.num_9.setFont(self.font)

        self.num_plus = QPushButton('+', self)
        self.num_plus.resize(75, 75)
        self.num_plus.move(245, 420)
        self.num_plus.setFont(self.font)
        self.num_plus.clicked.connect(self.vvod)

        self.num_C = QPushButton('C', self)
        self.num_C.resize(103, 75)
        self.num_C.move(5, 500)
        self.num_C.clicked.connect(self.c_knopka)
        self.num_C.setFont(self.font)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(75, 75)
        self.num_0.move(85, 420)
        self.num_0.clicked.connect(self.vvod_0)
        self.num_0.setStyleSheet("background-color: snow")
        self.num_0.setFont(self.font)

        self.num_minus = QPushButton('-', self)
        self.num_minus.resize(75, 75)
        self.num_minus.move(245, 340)
        self.num_minus.setFont(self.font)
        self.num_minus.clicked.connect(self.vvod)

        self.num_dot = QPushButton('.', self)
        self.num_dot.resize(75, 75)
        self.num_dot.move(165, 420)
        self.num_dot.setStyleSheet("background-color: snow")
        self.num_dot.clicked.connect(self.f_tochka)
        self.num_dot.setFont(self.font)

        self.num_p_m = QPushButton('±', self)
        self.num_p_m.resize(75, 75)
        self.num_p_m.move(5, 420)
        self.num_p_m.setStyleSheet("background-color: snow")
        self.num_p_m.setFont(self.font)
        self.num_p_m.clicked.connect(self.f_plusminus)

        self.num_eq = QPushButton('=', self)
        self.num_eq.resize(103, 75)
        self.num_eq.move(216, 500)
        self.num_eq.clicked.connect(self.ravno)
        self.num_eq.setStyleSheet("background-color: gray")
        self.num_eq.setFont(self.font)

        self.udalenie = QPushButton('←', self)
        self.udalenie.resize(103, 75)
        self.udalenie.move(111, 500)
        self.udalenie.clicked.connect(self.udalen)
        self.udalenie.setFont(self.font)

        self.skob_grusn = QPushButton('(', self)
        self.skob_grusn.resize(75, 75)
        self.skob_grusn.move(5, 100)
        self.skob_grusn.setFont(self.font)
        self.skob_grusn.clicked.connect(self.vvod)

        self.skob_vesel = QPushButton(')', self)
        self.skob_vesel.resize(75, 75)
        self.skob_vesel.move(85, 100)
        self.skob_vesel.setFont(self.font)
        self.skob_vesel.clicked.connect(self.vvod)

        self.kvadrat = QPushButton('x²', self)
        self.kvadrat.resize(75, 75)
        self.kvadrat.move(165, 100)
        self.kvadrat.setFont(self.font)
        self.kvadrat.clicked.connect(self.f_kvadrat)

        self.koren = QPushButton('√', self)
        self.koren.resize(75, 75)
        self.koren.move(245, 100)
        self.koren.clicked.connect(self.f_koren)
        self.koren.setFont(self.font)

    def vvod(self):
        self.num = self.sender().text()
        self.strokavivoda += self.num
        self.label.setText(self.strokavivoda)

    def vvod_0(self):
        if len(self.strokavivoda) > 1 or self.label.text() != '0':
            self.num = self.sender().text()
            self.strokavivoda += self.num
            self.label.setText(self.strokavivoda)
        else:
            return

    def c_knopka(self):
        self.strokavivoda = ''
        self.label.setText("0")

    def ravno(self):

        try:
            self.ans = eval(self.strokavivoda)
            self.history.append(self.strokavivoda + '=')
            self.label.setText(str(self.ans))
            self.strokavivoda = str(self.ans)
            self.history.append(self.strokavivoda + '\n')

        except:
            self.label.setText("Wrong Input")

    def udalen(self):

        if len(self.strokavivoda) > 1 and self.label.setText != "Wrong Input":
            self.strokavivoda = self.strokavivoda[:len(self.strokavivoda) - 1]
            self.label.setText(self.strokavivoda)

        elif len(self.strokavivoda) == 1:
            self.strokavivoda = ''
            self.label.setText('0')

        elif self.label.text() == "Wrong Input":
            self.label.setText('0')

    def f_koren(self):

        try:
            self.kor = self.label.text() + "** .5"
            self.ans = eval(self.kor)
            self.history.append('√' + self.strokavivoda + "=")
            self.label.setText(str(self.ans))
            self.strokavivoda = str(self.ans)
            self.history.append(self.strokavivoda + "\n")
        except:
            self.label.setText("Wrong Input")

    def f_kvadrat(self):

        try:
            self.kor = self.label.text() + "**2"
            self.ans = eval(self.kor)
            self.history.append(self.strokavivoda + "*" + self.strokavivoda + "=")
            self.label.setText(str(self.ans))
            self.strokavivoda = str(self.ans)
            self.history.append(self.strokavivoda + "\n")
        except:
            self.label.setText("Wrong Input")

    def f_plusminus(self):

        if self.label.text() != "0":
            if self.label.text()[0] == '-':
                self.znach = self.label.text()[1:]
            else:
                self.znach = f'-{self.label.text()}'
            self.strokavivoda = self.znach
            self.label.setText(str(self.strokavivoda))

    def f_tochka(self):

        if self.label.text() == '0':
            self.num = "0" + self.sender().text()
            self.strokavivoda += self.num
            self.label.setText(self.strokavivoda)
        else:
            self.num = self.sender().text()
            self.strokavivoda += self.num
            self.label.setText(self.strokavivoda)

    def f_istoria(self):

        for i in self.history:
            for j in i:
                self.pustoispisok += j
        self.label2.setText(self.pustoispisok)
        self.pustoispisok = ""

        if self.proverkatruefalse:
            self.label.hide()
            self.num_1.hide()
            self.num_2.hide()
            self.num_3.hide()
            self.num_div.hide()
            self.num_4.hide()
            self.num_5.hide()
            self.num_6.hide()
            self.num_mul.hide()
            self.num_7.hide()
            self.num_8.hide()
            self.num_9.hide()
            self.num_plus.hide()
            self.num_C.hide()
            self.num_0.hide()
            self.num_minus.hide()
            self.num_dot.hide()
            self.num_p_m.hide()
            self.num_eq.hide()
            self.udalenie.hide()
            self.skob_grusn.hide()
            self.skob_vesel.hide()
            self.kvadrat.hide()
            self.koren.hide()
            self.label2.show()
            self.btn_clear_history.show()
            self.proverkatruefalse = False


        elif self.proverkatruefalse == False:
            self.label.show()
            self.num_1.show()
            self.num_2.show()
            self.num_3.show()
            self.num_div.show()
            self.num_4.show()
            self.num_5.show()
            self.num_6.show()
            self.num_mul.show()
            self.num_7.show()
            self.num_8.show()
            self.num_9.show()
            self.num_plus.show()
            self.num_C.show()
            self.num_0.show()
            self.num_minus.show()
            self.num_dot.show()
            self.num_p_m.show()
            self.num_eq.show()
            self.udalenie.show()
            self.skob_grusn.show()
            self.skob_vesel.show()
            self.kvadrat.show()
            self.koren.show()
            self.label2.hide()
            self.btn_clear_history.hide()
            self.proverkatruefalse = True

    def f_clear_istoria(self):

        self.history = []
        for i in self.history:
            for j in i:
                self.pustoispisok += j
        self.label2.setText(self.pustoispisok)
        self.pustoispisok = ""


class Weather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Погода!")
        self.initUI()  # передали функцию.
        app.setStyleSheet("QLabel{font-size: 14pt;} {bold}")
        self.setWindowIcon(QIcon('weather.png'))

    def initUI(self):

        self.setFixedSize(480, 260)

        font_Serif1 = QFont()
        font_Serif1.setFamily(u"MS Serif")
        font_Serif1.setPointSize(15)
        font_Serif1.setBold(True)

        font_Serif2_bold = QFont()
        font_Serif2_bold.setFamily(u'Comic Sans MS')
        font_Serif2_bold.setPointSize(15)
        font_Serif2_bold.setBold(True)
        font_Serif2_bold.setItalic(True)

        self.label = QLabel(self)
        self.label.setText("Введите город, \nв котором хотите узнать погоду:")
        self.label.setGeometry(0, 5, 480, 80)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.btn_vvod = QPushButton('Узнать погоду', self)
        self.btn_vvod.resize(150, 50)
        self.btn_vvod.move(60, 140)
        self.btn_vvod.clicked.connect(self.vivod_pogodi)

        self.strokawwoda = QLineEdit(self)
        self.strokawwoda.setGeometry(150, 50, 150, 20)
        self.strokawwoda.move(60, 100)  # перенос строки
        self.strokawwoda.setText("")
        self.strokawwoda.returnPressed.connect(self.vivod_pogodi)

        self.labelvivod = QLabel(self)
        self.labelvivod.setGeometry(200, 50, 300, 200)
        self.labelvivod.setFont(font_Serif2_bold)
        self.labelvivod.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)

    def vivod_pogodi(self):

        place = self.strokawwoda.text()
        try:
            owm = OWM('81d46dae5d81269c5173584ee79c5a4d')
            mgr = owm.weather_manager()

            observation = mgr.weather_at_place(place)
            w = observation.weather

            wind = w.wind()['speed']  # {'speed': 4.6, 'deg': 330}
            wlazhn = w.humidity  # 87
            temper = w.temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

            self.labelvivod.setText(f'Ветер {wind} м/с.\nТемпература {temper}°.\nВлажность {wlazhn}%.')
        except:
            self.labelvivod.setText('Неправильно введен \nгород.')


class News(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рандомные новости")
        app.setStyleSheet("QLabel{font-size: 14pt;} {bold}")
        self.setWindowIcon(QIcon('news.png'))
        self.initUI()  # передали функцию.

    def initUI(self):
        self.setFixedSize(480, 260)
        self.btn_vvod = QPushButton('Запили новость', self)
        self.btn_vvod.resize(440, 30)
        self.btn_vvod.move(20, 220)
        self.btn_vvod.clicked.connect(self.vivod_novosti_func)

        self.labelvivod = QLabel(self)
        self.labelvivod.setGeometry(10, 10, 450, 200)
        self.labelvivod.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.labelvivod.setWordWrap(True)

        self.url = "https://www.rbc.ru/story/5eeb458f9a79472a78dda964"  # не забывать добавлять S в конце http
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')  # подключили инструмент для парсинга
        self.table = self.soup.find_all('span', attrs={'class': 'item__title rm-cm-item-text'})
        self.howmuchnews = len(self.table) - 1

    def vivod_novosti_func(self):
        randomwalue = random.randint(0, self.howmuchnews)

        for i in self.table[randomwalue]:
            self.labelvivod.setText(i[69:])
            break


class Calendar():
    def __init__(self):
        super().__init__()

        self.root = Tk()
        self.root.title('Календарище')
        self.root.iconbitmap(r'calendar.ico')
        self.days = []
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.prew_button = Button(self.root, text='<', command=self.prew)
        self.prew_button.grid(row=0, column=0, sticky='nsew')
        self.next_button = Button(self.root, text='>', command=self.next)
        self.next_button.grid(row=0, column=6, sticky='nsew')
        self.info_label = Label(self.root, text='0', width=1, height=1,
                                font=('Verdana', 16, 'bold'), fg='blue')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

        for n in range(7):
            self.lbl = Label(self.root, text=calendar.day_abbr[n], width=1, height=1,
                             font=('Verdana', 10, 'normal'), fg='darkblue')
            self.lbl.grid(row=1, column=n, sticky='nsew')
        for row in range(6):
            for col in range(7):
                self.lbl = Label(self.root, text='0', width=4, height=2,
                                 font=('Verdana', 16, 'bold'))
                self.lbl.grid(row=row + 2, column=col, sticky='nsew')
                self.days.append(self.lbl)
        self.fill()
        self.root.mainloop()

    def prew(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def fill(self):
        self.info_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
        self.month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            self.prew_month_days = calendar.monthrange(self.year - 1, 12)[1]
        else:
            self.prew_month_days = calendar.monthrange(self.year, self.month - 1)[1]
        self.week_day = calendar.monthrange(self.year, self.month)[0]
        for n in range(self.month_days):
            self.days[n + self.week_day]['text'] = n + 1
            self.days[n + self.week_day]['fg'] = 'black'
            if self.year == self.now.year and self.month == self.now.month and n == self.now.day - 1:
                self.days[n + self.week_day]['background'] = 'green'
            else:
                self.days[n + self.week_day]['background'] = 'lightgray'
        for n in range(self.week_day):
            self.days[self.week_day - n - 1]['text'] = self.prew_month_days - n
            self.days[self.week_day - n - 1]['fg'] = 'gray'
            self.days[self.week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6 * 7 - self.month_days - self.week_day):
            self.days[self.week_day + self.month_days + n]['text'] = n + 1
            self.days[self.week_day + self.month_days + n]['fg'] = 'gray'
            self.days[self.week_day + self.month_days + n]['background'] = '#f3f3f3'


class Zametki(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Почти гугл notes")
        app.setStyleSheet("QLabel{font-size: 14pt;} {bold}")
        self.setWindowIcon(QIcon('note.png'))
        self.initUI()  # передали функцию.

    def initUI(self):

        self.setFixedSize(860, 480)
        self.conn = sqlite3.connect(r'C:\Users\r80\YandexDisk\Курсы Python\7урок\orders.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''SELECT*FROM tab_10''')
        self.k = self.cursor.fetchall()
        self.zametka = ''
        for i in self.k:
            for j in i:
                self.zametka += j
                self.zametka += "\n"

        self.labelvivod = QLabel(self)
        self.labelvivod.show()
        self.labelvivod.setGeometry(10, 50, 840, 420)
        self.labelvivod.setAlignment(Qt.AlignHCenter | Qt.AlignCenter)
        self.labelvivod.setWordWrap(True)
        style_1 = 'border:3px solid cyan;'  # разукрасили рамку
        self.labelvivod.setStyleSheet(style_1)
        self.labelvivod.setText(self.zametka)

        add_to_bd = QAction(QIcon('toolbar\open.png'), 'Добавить новую заметку', self)
        exitAction = QAction(QIcon('toolbar\exit.png'), 'Выход из программы', self)
        editAction = QAction(QIcon('toolbar\edit.png'), 'Редактировать заметки', self)
        add_to_bd.triggered.connect(self.okno_dobawleniya_v_bd)
        exitAction.triggered.connect(qApp.quit)
        editAction.triggered.connect(self.okno_redactirovaniya_bd)

        self.toolbar = self.addToolBar('')
        self.toolbar.show()
        self.toolbar.addAction(add_to_bd)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(exitAction)

        self.strokawwoda = QLineEdit(self)
        self.strokawwoda.setGeometry(10, 20, 380, 50)
        self.strokawwoda.setText("")
        self.strokawwoda.hide()
        self.strokawwoda.returnPressed.connect(self.dobavlenie_v_bd_func)

        self.btn_dobavit = QPushButton('Добавить заметку', self)
        self.btn_dobavit.resize(380, 50)
        self.btn_dobavit.move(10, 80)
        self.btn_dobavit.clicked.connect(self.dobavlenie_v_bd_func)
        self.btn_dobavit.hide()

        self.btn_nazad = QPushButton('Назад', self)
        self.btn_nazad.resize(380, 50)
        self.btn_nazad.move(10, 140)
        self.btn_nazad.clicked.connect(self.mainMenu)
        self.btn_nazad.hide()

        self.strokaedit = QLineEdit(self)
        self.strokaedit.setGeometry(30, 200, 800, 30)
        self.strokaedit.hide()

        self.btn_delete = QPushButton("Удалить заметку", self)
        self.btn_delete.resize(390, 40)
        self.btn_delete.move(30, 300)
        self.btn_delete.clicked.connect(self.udalenie_knopkoi_func)
        self.btn_delete.hide()

        self.btn_redactirovat = QPushButton("Редактировать заметку", self)
        self.btn_redactirovat.resize(390, 40)
        self.btn_redactirovat.move(440, 300)
        self.btn_redactirovat.clicked.connect(self.redactirovanie_knopkoi_func)
        self.btn_redactirovat.hide()

        self.btn_v_menu = QPushButton("Назад", self)
        self.btn_v_menu.resize(400, 40)
        self.btn_v_menu.move(220, 350)
        self.btn_v_menu.clicked.connect(self.nazad_iz_okna_redact)
        self.btn_v_menu.hide()

        self.combobox = QComboBox(self)
        self.combobox.setGeometry(10, 20, 550, 20)
        self.combobox.move(150, 150)
        self.combobox.hide()

    def okno_dobawleniya_v_bd(self):
        self.setFixedSize(400, 200)
        self.labelvivod.hide()
        self.toolbar.hide()
        self.strokawwoda.show()
        self.btn_dobavit.show()
        self.btn_nazad.show()

    def dobavlenie_v_bd_func(self):
        self.zametka = self.strokawwoda.text()
        self.cursor.execute('''INSERT INTO tab_10 VALUES (?)''', (self.zametka,))
        self.conn.commit()
        self.strokawwoda.hide()
        self.btn_dobavit.hide()
        self.btn_nazad.hide()
        self.initUI()

    def mainMenu(self):
        self.strokawwoda.hide()
        self.btn_dobavit.hide()
        self.btn_nazad.hide()
        self.initUI()

    def okno_redactirovaniya_bd(self):
        self.labelvivod.hide()
        self.toolbar.hide()
        self.cursor.execute('''SELECT*FROM tab_10''')
        self.k = self.cursor.fetchall()
        self.combobox.show()
        self.combobox.clear()
        self.s = ''
        for i in self.k:
            for j in i:
                self.s += j
                self.combobox.addItem(self.s)
                self.s = ''
        self.combobox.activated[str].connect(self.onActivated)
        self.strokaedit.show()
        self.btn_delete.show()
        self.btn_redactirovat.show()
        self.btn_v_menu.show()

    def udalenie_knopkoi_func(self):
        self.cursor.execute('''DELETE FROM tab_10 WHERE id=?''', (self.combobox.currentText(),))
        self.conn.commit()
        self.okno_redactirovaniya_bd()

    def redactirovanie_knopkoi_func(self):

        self.cursor.execute('''DELETE FROM tab_10 WHERE id=?''', (self.combobox.currentText(),))
        self.cursor.execute('''INSERT INTO tab_10 VALUES (?)''', (self.strokaedit.text(),))
        self.conn.commit()
        self.okno_redactirovaniya_bd()

    def onActivated(self):
        self.strokaedit.setText(self.combobox.currentText())

    def nazad_iz_okna_redact(self):
        self.strokaedit.hide()
        self.btn_delete.hide()
        self.btn_redactirovat.hide()
        self.btn_v_menu.hide()
        self.combobox.hide()
        self.initUI()


class Radio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canals = ["АвтоРадио|https://ic7.101.ru:8000/v3_1?29f32f43",
                       "RockFM|https://nashe1.hostingradio.ru:80/rock-128.mp3?124e",
                       "НашеРадио|https://nashe1.hostingradio.ru/nashe-128.mp3?6717",
                       "RadioRecord|https://air.radiorecord.ru:805/rr_320?edc6"]
        self.setWindowTitle("Радио")
        app.setStyleSheet("QLabel{font-size: 14pt;} {bold}")
        self.setWindowIcon(QIcon('radio.png'))
        self.setFixedSize(260, 130)


        self.combo = QComboBox(self)
        self.combo.move(20, 30)

        for x in self.canals:
            self.mas = x.split('|')
            self.name = self.mas[0]
            self.canal = self.mas[1]
            self.combo.addItem(self.name)

        self.play_btn = QPushButton('Play', self)
        self.play_btn.move(150, 10)
        self.play_btn.clicked.connect(self.playradio_func)

        self.stop_btn = QPushButton('Exit', self)
        self.stop_btn.move(150, 40)
        self.stop_btn.clicked.connect(self.stopradio_func)

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.setGeometry(20, 80, 230, 30)
        self.sld.valueChanged[int].connect(self.changeValue)


    def changeValue(self, value):
        try:
            self.ppp.audio_set_volume(value)
        except AttributeError:
            pass


    def playradio_func(self):

        self.source = self.combo.currentText()
        if self.source == 'АвтоРадио':
            time.sleep(1)
            for x in self.canals:
                if self.source in x:
                    self.mas = x.split('|')
                    self.canal = self.mas[1].strip()
            self.ppp = vlc.MediaPlayer(self.canal)
            self.ppp.audio_set_volume(50)
            self.ppp.play()

        elif self.source == 'RockFM':
            time.sleep(1)
            for x in self.canals:
                if self.source in x:
                    self.mas = x.split('|')
                    self.canal = self.mas[1].strip()
            self.ppp = vlc.MediaPlayer(self.canal)
            self.ppp.audio_set_volume(50)
            self.ppp.play()

        elif self.source == 'НашеРадио':
            time.sleep(1)
            for x in self.canals:
                if self.source in x:
                    self.mas = x.split('|')
                    self.canal = self.mas[1].strip()
            self.ppp = vlc.MediaPlayer(self.canal)
            self.ppp.audio_set_volume(50)
            self.ppp.play()

        elif self.source == 'RadioRecord':
            time.sleep(1)
            for x in self.canals:
                if self.source in x:
                    self.mas = x.split('|')
                    self.canal = self.mas[1].strip()
            self.ppp = vlc.MediaPlayer(self.canal)
            self.ppp.audio_set_volume(50)
            self.ppp.play()


    def stopradio_func(self):
        self.source = self.combo.currentText()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
