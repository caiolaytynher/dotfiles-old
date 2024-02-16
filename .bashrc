# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# alias ls='ls --color=auto'
alias ls='exa -lB --no-time --group-directories-first --icons'
alias la='exa -laB --no-time --group-directories-first --icons'
alias cat='bat'
PS1='[\u@\h \W]\$ '

eval "$(starship init bash)"

eval "$(zoxide init bash)"

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

eval "$(pyenv virtualenv-init -)"
