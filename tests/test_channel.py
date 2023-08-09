import json
import os.path
import pytest

from src.channel import Channel


@pytest.fixture()
def channel_1():
    """Добавляем fixture для инициализации экземпляра класса для теста."""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


@pytest.fixture()
def channel_2():
    """Добавляем fixture для инициализации экземпляра класса для теста."""
    return Channel('UCwHL6WHUarjGfUM_586me8w')


def test_channel_init(channel_1):
    """
    Когда создаем экземпляр класса channel_1 с ID канала youtube,
    то возвращается Х атрибут.
    """
    assert channel_1.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'


def test_print_info(channel_1):
    """
    Когда вызываем метод print_info() у созданного экземпляра класса channel_1,
    то возвращается объект типа None и печатается информация формата json.
    """
    assert channel_1.print_info() is None


# TestCases for homework-2

def test_get_service():
    """Возвращается ли объект"""
    assert isinstance(Channel.get_service(), object)


def test_to_json():
    filename = "../homework-2/moscowpython.json"
    check_file = os.path.exists(filename)
    assert check_file == True

    with open(filename) as f:
        data = json.load(f)
    assert data["title"] == "MoscowPython"
    assert data["description"] == ("Видеозаписи со встреч питонистов и "
                                   "джангистов в Москве и не только. :)\n"
                                   "Присоединяйтесь: https://www.facebook.com/"
                                   "groups/MoscowDjango! :)")
    assert data["url"] == ("https://www.youtube.com/channel/"
                           "UC-OVMPlMA3-YCIeg4z5z23A")
    assert data["subscriber_count"] == "26300"
    assert data["video_count"] == "695"
    assert data["view_count"] == "2367648"


# TestCases for homework-3
def test_class_str(channel_1):
    """Вызывает дандер метод __str__ для вывода информации о названии канала и ссылки на него"""
    assert str(channel_1) == "MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)"


def test__add__(channel_1, channel_2):
    assert channel_1 + channel_2 == 102300


def test__sub__(channel_1, channel_2):
    assert channel_1 - channel_2 == -49700
    assert channel_2 - channel_1 == 49700


def test__gt__(channel_1, channel_2):
    assert (channel_1 > channel_2) == False


def test__ge__(channel_1, channel_2):
    assert (channel_1 >= channel_2) == False


def test__lt__(channel_1, channel_2):
    assert (channel_1 < channel_2) == True


def test__le__(channel_1, channel_2):
    assert (channel_1 <= channel_2) == True


def test__eq__(channel_1, channel_2):
    assert (channel_1 == channel_2) == False
