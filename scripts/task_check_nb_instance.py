#! -*- coding: utf-8 -*-

import getpass
import os

from brome.core.model.utils import *
from mailer import Mailer
from mailer import Message

from model.basetest import BaseTest
from model.user import User

class Test(BaseTest):

    name = 'Check number instance'

    def run(self, **kwargs):

        self.info_log("Running...")

        username = self.pdriver.get_config_value('project:username')
        password = getpass.getpass(prompt='Password: ')
        user = User(self.pdriver, username, password)

        self.app.login(user)

        self.app.go_to_ec2()

        nb_instance_alive = self.app.get_nb_instance_alive()

        self.pdriver.take_screenshot("Ec2-page")

        screenshot_path = os.path.join(self.pdriver.test_instance._screenshot_dir, "Ec2-page.png")

        self.pdriver.info_log("Number of instance alive: %d"%nb_instance_alive)

        from_email = self.pdriver.get_config_value("project:from_email")
        to_email = self.pdriver.get_config_value("project:to_email")
        subject = self.pdriver.get_config_value("project:subject")
        smtp_server = self.pdriver.get_config_value("project:smtp_server")
        message = Message(From=from_email,
                          To=to_email,
                          Subject=subject)
        message.Body = "%d"%nb_instance_alive
        message.attach(screenshot_path)

        sender = Mailer(smtp_server)
        sender.send(message)
