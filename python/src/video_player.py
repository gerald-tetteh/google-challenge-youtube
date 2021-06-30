"""A video player class."""

import random
from collections import defaultdict
from .video_library import VideoLibrary
from .video_playlist import Playlist


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
        self.playlists = []
        self.playlist_names = defaultdict(lambda: None)

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        list_of_videos = self._video_library.get_all_videos()
        list_of_videos.sort(key=lambda a: a.title)
        print("Here's a list of all available videos:")
        for i in range(len(list_of_videos)):
            print(list_of_videos[i])

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

        if(not self.is_paused and self.currently_playing != None):
            print("Cannot continue video: Video is not paused")
            return
        if(self.currently_playing == None):
            print("Cannot continue video: No video is currently playing")
            return
        self.is_paused = False
        print(f"Continuing video: {self.currently_playing.title}")

    def show_playing(self):
        """Displays video currently playing."""

        if(self.currently_playing == None):
            print("No video is currently playing")
            return
        if(self.is_paused):
            print(f"Currently playing:{self.currently_playing} - PAUSED")
        else:
            print(f"Currently playing:{self.currently_playing}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if(self.playlist_names[playlist_name.lower()] != None):
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlist_names[playlist_name.lower()] = len(self.playlists)
            playlist = Playlist(playlist_name)
            self.playlists.append(playlist)
            print(f"Successfully created new playlist: {playlist.name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if(self.playlist_names[playlist_name.lower()] == None):
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        video = self._video_library.get_video(video_id)
        if(video == None):
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        playlist = self.playlists[self.playlist_names[playlist_name.lower()]]
        result = playlist.add_video(video_id)
        if(result == 0):
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""

        if(len(self.playlists) == 0):
            print("No playlists exist yet")
        else:
            playlists = sorted(self.playlists,key=lambda a: a.name.lower())
            print("Showing all playlists:")
            for i in range(len(playlists)):
                print(f" {playlists[i].name}")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if(self.playlist_names[playlist_name.lower()] == None):
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        playlist = self.playlists[
            self.playlist_names[playlist_name.lower()]]
        print(f"Showing playlist: {playlist_name}")
        if(len(playlist.videos) == 0):
            print(" No videos here yet")
        else:
            videos = playlist.videos[::-1]
            for i in range(len(videos)):
                video = self._video_library.get_video(playlist.videos[i])
                print(f" {video}")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        if(self.playlist_names[playlist_name.lower()] == None):
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
            return
        video = self._video_library.get_video(video_id)
        if(video == None):
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        playlist = self.playlists[
            self.playlist_names[playlist_name.lower()]]
        result = playlist.remove_video(video_id)
        if(result == 0):
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            print(f"Removed video from {playlist_name}: {video.title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if(self.playlist_names[playlist_name.lower()] == None):
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        playlist = self.playlists[
            self.playlist_names[playlist_name.lower()]]
        playlist.clear_playlist()
        print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        if(self.playlist_names[playlist_name.lower()] == None):
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        playlist = self.playlists[
            self.playlist_names[playlist_name.lower()]]
        self.playlists.remove(playlist)
        del self.playlist_names[playlist_name.lower()]
        print(f"Deleted playlist: {playlist_name}")

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
