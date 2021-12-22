from webbot import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request


date = "2020-02-23"
enddate = "2020-02-29"
shifts = []

web = Browser()


web.go_to("https://na.amzheimdall.com/login?clientId=WorkforceManagementG"
          "oa-prod-na&nonce=1%3AoWXDoxdtXKP_bnyyupywTgweJTjPQy1YNcpcuqFtxPM&re"
          "direct_uri=https%3A%2F%2Fna.amazonmoment.com%2Fgoa%2Fwfsm%2Fauthen"
          "ticate")

web.type("MIENKK", into="Username")
web.press(web.Key.ENTER)
web.type("Ilovespiderman01!", into="Password")
web.press(web.Key.ENTER)

page = web.go_to("https://na.amazonmoment.com/goa/wfm/associate/adjustments")

web.click("Filter", multiple=True)


