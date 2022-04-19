from colors import Colors

colors = Colors(
    background="#232222",
    accent_1="#2C3325",
    accent_2="#5E4B44",
    active="#E6E3E2",
    inactive="#323731",
)

if __name__ == "__main__":
    print(f'{colors.background = }')
    print(f'{colors.foreground = }')
    print(f'{colors.accent_1 = }')
    print(f'{colors.accent_2 = }')
    print(f'{colors.active = }')
    print(f'{colors.inactive = }')