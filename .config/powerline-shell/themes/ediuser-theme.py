from powerline_shell.themes.default import DefaultColor

"""
colors from https://www.nordtheme.com/docs/colors-and-palettes
"""

# RESET is not a real color code. It is used as in indicator
# within the code that any foreground / background color should
# be cleared
blank = -1

night0 = 236 # nord0
night1 = 237 # nord1
night2 = 238 # nord2
night3 = 403
orange0  = 166 # nord4
orange1  = 208 # nord5
orange2  = 214 # nord6
frost0 = 244 # nord7
frost1 = 245 # nord8
frost2 = 249 # nord9
frost3 = 239  # nord10
red    = 167 # nord11
red0   = 52
orange = 173 # nord12
yellow = 179 # nord13
green  = 150 # nord14
green0 = 65
purple = 139 # nord15

class Color(DefaultColor):
    USERNAME_BG = blank
    USERNAME_FG = orange0

    HOSTNAME_FG = orange0
    HOSTNAME_BG = night0

    HOME_BG = frost2
    HOME_FG = orange2
    PATH_BG = night0
    PATH_FG = orange0
    CWD_FG = orange0
    CWD_BG = night3
    SEPARATOR_FG = orange0

    READONLY_BG = red
    READONLY_FG = orange2

    SSH_BG = orange
    SSH_FG = orange2

    REPO_CLEAN_BG = green0 
    REPO_CLEAN_FG = night1
    REPO_DIRTY_BG = red0
    REPO_DIRTY_FG = orange2

    JOBS_FG = frost3
    JOBS_BG = night0

    CMD_PASSED_BG = blank
    CMD_PASSED_FG = orange2
    CMD_FAILED_BG = blank
    CMD_FAILED_FG = orange2

    SVN_CHANGES_BG = REPO_DIRTY_FG
    SVN_CHANGES_FG = REPO_DIRTY_BG

    GIT_AHEAD_BG = night3
    GIT_AHEAD_FG = orange0
    GIT_BEHIND_BG = night3
    GIT_BEHIND_FG = orange0

    GIT_STAGED_BG = frost0
    GIT_STAGED_FG = night1
    GIT_NOTSTAGED_BG = orange
    GIT_NOTSTAGED_FG = orange2
    GIT_UNTRACKED_BG = purple
    GIT_UNTRACKED_FG = orange2
    GIT_CONFLICTED_BG = red
    GIT_CONFLICTED_FG = orange2

    GIT_STASH_BG = night0 
    GIT_STASH_FG = night1

    VIRTUAL_ENV_BG = green
    VIRTUAL_ENV_FG = night1

    BATTERY_NORMAL_BG = green
    BATTERY_NORMAL_FG = night1
    BATTERY_LOW_BG = red
    BATTERY_LOW_FG = orange2

    AWS_PROFILE_FG = frost3
    AWS_PROFILE_BG = night0

    TIME_BG = night3
    TIME_FG = orange0
