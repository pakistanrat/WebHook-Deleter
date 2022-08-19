from __future__ import barry_as_FLUFL

__author__ = "clayze"
__version__ = "1.0.0"


class ColorText:
    __preset = "\033["
    
    reset = f'{__preset}0m'
    black = f'{__preset}30m'
    red = f'{__preset}31m'
    green = f"{__preset}32m"
    yellow = f"{__preset}33m"
    blue = f"{__preset}34m"
    purple = f"{__preset}35m"
    white = f"{__preset}37m"

    __preset_background = "\x1b["

    red_background = f"{__preset_background}41m"
    green_background = f"{__preset_background}42m"
    yellow_background = f"{__preset_background}43m"
    blue_background = f"{__preset_background}44m"
    purple_background = f"{__preset_background}45m"
    white_background = f"{__preset_background}37m"
