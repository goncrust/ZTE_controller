from selenium import webdriver
import time
import calendar


class Commands:

    def __init__(self, browser, ip):
        self.browser = browser
        self.ip = ip

    def shutdown(self, schedule, date):

        turn_off = self.browser.find_element_by_xpath('//*[@id="logout"]/a[1]')

        # Schedule
        timer = 0
        if schedule:
            if not date:
                timer = input("Timer (hours:minutes:seconds): ")
                hours, minutes, seconds = timer.split(":")

                timer = int(hours)*60*60 + int(minutes)*60 + int(seconds)

            if date:
                timer = input("When (day/month hour:minute:second): ")
                dday, dmonth = timer.split(" ")[0].split("/")
                dhour = timer.split(" ")[1]

                cyear = time.localtime()[0]
                cmonth = time.localtime()[1]

                dyear = cyear
                if int(dmonth) < cmonth:
                    dyear += 1

                date = str(
                    dday) + " " + str(calendar.month_abbr[int(dmonth)]) + " " + str(dyear) + " " + dhour

                timer = time.mktime(time.strptime(
                    date, "%d %b %Y %H:%M:%S")) - time.time()

        print("Waiting " + str(timer) + " seconds (" + str(time.asctime(time.localtime(time.time() + timer))
                                                           ) + ")" + " until shuting down...")
        time.sleep(timer)

        # Click
        turn_off.click()

        # Confirm
        container = self.browser.find_element_by_id('confirm-container')
        yes = container.find_element_by_xpath('//*[@id="yesbtn"]')
        yes.click()

        print("Shutdown completed.")

        return True

    def stats(self):
        self.start_page()

    def help(self):
        self.print_help()

    def print_help(self):
        print("Commands:")
        print(" stats - show current router statistics")
        print(" shutdown - turns off router (can take arguments: -sT (schedule with timer) -sD (schedule with date))")
        print(" help - prits this page")
        print(" quit - close program")

    def start_page(self):
        self.browser.get(self.ip)
