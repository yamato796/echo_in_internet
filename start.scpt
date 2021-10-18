#!/usr/bin/osascript
tell application "iTerm2"
    tell current session of current tab of current window
        split vertically with default profile
        write text "tshark -i en1"
    end tell
    tell second session of current tab of current window
        write text "echo test2"
    end tell
end tell
