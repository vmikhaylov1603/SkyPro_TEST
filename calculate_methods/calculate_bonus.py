def calculate_percentage_bonus_by_worked_days_and_sicking(worked_days, is_sick):
    """
    Рассчитывает процент годовой премии на основе стажа работы и информации, болел ли сотрудник в течении года
    :param worked_days: стаж работы в днях
    :param is_sick: болел ли сотрудник в течении года
    :return: рассчитанный процент для премирования
    """
    bonus_in_percentage = 0

    if worked_days > 1095:  # более 3 лет
        bonus_in_percentage = 30

    if 547 <= worked_days <= 1095:  # от 1,5 до 3 лет
        bonus_in_percentage = 25

    if 90 <= worked_days < 547:  # от 90 дней до 1,5 лет (так как полтора года это 547,5 дней - то сделаем допущение)
        bonus_in_percentage = 15

    if worked_days < 90:  # менее 90 дней
        bonus_in_percentage = 0  # явно указываем эту бизнес-логику

    if not is_sick:  # если сотрудник не болел в течении года, то к премии добавляется 3 %
        bonus_in_percentage += 3

    return bonus_in_percentage


def calculate_bonus(annual_income, worked_days, is_sick):
    """
    Рассчитывает годовую премию на основе годового дохода, стажа работы и информации, болел ли сотрудник в течении года
    :param annual_income: годовой доход
    :param worked_days: стаж работы в днях
    :param is_sick: болел ли сотрудник в течении года
    :return: размер годовой премии
    """
    bonus_in_percentage = calculate_percentage_bonus_by_worked_days_and_sicking(worked_days, is_sick)
    return (annual_income/100) * bonus_in_percentage
