from manimlib.imports import *


class VectoresComoEscalares(VectorScene):
    CONFIG = {
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "stroke_opacity": 0.8,
        },
        "background_line_style": {"stroke_width": 2, "stroke_opacity": 0.5,},
        "vcoords": ([3, 2]),
        "vcolor": ORANGE,
        "vcoords1": ([1, 0]),
        "vcoords1_2": ([3, 0]),
        "vcoords2": ([0, 1]),
        "vcoords2_2": ([0, 2]),
        "vcolor1": X_COLOR,
    }

    def construct(self):
        grid = NumberPlane(**self.CONFIG)
        self.add(grid)
        self.lock_in_faded_grid()
        self.play(ShowCreation(grid), run_time=2)
        self.wait()

        kwargs = {
            "stroke_width": 4,
        }

        vector = Vector(self.vcoords, **kwargs).set_color(ORANGE)
        vector_2 = vector.copy()
        self.play(
            ShowCreation(vector)
        )  # self.add_vector(self.vcoords, self.vcolor, **kwargs)
        array, x_line, y_line = self.vector_to_coords(vector)
        self.add(array)
        self.wait(2)

        txt = TextMobject(
            "Piensen en cada coordenada como un escalar",
            tex_to_color_map={"coordenada": "#a2cadf", "escalar": "#dfb7a2"},
        )

        txt.to_edge(UP)
        m = Matrix([3, 2]).move_to(array.get_center()).scale(0.8)
        m2 = m.copy()
        m2[0][0].set_color(X_COLOR)
        m2[0][1].set_color(Y_COLOR)
        self.add(m)
        x_scalar = TexMobject("3").move_to(2.5 * LEFT + 2 * UP).set_color(X_COLOR)
        xs_copy = x_scalar.copy()
        y_scalar = TexMobject("2").move_to(2.5 * RIGHT + 2 * UP).set_color(Y_COLOR)
        ys_copy = y_scalar.copy()
        self.play(
            Uncreate(vector),
            FadeOut(array, run_time=0.1),
            ReplacementTransform(m[0][0], x_scalar),
            ReplacementTransform(m[0][1], y_scalar),
            FadeOut(VGroup(m[1], m[2])),
            DrawBorderThenFill(txt),
        )
        self.wait(0.5)

        new_vector1 = (
            Vector(self.vcoords1, **kwargs).set_color(X_COLOR).move_to(3.5 * LEFT)
        )
        new_vector1_2 = (
            Vector(self.vcoords1_2, **kwargs)
            .set_color(X_COLOR)
            .move_to(new_vector1.get_center() + RIGHT)
        )
        new_vector2 = (
            Vector(self.vcoords2, **kwargs)
            .set_color(Y_COLOR)
            .move_to(3.5 * RIGHT + 0.5 * UP)
        )
        new_vector2_2 = (
            Vector(self.vcoords2_2, **kwargs)
            .set_color(Y_COLOR)
            .move_to(new_vector2.get_center() + 0.5 * UP)
        )
        self.play(ShowCreation(new_vector1), ShowCreation(new_vector2))
        self.wait()
        self.play(
            ReplacementTransform(new_vector1, new_vector1_2),
            ReplacementTransform(new_vector2, new_vector2_2),
        )
        self.wait()
        self.play(
            FadeOut(txt),
            Uncreate(new_vector1_2),
            Uncreate(new_vector2_2),
            ShowCreation(vector_2),
            ReplacementTransform(x_scalar, m2[0][0]),
            ReplacementTransform(y_scalar, m2[0][1]),
            FadeIn(VGroup(m2[1], m2[2])),
        )
        self.wait()

        kwargs1 = {
            "direction": "right",
        }
        kwargs2 = {
            "direction": "left",
        }

        i_hat, j_hat = self.get_basis_vectors()
        self.add_vector(i_hat)
        i_hat_lab = self.label_vector(
            i_hat, "\\hat{\\imath}", color=X_COLOR, label_scale_factor=1, **kwargs1
        )
        self.add_vector(j_hat)
        j_hat_lab = self.label_vector(
            j_hat, "\\hat{\\jmath}", color=Y_COLOR, label_scale_factor=1, **kwargs2
        )
        self.wait()

        faded_i = i_hat.copy().fade(0.7)
        scaled_i = Vector([3, 0], color=i_hat.get_color(), **kwargs)
        m3 = m2[0][0]
        i_hat_lab.generate_target()
        scaled_i_lab = i_hat_lab.target.shift(1.25 * RIGHT)
        escalar_i_hat = xs_copy.next_to(scaled_i_lab, LEFT, buff=0.1)
        # scaled_i_lab.generate_target()
        self.play(
            Transform(i_hat.copy(), faded_i),
            Transform(i_hat, scaled_i),
            MoveToTarget(i_hat_lab),
            Transform(m3, escalar_i_hat),
        )
        self.wait()

        faded_j = j_hat.copy().fade(0.7)
        scaled_j = Vector([0, 2], color=j_hat.get_color(), **kwargs)
        m4 = m2[0][1]
        j_hat_lab.generate_target()
        sc = j_hat_lab.target.shift(0.5 * UP)
        escalar_j_hat = ys_copy.next_to(sc, LEFT, buff=0.1)
        # scaled_i_lab.generate_target()
        self.play(
            ReplacementTransform(j_hat.copy(), faded_j),
            ReplacementTransform(j_hat, scaled_j),
            MoveToTarget(j_hat_lab),
            ReplacementTransform(m4, escalar_j_hat),
            FadeOut(VGroup(m2[1], m2[2])),
        )
        self.wait()

        complete_j_vector = VGroup(scaled_j, j_hat_lab, escalar_j_hat, sc)
        complete_j_vector.generate_target()
        complete_j_vector.target.shift(3 * RIGHT)
        self.play(MoveToTarget(complete_j_vector))
        self.wait()

        txt2 = TextMobject(
            "El vector dado puede expresarse como", tex_to_color_map={"vector": ORANGE},
        )
        eq = TexMobject("3\\hat{\\imath}", "+", "2\\hat{\\jmath}").scale(1.2)
        for element, color in [(0, X_COLOR), (2, Y_COLOR)]:
            eq[element].set_color(color)

        eq.next_to(txt2, DOWN)
        self.play(Write(VGroup(txt2, eq).to_corner(UL)))
        self.wait()


