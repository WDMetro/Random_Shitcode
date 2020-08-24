from manimlib.imports import *


class Test(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "text": Text("this is a test").scale(2).set_color(BLACK),
    }

    def construct(self):
        self.play(Write(self.text, run_time=5))
        self.wait()
