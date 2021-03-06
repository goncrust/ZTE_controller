from selenium import webdriver
import time
from commands import Commands


class ZTE_controller:
    def __init__(self):
        self.main()

    def main(self):

        # Start safari
        self.browser = webdriver.Safari()

        # IP
        self.ip = input("IP: ")
        self.ip = 'http://' + str(self.ip)

        # Open webpage
        self.browser.get(self.ip)

        # PASSWORD
        password_field = self.browser.find_element_by_id('mainContainer')
        self.passwd = input("Password: ")
        password_field.send_keys(self.passwd)

        # Login
        button = password_field.find_element_by_id('btnLogin')
        button.click()

        # Commands class
        self.cmds = Commands(self.browser, self.ip)

        # Enter main loop
        self.main_loop()

    # Main loop
    def main_loop(self):
        self.running = True

        while self.running:

            print("\nType help for a list of commands")
            command = input("> ")
            print("")

            self.command(command)

        self.browser.close()

    # Process command
    def command(self, command):

        result_s = False
        # shutdown rooter
        if command == "shutdown":
            result_s = self.cmds.shutdown(False, False)

        elif command == "shutdown -sT":
            result_s = self.cmds.shutdown(True, False)

        elif command == "shutdown -sD":
            result_s = self.cmds.shutdown(True, True)

        # stats
        elif command == "stats":
            self.cmds.stats()

        # help page
        elif command == "help":
            self.cmds.help()

        # quit
        elif command == "quit":
            self.running = False

        # defualt
        else:
            self.cmds.help()

        if result_s:
            self.running = False


controller = ZTE_controller()
