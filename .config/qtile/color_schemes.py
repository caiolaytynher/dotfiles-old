from color_scheme import ColorScheme, Primary, Normal, Bright

gruvbox = ColorScheme(
    primary=Primary(
        background_darker=["#1d2021", "#1d2021"],
        background_dark=["#32302f", "#32302f"],
        background=["0x282828", "0x282828"],
        background_light=["#3c3836", "#3c3836"],
        background_lighter=["#504945", "#504945"],
        foreground_darker=["#d5c4a1", "#d5c4a1"],
        foreground_dark=["#ebdbb2", "#ebdbb2"],
        foreground=["0xebdbb2", "0xebdbb2"],
        foreground_light=["#f2e5bc", "#f2e5bc"],
        foreground_lighter=["#f9f5d7", "#f9f5d7"],
    ),
    normal=Normal(
        black=["0x282828", "0x282828"],
        red=["0xcc241d", "0xcc241d"],
        green=["0x98971a", "0x98971a"],
        # yellow=['0xd79921', '0xd79921'],
        yellow=["#d65d0e", "#d65d0e"],  # Normal Orange
        blue=["0x458588", "0x458588"],
        magenta=["0xb16286", "0xb16286"],
        cyan=["0x689d6a", "0x689d6a"],
        white=["0xa89984", "0xa89984"],
    ),
    bright=Bright(
        black=["0x928374", "0x928374"],
        red=["0xfb4934", "0xfb4934"],
        green=["0xb8bb26", "0xb8bb26"],
        # yellow=['0xfabd2f', '0xfabd2f'],
        bright_orange=["#fe8019", "#fe8019"],  # Bright Orange
        blue=["0x83a598", "0x83a598"],
        magenta=["0xd3869b", "0xd3869b"],
        cyan=["0x8ec07c", "0x8ec07c"],
        white=["0xebdbb2", "0xebdbb2"],
    ),
)
