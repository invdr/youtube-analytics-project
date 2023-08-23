import datetime
import os
from src.video import Video

import isodate

from googleapiclient.discovery import build


class PlayList:
    __api_key: str = os.getenv('YT_API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id

        youtube = self.get_service()
        playlists = youtube.playlists().list(id=self.__playlist_id,
                                             part='contentDetails,snippet').execute()
        self.title = playlists['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + playlists['items'][0]['id']
        self.video_info = []  # список для информации о видео по его id
        self.get_video_info()

    def get_video_info(self):
        """Функция для получения информации о видео по его id"""

        youtube = self.get_service()
        # получаем информацию плейлиста по его id
        playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        # формируем список из id всех видеороликов из плейлиста
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

        # формируем словарь с информацией о видеороликах из списка "video_ids"
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)).execute()

        # добавляем в список "video_info" информацию о видеороликах из "video_response"
        for video in video_response['items']:
            video_obj = Video(video['id'])
            self.video_info.append({
                'id': video['id'],
                'duration': isodate.parse_duration(video['contentDetails']['duration']),
                'like_count': int(video_obj.like_count),
                'url': video_obj.video_url,
            })

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.__youtube

    @property
    def total_duration(self):
        total = datetime.timedelta(seconds=0)
        for video in self.video_info:
            total += video['duration']
        return total

    def show_best_video(self):
        best_video_url = ''
        max_like = 0
        for video in self.video_info:
            if video['like_count'] > max_like:
                max_like = video['like_count']
                best_video_url = video['url']
        return best_video_url
