from manimlib.imports import *


class ExplicacionTL(Scene):
    def construct(self):
        self.agregar_titulo()
        self.mostrar_funcion()
        self.wait(11)

    def agregar_titulo(self):
        global titulo, titulo_2, brace, funcion
        titulo = TextMobject("Transformación ", "Lineal")
        titulo.to_edge(UP)
        transformacion, lineal = titulo.split()
        lineal_sin_fade = lineal.copy()
        titulo_2 = VGroup(transformacion, lineal_sin_fade)
        brace = Brace(transformacion, DOWN)
        funcion = TextMobject("Función").next_to(brace, DOWN)
        funcion.set_color(ORANGE)

        self.play(Write(titulo, run_time=1))
        self.wait()
        self.play(GrowFromCenter(brace), Write(funcion), ApplyMethod(lineal.fade))

    def mostrar_funcion(self):
        f_de_x = TexMobject("f(x)")
        L_de_v = TexMobject("L(\\vec{\\textbf{v}})")
        numeros = [4, -2, 3]
        input_nums = VGroup(*list(map(TexMobject, list(map(str, numeros)))))
        output_nums = VGroup(*[TexMobject(str(num ** 2)) for num in numeros])

        for mob in input_nums, output_nums:
            mob.arrange_submobjects(DOWN, buff=1)
        input_nums.next_to(f_de_x, LEFT, buff=1)
        output_nums.next_to(f_de_x, RIGHT, buff=1)
        punto_de_f = VectorizedPoint(f_de_x.get_center())

        vect1 = Matrix([5, 2])
        vect1.next_to(L_de_v, LEFT, buff=1)
        vect2 = Matrix([-2, 7])
        vect2.next_to(L_de_v, RIGHT, buff=1)

        vect_de_entrada = TextMobject("Vector de entrada")
        vect_de_entrada.set_color(PURPLE)
        vect_de_entrada.next_to(vect1, DOWN)
        vect_de_salida = TextMobject("Vector de salida")
        vect_de_salida.set_color(BLUE)
        vect_de_salida.next_to(vect2, DOWN)

        self.play(DrawBorderThenFill(f_de_x, run_time=1))
        self.play(Write(input_nums, run_time=2))
        self.wait(0.5)
        for mob in punto_de_f, output_nums:
            self.play(Transform(input_nums, mob, run_time=0.30, rate_fun=running_start))
        self.wait()

        self.play(FadeOut(input_nums), Transform(f_de_x, L_de_v))
        self.play(Write(vect_de_entrada), Write(vect1))
        self.wait(0.5)
        for mob in punto_de_f, vect2:
            self.play(Transform(vect1, mob, run_time=0.5, rate_fun=running_start))
        self.play(Write(vect_de_salida))
        self.wait()

        ec_group1 = VGroup(
            vect_de_entrada, vect_de_salida, f_de_x, vect1, titulo, brace, funcion
        )
        pregunta_1 = TextMobject("Si son lo mismo,", "¿Por qué tienen distinto nombre?")
        pregunta_1_top, pregunta_1_bottom = pregunta_1.split()
        pregunta_1_top.move_to(ORIGIN + 0.5 * UP)
        pregunta_1_bottom.next_to(pregunta_1_top, DOWN)
        for letter in pregunta_1_bottom.submobjects[1:7]:
            letter.set_color(MAROON_C)
        self.play(FadeOut(ec_group1, run_time=0.5), Write(pregunta_1_top, run_time=1))
        self.play(Write(pregunta_1_bottom, run_time=1))
        self.wait(2)
        self.play(Transform(pregunta_1, titulo_2, run_time=1))
        self.wait()

        brace2 = Brace(titulo_2, DOWN)
        movimiento = brace2.get_text("Movimiento")
        movimiento.set_color("#ffa700")
        movimiento.next_to(brace2, DOWN)
        self.play(GrowFromCenter(brace2), Write(movimiento, run_time=1))
        self.wait()


class Movimiento(VectorScene):
    def construct(self):
        grid = self.add_plane(animate=True)
        self.wait()
        t_matrix = [[0, -1], [2, -1]]
        v1_coords = [-2, 2]
        v1 = Vector(v1_coords)
        v1.set_color("#8b8b00")
        v2 = Vector(np.dot(np.array(t_matrix).transpose(), v1_coords), color="#8b008b")
        input_vector = TextMobject("Vector de entrada", run_time=1)
        input_vector.set_color(v1.get_color())
        input_vector.next_to(v1.get_end(), UP)
        output_vector = TextMobject("Vector de salida", run_time=1)
        output_vector.set_color(v2.get_color())
        output_vector.next_to(v2.get_end(), UP)
        self.play(GrowArrow(v1))
        self.play(Write(input_vector))
        self.wait()
        self.play(
            ReplacementTransform(v1.copy(), v2, path_arc=-np.pi / 2, run_time=3),
            ApplyMethod(v1.fade),
        )
        self.play(Write(output_vector))
        self.wait()


