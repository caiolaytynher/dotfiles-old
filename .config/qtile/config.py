# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
import socket
import subprocess
import psutil  # Enable Swallow
from collections import namedtuple  # Better color organization
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy

from libqtile.widget import Spacer

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


terminal = "alacritty"  # terminal of choice

keys = [
    # ---------------------
    # SUPER + FUNCTION KEYS
    # ---------------------
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn("xterm")),
    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "d", lazy.spawn("nwggrid -p -o 0.4")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "KP_Enter", lazy.spawn("alacritty")),
    Key([mod], "x", lazy.shutdown()),
    # ------------------
    # SUPER + SHIFT KEYS
    # ------------------
    Key([mod, "shift"], "Return", lazy.spawn("pcmanfm")),
    Key(
        [mod, "shift"],
        "d",
        lazy.spawn(
            "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf "
            + "'#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'"
        ),
    ),
    #    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
    # ------------------
    # CONTROL + ALT KEYS
    # ------------------
    Key(
        ["mod1", "control"],
        "o",
        lazy.spawn(home + "/.config/qtile/scripts/picom-toggle.sh"),
    ),
    Key(["mod1", "control"], "t", lazy.spawn("xterm")),
    Key(["mod1", "control"], "u", lazy.spawn("pavucontrol")),
    # --------------
    # ALT + ... KEYS
    # --------------
    Key(["mod1"], "p", lazy.spawn("pamac-manager")),
    Key(["mod1"], "f", lazy.spawn("firedragon")),
    Key(["mod1"], "m", lazy.spawn("pcmanfm")),
    Key(["mod1"], "w", lazy.spawn("garuda-welcome")),
    # --------------------
    # CONTROL + SHIFT KEYS
    # --------------------
    Key([mod2, "shift"], "Escape", lazy.spawn("lxtask")),
    # -----------
    # SCREENSHOTS
    # -----------
    Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures")),
    Key([mod2], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures")),
    #    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),
    # ---------------
    # MULTIMEDIA KEYS
    # ----------------------------
    # INCREASE/DECREASE BRIGHTNESS
    # ----------------------------
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    # -----------------------------
    # INCREASE/DECREASE/MUTE VOLUME
    # -----------------------------
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    #    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    #    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    #    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    #    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),
    # -----------------
    # QTILE LAYOUT KEYS
    # -----------------
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    # ------------
    # CHANGE FOCUS
    # ------------
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # ----------------------------
    # RESIZE UP, DOWN, LEFT, RIGHT
    # ----------------------------
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    # -----------------------------------
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    # -----------------------------------
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # -------------------
    # FLIP LAYOUT FOR BSP
    # -------------------
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # ----------------------------------
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    # ----------------------------------
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # ------------------
    ### Treetab controls
    # ------------------
    Key(
        [mod, "control"],
        "k",
        lazy.layout.section_up(),
        desc="Move up a section in treetab",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.section_down(),
        desc="Move down a section in treetab",
    ),
    # --------------------------------------------------
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    # --------------------------------------------------
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    # ----------------------
    # TOGGLE FLOATING LAYOUT
    # ----------------------
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# group_labels = ["", "", "", "", "", "", "", "", "", ""]
group_labels = ["", "", "", "", "", "", "", "", "", ""]

group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "treetab",
    "floating",
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # -----------------
            # CHANGE WORKSPACES
            # -----------------
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # ------------------------------------------------------------
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            # ------------------------------------------------------------
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # ---------------------------------------------------------------------------
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            # ---------------------------------------------------------------------------
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(),
            ),
        ]
    )

# COLORS FOR THE BAR


def listify(color_name: str, gradient_color: str = "") -> list[str]:
    """
    Converts a color into a valid qtile color list format.
    '#FFFFFF' -> ['#FFFFFF', '#FFFFFF']
    """
    if gradient_color:
        return [color_name, gradient_color]

    return [color_name] * 2


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

PalleteTemplate = namedtuple(
    "PalleteTemplate",
    [
        "primary",
        "normal",
        "bright",
        "dim",
    ],
)

garuda_dracula = PalleteTemplate(
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

# LAYOUTS

layout_theme = {
    "margin": 9,
    "border_width": 2,
    "border_focus": garuda_dracula.normal.blue,
    "border_normal": garuda_dracula.dim.white,
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(
        sections=["FIRST", "SECOND"],
        bg_color="#141414",
        active_bg="#0000ff",
        inactive_bg="#1e90ff",
        padding_y=5,
        section_top=10,
        panel_width=280,
    ),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme),
]


# WIDGETS FOR THE BAR


widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=15,
    padding=2,
    background=garuda_dracula.primary.background,
    foreground=garuda_dracula.primary.foreground,
)


def init_powerline_widget(
    foreground: list[str] = garuda_dracula.primary.foreground,
    background: list[str] = garuda_dracula.primary.background,
    # text="",
    text=" ",
    # text="",
) -> widget.TextBox:
    """
    Creates a template widget to create the powerline effect implementation.
    """
    return widget.TextBox(
        text=text,
        padding=0,
        foreground=foreground,
        background=background,
        fontsize=32,
    )


prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

