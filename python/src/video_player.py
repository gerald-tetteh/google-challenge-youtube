"""A video player class."""

import random
from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currently_playing = None
        self.is_paused = False
        self.playing_video = "Playing video: {}"
        self.stopping_video = "Stopping video: {}"
        self.cannot_play = "Cannot play video: Video does not exist"
        self.cannot_stop = "Cannot stop video: No video is currently playing"

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        list_of_videos = self._video_library.get_all_videos()
        list_of_videos.sort(key=lambda a: a.title)
        print("Here's a list of all available videos:")
        for i in range(len(list_of_videos)):
            video = list_of_videos[i]
            tags = " ".join([tag for tag in video.tags])
            video_string = f" {video.title} ({video.video_id}) [{tags}]"
            print(video_string)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        video = self._video_library.get_video(video_id)
        if(video == None):
            print(self.cannot_play)
            return
        if(self.currently_playing != None):
            print(self.stopping_video.format(self.currently_playing.title))
        self.currently_playing = video
        self.is_paused = False
        print(self.playing_video.format(self.currently_playing.title))

    def stop_video(self):
        """Stops the current video."""

        if(self.currently_playing == None):
            print(self.cannot_stop)
            return
        print(self.stopping_video.format(self.currently_playing.title))
        self.currently_playing = None
        self.is_paused = False

    def play_random_video(self):
        """Plays a random video from the video library."""

        video = random.choice(self._video_library.get_all_videos())
        self.play_video(video.video_id)

    def pause_video(self):
        """Pauses the current video."""

        if(self.currently_playing != None and not self.is_paused):
            self.is_paused = True
            print(f"Pausing video: {self.currently_playing.title}")
            return
        if(self.currently_playing == None):
            print("Cannot pause video: No video is currently playing")
            return
        if(self.is_paused):
            print(f"Video already paused: {self.currently_playing.title}")

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
