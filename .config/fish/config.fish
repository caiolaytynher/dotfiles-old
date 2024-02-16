set fish_greeting
set VIRTUAL_ENV_DISABLE_PROMPT "1"
# set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

if type "qtile" >> /dev/null 2>&1 # similar to type -q, but includes the errors
  set -x QT_QPA_PLATFORMTHEME "qt5ct"
end

function mkvenv
  set -l name (basename (pwd))
  set -l venvpath $HOME/.python-venvs

  if test -e $venvpath/$name
    echo "The venv already exists."
    return
  end

  python -m venv $HOME/.python-venvs/$name
end

function rmvenv
  set -l name (basename (pwd))
  set -l venvpath $HOME/.python-venvs

  if not test "$VIRTUAL_ENV" = "" # if venv is active
    deactivate
  end

  if test -e $venvpath/$name/
    rm -r $venvpath/$name/
  end
end

function activate
  set -l name (basename (pwd))
  set -l venvpath $HOME/.python-venvs

  if not test -e $venvpath/$name/
    read -P 'No venv available, create one? (Y/n) ' -l choice
    set -l choice (string lower $choice)

    if test $choice = "n"
      return
    end

    mkvenv
  end

  source $venvpath/$name/bin/activate.fish
end

if status --is-interactive
  # Commands to run in interactive sessions, i.e. connected to a keyboard
  # zoxide init --cmd cd fish | source
  zoxide init fish | source

  # if type -q neofetch
  #   neofetch
  # end

  if type -q starship
    starship init fish | source
  end

  set -l projects $HOME/Projects
  set -l venvs $HOME/.python-venvs

  abbr --add --global pyproj "cd $projects/python"
  abbr --add --global pytesting "cd $projects/python/testing"
  abbr --add --global cproj "cd $projects/c"
  abbr --add --global prog2 "cd $projects/c/prog-ii"
  abbr --add --global base "source $venvs/base/bin/activate.fish"

  alias ls 'exa -lB --no-time --group-directories-first --icons'
  alias la 'exa -laB --no-time --group-directories-first --icons'
  alias cat 'bat'
  alias grep 'rg'
end

