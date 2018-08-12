import os

import pytest

from autocomplete.repository import AppsRepository

os.chdir('..')

TEST_FILE = os.path.dirname(os.path.realpath(__file__)) + '/../6500titles.csv'


@pytest.fixture(scope="module")
def apps_repo():
    return AppsRepository(TEST_FILE)


def test_init(apps_repo):
    with open(TEST_FILE, 'r') as f:
        for line in f:
            assert unicode(line.rstrip().lower()) in apps_repo


def test_get(apps_repo):
    prefix = 'Fac'
    results = apps_repo.get(prefix)
    with open(TEST_FILE, 'r') as f:
        for line in f:
            if line.startswith(prefix):
                assert line.rstrip() in results
