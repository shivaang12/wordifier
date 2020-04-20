import pytest
from wordifier import indexifier


@pytest.fixture
def indexifier_with_default():
    return indexifier.Indexifier(3)


def test_default_values(indexifier_with_default):
    assert indexifier_with_default.list_of_indexes == []
    assert indexifier_with_default.number_length == 3


def test_get_all_possible_indexes(indexifier_with_default):
    assert indexifier_with_default.list_of_indexes == []
    assert [[0, 3]] in indexifier_with_default.get_all_possible_indexes()
    assert indexifier_with_default.list_of_indexes != []


def test_divide_array(indexifier_with_default):
    assert [[0, 1], [1, 2]] in indexifier_with_default.divide_array([[0, 2]], 0)


def test_generate_indexes(indexifier_with_default):
    assert indexifier_with_default.list_of_indexes == []
    indexifier_with_default.generate_indexes()
    assert [[0, 3]] in indexifier_with_default.list_of_indexes
