"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self,name) -> None:
        self.name = name
        self.videos = []
    
    def add_video(self,video_id) -> int:
        """Adds video id to videos array"""
        if(video_id in self.videos):
            return 0;
        self.videos.append(video_id)
        return 1;
    
    def get_all_videos(self) -> list:
        """Returns videos array"""
        return self.videos

    def remove_video(self,video_id) -> int:
        """Remove video from playlist"""
        if(video_id not in self.videos):
            return 0;
        self.videos.remove(video_id)
        return 1;

    def clear_playlist(self) -> None:
        self.videos = []