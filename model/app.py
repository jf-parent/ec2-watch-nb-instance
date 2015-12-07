#! -*- coding: utf-8 -*-

class App(object):
    def __init__(self, pdriver):
        self.pdriver = pdriver

    def go_to_login(self):
        self.pdriver.info_log("Going to the login page...")

        self.pdriver.get("https://console.aws.amazon.com/console/home")
    
    def go_to_ec2(self):
        self.pdriver.info_log("Going to the ec2 page...")

        self.pdriver.get("https://console.aws.amazon.com/ec2/v2/home?region=us-east-1")

    def login(self, user):
        self.pdriver.info_log("Login with %s..."%user)

        self.go_to_login()

        self.pdriver.wait_until_visible('sv:login_button')

        self.pdriver.find('sv:login_username_input').send_keys(user.get_username())
        self.pdriver.find('sv:login_password_input').send_keys(user.get_password())

        self.pdriver.find('sv:login_button').click()
        self.pdriver.wait_until_not_visible('sv:login_button', timeout = 10)

    def get_nb_instance_alive(self):
        self.pdriver.info_log("Getting the number of instance alive...")

        self.pdriver.wait_until_visible("sv:nb_instance_alive_div", timeout = 10)

        nb_instance_alive = int(self.pdriver.find("sv:nb_instance_alive_div").text)
        
        return nb_instance_alive
