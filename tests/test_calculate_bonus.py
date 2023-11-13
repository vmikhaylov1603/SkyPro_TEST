"""
Так как основную логику подсчета процента премирования на основе граничных значений/классов эквивалетности мы
проверяем в других тестах, то здесь можно проверить основную логику для некоторых значений процентов с премией - и этого
будет достаточно для покрытия.
Тестировать будем на данных, приближенных к реальности.
Для повышения покрытия будем брать для каждого теста данные из разных классов эквивалетности.
Так же сделаем важные тесты для расчетов - например нецелые числа.
"""

from calculate_methods.calculate_bonus import calculate_bonus


def test_bonus_with_sicking_0_percentage():
    assert calculate_bonus(900000, 60, True) == 0


def test_bonus_without_sicking_25_percentage():
    assert calculate_bonus(900000, 800, True) == 225000


def test_bonus_with_sicking_28_percentage():
    assert calculate_bonus(900000, 800, False) == 252000


def test_bonus_with_sicking_30_percentage_fraction_number():  # проверяем премию -  нецелое число
    assert calculate_bonus(957555, 1100, True) == 287266.5


def test_bonus_with_sicking_25_percentage_fraction_number_high_accuracy():
    assert calculate_bonus(957255, 800, True) == 239313.74999999997  # нужно ли проверять такую точность - зависит от бизнес-контекста
