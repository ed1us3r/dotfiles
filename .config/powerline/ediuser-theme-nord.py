from powerline_shell.themes.default import DefaultColor

"""
colors from https://www.nordtheme.com/docs/colors-and-palettes
"""

# RESET is not a real color code. It is used as in indicator
# within the code that any foreground / background color should
# be cleared
blank = -1

nord0 = 401
nord1 = 402
nord2 = 403
nord3 = 404
nord4 = 405
nord5 = 406
nord6 = 407

frost0 = 244
frost1 = 245
frost2 = 249 
frost3 = 239
 
red    = 167 
red0   = 52
orange = 173 
yellow = 179 
green  = 150 
green0 = 65
purple = 139 

class Color(DefaultColor):
    USERNAME_BG = blank
    USERNAME_FG = nord0

    HOSTNAME_FG = nord0
    HOSTNAME_BG = nord1

    HOME_BG = frost2
    HOME_FG = nord2
    PATH_BG = nord1
    PATH_FG = nord0
    CWD_FG = nord0
    CWD_BG = nord3
    SEPARATOR_FG = nord0

    READONLY_BG = red
    READONLY_FG = nord2

    SSH_BG = orange
    SSH_FG = nord2

    REPO_CLEAN_BG = green0 
    REPO_CLEAN_FG = nord4
    REPO_DIRTY_BG = red0
    REPO_DIRTY_FG = nord2

    JOBS_FG = frost3
    JOBS_BG = nord1

    CMD_PASSED_BG = blank
    CMD_PASSED_FG = nord2
    CMD_FAILED_BG = blank
    CMD_FAILED_FG = nord2

    SVN_CHANGES_BG = REPO_DIRTY_FG
    SVN_CHANGES_FG = REPO_DIRTY_BG

    GIT_AHEAD_BG = nord3
    GIT_AHEAD_FG = nord0
    GIT_BEHIND_BG = nord3
    GIT_BEHIND_FG = nord0

    GIT_STAGED_BG = frost0
    GIT_STAGED_FG = nord6
    GIT_NOTSTAGED_BG = orange
    GIT_NOTSTAGED_FG = nord2
    GIT_UNTRACKED_BG = purple
    GIT_UNTRACKED_FG = nord2
    GIT_CONFLICTED_BG = red
    GIT_CONFLICTED_FG = nord2

    GIT_STASH_BG = nord1 
    GIT_STASH_FG = nord6

    VIRTUAL_ENV_BG = green
    VIRTUAL_ENV_FG = nord6

    BATTERY_NORMAL_BG = green
    BATTERY_NORMAL_FG = nord6
    BATTERY_LOW_BG = red
    BATTERY_LOW_FG = nord2

    AWS_PROFILE_FG = frost3
    AWS_PROFILE_BG = nord1

    TIME_BG = nord3
    TIME_FG = nord0
