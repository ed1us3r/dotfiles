# dotfiles
A Space for all of my configs. 

## What do i need?

**BASIC**

- [x] git
- [x] bash

**EXTENDED**

- [x] powerline
- [x] fish
- [x] toolbox

**Optional**

- [x] fortune & cowsay
- [x] thefuck
- [x] touchegg

## Init

Source [gist:ed1us3r/init-dots.sh](https://gist.github.com/ed1us3r/50e031a3bbd799212e749d33c278126a)

``` bash

(
  dots() { git -C $HOME --git-dir=$HOME/.dotfiles --work-tree=$HOME $@; };
  export dots &&
  cd ~ &&
  git clone --bare https://github.com/ed1us3r/dotfiles .dotfiles &&
  dots config --local status.showUntrackedFiles no &&
  dots reset --hard &&
  echo "Init Complete" &&
  bash -i source ~/.bash_profile
)
```

## Init - Manually

At the core of it all, is an alias in my .zshrc/.bashrc:

``` bash
alias dots="git -C $HOME --git-dir=$HOME/.dotfiles --work-tree=$HOME"
```

I have a script that automates install, but it can be manually installed with:

``` bash 
cd ~
git clone --bare https://github.com/<my-git-acc>/dotfiles .dotfiles
dots config --local status.showUntrackedFiles no
dots reset --hard
```

So my home directory is basically a git repo, but to avoid tools getting confused, I renamed .git to .dotfiles

## Credits

https://www.reddit.com/r/git/comments/qy03le/aliasfree_gitonly_approach_to_tracking_dotfiles/

In Combination with

https://www.reddit.com/r/linuxquestions/comments/r3qyjf/dotfile_manager_like_git/?chainedPosts=t3_qy03le 

runroot fuckup with my moved containers partition.

https://github.com/containers/podman/issues/3234
