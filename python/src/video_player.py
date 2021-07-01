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
        # store names of playlists in lower case
        self.playlist_names = defaultdict(lambda: None)
    
    def _filter_flagged_videos(self) -> list:
        all_videos = self._video_library.get_all_videos()
        return list(filter(lambda video: not video.is_flagged,all_videos))

    def _print_flagged_video(self,video):
        print(f" {video} - FLAGGED (reason: {video.flagged_reason})")

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        list_of_videos = self._video_library.get_all_videos()
        list_of_videos.sort(key=lambda a: a.title)
        print("Here's a list of all available videos:")
        for i in range(len(list_of_videos)):
            if(list_of_videos[i].is_flagged):
                self._print_flagged_video(list_of_videos[i])
                continue
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
        if(video.is_flagged):
            print(f"Cannot play video: Video is currently flagged (reason: {video.flagged_reason})")
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

        available_videos = self._filter_flagged_videos()
        if(len(available_videos) == 0):
            print("No videos available")
            return
        video = random.choice(available_videos)
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
        if(video.is_flagged):
            print(f"Cannot add video to {playlist_name}: " \
                f"Video is currently flagged (reason: {video.flagged_reason})")
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
                if(video.is_flagged):
                    self._print_flagged_video(video)
                    continue
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
    
    def _filter_videos(self,filter_function,search_term):
        """Filter out videos that match the search term

        Args:
            filter_function: The function used to select applicable videos
            search_term: String used to filter videos
        """
        all_videos = self._video_library.get_all_videos()
        search_results = list(filter(filter_function,all_videos))
        search_results.sort(key=lambda video: video.title.lower())
        return search_results
    
    def _display_results_and_options(self, search_results, search_term):
        """Display search results and option for user to play a selected
        video

        Args:
            search_results: A list containing filtered videos
            search_term: String used to filter videos
        """
        if(len(search_results) == 0):
            print(f"No search results for {search_term}")
        else:
            print(f"Here are the results for {search_term}:")
            for i in range(len(search_results)):
                print(f" {i+1}){search_results[i]}")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            try:
                video_number = int(input()) - 1
            except Exception:
                return
            if(video_number > len(search_results) or video_number < 0):
                return
            self.play_video(search_results[video_number].video_id)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        search_filter = lambda video: search_term.lower() in \
            video.title.lower() and not video.is_flagged
        search_results = self._filter_videos(search_filter,search_term)
        self._display_results_and_options(search_results,search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        search_function = lambda video: video_tag.lower() in \
            video.tags and not video.is_flagged
        search_results = self._filter_videos(search_function,video_tag)
        self._display_results_and_options(search_results,video_tag)

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        video = self._video_library.get_video(video_id)
        if(video == None):
            print(f"Cannot flag video: Video does not exist")
            return
        if(video.is_flagged):
            print("Cannot flag video: Video is already flagged")
            return
        video.set_flagged(True)
        video.set_flagged_reason(flag_reason)
        if(self.currently_playing == video):
            self.stop_video()
        print(f"Successfully flagged video: {video.title} (reason: {video.flagged_reason})")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if(video == None):
            print("Cannot remove flag from video: Video does not exist")
            return
        if(not video.is_flagged):
            print("Cannot remove flag from video: Video is not flagged")
            return
        video.set_flagged(False)
        video.set_flagged_reason(None)
        print(f"Successfully removed flag from video: {video.title}")