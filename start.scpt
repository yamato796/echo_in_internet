#!/usr/bin/osascript
if application "iTerm" is running then
    tell application "iTerm"
        create window with default profile
    end tell
else 
    activate application "iTerm"
end if

tell application "iTerm"
    tell current session of current tab of current window
    split vertically with default profile
        write text "cd ~/echo_in_internet"
        write text "python3 main.py 2>&1 1>out.txt &"
        write text "tshark -i en1"
    end tell
    tell second session of current tab of current window
        set columns to 60 
        write text "cd ~/echo_in_internet"
        write text "tail -f audio_record.log"
    end tell
end tell
