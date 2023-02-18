from src.pre_built.counter import count_ocurrences


def test_counter():
    '''Testa a ocorrência das palavras Python e Javascript no arquivo
    informado '''
    assert count_ocurrences('data/jobs.csv', 'Python') == 1639
    assert count_ocurrences('data/jobs.csv', 'Javascript') == 122
