# -*- coding: utf-8 -*-


def pytest_addoption(parser):
    parser.addini('username', 'username of e-learning', 'args')
    parser.addini('password', 'password of e-learning', 'args')
    parser.addini('file_path', 'path of file to upload', 'args')
