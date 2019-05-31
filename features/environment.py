"""
environment.py
"""

from selenium import webdriver
from features.browser import Browser, Google, Cbr


def before_all(context):
    context.browser = Browser()
    context.google = Google()
    context.cbr = Cbr()

def after_all(context):
    context.browser.close()
