set fish_greeting
set VIRTUAL_ENV_DISABLE_PROMPT "1"
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

if type "qtile" >> /dev/null 2>&1
    set -x QT_QPA_PLATFORMTHEME "qt5ct"
end

alias ls 'exa -lB --no-time --group-directories-first --icons'
alias la 'exa -laB --no-time --group-directories-first --icons'
alias cat 'bat'
alias grep 'rg'

if status --is-interactive
    # source ("/usr/bin/starship" init fish --print-full-init | psub)
    abbr --add --global pyproj "cd $HOME/Documents/python"
    abbr --add --global cproj "cd $HOME/Documents/c"
    abbr --add --global prog-ii "cd $HOME/Documents/c/prog-ii"
    abbr --add --global base "source $HOME/.python-venvs/base/bin/activate.fish"
    abbr --add --global ic "source $HOME/.python-venvs/ic/bin/activate.fish"
end

if status --is-interactive && type -q neofetch
    # Commands to run in interactive sessions can go here
    neofetch
end

starship init fish | source

