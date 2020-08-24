from manimlib.imports import *


class Grafica(GraphScene):
    # Defino las caracteristicas de la grafica y las inicializo en la clase:
    CONFIG = {
        "y_max": 2,
        "y_min": -0.5,
        "x_max": 4,
        "x_min": -4,
        "graph_origin": ORIGIN + 2 * DOWN,
        "axes_color": RED,
        "x_labeled_nums": range(-4, 6, 2),
        "x_axis_width": 12,
        "x_label_decimal": 1,
        "x_label_direction": UP,
        "y_labeled_nums": range(1, 2, 2),
        "y_tick_frequency": 0.5,
        "y_axis_height": 7,
        "y_label_direction": RIGHT,
        "y_label_decimal": 3,
    }

    # Defino la funcion que me permitira proyectar todo en la pantalla:
    def construct(self):
        eq = TextMobject(
            "La integral de Gauss es", tex_to_color_map={"Gauss": RED}
        )  # Primer texto.
        eq2 = TexMobject(
            "\\int_{-\\infty}^\\infty e^{-x^2} dx = \\sqrt{\\pi}"
        )  # Segundo texto.
        eq.next_to(eq2, 1 * UP)  # Acomodo del p.t.
        eq2.next_to(eq, 4 * DOWN)  # Acomodo del s.t.
        eq.scale(2)  # Escala del p.t.
        eq2.scale(2)  # Escala del s.t.

        self.play(DrawBorderThenFill(eq))  # Animacion del p.t.
        self.play(FadeInFromDown(eq2))  # Animacion del s.t.
        self.wait(2)

        #   Segunda seccion:
        eq3 = TextMobject(
            "Y su gráfica se ve así:", tex_to_color_map={"así": BLUE}
        )  #  Tercer texto.
        eq3.to_corner(UL)  # Acomodo del t.t. a la esquina superior izquierda.
        self.play(
            FadeOutAndShiftDown(eq2), Transform(eq, eq3)
        )  # Animacion de desaparicion del s.t. y trasnf. del p.t. al t.t.
        self.setup_axes(animate=True)  # Aparicion de los ejes coordenados.

        #  Grafica:
        graph = self.get_graph(
            lambda x: np.exp(-(x ** 2)), color=BLUE, x_min=-4, x_max=4
        )  # Definicion de la grafica.
        label = self.get_graph_label(
            graph, label="y={e}^{-x^2}", x_val=0.5, direction=2 * RIGHT
        )  # Definicion del texto con la eq. de la grafica.
        self.play(ShowCreation(graph))  # Aparicion de la grafica.
        self.play(ShowCreation(label))  # Aparicion del texto con la func.
        self.wait()

        #   Sumatoria de Riemann:
        sdr = TextMobject(
            "La suma de ",
            "Riemann ",
            "es entonces ",
            "$\\displaystyle\\sum_{i=1}^{n}$",
            "$f({x}_{i})$",
            "$\\Delta x$",
        )
        for i, color in [(1, GREEN), (3, YELLOW), (5, ORANGE)]:
            sdr[i].set_color(color)
        p1 = sdr[0:3].next_to(sdr[3:6], UP).scale(0.8)
        p2 = sdr[3:6].next_to(sdr[0:3], DOWN)
        sdrf = VGroup(p1, p2)
        sdrf.to_corner(UL)
        self.play(Transform(eq, p1))
        self.play(Write(p2))

        #   Adicion de los rectangulos de Riemann:
        kwargs = {  #   Esablezco los argumentos extra que la funcion puede aceptar.
            "x_min": -2,
            "x_max": 2,
            "fill_opacity": 0.75,
            "stroke_width": 0.25,
        }
        # Limites y delta x para los rectangulos.
        # a = -2
        # b = 2
        # n = 4
        # dx = (b - a) / n
        self.rect_list = self.get_riemann_rectangles_list(  #    Regresa una lista con multiples VGroups de R.R.
            graph, 7, start_color=PINK, end_color=GREEN, **kwargs
        )
        plain_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0),
            dx=0.5,
            start_color=invert_color(PINK),
            end_color=invert_color(GREEN),
            **kwargs
        )
        rects = self.rect_list[0]  #  Define el tamaño de los rect.
        self.transform_between_riemann_rects(  # Aparicion del primer VGroup de rect.
            plain_rects, rects, replace_mobject_with_target_in_scene=True, run_time=1
        )

        for i in range(
            1, 7
        ):  # Ciclo for para mantener la transicion de los rect. segun las iteraciones dadas en self.rect_list.
            self.transform_between_riemann_rects(
                self.rect_list[i - 1],
                self.rect_list[i],
                dx=1,
                replace_mobject_with_target_in_scene=True,
                run_time=1,
            )
        self.wait(2)

