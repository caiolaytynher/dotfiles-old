#!/bin/sh

color_schemes="Dracula\nGruvbox"
theme_path=$HOME/.config/rofi/change-color-scheme.rasi
chosen=$(printf $color_schemes | rofi -dmenu -i -p " " -theme $theme_path)

if [[ $chosen =~ "Dracula" ]]; then
	color_scheme="dracula"
elif [[ $chosen =~ "Gruvbox" ]]; then
	color_scheme="gruvbox"
fi

app_path=$HOME/Documents/python/change-color-scheme/src/main.py

python $app_path $color_scheme
