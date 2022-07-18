#!/bin/sh

function show_brightness() {
    brightness=$(printf "%.0f" $(brillo))
    dunstify -a "change_brightness" \
             -u low \
             -r 9991 \
             -h int:value:$brightness \
             -t 2000 \
             -i "$HOME/.config/dunst/icons/brightness.svg" \
             "Brightness: $brightness%"
}

case $1 in
    up)
        pkexec brillo -q -A 5
        show_brightness
        ;;
    down)
        pkexec brillo -q -U 5
        show_brightness
        ;;
    *)
        exit 1
        ;;
esac
