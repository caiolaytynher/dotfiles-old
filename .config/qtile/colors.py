class Colors():
    def __init__(self, **kwargs):
        self.background = [kwargs.get('background')] * 2
        self.foreground = [kwargs.get('foreground', '#FFFFFF')] * 2
        self.accent_1 = [kwargs.get('accent_1')] * 2
        self.accent_2 = [kwargs.get('accent_2')] * 2
        self.active = [kwargs.get('active')] * 2
        self.active_contrast = [kwargs.get('active_contrast')] * 2
        self.inactive = [kwargs.get('inactive')] * 2
