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
import socket

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from colors import Colors

colors = Colors(
    background="#2D2A2E",
    foreground="#FCFCFA",
    accent_1="#9A348E",
    accent_2="#DA627D",
    active="#FCA17D",
    inactive="#875541",
)

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Super + key
    Key(
        [mod],
        "h",
        lazy.layout.left(),
        desc="Move focus to left",
    ),
    Key(
        [mod],
        "l",
        lazy.layout.right(),
        desc="Move focus to right",
    ),
    Key(
        [mod],
        "j",
        lazy.layout.down(),
        desc="Move focus down",
    ),
    Key(
        [mod],
        "k",
        lazy.layout.up(),
        desc="Move focus up",
    ),
    Key(
        [mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    Key(
        [mod],
        "q",
        lazy.window.kill(),
        desc="Kill focused window",
    ),
    Key(
        [mod],
        "Return",
        lazy.spawn(terminal),
        desc="Launch terminal",
    ),
    Key(
        [mod],
        "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts",
    ),
    Key(
        [mod],
        "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("dmenu_run"),
        desc="Reset all window sizes",
    ),
    # Super + shift + key
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move window up",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        desc="Move window up",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Super + control + key
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down",
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        desc="Grow window up",
    ),
    Key(
        [mod, "control"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile",
    ),
    Key(
        [mod, "control"],
        "r",
        lazy.reload_config(),
        desc="Reload the config",
    ),
    # Alt + key
    Key(
        ["mod1"],
        "m",
        lazy.spawn("pcmanfm"),
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
    "margin": 16,
    "border_width": 2,
    "border_focus": colors.active,
    "border_normal": colors.inactive,
}

layouts = [
    layout.MonadTall(**layout_theme),
    # layout.Columns(margin=16, border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2),
    # layout.Columns(**layout_theme),
    # layout.Columns(**layout_theme),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(**layout_theme, num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    layout.TreeTab(**layout_theme),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="CaskaydiaCove Nerd Font Mono",
    fontsize=14,
    padding=3,
    background=colors.background,
    foreground=colors.foreground,
)
extension_defaults = widget_defaults.copy()

prompt = f"{os.environ['USER']}@{socket.gethostname()}: "

widgets_list = [
    widget.Sep(
        linewidth=3,
        paddding=10,
        foreground=colors.background,
    ),
    widget.QuickExit(
        default_text="",
        fontsize=32,
        countdown_format="{}",
    ),
    widget.Sep(
        linewidth=1,
        paddding=10,
        foreground=colors.background,
    ),
    widget.GroupBox(
        fontsize=12,
        margin_y=3,
        margin_x=2,
        padding_y=5,
        padding_x=4,
        borderwidth=3,
        active=colors.active,
        inactive=colors.inactive,
        rounded=False,
        highlight_method="line",
        highlight_color=colors.inactive,
        this_current_screen_border=colors.active,
        this_screen_border=colors.active,
        other_current_screen_border=colors.inactive,
        other_screen_border=colors.inactive,
    ),
    widget.WindowName(
        padding=0,
    ),
    widget.TextBox(
        font="CaskaydiaCove Nerd Font Mono",
        text="",
        padding=0,
        foreground=colors.accent_1,
        fontsize=37,
    ),
    widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
        background=colors.accent_1,
        padding=0,
        scale=0.7,
    ),
    widget.CurrentLayout(
        background=colors.accent_1,
    ),
    # widget.CheckUpdates(
    #     update_interval = 1800,
    #     distro = "Arch_checkupdates",
    #     display_format = "Updates: {updates} ",
    #     colour_have_updates = colors,
    #     colour_no_updates = colors,
    #     padding = 5,
    #     background = colors
    # ),
    widget.TextBox(
        font="CaskaydiaCove Nerd Font Mono",
        text="",
        padding=0,
        foreground=colors.accent_2,
        background=colors.accent_1,
        fontsize=37,
    ),
    widget.Clock(
        format="%d/%m/%Y %H:%M",
        background=colors.accent_2,
    ),
    widget.TextBox(
        font="CaskaydiaCove Nerd Font Mono",
        text="",
        padding=0,
        foreground=colors.accent_1,
        background=colors.accent_2,
        fontsize=37,
    ),
    widget.Systray(
        background=colors.accent_1,
        padding=5,
    ),
    # widget.BatteryIcon(
    #     background=colors,
    # ),
    # widget.Battery(
    #     background=colors,
    #     fontsize=12,
    #     format="{percent:2.0%}",
    # ),
    widget.Sep(
        linewidth=1,
        padding=10,
        background=colors.accent_1,
        foreground=colors.accent_1,
    ),
]


screens = [
    Screen(
        top=bar.Bar(
            widgets=widgets_list,
            size=24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
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
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
