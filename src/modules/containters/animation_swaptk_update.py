class AnimationSwapTK(AnimationTK):
    def __init__(self):
        super().__init__()
        self._Start = None
        self._End = None
        self.p = None

    def add_animation_end(self, animTK : AnimationTK):
        if self._Start is None:
            self._Start = animTK
            self._End = animTK
            self.p = animTK
        else:
            self._End.nextNode = animTK
            self._End = animTK

    def get_current_animation(self):
        if self.p is not None:
            return self.p

    def play_animation(self):
        if self.p is not None:
            self.p.play_animation()

    def swap_animation(self):
        if self._Start is None:
            return

        if self.p is None:
            self.p = self._Start
        else:
            self.p = getattr(self.p, 'nextAnim', None)
            if self.p is None:
                self.p = self._Start
