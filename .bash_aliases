# Global Aliases
# Careful in here! Just juse "alias <ALIAS>='command1 arg1 arg2' " - Syntax as this file is sourced across diffrent shell's.

# LS and CD
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'
alias please='sudo'
alias shutdown='systemctl poweroff'
alias reboot='systemctl reboot'
#alias .='cd ..'
alias ..='cd ..'
alias cls='clear'

alias oc='kubectl'

alias kubectl='kubecolor'

# Dots config !!!
alias dots="git -C $HOME --git-dir=$HOME/.dotfiles --work-tree=$HOME"
