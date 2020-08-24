from manimlib.imports import *


class Prueba(Scene):
    def construct(self):
        text = TextMobject("Puto el que lo lea.")
        text.scale(1)

        self.play(Write(text))
        self.wait()


class Ecuaciones(Scene):
    def construct(self):
        eq = TextMobject("La integral de Gauss es", tex_to_color_map={"Gauss": RED})
        # eq2 = TextMobject("$\\int_{-\\infty}^\\infty e^{-x^2} dx = \\sqrt{\\pi}$") -> Si no se utiliza TexMobject, se requieren los signos de dolar.
        eq2 = TexMobject(
            "\\int_{-\\infty}^\\infty e^{-x^2} dx = \\sqrt{\\pi}"
        )  # -> Utilizando TexMobject, para poner texto se utiliza \\text{}.
        eq.next_to(eq2, 1 * UP)
        eq2.next_to(eq, 4 * DOWN)
        eq.scale(2)
        eq2.scale(2)

        self.play(ShowCreation(eq))
        self.play(FadeInFromDown(eq2))
        self.wait(2)

        eq3 = TextMobject("Y su gráfica se ve así:", tex_to_color_map={"así": BLUE})
        eq3.to_corner(UL)
        self.play(FadeOutAndShiftDown(eq2), Transform(eq, eq3))
        # self.play(Transform(eq, eq3))
        # self.play(FadeOut(eq), FadeOut(eq2))
        # self.play()
        self.wait(3)


# class Color(Scene):
#     def construct(self):
#         ej = TextMobject("Esto es un texto", tex_to_color_map={"texto": YELLOW})

#         self.play(Write(ej))
#         self.wait()


class Figuras(Scene):
    def construct(self):
        pointer = CurvedArrow(5 * RIGHT, 2 * RIGHT, angle=-TAU / 4, color=MAROON_C)
        p2 = CurvedArrow(5 * LEFT, 2 * LEFT, color=PINK)

        self.play(ShowCreation(pointer, rate_func=rush_into))
        self.wait()
        self.play(Write(p2))
        self.wait(2)


class Arreglos(Scene):
    def construct(self):
        texto = TextMobject(
            "El teorema de Pitágoras es ", "$c^2$", "=", "$a^2$", "+", "$b^2$"
        )

        # Debido a que el texto es un array, se pueden especificar colores para cada miembro:
        texto[1].set_color(RED)
        texto[2].set_color(ORANGE)
        texto[3].set_color(BLUE)
        texto[4].set_color(YELLOW)
        texto[5].set_color(BLUE)

        # Variables relacionadas al array:
        eq = VGroup(texto[1:6])
        txt = texto[0]
        c2 = texto[1]
        a2 = texto[3]
        b2 = texto[5]

        self.play(Write(texto))
        self.wait()

        # Caracteristicas del triangulo y su posicion:
        tri = Polygon(ORIGIN, 3 * UP, 4 * RIGHT, color=BLUE)
        tri.scale(0.7)
        tri.move_to(eq.get_center())

        # Creacion de una referncia para la posicion de la primer parte del texto y despl. a la izquierda:
        txt.generate_target()
        txt.target.shift(LEFT)

        # Creación de un target para c^2 y despl. a la hipotenusa:
        c2.generate_target()
        c2.target.move_to(tri.get_center() + 0.28 * UP + 0.3 * RIGHT)

        # Creación de un target para a^2 y despl. a un cateto:
        a2.generate_target()
        a2.target.shift(1.75 * LEFT)

        # Creación de un target para b^2 y despl. a un cateto:
        b2.generate_target()
        b2.target.shift(LEFT + 1.38 * DOWN)

        # Creación de la línea roja de la hipotenusa:
        inicio = np.array([4, 0, 0])
        final = np.array([0, 3, 0])
        hip = Line(inicio, final, color="#f30000").scale(0.7)
        hip.move_to(tri.get_center())

        # Recall a las animaciones:
        self.play(
            MoveToTarget(txt),
            MoveToTarget(c2),
            ShowCreation(tri, rate_func=rush_into),
            FadeOutAndShiftDown(texto[2]),
            MoveToTarget(a2),
            MoveToTarget(b2),
            FadeOutAndShift(texto[4], RIGHT),
        )
        self.play(DrawBorderThenFill(hip))
        self.wait(2)

