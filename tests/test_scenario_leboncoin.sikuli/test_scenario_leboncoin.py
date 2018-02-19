# -*- coding:utf-8 -*-

"""
    Test Scenario: Leboncoin
    ==============================

    What is tested here ?
    ---------------------

    1. As a visitor I can create an account
    2. As a user I can login
    3. As an unregistered user I can't login

    Dependencies
    ------------

    Describe dependencies.
    Dependencies are important to be known as if the scenario fails,
    we should unit test the dependencies before giving a status of the application !

    - src/objects/Chrome.sikuli: Chrome Application Object

    Results:
    --------

    The results of these tests will be stored in:
    out/smoketests/leboncoin

    .. sectionauthor:: Adrian Pothuaud <adrianpothuaud2@gmail.com>

"""

import unittest
import datetime
now = datetime.datetime.now()
import os
import HTMLTestRunner
import testscontext

# dependencies
# (those we should verify in case of failures)
import Chrome
import path_utils
import image_utils


# define test classes here
# scenario 1
class ICanCreateAnAccount(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.chrome = Chrome.Chrome()
        path_utils.add_image_path(os.path.join(
            testscontext.rootpath,
            "imgs",
            "leboncoin"
        ))
        self.user = {
            "username": "unregistered{}{}{}{}".format(
                now.month, now.day, now.hour, now.minute
            ),
            "email": "unregistered{}{}{}{}@test.com".format(
                now.month, now.day, now.hour, now.minute
            ),
            "password": "unregistered123456"
        }

    @classmethod
    def tearDownClass(self):
        App.close('Google Chrome')

    def test_A_GoToLeboncoin(self):
        self.chrome.open()
        wait(2)
        self.chrome.new_tab("https://www.leboncoin.fr/")
        wait("se_connecter.png", 10)

    def test_B_GoToLoginPanel(self):
        click("se_connecter.png")
        wait("login_email.png", 10)
        image_utils.wait_all(["login_password.png", "login.png"])

    def test_C_GoToCreateAccount(self):
        click("creer_un_compte.png")
        wait("particulier.png", 10)
        click("particulier.png")
        wait("conditions.png", 10)
        image_utils.wait_all([
            "email_field.png",
            "offers.png",
            "password_confirm_field.png",
            "password_field.png",
            "pseudo_field.png"
        ])

    def test_D_FillCreateAccountForm(self):
        paste("pseudo_field.png", self.user["username"])
        paste("email_field.png", self.user["email"])
        paste("password_field.png", self.user["password"])
        paste("password_confirm_field.png", self.user["password"])
        find("conditions.png").click("checkbox.png")
        click("create_personal_account.png")

    def test_E_WaitAccountValidation(self):
        wait("activer.png", 10)


# scenario 2
class ICanLoginWithValidUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.chrome = Chrome.Chrome()
        path_utils.add_image_path(os.path.join(
            testscontext.rootpath,
            "imgs",
            "leboncoin"
        ))
        self.user = {
            "username": "adrianpothuaud4",
            "email": "adrianpothuaud4@gmail.com",
            "password": "password123"
        }

    @classmethod
    def tearDownClass(self):
        wait("deco.png")
        click("deco.png")
        wait(3)
        App.close('Google Chrome')

    def test_A_GoToLeboncoin(self):
        self.chrome.open()
        self.chrome.new_tab("https://www.leboncoin.fr/")
        wait("se_connecter.png", 10)

    def test_B_GoToLoginPanel(self):
        click("se_connecter.png")
        wait("login_email.png", 10)
        image_utils.wait_all(["login_password.png", "login.png"])

    def test_C_FillLoginForm(self):
        paste("login_email.png", self.user["email"])
        paste("login_password.png", self.user["password"])
        click("login.png")

    def test_D_WaitMesannonces(self):
        wait("mes_annonces.png", 10)

# scenario 3
class ICannotLoginWithInvalidUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.chrome = Chrome.Chrome()
        path_utils.add_image_path(os.path.join(
            testscontext.rootpath,
            "imgs",
            "leboncoin"
        ))
        self.user = {
            "username": "unregistered123456",
            "email": "unregistered123456@test.com",
            "password": "unregistered123456"
        }

    @classmethod
    def tearDownClass(self):
        App.close('Google Chrome')

    def test_A_GoToLeboncoin(self):
        self.chrome.open()
        self.chrome.new_tab("https://www.leboncoin.fr/")
        wait("se_connecter.png", 10)

    def test_B_GoToLoginPanel(self):
        click("se_connecter.png")
        wait("login_email.png", 10)
        image_utils.wait_all(["login_password.png", "login.png"])

    def test_C_FillLoginForm(self):
        paste("login_email.png", self.user["email"])
        paste("login_password.png", self.user["password"])
        click("login.png")

    def test_D_WaitNoAccountMatch(self):
        wait("aucun_compte.png", 10)


if __name__ == '__main__':

    test_list = unittest.TestSuite()

    for tc in (ICanCreateAnAccount, ICanLoginWithValidUser, ICannotLoginWithInvalidUser):
        tests = unittest.TestLoader().loadTestsFromTestCase(tc)
        test_list.addTests(tests)

    now = datetime.datetime.now()
    filename = "{}-{}-{}.{}h{}.html".format(
        now.year, now.month, now.day, now.hour, now.minute
    )
    with open(os.path.join(testscontext.outpath, 'smoketests', 'leboncoin', filename), 'w') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = rf, description="Test Scenario: Leboncoin login. Environment: {}.".format(Env.getOS()),
            title="Leboncoin", dirTestScreenshots=os.path.join(testscontext.outpath, 'smoketests', 'leboncoin', 'screenshots')
        )
        runner.run(test_list)
