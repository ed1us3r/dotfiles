# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi



# User specific environment and startup programs
if [ -f ~/.config/dots/include ]; then
    . ~/.config/dots/include
fi


# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
  # kubectl shell completion
  source '/home/ediuser/.kube/completion.bash.inc'
  