fg_spacer = widget.Spacer(
    length=9,
    background=garuda_dracula.normal.blue,
)
bg_spacer = widget.Spacer(
    length=7,
)
group_box = widget.GroupBox(
    fontsize=40,
    borderwidth=3,
    active=garuda_dracula.primary.foreground,
    inactive=garuda_dracula.dim.white,
    rounded=False,
    highlight_method="text",
    urgent_alert_method="text",
    this_current_screen_border=garuda_dracula.normal.blue,
    disable_drag=True,
)
hidden_task_list = widget.WidgetBox(
    widgets=[
        widget.TaskList(
            highlight_method="border",
            borderwidth=1,
            icon_size=17,
            max_title_width=150,
            rounded=True,
            padding=1,
            border=garuda_dracula.normal.blue,
            margin=0,
            txt_floating="🗗",
            txt_minimized=">_ ",
        ),
    ],
    text_closed=" ",
    text_open=" ",
    foreground=garuda_dracula.normal.blue,
)
current_layout = [
    widget.CurrentLayoutIcon(
        background=garuda_dracula.normal.blue,
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        padding=0,
        scale=0.7,
    ),
    widget.CurrentLayout(
        background=garuda_dracula.normal.blue,
    ),
]
check_updates = widget.CheckUpdates(
    background=garuda_dracula.normal.blue,
    display_format=" {updates}",
    no_update_string=" 0",
    mouse_callbacks={
        "Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")
    },
)
hidden_net = widget.WidgetBox(
    widgets=[
        widget.Net(
            # interface=["wlp6s0"],
            interface=["wlp1s0"],
            format="{down} 祝{up}",
            padding=0,
            foreground=garuda_dracula.normal.blue,
        )
    ],
    text_closed=" ",
    text_open=" : ",
    foreground=garuda_dracula.normal.blue,
)
hidden_pc_status = widget.WidgetBox(
    widgets=[
        widget.DF(
            foreground=garuda_dracula.normal.blue,
            visible_on_warn=False,
            format=" {uf}G {r:.0f}% ",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
        ),
        widget.CPU(
            foreground=garuda_dracula.normal.blue,
            update_interval=1,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
            format=" {freq_current}GHz {load_percent}% ",
        ),
        widget.Memory(
            foreground=garuda_dracula.normal.blue,
            format=" {MemUsed:.0f}M/{MemTotal:.0f}M",
            update_interval=1,
            measure_mem="M",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(terminal + " -e htop")},
        ),
    ],
    text_closed="",
    text_open=": ",
    foreground=garuda_dracula.normal.blue,
)
clock = widget.Clock(
    background=garuda_dracula.normal.blue,
    format=" %d/%m/%Y  %H:%M",
)
hidden_systray = widget.WidgetBox(
    widgets=[
        widget.Systray(
            icon_size=20,
            padding=4,
        ),
    ],
    foreground=garuda_dracula.normal.blue,
    text_closed="  ",
    text_open="  ",
)
battery = widget.Battery(
    foreground=garuda_dracula.normal.blue,
    format="{char} {percent:2.0%}",
    charge_char=" ",
    discharge_char="",
    full_char="",
    unknown_char="",
    empty_char="",
    low_percentage=0.2,
)
python_logo = widget.TextBox(
    text=" ",
    fontsize=20,
    background=garuda_dracula.normal.blue,
    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("jgmenu_run")},
)
right_separator_bg = init_powerline_widget(
    background=garuda_dracula.normal.blue,
    foreground=garuda_dracula.primary.background,
)
right_separator_fg = init_powerline_widget(
    foreground=garuda_dracula.normal.blue,
    background=garuda_dracula.primary.background,
)
left_separator_bg = init_powerline_widget(
    text=" ",
    background=garuda_dracula.normal.blue,
    foreground=garuda_dracula.primary.background,
)
left_separator_fg = init_powerline_widget(
    text=" ",
    foreground=garuda_dracula.normal.blue,
    background=garuda_dracula.primary.background,
)

widgets_list = [
    fg_spacer,
    python_logo,
    left_separator_fg,
    group_box,
    left_separator_bg,
    *current_layout,
    left_separator_fg,
    hidden_task_list,
    widget.Spacer(),
    hidden_systray,
    hidden_pc_status,
    right_separator_fg,
    check_updates,
    right_separator_bg,
    hidden_net,
    right_separator_fg,
    clock,
    right_separator_bg,
    battery,
    bg_spacer,
]

widgets_screen1 = widgets_list.copy()
widgets_screen2 = widgets_list.copy()

screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_screen1,
            size=25,
            opacity=1,
            background="000000",
            margin=[9, 9, 2, 9],
        )
    ),
    Screen(
        top=bar.Bar(
            widgets=widgets_screen2,
            size=20,
            opacity=1,
            background="000000",
        )
    ),
]

# MOUSE CONFIGURATION
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["pcmanfm", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "pcmanfm", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(title="branchdialog"),
        Match(title="Open File"),
        Match(title="pinentry"),
        Match(wm_class="ssh-askpass"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="Lxpolkit"),
        Match(wm_class="yad"),
        Match(wm_class="Yad"),
        Match(wm_class="Cairo-dock"),
        Match(wm_class="cairo-dock"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"

# ENABLE SWALLOW


@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {
        c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()
    }
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, "parent"):
        window.parent.minimized = False
