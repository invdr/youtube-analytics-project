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
