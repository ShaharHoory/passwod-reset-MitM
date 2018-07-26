from selenium import webdriver

import Driver
import os

class PasswordReset:
    def __init__(self):
        pass

    url = ''

    @staticmethod
    def connect_to_site(phoneNum):
        global url
        Driver.Instance.get("https://www.facebook.com")
        Driver.Instance.find_element_by_link_text("Forgotten account?").click()
        phone_num_text_box = Driver.Instance.find_element_by_id('identify_email')
        phone_num_text_box.send_keys(phoneNum)
        phone_num_text_box.submit()
        Driver.Instance.implicitly_wait(5) #was 10, if not working change back to 10
        Driver.Instance.find_element_by_name("reset_action").click()
        url = Driver.Instance.current_url
        Driver.CloseDriver()

    @staticmethod
    def reset_password(code, phoneNum):
        global url
        Driver.Initialize()
        Driver.Instance.get(url)
        phone_num_text_box = Driver.Instance.find_element_by_id('identify_email')
        phone_num_text_box.send_keys(phoneNum)
        phone_num_text_box.submit()
        Driver.Instance.implicitly_wait(10)
        Driver.Instance.find_element_by_name("reset_action").click()
        #--code page--
        Driver.Instance.find_element_by_id('recovery_code_entry').send_keys(code)
        Driver.Instance.find_element_by_name("reset_action").click()
        #--change password page
        new_pass = PasswordReset.generate_password()
        Driver.Instance.find_element_by_id('password_new').send_keys(new_pass)
        Driver.Instance.find_element_by_id('btn_continue').click()
        Driver.CloseDriver()
        PasswordReset.write_password(phoneNum, new_pass)

    @staticmethod
    def generate_password(length=8, charset='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'):
        random_bytes = os.urandom(length)
        len_charset = len(charset)
        indices = [int(len_charset * (ord(byte) / 256.0)) for byte in random_bytes]
        return ''.join([charset[index] for index in indices])

    @staticmethod
    def write_password(phoneNum, new_pass):
        with open('passwords.txt', 'a+') as f:
            f.write('phone number: ' + phoneNum + ' password: ' + new_pass)