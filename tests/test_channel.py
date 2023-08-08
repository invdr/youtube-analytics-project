import json
import os.path
import pytest

from src.channel import Channel


@pytest.fixture()
def channel_1():
    """Добавляем fixture для инициализации экземпляра класса для теста."""
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


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
    filename = 'homework-2/moscowpython.json'
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

