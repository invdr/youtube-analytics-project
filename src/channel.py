import json
import os

from googleapiclient.discovery import build

API_KEY: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала."""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется по id канала."""
        yt_obj = self.get_service()

        self.__channel_id = channel_id
        channel = yt_obj.channels().list(id=self.channel_id,
                                         part='snippet,statistics').execute()

        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = (channel['items'][0]['statistics']
        ['subscriberCount'])
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']

    def __str__(self):
        """Возвращает название и ссылку на канал по шаблону."""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """Складывает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """Вычитает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """Сравнивает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """Сравнивает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        """Сравнивает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """Сравнивает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        """Сравнивает экземпляры класса по атрибуту subscriber_count."""
        return int(self.subscriber_count) == int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        channel = youtube.channels().list(id=self.channel_id,
                                          part='snippet,statistics').execute()
        printj = json.dumps(channel, indent=2, ensure_ascii=False)
        print(printj)

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        return youtube

    def to_json(self, filename):
        """Сохраняет в json-файл значения атрибутов экземпляра Channel"""
        with open(filename, 'w', encoding='windows-1251') as f:
            channel_info = {'title': self.title,
                            'description': self.description,
                            'url': self.url,
                            'subscriber_count': self.subscriber_count,
                            'video_count': self.video_count,
                            'view_count': self.view_count,
                            }
            json.dump(channel_info, f, indent=4, ensure_ascii=False)
