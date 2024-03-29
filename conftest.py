import importlib
import pytest
import json
import jsonpickle
import os.path
from fixture.application import Application
from fixture.db import DbFixture


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config_file:
            target = json.load(config_file)
    return target

#@pytest.fixture
#def app(request):
    #global fixture
    #browser = request.config.getoption("--browser")
    #web_config = load_config( request.config.getoption("--target")) ['web']
    #"""if target is None:
       #config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
       #with open(config_file) as config_file:
           #target = json.load(config_file)"""
    #if fixture is None or not fixture.is_valid():
        #fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    #fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    #fixture.session.ensure_login(username="admin", password="secret")
    #return fixture

@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture (scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdate = load_from_module(fixture[5:])
            metafunc.parametrize(fixture,testdate, ids=[str(x) for x in testdate])
        elif fixture.startswith("json_"):
            testdate = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdate, ids=[str(x) for x in testdate])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())