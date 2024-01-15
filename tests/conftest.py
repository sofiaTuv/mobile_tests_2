import os
import pytest
from dotenv import load_dotenv


@pytest.fixture
def url():
    return os.getenv('WEB_URL')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
