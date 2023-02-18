from src.pre_built.brazilian_jobs import read_brazilian_file
from tests.brazilian.mocks import brazilian_mock


def test_brazilian_jobs():
    assert read_brazilian_file(
        "tests/mocks/brazilians_jobs.csv") == brazilian_mock
