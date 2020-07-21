from selenium import webdriver
from passwordFile import *
import pymysql
import random as rand
import time


def getBrowser():
    browser = webdriver.Chrome('/Users/christian/Downloads/chromedriver')
    browser.get('https://twitter.com/login')
    time.sleep(3)
    return browser


def login(browser):
    username = browser.find_element_by_name('session[username_or_email]')
    password = browser.find_element_by_name('session[password]')
    username.send_keys(twitter_username)
    password.send_keys(twitter_password)
    password.submit()
    time.sleep(3)


def tweet(browser, tweet_content):
    tweet_box = browser.find_element_by_class_name('public-DraftStyleDefault-block')
    tweet_paragraph = "Today I'm feeling " + tweet_content[0] + ". " + tweet_content[1]
    tweet_box.send_keys(tweet_paragraph)
    tweet_button = browser.find_element_by_class_name(
        'css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.'
        'r-1phboty.r-rs99b7.r-1w2pmg.r-1n0xq6e.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr')
    tweet_button.click()
    time.sleep(3)


def logout(browser):
    picture_button = browser.find_element_by_class_name('css-18t94o4.css-1dbjc4n.r-1awozwy.r-sdzlij.'
                                                        'r-6koalj.r-18u37iz.r-1ny4l3l.r-1sp51qo.r-o7ynqc.r-6416eg')
    picture_button.click()
    time.sleep(3)
    logout_button = browser.find_element_by_partial_link_text('Log out')
    logout_button.click()
    logout_button = browser.find_element_by_class_name('css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty'
                                                       '.r-rs99b7.r-16y2uox.r-1w2pmg.r-1vuscfd.r-1dhvaqw.r-1ny4l3l'
                                                       '.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr')
    logout_button.click()
    time.sleep(3)


def database():
    db = pymysql.connect(hostname, database_username, database_password, database_name)
    cursor = db.cursor()
    sql = "SELECT * FROM tweets"
    cursor.execute(sql)
    feeling = rand.randint(0, 4)
    story = rand.randint(1, 5)
    results = cursor.fetchall()
    emotion = results[feeling][0]
    message = results[feeling][story]
    db.close()
    tweet_content = (emotion, message)
    return tweet_content


def inspect_element(browser):
    browser.getPageSource()
    time.sleep(3)
