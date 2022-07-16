#!/bin/sh

normal_background="#282828"
normal_foreground="#ebdbb2"
selected_background="#d65d0e"
selected_foreground="#ebdbb2"

dmenu_run -i -nb $normal_background \
             -nf $normal_foreground \
             -sb $selected_background \
             -sf $selected_foreground \
             -fn "JetBrainsMono Nerd Font:bold:pixelsize=26"
