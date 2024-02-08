import time
import webbrowser
from time import sleep

from ovos_plugin_manager.templates.media import WebPlayerBackend


class WebBrowserMediaService(WebPlayerBackend):

    def __init__(self, config, bus=None):
        super().__init__(config, bus)
        self.process = None
        self._stop_signal = False
        self._is_playing = False
        self._paused = False
        self.ts = 0

    def on_track_start(self):
        self.ts = time.time()
        # Indicate to audio service which track is being played
        if self._track_start_callback:
            self._track_start_callback(self._now_playing)

    def on_track_end(self):
        self._is_playing = False
        self._paused = False
        self.process = None
        self.ts = 0
        if self._track_start_callback:
            self._track_start_callback(None)

    def supported_uris(self):
        return ['http', 'https']

    def play(self, repeat=False):
        """ Play playlist using webbrowser. """
        self.on_track_start()
        webbrowser.open_new(self._now_playing)

    def stop(self):
        """ Stop webbrowser playback. """
        if self._is_playing:
            self._stop_signal = True
            while self._is_playing:
                sleep(0.1)
            self._stop_signal = False
            self.on_track_end()
            return True
        return False

    def pause(self):
        """ Pause webbrowser playback. """
        # Not available in this plugin

    def resume(self):
        """ Resume paused playback. """
        # Not available in this plugin

    def lower_volume(self):
        """Lower volume.

        This method is used to implement audio ducking. It will be called when
        OpenVoiceOS is listening or speaking to make sure the media playing isn't
        interfering.
        """
        # Not available in this plugin

    def restore_volume(self):
        """Restore normal volume.

        Called when to restore the playback volume to previous level after
        OpenVoiceOS has lowered it using lower_volume().
        """
        # Not available in this plugin

    def get_track_length(self) -> int:
        """
        getting the duration of the audio in milliseconds
        """
        # we only can estimate how much we already played as a minimum value
        return self.get_track_position()

    def get_track_position(self) -> int:
        """
        get current position in milliseconds
        """
        # approximate given timestamp of playback start
        if self.ts:
            return int((time.time() - self.ts) * 1000)
        return 0

    def set_track_position(self, milliseconds):
        """
        go to position in milliseconds
          Args:
                milliseconds (int): number of milliseconds of final position
        """
        # Not available in this plugin
