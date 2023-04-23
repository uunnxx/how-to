import sys
import pytest

def greet(to_out, to_err=None):
    print(to_out)
    if to_err:
        print(to_err, file=sys.stderr)


greet("Hi there", "Error text")


@pytest.fixture()
def config():
    return {
        'name': 'Foo',
        'email': 'foo@bar.com'
    }


def test_some_data(config):
    print(config)


@pytest.fixture()
def configuration():
    print('Before')
    yield { 'name': 'Foo Bar' }

    print('After')


def test_aapp(configuration):
    print('In test')
    print(configuration)


