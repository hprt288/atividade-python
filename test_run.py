from datetime import date

from run import dias_que_faltam, idade


def test_idade():
    assert idade(date(2000, 1, 1), date(2026, 10, 19)) == 26
    assert idade(date(2000, 12, 31), date(2026, 10, 19)) == 25


def test_dias_que_faltam():
    assert dias_que_faltam(date(2026, 10, 20), date(2026, 10, 19)) == 1
    assert dias_que_faltam(date(2026, 11, 18), date(2026, 10, 19)) == 30
