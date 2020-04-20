#!/usr/bin/env python

"""Tests for `wordifier` package."""


from wordifier import wordifier


def test_words_to_number():
    assert wordifier.words_to_number("+1-800-PAINTER") == "1-800-724-6837"
    assert wordifier.words_to_number("800-PAINTER") == "800-724-6837"
    assert wordifier.words_to_number("800PAINTER") == "800-724-6837"
    assert wordifier.words_to_number("800-72-HOT-37") == "800-724-6837"


def test_number_to_words():
    assert wordifier.number_to_words("1-800-724-6837") == "1-800-PAINTER"
    assert wordifier.number_to_words("+1-800-724-6837") == "1-800-PAINTER"


def test_all_wordifications():
    assert "1-800-PAINTER" in wordifier.all_wordifications("1-800-724-6837")
    assert "1-800-72-HOT-37" in wordifier.all_wordifications("1-800-724-6837")
    assert "1-800-FLOWERS" in wordifier.all_wordifications("1-800-356-9377")
    assert wordifier.all_wordifications("000-000-0000") == []
