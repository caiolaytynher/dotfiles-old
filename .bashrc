#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# alias ls='ls --color=auto'
alias ls='exa -lB --no-time --group-directories-first --icons'
alias la='exa -laB --no-time --group-directories-first --icons'
alias cat='bat'
PS1='[\u@\h \W]\$ '

neofetch

eval "$(starship init bash)"

