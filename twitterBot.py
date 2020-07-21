# This program is an Twitter-Bot created by Christian Bloemhof
# Start Date: June 18, 2020
# This project showcases:
#   - Selenium (creating a bot that can do something online)
#   - SQL (accessing personal database)
#   - Python
#   - Automation (this program runs twice a week automatically)

from botFuncs import *


def main():
    browser = getBrowser()
    login(browser)
    tweet_content = database()
    tweet(browser, tweet_content)
    logout(browser)
    browser.quit()


if __name__ == "__main__":
    main()
