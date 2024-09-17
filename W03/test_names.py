from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():

    assert make_full_name("Bill", "McDonald")      == "McDonald; Bill"
    assert make_full_name("Sammantha", "Williams") == "Williams; Sammantha"
    assert make_full_name("Tom", "Beckman")        == "Beckman; Tom"
    assert make_full_name("Shannon", "Henderson")  == "Henderson; Shannon"



def test_extract_family_name():

    assert extract_family_name("McDonald; Bill")      == "McDonald"
    assert extract_family_name("Williams; Sammantha") == "Williams"
    assert extract_family_name("Beckman; Tom")        == "Beckman"
    assert extract_family_name("Henderson; Shannon")  == "Henderson"



def test_extract_given_name():

    assert extract_given_name("McDonald; Bill")      == "Bill"
    assert extract_given_name("Williams; Sammantha") == "Sammantha"
    assert extract_given_name("Beckman; Tom")        == "Tom"
    assert extract_given_name("Henderson; Shannon")  == "Shannon"




pytest.main(["-v", "--tb=line", "-rN", __file__])