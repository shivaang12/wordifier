from wordifier import helper


def test_english_dictionary():
    assert helper.english_dict.check("TRUE") is True
    assert helper.english_dict.check("Hotel") is True
    assert helper.english_dict.check("Beer") is True
    assert helper.english_dict.check("Hywq") is False


def test_number_to_alpha_dict():
    assert "A" in helper.number_to_alpha_dict["2"]
    assert "Z" not in helper.number_to_alpha_dict["3"]
    assert "Q" in helper.number_to_alpha_dict["7"]


def test_find_vanity_number_format():
    assert helper.find_vanity_number_format("1-800-123-4567") == ("1-800-", "1234567")
    assert helper.find_vanity_number_format("800-123-4567") == ("800-", "1234567")


def test_find_words():
    assert "PAINTER" in helper.find_words("7246837")


def test_count_alpha():
    assert helper.count_alpha("123abc") == 3
    assert helper.count_alpha("123") == 0


def test_get_alpha_numeric_format():
    assert helper.get_alpha_numeric_format("72HOT37") == "72-HOT-37"


def test_index_division_array():
    assert [[0, 7]] in helper.index_division_array.get_all_possible_indexes()
    assert [[0, 1], [1, 7]] in helper.index_division_array.get_all_possible_indexes()
    assert [[0, 5], [5, 6], [6, 7]] in helper.index_division_array.get_all_possible_indexes()