class CombinacionLineal(VectorScene):
    CONFIG = {
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "stroke_opacity": 0.8,
            "unit_size": 0.6,
        },
        "y_axis_config": {"label_direction": UP},
        "background_line_style": {"stroke_width": 2, "stroke_opacity": 0.5,},
        "x_min": -20,
        "x_max": 20,
        "y_min": -10,
        "y_max": 10,
        "v1color": BLUE,
        "v2_3_color": RED,
        "kwargs_v1": {"stroke_width": 4},
    }

    def construct(self):
        grid = NumberPlane(**self.CONFIG)
        self.add(grid)
        self.wait()

        v1 = self.add_vector(grid.c2p(11, 1), self.v1color, **self.kwargs_v1)
        v1_label = Matrix([11, 1]).move_to(v1.get_end() - 0.5 * RIGHT + UP).scale(0.7)
        for element in [0, 1]:
            v1_label[0][element].set_color(self.v1color)
        self.play(Write(v1_label))
        self.wait()

        v2 = Vector(grid.c2p(2, 4), **self.kwargs_v1,).set_color(RED)
        v2_label = Matrix([2, 4]).next_to(v2.get_end()).scale(0.7)
        for element in [0, 1]:
            v2_label[0][element].set_color(self.v2_3_color)
        v3 = Vector(grid.c2p(9, -3), **self.kwargs_v1,).set_color(RED)
        v3_label = Matrix([9, -3]).next_to(v3.get_end()).scale(0.7)
        for element in [0, 1]:
            v3_label[0][element].set_color(self.v2_3_color)
        self.play(GrowArrow(v2), Write(v2_label))
        self.play(GrowArrow(v3), Write(v3_label))
        self.wait(2)

        txt = TextMobject(
            "Según nuestros cálculos,", tex_to_color_map={"cálculos": RED}
        )
        eq = TexMobject("C_1 ", "= ", "1", "\\text{ y }", " C_2 ", "= ", "1").scale(0.8)
        for element, color in [(0, GREEN), (4, GREEN)]:
            eq[element].set_color(color)
        eq.next_to(txt, DOWN)
        VGroup(txt, eq).to_corner(UL)
        self.play(DrawBorderThenFill(txt))
        self.play(DrawBorderThenFill(eq))
        self.wait()

        txt2 = TextMobject(
            "Sust. en la def. de combinación lineal:",
            tex_to_color_map={"combinación lineal": "#b7a2df"},
        ).scale(0.7)
        txt2.next_to(eq, DOWN)
        self.play(Write(txt2))
        self.wait(0.5)

        eq_c_l = TexMobject("{C_1}", "{V_1}", "+", "{C_2}", "{V_2}", "=", "V").scale(
            0.8
        )
        for i, color in [(0, GREEN), (1, RED), (3, GREEN), (4, RED), (6, BLUE)]:
            eq_c_l[i].set_color(color)
        eq_c_l.next_to(txt2, 2.5 * DOWN)
        self.play(Write(eq_c_l))
        self.wait(0.5)
        # Se puede reducir con una lista de variables:
        eq[2].generate_target()
        eq[2].target.move_to(eq_c_l[0].get_center() + 0.50 * LEFT)
        eq[6].generate_target()
        eq[6].target.move_to(eq_c_l[3].get_center())
        v2_label.generate_target()
        v2_label.target.move_to(eq_c_l[1].get_center() + 0.25 * LEFT)
        v3_label.generate_target()
        v3_label.target.move_to(eq_c_l[4].get_center() + 0.30 * RIGHT)
        eq_c_l[5].generate_target()
        eq_c_l[5].target.shift(0.6 * RIGHT)
        v1_label.generate_target()
        v1_label.target.move_to(eq_c_l[6].get_center() + 0.9 * RIGHT)
        # Tambien se puede reducir con una lista de variables:
        self.play(
            FadeOut(eq[0:2]),
            FadeOut(eq[3:6]),
            FadeOut(eq_c_l[0]),
            MoveToTarget(eq[2]),
            FadeOut(eq_c_l[3]),
            MoveToTarget(eq[6]),
            FadeOut(eq_c_l[1]),
            MoveToTarget(v2_label),
            FadeOut(eq_c_l[4]),
            MoveToTarget(v3_label),
            MoveToTarget(eq_c_l[5]),
            FadeOutAndShift(eq_c_l[6], RIGHT),
            MoveToTarget(v1_label),
        )
        self.wait(0.5)
        cls1 = VGroup(
            eq[2], eq[6], v2_label, v3_label, eq_c_l[2], eq_c_l[5], v1_label, txt2
        )
        cls1.generate_target()
        cls1.target.shift(1.5 * UP)
        self.play(MoveToTarget(cls1), FadeOutAndShift(txt, UP))
        self.wait(0.5)

        txt3 = TextMobject(
            "Simplificando las operaciones:", tex_to_color_map={"operaciones": YELLOW}
        ).scale(0.7)
        txt3.move_to(txt2.get_center() + 1.9 * DOWN + 0.6 * LEFT)
        mfl = Matrix([11, 1]).move_to(v2_label.get_center() + 1.9 * DOWN).scale(0.7)
        for i, color in [(0, RED), (1, RED)]:
            mfl[0][i].set_color(color)
        equal = TextMobject("=").next_to(mfl, RIGHT)
        mfr = Matrix([11, 1]).next_to(equal, RIGHT).scale(0.7)
        for i, color in [(0, BLUE), (1, BLUE)]:
            mfr[0][i].set_color(color)
        self.play(ReplacementTransform(txt2.copy(), txt3))
        self.wait(0.5)
        self.play(Write(mfl), Write(equal), Write(mfr))
        self.wait()
        self.play(ApplyMethod(v3.shift, v2.get_end()))
        self.wait()

