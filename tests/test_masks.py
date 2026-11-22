import pytest
import src.masks

def test_get_mask_card_number():
    assert src.masks.get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

def test_get_mask_card_number_str():
    with pytest.raises(TypeError):
        src.masks.get_mask_card_number(7000792289606361)

def test_get_mask_card_number_len():
    with pytest.raises(ValueError):
        src.masks.get_mask_card_number("700")

def test_get_mask_card_number_len():
    with pytest.raises(ValueError):
        src.masks.get_mask_card_number("")

def test_get_mask_account():
    assert src.masks.get_mask_account('73654108430135874305') == '**4305'

def test_get_mask_account_str():
    with pytest.raises(TypeError):
        src.masks.get_mask_account(73654108430135874305)

def test_get_mask_account_len():
    with pytest.raises(ValueError):
        src.masks.get_mask_account("7")

def test_get_mask_account_len():
    with pytest.raises(ValueError):
        src.masks.get_mask_account("")

