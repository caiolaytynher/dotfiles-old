set fish_greeting
set VIRTUAL_ENV_DISABLE_PROMPT "1"
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"

if type "qtile" >> /dev/null 2>&1 # similar to type -q, but includes the errors
  set -x QT_QPA_PLATFORMTHEME "qt5ct"
end

alias ls 'exa -lB --no-time --group-directories-first --icons'
alias la 'exa -laB --no-time --group-directories-first --icons'
alias cat 'bat'
alias grep 'rg'

if type -q python
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

    if test -e $venvpath/$name/
      rm -r $venvpath/$name/
    end
  end

  function activate
    set -l name (basename (pwd))
    set -l venvpath $HOME/.python-venvs

    if not test -e $venvpath/$name/
      echo "No venv available, create one? (Y/n)"
      read choice

      if not test \( $choice = "Y" \) -o \( $choice = "y" \)
        return
      end

      mkvenv
    end

    source $venvpath/$name/bin/activate.fish
  end
end

if status --is-interactive
  # Commands to run in interactive sessions, i.e. connected to a keyboard

  if type -q neofetch
    neofetch
  end

  if type -q starship
    starship init fish | source
  end

  abbr --add --global pyproj "cd $HOME/Projects/python"
  abbr --add --global pytesting "cd $HOME/Projects/python/testing"
  abbr --add --global cproj "cd $HOME/Projects/c"
  abbr --add --global prog2 "cd $HOME/Projects/c/prog-ii"
  abbr --add --global base "source $HOME/.python-venvs/base/bin/activate.fish"
end
