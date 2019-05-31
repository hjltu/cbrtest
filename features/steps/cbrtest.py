"""
cbrtest.py
"""

import time
from behave import *


# visit on google
@when('open google.ru')
def step(context):
    context.google.open_url('http://www.google.com')
    time.sleep(3)

@then('search bar must be empty')
def step(context):
    search = context.google.check_search('q')
    assert search.get_attribute('value') == ''

# google search
@when('fill the search bar')
def step(context):
    search = context.google.fill_search_bar('Центральный банк РФ')
    assert search.get_attribute('value') == 'Центральный банк РФ'

@then('click the search button')
def step(context):
    context.google.click_search()
    time.sleep(5)

# open cbr.ru
@when('found link cbr.ru')
def step(context):
    context.google.find_element(url='https://www.cbr.ru/')

@then('click on the link cbr.ru')
def step(context):
    context.google.click_link(9)

# open reception
@given('checked that the site is open')
def step(context):
    site = context.cbr.check_current_url()
    assert site == 'https://www.cbr.ru/'

@when('open link "Reception"')
def step(context):
    context.cbr.find_element(url='/Reception/')
    res = context.cbr.click_link(5)
    assert res is None

@then('open section "Write thanks"')
def step(context):
    context.cbr.find_element(
        url='/Reception/Message/Register?messageType=Gratitude')
    context.cbr.click_link(5)

# Write thanks message
@when('write text')
def step(context):
    context.cbr.write_text('MessageBody', 'случайный текст')

@when('click checkbox')
def step(context):
    context.cbr.find_element(byid='_agreementFlag')
    res = context.cbr.click_link(1)
    assert res is None

@then('take a screenshot')
def step(context):
    res = context.cbr.take_screenshot('1.png')
    assert res is None

# Compare two "About" texts
@when('click on burger')
def step(context):
    context.cbr.find_element(classname='burger')
    res = context.cbr.click_link(5)
    assert res is None

@when('open link "About"')
def step(context):
    context.cbr.find_element(text='О сайте')
    res = context.cbr.click_link(5)
    assert res is None

@when('open link "Warning"')
def step(context):
    context.cbr.find_element(url='/About/warning/')
    res = context.cbr.click_link(5)
    assert res is None

@then('save warning text')
def step(context):
    context.cbr.save_text('content')

@when('change language on "en"')
def step(context):
    context.cbr.find_element(
        '/Localization/SwitchLanguage?url=%2FAbout%2Fwarning%2F&from=ru-RU&to=en-GB',
        None, None)
    res = context.cbr.click_link(1)
    assert res is None

@when('compare new text')
def step(context):
    res = context.cbr.compare_text('content')
    assert res is None

@then('take another screenshot')
def step(context):
    res = context.cbr.take_screenshot('2.png')
    assert res is None
