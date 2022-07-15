from dataclasses import dataclass


@dataclass
class Primary:
    background_darker: str
    background_dark: str
    background: str
    background_light: str
    background_lighter: str
    foreground_darker: str
    foreground_dark: str
    foreground: str
    foreground_light: str
    foreground_lighter: str


@dataclass
class Normal:
    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str


@dataclass
class Bright:
    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str


@dataclass
class ColorScheme:
    primary: Primary
    normal: Normal
    bright: Bright
