# dotfiles
A Space for all of my configs. 

## Init

At the core of it all, is an alias in my .zshrc/.bashrc:

```
alias dots="git -C $HOME --git-dir=$HOME/.dotfiles --work-tree=$HOME"
```

I have a script that automates install, but it can be manually installed with:

```
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

