# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/caio/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

[[ $- != *i* ]] && return

alias ls='exa -lB --no-time --group-directories-first --icons'
alias la='exa -laB --no-time --group-directories-first --icons'
alias cat='bat'

neofetch

eval "$(starship init zsh)"

# Plugins
source $HOME/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $HOME/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source $HOME/.config/zsh/zsh-history-substring-search/zsh-history-substring-search.zsh
