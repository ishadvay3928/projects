from project import check_correct_args, diagnose_disease , find_age
import pytest

def test_check_correct_arg():
    with pytest.raises(SystemExit):
        check_correct_args()


def test_diagnose_disease():
    assert diagnose_disease("cold") == "Flu"
    assert diagnose_disease("fever") == "Malaria"
    assert diagnose_disease("nausea") == "Dengue"
    assert diagnose_disease("headache") == "Migraine"


def test_find_age():
    assert find_age("2001") == "Age 21"
    assert find_age("2003") == "Age 19"