from my_utils import listify
from collections import namedtuple

Colors = namedtuple(
    "Colors",
    [
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    ],
)

PrimaryColors = namedtuple(
    "PrimaryColors",
    [
        "background",
        "foreground",
    ],
)

ColorPallete = namedtuple(
    "ColorPallete",
    [
        "primary",
        "normal",
        "bright",
        "dim",
    ],
)

garuda_dracula = ColorPallete(
    primary=PrimaryColors(
        background=listify("#282a36"),
        foreground=listify("#f8f8f2"),
    ),
    normal=Colors(
        black=listify("#000000"),
        red=listify("#ff5555"),
        green=listify("#50fa7b"),
        yellow=listify("#f1fa8c"),
        blue=listify("#bd93f9"),
        magenta=listify("#ff79c6"),
        cyan=listify("#8be9fd"),
        white=listify("#bbbbbb"),
    ),
    bright=Colors(
        black=listify("#555555"),
        red=listify("#ff5555"),
        green=listify("#50fa7b"),
        yellow=listify("#f1fa8c"),
        blue=listify("#caa9fa"),
        magenta=listify("#ff79c6"),
        cyan=listify("#8be9fd"),
        white=listify("#ffffff"),
    ),
    dim=Colors(
        black=listify("#000000"),
        red=listify("#a90000"),
        green=listify("#049f2b"),
        yellow=listify("#a3b106"),
        blue=listify("#530aba"),
        magenta=listify("#bb006b"),
        cyan=listify("#433364"),
        white=listify("#5f5f5f"),
    ),
)
