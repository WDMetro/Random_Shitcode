from manimlib.imports import *


class TransformacionLineal(LinearTransformationScene):
    CONFIG = {
        "foreground_plane_kwargs": {
            "x_radius": FRAME_WIDTH,
            "y_radius": FRAME_HEIGHT,
            "background_line_style": {
                "stroke_width": 2,
                "stroke_opacity": 0.5,
                "stroke_color": RED_D,
            },
        },
        "show_basis_vectors": False,
    }

    def construct(self):
        self.setup()
        self.play(
            ShowCreation(self.plane, run_time=2),
            ShowCreation(self.background_plane, run_time=2),
        )
        self.wait(0.5)

        txt1 = (
            TextMobject("Los ", "eigenvectores ", "de la ", "transformación")
            .scale(0.8)
            .to_corner(UR, buff=0.2)
        )
        for word, color in [(1, "#d8e64c"), (3, "#4cd8e6")]:
            txt1[word].set_color(color)

        transf = Matrix([[3, 1], [0, 2]]).next_to(txt1.get_center(), DOWN).scale(0.9)
        for i, j in [(0, 0), (0, 2)]:
            transf[i][j].set_color(X_COLOR)
        for i, j in [(0, 1), (0, 3)]:
            transf[i][j].set_color(Y_COLOR)
        self.play(Write(txt1, run_time=1))
        self.play(DrawBorderThenFill(transf, run_time=1))
        self.wait(0.5)

        v1kwa = {"stroke_width": 4, "tip_length": 0.30}

        linev1 = Line((4, -4, 0), (-4, 4, 0)).set_color("#e64cd8")
        v1 = self.add_vector([-1, 1], "#e6a74c", **v1kwa)
        self.add_foreground_mobjects(v1)
        v1_label = Matrix([-1, 1]).next_to(v1.get_end(), LEFT).scale(0.7)
        for i in range(0, 2):
            v1_label[0][i].set_color("#e6a74c")
        self.play(Write(v1_label))
        linev2 = Line((-8, 0, 0), (8, 0, 0)).set_color("#e64cd8")
        v2 = self.add_vector([1, 0], "#4cd8e6", **v1kwa)
        self.add_foreground_mobjects(v2)
        v2_label = Matrix([1, 0]).next_to(v2.get_end(), UP).scale(0.7)
        for i in range(0, 2):
            v2_label[0][i].set_color("#4cd8e6")
        self.play(Write(v2_label))
        txt2 = TextMobject("Coordenadas iniciales:")
        txt2.to_corner(DL)
        linev3 = Line((-2, 4, 0), (2, -4, 0)).set_color("#e64cd8")
        v3 = self.add_vector([1, -2], YELLOW, **v1kwa)
        self.add_foreground_mobjects(v3)
        text_vect_arbit = (
            TextMobject("$\\vec{v}$ = Vector arbitrario")
            .set_color(YELLOW)
            .move_to(v3.get_end() + 2 * RIGHT)
            .scale(0.8)
        )
        self.play(Write(text_vect_arbit))
        self.wait(2)

        sub_gen = (
            TextMobject("Subespacio generado")
            .scale(0.8)
            .set_color("#e64cd8")
            .move_to(ORIGIN + 4 * RIGHT + 0.5 * DOWN)
        )

        self.play(
            ShowCreation(linev1),
            ShowCreation(linev2),
            ShowCreation(linev3),
            Write(txt2),
            Write(sub_gen),
            ApplyMethod(v1_label.move_to, txt2.get_center() + UP + 0.5 * LEFT),
            ApplyMethod(v2_label.move_to, txt2.get_center() + UP + 0.5 * RIGHT),
            FadeOut(text_vect_arbit),
        )
        self.wait()

        txt_ap = TextMobject("Aplicando la ", "transformación", ":").to_corner(UR)
        txt_ap[1].set_color("#4cd8e6")
        self.play(ReplacementTransform(txt1, txt_ap), FadeOut(transf), FadeOut(sub_gen))
        self.wait(0.1)
        self.apply_transposed_matrix([[3, 0], [1, 2]])
        self.wait()

        v1f_label = Matrix([-2, 2]).next_to(v1.get_end(), LEFT).scale(0.7)
        for i in range(0, 2):
            v1f_label[0][i].set_color("#e6a74c")
        v2f_label = Matrix([3, 0]).next_to(v2.get_end(), UP).scale(0.7)
        for i in range(0, 2):
            v2f_label[0][i].set_color("#4cd8e6")
        self.play(Write(v1f_label), Write(v2f_label))
        self.wait()

        txt3 = TextMobject("Coordenadas finales:")
        txt3.to_corner(DR)

        self.play(
            Write(txt3),
            ApplyMethod(v1f_label.move_to, txt3.get_center() + UP + 0.5 * LEFT),
            ApplyMethod(v2f_label.move_to, txt3.get_center() + UP + 0.5 * RIGHT),
        )
        self.wait(0.5)

        braces1 = Brace(v1, LEFT)
        eq_text1 = braces1.get_text("2")
        eq_text1.set_color("#e6a74c")
        braces2 = Brace(v2, DOWN)
        eq_text2 = braces2.get_text("3")
        eq_text2.set_color("#4cd8e6")
        evtext = TextMobject(
            "Y los eigenvalores son:", tex_to_color_map={"eigenvalores": "#d8e64c"}
        ).to_corner(UR)
        self.play(
            ReplacementTransform(txt_ap, evtext),
            GrowFromCenter(braces1),
            Write(eq_text1),
            GrowFromCenter(braces2),
            Write(eq_text2),
        )
        self.wait(2)

