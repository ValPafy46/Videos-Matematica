from manim import *
import numpy as np

class EquaçõesSegundoGrau(Scene):
    def construct(self):

        # Animação Introdutória

        background = Tex(
            r"$2x^{2}+3x-4=0$",
            color=WHITE,
            font_size=90,
            fill_opacity=0.3
        )
        background.move_to(UP * 2.5)

        background1 = Tex(
            r"$-x^{2}+4x+1=0$",
            color=WHITE,
            font_size=90,
            fill_opacity=0.3 
        )
        background1.move_to(DOWN * 2.5)

        main_title = Tex(
            "Equações de 2º Grau",
            color=WHITE,
            font_size=130
        )

        sub_title = Tex(
            "Estrutura",
            color=BLUE,
            font_size=70
        )
        sub_title.move_to(main_title.get_bottom()+DOWN*0.7)

        introax = Axes(
            x_range=[-10, 10],
            y_range=[-7,7]
        )
        introfunc = introax.plot(
            lambda x: 0.5*np.sin(x)+0.4*np.sin(0.5*x+1),
            color=GREEN,
            stroke_width=8,
        )

        self.play(Create(introfunc), run_time=3)
        self.play(Write(main_title), Create(sub_title))
        self.wait(1)
        self.play(Write(background), Write(background1), run_time=2.5)
        self.wait(2)
        self.play(FadeOut(introfunc, main_title, background1, background, sub_title))
        self.wait(1)

        # Animação Coeficientes


        # Lista de coeficientes para a equação
        coefficients = [
            (3, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (2, 4, 6),
            (4, 3, 8),
            (2, 5, 1)
        ]
        
        # Função para criar o texto da equação
        def get_equation_text(a, b, c, size, Color):
            if a and b and c:
                return MathTex(f"{a}x^2 + {b}x + {c} = 0", font_size=size, color=Color)
            elif b == 0 and c == 0:
                return MathTex(f"{a}x^2 = 0", font_size=size, color=Color)
            elif b == 0:
                return MathTex(f"{a}x^2 + {c} = 0", font_size=size, color=Color)
            elif c == 0:
                return MathTex(f"{a}x^2 + {b}x = 0", font_size=size, color=Color)

        
        # Cria a equação inicial e adiciona na cena
        a, b, c = coefficients[0]
        equation = get_equation_text(a, b, c, 100, GREEN)
        equation.move_to(ORIGIN)
        self.play(Create(equation))

        # Atualiza a equação a cada 1.5 segundos
        for coef in coefficients:
            a, b, c = coef
            new_equation = get_equation_text(a, b, c, 100, GREEN)
            self.play(Transform(equation, new_equation), run_time=1.5)
            self.wait(1)
        
        # Espera um pouco no final
        self.wait(1)
        self.remove(equation)

        # EXPLICAÇÃO CONSTITUIÇÃO
        eq1 = Tex(
            r"$2x^{2}+5x+1=0$",
            font_size=100,
            color=GREEN
        )
        eq_cano = Tex(
            r"$ax^{2}+bx+c=0$",
            color=BLUE,
            font_size= 110
        )
        eq_cano.move_to(DOWN*0.7)

        self.add(eq1)
        self.play(eq1.animate.move_to(UP*2.5), run_time=2)
        self.wait(1)

        text = Text("Todas as Equações de 2º Grau Seguem:", font_size=50)
        text.move_to(UP*0.5)
        self.wait(0.5)

        note1 = Tex(
            r"$a\neq 0$",
            color= WHITE,
            font_size = 80
        )
        note1.move_to(eq_cano.get_bottom() + DOWN*0.8)

        self.play(Write(text))
        self.wait(0.5)
        self.play(Write(eq_cano), eq1.animate.set_opacity(0.3))
        self.play(Indicate(eq_cano))

        self.wait(2)
        self.play(Write(note1))
        self.play(Circumscribe(note1))
        self.wait(1.5)
        self.play(FadeOut(note1, text))

        text1 = Tex(
            r"$a=2, b=5,c=1$",
            font_size = 80
        )


        self.play(eq1.animate.set_opacity(1), eq_cano.animate.move_to(eq1.get_bottom()+DOWN))
        text1.move_to(eq_cano.get_bottom()+DOWN*3)
        self.play(Write(text1), eq_cano.animate.set_opacity(0.3))
        self.play(Circumscribe(text1))
        self.wait(2.5)
        self.play(FadeOut(text1), eq_cano.animate.set_opacity(1))
        self.wait(0.5)

        self.play(eq_cano.animate.move_to(ORIGIN), eq1.animate.set_opacity(0.3))

        text2 = Text(
            "Forma Canónica",
            font_size=60
        )
        text2.to_corner(DOWN, buff=0.5)

        seta1 = Arrow(
            start = text2.get_top(),
            end = eq_cano.get_bottom(),
            buff = 0.1,
            color = WHITE
        )

        self.play(Write(text2))
        self.play(Create(seta1), Circumscribe(eq_cano), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(seta1, text2, eq_cano, eq1))


        # TIPOS DE EQUAÇÃO DE 2º GRAU

        title = Tex(
            "Tipos de Equação de 2º Grau",
            font_size=70
        )
        text_completa = Tex(
            "Equação Completa",
            color=BLUE,
            font_size=65
        )
        text_completa.move_to(title.get_bottom()+DOWN*0.8)

        text_completa_descr = Tex(
            "Todas as letras não são 0",
            font_size=55,
            color=GREEN
        )


        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_corner(UP, buff=1))

        # Equação Completa

        text_completa.move_to(title.get_bottom()+DOWN*0.8)
        text_completa_descr.move_to(text_completa.get_bottom()+DOWN*0.5)

        self.wait(1.5)

        self.play(Write(text_completa))
        self.wait(0.5)
        self.play(Write(text_completa_descr))
        
        eq1 = get_equation_text(-2, 4, 2, 70, YELLOW).move_to(ORIGIN+DOWN*0.5) # Diferença de 1
        eq2 = get_equation_text(3, 5, 4, 70, YELLOW).move_to(ORIGIN+DOWN*1.5)
        eq3 = get_equation_text(6, 2, 3, 70, YELLOW).move_to(ORIGIN+DOWN*2.5)

        self.wait(2)
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))

        self.wait(5)

        # Equação Incompleta

        text_incompleta = Tex(
            "Equação Incompleta",
            color=BLUE,
            font_size=65
        )
        text_incompleta.move_to(title.get_bottom()+DOWN*0.8)

        text_incompleta_descr = Tex(
            "b, c ou ambos são 0",
            font_size=55,
            color=GREEN
        )

        text_incompleta_descr.move_to(text_incompleta.get_bottom()+DOWN*0.5)
        self.play(FadeOut(eq1, eq2, eq3))
        self.play(ReplacementTransform(text_completa,text_incompleta),
                  ReplacementTransform(text_completa_descr, text_incompleta_descr))

        eq1 = get_equation_text(2, 4, 0, 70, YELLOW).move_to(ORIGIN+DOWN*0.5) # Diferença de 1
        eq2 = get_equation_text(-3, 0, 2, 70, YELLOW).move_to(ORIGIN+DOWN*1.5)
        eq3 = get_equation_text(2, 0, 0, 70, YELLOW).move_to(ORIGIN+DOWN*2.5)

        self.wait(2)
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))

        self.wait(5)
        self.play(FadeOut(title, text_incompleta, text_incompleta_descr, eq1, eq2, eq3))


        # FIM
        self.wait(2)
        text_final = Tex(
            "Nos Próximos Vídeos...",
            color=BLUE,
            font_size=100
        )

        self.play(Write(text_final))
        self.play(ApplyWave(text_final))

        self.wait(3)
        self.play(Unwrite(text_final))
