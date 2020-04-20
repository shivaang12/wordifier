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
