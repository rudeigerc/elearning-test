# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium

def test_tongqu(selenium):
    selenium.get('https://tongqu.me/')
    assert selenium.title == '同去网'
