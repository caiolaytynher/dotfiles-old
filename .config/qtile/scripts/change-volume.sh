#!/bin/sh

function show_volume() {
    volume=$(pamixer --get-volume)
    dunstify -a "change_volume" \
             -u low \
             -r 9992 \
             -h int:value:"$volume" \
             -t 2000 \
             -i "$HOME/.config/dunst/icons/volume-$1.svg" \
             "Volume: $volume%"
}

case $1 in
    up)
        pamixer -u
        pamixer -i 5
        show_volume up
        ;;
    down)
        pamixer -u
        pamixer -d 5
        show_volume down
        ;;
    mute)
        pamixer -t
        if [[ $(pamixer --get-mute) == "true" ]]; then
            dunstify -a "change_volume" \
                     -u low \
                     -r 9992 \
                     -t 2000 \
                     -i "$HOME/.config/dunst/icons/volume-mute.svg" \
                     "Muted"
        else
            show_volume up
        fi
        ;;
    *)
        exit 1
        ;;
esac
