"""
Тестируем логику подсчета процента премии если сотрудник не болел в течении года (с учетом надбавки)
Так как основную логику подсчета процента премирования на основе граничных значений/классов эквивалетности мы
проверяем в других тестах, то здесь можно проверить основную логику для каждого значения процентов с премией - и этого
будет достаточно для покрытия
"""

from calculate_methods.calculate_bonus import calculate_percentage_bonus_by_worked_days_and_sicking


def test_bonus_3():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(60, False) == 3


def test_bonus_18():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(100, False) == 18


def test_bonus_28():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(800, False) == 28


def test_bonus_33():
    assert calculate_percentage_bonus_by_worked_days_and_sicking(1100, False) == 33