class TodosLosVectores(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors": False,
        "kwargs": {
            "tip_length": 0.25,
            "tip_width_to_length_ratio": 1,
            "max_tip_length_to_length_ratio": 0.35,
            "max_stem_width_to_tip_width_ratio": 0.3,
            "propagate_style_to_family": False,
            "preserve_tip_size_when_scaling": True,
            "normal_vector": OUT,
            "use_rectangular_stem": True,
            "rectangular_stem_width": 0.05,
        },
        "use_dots": False,
    }

    def construct(self):
        vectores = VGroup(
            *[
                Vector([x, y], **self.kwargs)
                for x in np.arange(
                    -int(FRAME_X_RADIUS) + 0.5, int(FRAME_X_RADIUS) + 0.5
                )
                for y in np.arange(
                    -int(FRAME_Y_RADIUS) + 0.5, int(FRAME_Y_RADIUS) + 0.5
                )
            ]
        )

        vectores.set_submobject_colors_by_gradient(PINK, BLUE_E, YELLOW)
        t_matrix = [[0, -1], [2, -1]]
        vectores_transformados = VGroup(
            *[
                Vector(
                    np.dot(np.array(t_matrix).transpose(), v.get_end()[:2]),
                    color=v.get_color(),
                )
                for v in vectores.split()
            ]
        )

        self.wait(2)
        self.play(ShowCreation(vectores, run_time=3))
        self.wait()

        if self.use_dots:
            self.play(Transform(vectores, self.vectors_to_dots(vectores), run_time=2))
            vectores_transformados = self.vectors_to_dots(vectores_transformados)
            self.wait()

        self.play(
            Transform(vectores, vectores_transformados, run_time=3, path_arc=-np.pi / 2)
        )
        self.wait(2)

    def vectors_to_dots(self, vectores):
        return VGroup(
            *[Dot(v.get_end(), color=v.get_color()) for v in vectores.split()]
        )


class VectoresAPuntos(TodosLosVectores):
    CONFIG = {"use_dots": True}


class TransfLin(LinearTransformationScene):
    CONFIG = {
        "background_plane_kwargs": {
            "color": GREY,
            "axis_config": {"stroke_color": LIGHT_GREY, "stroke_width": 1,},
        },
        "foreground_plane_kwargs": {"x_radius": FRAME_WIDTH, "y_radius": FRAME_HEIGHT,},
        "show_basis_vectors": False,
        "first_transform": True,
        "dim_red": False,
        "t_matrix": [[2, 1], [1, 2]],
    }

    def construct(self):
        self.add(self.plane, self.background_plane)
        self.wait()

        if self.first_transform:
            i_hat, j_hat = self.get_basis_vectors()
            labels = self.get_basis_vector_labels()
            base_text = TextMobject(
                "Agregamos los vectores base:",
                tex_to_color_map={"vectores base": ORANGE},
            ).to_corner(UL)
            self.play(Write(base_text, run_time=1))
            self.add_vector(i_hat)
            self.add_vector(j_hat)
            self.play(*[Write(label) for label in labels])
            self.wait()
            self.play(*[Uncreate(label) for label in labels], Uncreate(base_text))
            self.wait()

        self.apply_transposed_matrix(self.t_matrix)
        self.wait()

        if self.dim_red:
            txt = TexMobject("det(", "L(\\vec{\\textbf{v}})", ")=0")
            txt[1].set_color(ORANGE)
            txt.to_corner(UL)
            self.play(DrawBorderThenFill(txt, run_time=1))
            self.wait(2)


class OtraTransfLineal(TransfLin):
    CONFIG = {"first_transform": False, "t_matrix": [[-2, 1], [4, 1]]}


class ReduciendoDimension(TransfLin):
    CONFIG = {"first_transform": False, "dim_red": True, "t_matrix": [[2, 1], [4, 2]]}


class FuncionesComplejas(LinearTransformationScene):
    CONFIG = {
        "function": lambda y: 0.5 * y ** 3,
        "show_basis_vectors": False,
        "foreground_plane_kwargs": {
            "x_radius": FRAME_X_RADIUS,
            "y_radius": FRAME_Y_RADIUS,
            "secondary_line_ratio": 0,
        },
    }

    def construct(self):
        self.setup()
        self.plane.prepare_for_nonlinear_transform(100)
        self.wait()
        self.play(
            ApplyMethod(
                self.plane.apply_complex_function,
                self.function,
                run_time=5,
                path_arc=np.pi / 2,
            )
        )
        self.wait()


class LaPalabraLineal(Scene):
    def construct(self):
        self.mostrar_titulo()
        self.condiciones()

    def mostrar_titulo(self):
        titulo = TextMobject("Transformación ", "Lineal")
        titulo.to_edge(UP)
        transformacion, lineal = titulo.split()
        tr_sin_fade = transformacion.copy()
        brace = Brace(lineal, DOWN)
        c_especiales = TextMobject("Condiciones especiales").next_to(brace, DOWN)
        c_especiales.set_color(ORANGE)
        self.play(Write(titulo, run_time=1))
        self.wait()
        self.play(
            GrowFromCenter(brace), Write(c_especiales), ApplyMethod(transformacion.fade)
        )
        self.wait()
        c_especiales.generate_target()
        c_especiales.target.next_to(titulo, DOWN, buff=1)
        self.play(
            MoveToTarget(c_especiales),
            Uncreate(brace),
            Transform(transformacion, tr_sin_fade),
        )
        self.wait()

    def condiciones(self):
        c1 = TextMobject("$\\bullet$ Las lineas deben serguir siendo lineas.")
        c2 = TextMobject(
            "$\\bullet$ Las lineas deben de estar separadas uniformemente."
        )
        c2.next_to(c1, DOWN)
        cond = VGroup(c1, c2)
        cond.move_to(UP)

        self.play(Write(c1))
        self.play(Write(c2))
        self.wait(19)

