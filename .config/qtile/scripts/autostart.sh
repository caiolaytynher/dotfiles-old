#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

lxsession &
run nm-applet &
picom --config .config/picom/picom-blur.conf --experimental-backends &
nitrogen --restore --set-zoom-fill &
run volumeicon &
flameshot &
