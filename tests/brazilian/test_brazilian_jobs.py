from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    assert "title" in read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0]
