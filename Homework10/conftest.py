import pytest
import time
import datetime


@pytest.fixture(scope="class")
def tests_timing():
    start = datetime.datetime.now()
    print(start.strftime("\n Сборка запущена: %H:%M:%S:%f"))
    yield
    end = datetime.datetime.now()
    print(end.strftime("\n Сборка прошла: %H:%M:%S:%f"))


@pytest.fixture()
def test_time():
    start = time.time()
    yield
    end = time.time()
    print(f"\n Время выполнения: {end - start}")