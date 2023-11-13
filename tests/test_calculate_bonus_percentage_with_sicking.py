"""
Тестируем логику подсчета процента премии если сотрудник болел в течении года (без учета надбавки)
Тесты распределены на основе проверки бизнес-логики - композиция по величине процента премирования
Проверяем граничные значения и значение из класса эквивалетности
"""

from calculate_methods.calculate_bonus import calculate_percentage_bonus_by_worked_days_and_sicking


def test_bonus_0():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(0, True) == 0 # не совсем понятно, стоит ли такое проверять. по хорошему - уточнить бизнес-логику
    assert calculate_percentage_bonus_by_worked_days_and_sicking(60, True) == 0 # любое значение внутри класса эквивалентности
    assert calculate_percentage_bonus_by_worked_days_and_sicking(89, True) == 0


def test_bonus_15():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(90, True) == 15
    assert calculate_percentage_bonus_by_worked_days_and_sicking(91, True) == 15
    assert calculate_percentage_bonus_by_worked_days_and_sicking(100, True) == 15  # любое значение внутри класса эквивалентности
    assert calculate_percentage_bonus_by_worked_days_and_sicking(546, True) == 15
    assert calculate_percentage_bonus_by_worked_days_and_sicking(546.9, True) == 15  # граничное значение - нецелое


def test_bonus_25():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(547, True) == 25
    assert calculate_percentage_bonus_by_worked_days_and_sicking(548, True) == 25
    assert calculate_percentage_bonus_by_worked_days_and_sicking(800, True) == 25  # любое значение внутри класса эквивалентности
    assert calculate_percentage_bonus_by_worked_days_and_sicking(1094, True) == 25
    assert calculate_percentage_bonus_by_worked_days_and_sicking(1095, True) == 25


def test_bonus_30():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(1096, True) == 30
    assert calculate_percentage_bonus_by_worked_days_and_sicking(1100, True) == 30 # любое значение внутри класса эквивалентности
