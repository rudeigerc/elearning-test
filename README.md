# elearning-test

## Build

### Install Chrome Driver

#### macOS

```shell
$ brew cask install chromedriver
```

#### Windows

Visit [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for more information.

### Install `selenium` and `pytest`

```shell
$ pip install selenium
$ pip install pytest
$ pip install pytest-selenium
```

## Config

See `conftest.py` and `pytest.ini`.

- username
- password
- file_path

## Run

```shell
$ pytest --driver Chrome
```

## Generate Report

Visit [pytest-html](https://github.com/pytest-dev/pytest-html) for more information.

```shell
$ pytest --driver Chrome --html=report.html
```

## Docs

- [selenium](https://seleniumhq.github.io/selenium/docs/api/py/index.html)
- [pytest](https://docs.pytest.org/en/latest/contents.html)
- [pytest-selenium](http://pytest-selenium.readthedocs.io/en/latest/index.html)