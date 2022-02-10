import robin_stocks.robinhood
import robin_stocks.robinhood as rs
import pyotp
import pandas as pd
import csv
import datetime
from pprint import pprint
import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text="Julio")

if __name__ == '__main__':
    MyApp().run()