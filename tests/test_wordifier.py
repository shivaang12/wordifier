#!/usr/bin/env python

"""Tests for `wordifier` package."""


from wordifier import wordifier


def test_words_to_number():
    assert wordifier.words_to_number("+1-800-PAINTER") == "1-800-724-6837"
