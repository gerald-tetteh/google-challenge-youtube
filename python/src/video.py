"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._is_flagged = False
        self._flagged_reason = None

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    def __repr__(self) -> str:
        tags = " ".join([tag for tag in self._tags])
        return f" {self._title} ({self._video_id}) [{tags}]"

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id
    
    @property
    def is_flagged(self) -> bool:
        """Returns the flagged state of a video"""
        return self._is_flagged
    
    @property
    def flagged_reason(self) -> str:
        """Returns reason video is flagged or None"""
        return self._flagged_reason

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
  
    def set_flagged(self,value) -> None:
        self._is_flagged = value
    
    def set_flagged_reason(self,value) -> None:
        self._flagged_reason = value