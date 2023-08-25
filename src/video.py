import json

from src.channel import Channel

# ввод id канала для извлечения данных видео
CHANNEL_ID = 'UC-OVMPlMA3-YCIeg4z5z23A'


class Video(Channel):
    def __init__(self, video_id, channel_id=CHANNEL_ID):
        super().__init__(channel_id)
        self.__video_id = video_id

        yt_obj = self.get_service()
        video_response = yt_obj.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                              id=video_id).execute()
        try:
            self.title = video_response['items'][0]['snippet']['title']
            self.video_url = 'https://youtu.be/' + self.__video_id
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except Exception:
            self.title = None
            self.video_url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id, channel_id=CHANNEL_ID):
        super().__init__(video_id, channel_id=CHANNEL_ID)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
