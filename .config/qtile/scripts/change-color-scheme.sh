#!/bin/sh

color_schemes="dracula\ngruvbox"
color_scheme=$(printf $color_schemes | rofi -dmenu -i -p " ")
app_path=$HOME/Documents/python/change-color-scheme/src/main.py

python $app_path $color_scheme
