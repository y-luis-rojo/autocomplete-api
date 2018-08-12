import os

import pytest

import app

os.chdir('..')

TEST_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../6500titles.csv'


@pytest.fixture(scope="session")
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def test_root(client):
    rv = client.get('/')
    json_data = rv.get_json()

    with open(TEST_FILE, 'r') as f:
        for line in f:
            assert line.rstrip().lower() in [i.lower() for i in json_data]


def test_prefix(client):
    prefix = 'fac'
    rv = client.get('/?prefix=' + prefix)
    json_data = rv.get_json()

    with open(TEST_FILE, 'r') as f:
        for line in f:
            if line.startswith(prefix):
                assert line.rstrip().lower() in [i.lower() for i in json_data]
