#! -*- coding: utf-8 -*-

from brome.core.model.stateful import Stateful

class User(Stateful):

    def __init__(self, pdriver, username, password):
        self.pdriver = pdriver
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def __repr__(self):
        return "User<username:'%s'>"%self.get_username()
