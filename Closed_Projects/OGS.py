from manimlib.imports import *
from fractions import Fraction


class ProcesoDeGS(VectorScene):
    CONFIG = {
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "stroke_opacity": 0.8,
        },
        "background_line_style": {
            "stroke_width": 2,
            "stroke_opacity": 0.5,
            "stroke_color": RED_D,
        },
        "v1_coords": [1, 2],
        "v2_coords": [-3, 4],
        "w2_coords": [-4, 2],
        "u1_coords": [0.4472, 0.8944],
        "u2_coords": [-0.8944, 0.4472],
    }

    def construct(self):
        plane = NumberPlane(**self.CONFIG)
        self.add(plane)

        kwargs = {
            "stroke_width": 4,
        }

        v1 = Vector(self.v1_coords, **kwargs).set_color(RED)
        v1_label = Matrix([1, 2]).next_to(v1.get_end(), RIGHT).scale(0.7)
        v2 = Vector(self.v2_coords, **kwargs).set_color(RED)
        v2_label = Matrix([-3, 4]).next_to(v2.get_end(), DOWN + 0.7 * LEFT).scale(0.7)
        for i, color in [(0, RED), (1, RED)]:
            v1_label[0][i].set_color(color)
            v2_label[0][i].set_color(color)
        for anim, vector, label in [
            (GrowArrow, v1, v1_label),
            (GrowArrow, v2, v2_label),
        ]:
            self.play(anim(vector, run_time=0.8))
            self.play(Write(label))
        self.wait()

        txt = TextMobject(
            "Ortogonalizando los vectores:",
            tex_to_color_map={"Ortogonalizando": "#a3f7a1"},
        ).scale(0.8)
        txt.to_corner(UR)
        w2 = Vector(self.w2_coords, **kwargs).set_color("#a3f7a1")
        w2_label = Matrix([-4, 2]).next_to(w2, LEFT).scale(0.7)
        for i in range(0, 2):
            w2_label[0][i].set_color("#a3f7a1")
        self.play(
            DrawBorderThenFill(txt),
            FadeToColor(v1, "#a3f7a1"),
            FadeToColor(v1_label[0][0:2], "#a3f7a1"),
            ReplacementTransform(v2, w2),
            ReplacementTransform(v2_label, w2_label),
        )
        self.wait()

        mkwargs = {"v_buff": 1.5}
        txt2 = TextMobject(
            "Ortonormalizando los vectores:",
            tex_to_color_map={"Ortonormalizando": "#a1a3f7"},
        ).scale(0.8)
        txt2.to_corner(UR)
        # u1_fe = TexMobject("\\frac{1}{\\sqrt{5}")
        # u2_fe = TexMobject("\\frac{2}{\\sqrt{5}")
        u1 = Vector(self.u1_coords, **kwargs).set_color("#a1a3f7")
        u1_label = (
            Matrix(["\\frac{1}{\\sqrt{5}", "\\frac{2}{\\sqrt{5}"], **mkwargs)
            .next_to(u1.get_end(), 0.5 * RIGHT)
            .scale(0.6)
        )
        u2 = Vector(self.u2_coords, **kwargs).set_color("#a1a3f7")
        u2_label = (
            Matrix(["\\frac{-2}{\\sqrt{5}", "\\frac{1}{\\sqrt{5}"], **mkwargs)
            .next_to(u2.get_end(), 0.1 * UP)
            .scale(0.6)
        )
        for i, color in [(0, "#a1a3f7"), (1, "#a1a3f7")]:
            u1_label[0][i].set_color(color)
            u2_label[0][i].set_color(color)
        self.play(
            ReplacementTransform(txt, txt2),
            ReplacementTransform(v1, u1),
            ReplacementTransform(v1_label, u1_label),
            ReplacementTransform(w2, u2),
            ReplacementTransform(w2_label, u2_label),
        )
        self.wait()
