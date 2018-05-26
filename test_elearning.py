# -*- coding: utf-8 -*-

import os
import pickle

import pytest
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver import ActionChains


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium


@pytest.fixture(autouse=True)
def login(pytestconfig, selenium):
    selenium.get('http://elearning.se.sjtu.edu.cn/')
    if os.path.exists('cookies.pkl'):
        with open('cookies.pkl', 'rb') as f:
            cookies = pickle.load(f)
            selenium.delete_all_cookies()
            selenium.add_cookie(cookies)
    else:
        username = selenium.find_element_by_name('loginname')
        username.send_keys(pytestconfig.getini('username'))
        password = selenium.find_element_by_name('password')
        password.send_keys(pytestconfig.getini('password'))
        selenium.find_element_by_class_name('commandbutton').click()
        wait = WebDriverWait(selenium, 10)
        wait.until(lambda _: selenium.current_url == 'http://elearning.se.sjtu.edu.cn/announcement/index.asp')
        cookies = selenium.get_cookies()[0]
        with open('cookies.pkl', 'wb') as f:
            pickle.dump(cookies, f)

    selenium.get('http://elearning.se.sjtu.edu.cn/profile.asp')


def test_input(selenium):
    question = selenium.find_element_by_name('txtQuestion')
    question.clear()
    question.send_keys('Software Testing')
    assert question.get_attribute('value') == 'Software Testing'

    submit_button = selenium.find_element_by_xpath('//a[@href="javascript:funUptdata();"]')
    submit_button.click()

    selenium.get('http://elearning.se.sjtu.edu.cn/profile.asp')
    question = selenium.find_element_by_name('txtQuestion')
    assert question.get_attribute('value') == 'Software Testing'


def test_select(selenium):
    political_affiliation = Select(selenium.find_element_by_name('lstPolity'))
    political_affiliation.select_by_value('3')
    assert political_affiliation.first_selected_option.get_attribute('value') is '3'

    submit_button = selenium.find_element_by_xpath('//a[@href="javascript:funUptdata();"]')
    submit_button.click()

    selenium.get('http://elearning.se.sjtu.edu.cn/profile.asp')
    political_affiliation = Select(selenium.find_element_by_name('lstPolity'))
    assert political_affiliation.first_selected_option.get_attribute('value') is '3'


def test_checkbox(selenium):
    system_subscribe = selenium.find_elements_by_xpath('//input[@type="checkbox"]')[0]
    is_selected = system_subscribe.is_selected()
    system_subscribe.click()
    assert system_subscribe.is_selected() is not is_selected

    submit_button = selenium.find_element_by_xpath('//a[@href="javascript:funUptdata();"]')
    submit_button.click()

    selenium.get('http://elearning.se.sjtu.edu.cn/profile.asp')
    system_subscribe = selenium.find_elements_by_xpath('//input[@type="checkbox"]')[0]
    assert system_subscribe.is_selected() is not is_selected


def test_upload(pytestconfig, selenium):
    photo = selenium.find_element_by_name('txtPhoto')
    photo.send_keys(pytestconfig.getini('file_path'))
    assert photo.get_attribute('value') is not None


def test_combined_action(selenium):
    remark = selenium.find_element_by_name('txtRemark')
    remark.send_keys('Software Testing')
    assert remark.get_attribute('value') == 'Software Testing'
    reset = selenium.find_element_by_xpath('//a[@href="javascript:funReset();"]')
    ActionChains(selenium).move_to_element(reset).click().perform()
    assert len(remark.get_attribute('value')) == 0
