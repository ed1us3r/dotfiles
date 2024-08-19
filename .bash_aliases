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

# FileSystem Util - enable color support conditionally
# enable color support of ls and also add handy aliases
# Uncomment if for better compatability as it prevents from failing alias statements when dircolors are not available
# fish (/bin/fish) Shell will fail when sourcing those aliases when if statement is active
#if [ -x /usr/bin/dircolors ]; then
test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
alias ls='ls --color=auto'
alias dir='dir --color=auto'
alias vdir='vdir --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
#fi

# Dots config !!!
alias dots="git -C $HOME --git-dir=$HOME/.dotfiles --work-tree=$HOME"