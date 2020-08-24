from manimlib.imports import *


class RotateObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP)
        textM.rotate(PI / 4)
        self.play(Write(textM), Write(textC))
        self.wait(2)
        self.play(Rotate(textM, TAU / 8, rate_func=smooth))
        self.wait(2)
        textM.rotate(PI / 4)
        self.wait(2)
        textM.rotate(PI / 4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)


class ListFor(Scene):
    def construct(self):  # no usar siempre frac
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in [0, 1, 3, 4]:
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)


class ForRange1(Scene):
    def construct(self):  # no usar siempre frac
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in range(3):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)


class ForRange2(Scene):
    def construct(self):  # no usar siempre frac
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i in range(2, 6):
            text[i].set_color(RED)
        self.play(Write(text))
        self.wait(3)


class ForTwoVariables(Scene):
    def construct(self):  # no usar siempre frac
        text = TexMobject("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]")
        for i, color in [(2, RED), (4, PINK)]:
            text[i].set_color(color)
        self.play(Write(text))
        self.wait(3)


class ChangeSize(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=0}^n i=\\frac{n(n+1)}{2}")
        self.add(text)
        self.wait()
        text.scale_in_place(2)
        self.wait(2)


class SuccessionExample1(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-2, x_max=2)
        text = TextMobject("Text").next_to(number_line, DOWN)
        dashed_line = DashedLine(
            number_line.get_left(), number_line.get_right(), color=YELLOW,
        ).set_stroke(width=11)

        self.add(number_line)
        self.wait(0.3)

        self.play(
            LaggedStart(
                *[
                    ShowCreationThenDestruction(dashed_segment)
                    for dashed_segment in dashed_line
                ],
                run_time=5,
            ),
            AnimationGroup(
                Animation(Mobject(), run_time=2.1), Write(text), lag_ratio=1
            ),
        )
        self.wait()


class ColoringText(Scene):
    def construct(self):
        text = TextMobject("Text or object")
        self.play(
            LaggedStart(
                *[Write(letter) for letter in text],
                run_time=5
                # ApplyMethod, letter, lambda m: (m.set_color, YELLOW), run_time=0.12
            )
        )
        self.wait(0.5)


class CrossText2(Scene):
    def construct(self):
        text = TexMobject("\\sum_{i=1}^{\\infty}i", "=", "-\\frac{1}{2}")
        eq = VGroup(text[1], text[2])
        cross = Cross(eq)
        cross.set_stroke(RED, 6)
        self.play(Write(text))
        self.wait(0.5)
        self.play(ShowCreation(cross))
        self.wait(2)


class CopyTextV1(Scene):
    def construct(self):
        formula = TexMobject(
            "\\frac{d}{dx}",  # 0
            "(",  # 1
            "u",  # 2
            "+",  # 3
            "v",  # 4
            ")",  # 5
            "=",  # 6
            "\\frac{d}{dx}",  # 7
            "u",  # 8
            "+",  # 9
            "\\frac{d}{dx}",  # 10
            "v",  # 11
        )
        formula.scale(2)
        self.play(Write(formula[0:7]))
        self.wait()
        self.play(
            ReplacementTransform(formula[2].copy(), formula[8]),
            ReplacementTransform(formula[4].copy(), formula[11]),
            ReplacementTransform(formula[3].copy(), formula[9]),
        )
        self.wait()
        self.play(
            ReplacementTransform(formula[0].copy(), formula[7]),
            ReplacementTransform(formula[0].copy(), formula[10]),
        )
        self.wait()


class CopyTwoFormulas1(Scene):
    def construct(self):
        formula1 = TexMobject(
            "\\neg", "\\forall", "x", ":", "P(x)"  # 0  # 1  # 2  # 3  # 4
        )
        formula2 = TexMobject(
            "\\exists", "x", ":", "\\neg", "P(x)"  # 0  # 1  # 2  # 3  # 4
        )
        for size, pos, formula in [(2, 2 * UP, formula1), (2, 2 * DOWN, formula2)]:
            formula.scale(size)
            formula.move_to(pos)
        self.play(Write(formula1))
        self.wait()
        changes = [
            [
                (0, 1, 2, 3, 4),
                # | | | | |
                # v v v v v
                (3, 0, 1, 2, 4),
            ],
        ]
        for pre_ind, post_ind in changes:
            self.play(
                *[
                    ReplacementTransform(formula1[i].copy(), formula2[j])
                    for i, j in zip(pre_ind, post_ind)
                ],
                run_time=2,
            )
            self.wait()


class ChangeTextColorAnimation(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.scale(3)
        self.play(Write(text))
        self.wait()
        self.play(text.set_color, YELLOW, run_time=2)
        self.wait()


class TransformIssuesSolutionInfallible(Scene):
    def construct(self):
        #                   0   1   2
        text_1 = TextMobject("A", "B", "C")
        # text_1=TextMobject("A","B","C")[0] # <- Recent versions
        #                   0
        text_2 = TextMobject("B")
        # text_2=TextMobject("B")[0]

        text_2.next_to(text_1, UP, buff=1)

        # Create a copy of the objects

        text_1_1_c = (
            TextMobject("B")
            .match_style(text_1[1])
            .match_width(text_1[1])
            .move_to(text_1[1])
        )

        # Add the elements 0 and 2 of text_1 to screen and text_2
        self.play(*[FadeIn(text_1[i]) for i in [0, 2]], FadeIn(text_2))

        self.wait()

        self.play(
            # Add [:] to the firts or second parameter
            ReplacementTransform(text_2, text_1_1_c)
        )
        self.remove(text_1_1_c)
        self.add(text_1[1])

        self.wait()


class ChangeBackgroundColor(Scene):
    CONFIG = {
        "camera_config": {"background_color": RED},
        "text": TexMobject(r"\frac{d}{dx}\Bigr|_{y=2}").scale(5),
    }

    def construct(self):
        self.add(self.text)
        self.wait()


class WhatIsCONFIG(Scene):
    CONFIG = {
        "object_1": TextMobject("Object 1"),
        "object_2": Square(),
        "number": 3,
        "vector": [1, 1, 0],
    }

    def construct(self):
        self.play(Write(self.object_1))
        self.play(self.object_1.scale, self.number)
        self.play(ReplacementTransform(self.object_1, self.object_2))
        self.play(self.object_2.shift, self.vector)
        self.wait()


class SceneFromAnotherScene(WhatIsCONFIG):
    CONFIG = {
        "object_1": TextMobject("Another object"),
        "object_2": Circle(),
        "number": 4,
        "vector": [-1, -1, 0],
    }


class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid(axis_color=BLUE)
        dot = Dot([1, 1, 0])
        self.add(screen_grid)
        self.play(FadeIn(dot))
        self.wait()

