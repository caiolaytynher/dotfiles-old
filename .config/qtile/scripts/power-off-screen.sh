#!/bin/sh

options="\n\n"
main_screen_theme=$HOME/.config/rofi/power-off-screen.rasi
confirmation_screen_theme=$HOME/.config/rofi/yes-or-no.rasi
option=$(printf $options | rofi -dmenu -theme $main_screen_theme)

if [[ -z $option ]]; then
    exit 1
fi

confirm=$(printf "Yes\nNo" | rofi -dmenu -p "Are you sure?" -theme $confirmation_screen_theme)

if [[ $confirm == "No" ]] || [[ -z $confirm ]]; then
    exit 1
fi

case $option in
    "") shutdown now ;;
    "") reboot ;;
    "") qtile cmd-obj -o cmd -f shutdown ;;
    *) exit 1 ;;
esac

