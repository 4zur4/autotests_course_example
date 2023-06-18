# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_all_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


@pytest.mark.smoke
def test_all_division_negative_numbers():
    assert all_division(-1, -1) == 1


def test_all_division_fractional_number():
    assert all_division(1, 0.5) == 2


def test_all_division_one_number():
    assert all_division(1, ) == 1


def test_all_division_one_negative_number():
    assert all_division(-1, 1) == -1

