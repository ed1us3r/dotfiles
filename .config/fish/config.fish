# Powerline Support
#xset b off

#set fish_function_path $fish_function_path "/usr/share/powerline/bindings/fish"

#source /usr/share/powerline/bindings/fish/powerline-setup.fish


set LC_CTYPE en_GB.UTF-8
set LC_TIME de_DE.UTF-8
set LC_ALL en_GB.UTF-8


# krew
set -gx PATH $PATH $HOME/.krew/bin


function fish_prompt
    powerline-shell --shell bare $status
end

# Aliases Import from Bash_aliases file
if test -f ~/.bash_aliases

  . ~/.bash_aliases
 
end

if test -f ~/.config/dircolors/nord_dir_colors

  test -r ~/.config/dircolors/nord_dir_colors && eval (dircolors ~/.config/dircolors/nord_dir_colors)

end


# Pager color adjustment

set fish_pager_color_selected_background --background=white



# Cowsay on Startup

fortune | cowsay -f ~/.config/cowsay/custom-cows/panda.cow



# Override fish-greeting

set fish_greeting



# visualbell disable

set visualbell none



# Path Add something to $path

# fish_add_path -a -path ~/.scripts

set --universal fish_user_paths $fish_user_paths ~/.scripts

set --universal fish_user_paths $fish_user_paths ~/bin



# When Using login Shell add

if status --is-login

    set -gx PATH $PATH ~/linux/bin

end



# podman aliases

alias podman-cleanup="podman rm -f (podman ps -qa)"

# other aliases

function fuck -d "Correct your previous console command"
  set -l fucked_up_command $history[1]
  env TF_SHELL=fish TF_ALIAS=fuck PYTHONIOENCODING=utf-8 thefuck $fucked_up_command THEFUCK_ARGUMENT_PLACEHOLDER $argv | read -l unfucked_command
  if [ "$unfucked_command" != "" ]
    eval $unfucked_command
    builtin history delete --exact --case-sensitive -- $fucked_up_command
    builtin history merge ^ /dev/null
  end
end

function podman-cleanup --wraps rm --description 'CLEANUP podman containers'

    podman rm -f (podman ps -qa)

end

set -gx KUBECONFIG '~/.kube/config'

# GPG setup

set -gx GPG_TTY (tty)
