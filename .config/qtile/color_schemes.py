from color_scheme import ColorScheme, Primary, Normal, Bright

gruvbox = ColorScheme(
    primary=Primary(
        background_darker="#1d2021",
        background_dark="#32302f",
        background="0x282828",
        background_light="#3c3836",
        background_lighter="#504945",
        foreground_darker="#d5c4a1",
        foreground_dark="#ebdbb2",
        foreground="0xebdbb2",
        foreground_light="#f2e5bc",
        foreground_lighter="#f9f5d7",
    ),
    normal=Normal(
        black="0x282828",
        red="0xcc241d",
        green="0x98971a",
        yellow="0xd79921",
        blue="0x458588",
        magenta="0xb16286",
        cyan="0x689d6a",
        white="0xa89984",
    ),
    bright=Bright(
        black="0x928374",
        red="0xfb4934",
        green="0xb8bb26",
        yellow="0xfabd2f",
        blue="0x83a598",
        magenta="0xd3869b",
        cyan="0x8ec07c",
        white="0xebdbb2",
    ),
    # extra=Extra(
    # 	normal_orange='#d65d0e',
    # 	bright_orange='#fe8019',
    # ),
)

dracula = ColorScheme(
    primary=Primary(
        background_darker="#191A21",
        background_dark="#21222C",
        background="#282a36",
        background_light="#343746",
        background_lighter="#424450",
        foreground="#f8f8f2",
    ),
    normal=Normal(
        black="#21222c",
        red="#ff5555",
        green="#50fa7b",
        yellow="#f1fa8c",
        blue="#bd93f9",
        magenta="#ff79c6",
        cyan="#8be9fd",
        white="#f8f8f2",
    ),
    bright=Bright(
        black="#6272a4",
        red="#ff6e6e",
        green="#69ff94",
        yellow="#ffffa5",
        blue="#d6acff",
        magenta="#ff92df",
        cyan="#a4ffff",
        white="#ffffff",
    ),
)
