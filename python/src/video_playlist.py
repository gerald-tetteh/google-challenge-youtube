"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self,name) -> None:
        """
        Args:
            name: The playlist name
        """
        self._name = name
        self._videos = []
    
    @property
    def name(self) -> str:
        return self._name
    
    def add_video(self,video_id) -> int:
        """Adds video id to videos array

        Args:
            video_id: The video id
        """
        if(video_id in self._videos):
            return 0;
        self._videos.append(video_id)
        return 1;
    
    def get_all_videos(self) -> list:
        """Returns videos array"""
        return self._videos

    def remove_video(self,video_id) -> int:
        """Remove video from playlist

        Args:
            video_id: The video id
        """
        if(video_id not in self._videos):
            return 0;
        self._videos.remove(video_id)
        return 1;

    def clear_playlist(self) -> None:
        self._videos = []