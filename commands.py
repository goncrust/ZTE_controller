from selenium import webdriver
import time


class Commands:

    def __init__(self, browser):
        self.browser = browser

    def shutdown(self, schedule):

        turn_off = self.browser.find_element_by_xpath('//*[@id="logout"]/a[1]')

        # Timer/schedule
        if not schedule:
            timer = input("Timer (minutes:seconds): ")
            minutes, seconds = timer.split(":")
            timer = int(minutes)*60 + int(seconds)

            print("Waiting " + str(timer) + " seconds until shuting down...")
            time.sleep(timer)

        if schedule:
            pass

        # Click
        turn_off.click()

        # Confirm
        container = self.browser.find_element_by_id('confirm-container')
        yes = container.find_element_by_xpath('//*[@id="yesbtn"]')
        yes.click()

    def help(self):
        self.print_help()

    def print_help(self):
        print("Commands:\n shutdown - turns off router (can take arguments: -s (schedule))\n help - prits this page")
