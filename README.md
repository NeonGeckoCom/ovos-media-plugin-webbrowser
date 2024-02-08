# ovos-media-plugin-webbrowser

[webbrowser](https://docs.python.org/3/library/webbrowser.html) plugin for [ovos-media](https://github.com/OpenVoiceOS/ovos-media)

Under Unix, graphical browsers are preferred under X11, but text-mode browsers will be used if graphical browsers are not available or an X11 display isn’t available. If text-mode browsers are used, the calling process will block until the user exits the browser.

If the environment variable BROWSER exists, it is interpreted as the os.pathsep-separated list of browsers to try ahead of the platform defaults. When the value of a list part contains the string %s, then it is interpreted as a literal browser command line to be used with the argument URL substituted for %s; if the part does not contain %s, it is simply interpreted as the name of the browser to launch. [1]

For non-Unix platforms, or when a remote browser is available on Unix, the controlling process will not wait for the user to finish with the browser, but allow the remote browser to maintain its own windows on the display. If remote browsers are not available on Unix, the controlling process will launch a new browser and wait.

## Install

`pip install ovos-media-plugin-webbrowser`

## Configuration


```javascript
{
 "media": {

    "preferred_web_services": ["webbrowser"],

    // PlaybackType.WEBVIEW handlers
    "web_players": {
        // webbrowser-open to handle uris
        "webbrowser": {
            // the plugin name
            "module": "ovos-media-web-plugin-webbrowser",

            // users may request specific handlers in the utterance
            // using these aliases
            "aliases": ["Browser"],

            // deactivate a plugin by setting to false
            "active": true
        }
    }
}
```