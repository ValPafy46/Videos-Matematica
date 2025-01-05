from manim import *
import numpy as np


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
    

    

class EquaçãoSegundoGrauResolução(Scene):

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
            "Resolução das Incompletas",
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


        # ANIMAÇÃO DE RESOLUÇÃO DE EQUAÇÃO COMPLETA

        eq1 = MathTex(
            r"6x^{2}+3x-9=0", color=GREEN, font_size=70
        )
        eq2 = MathTex(
            r"6x^{2}+3x=9", color=GREEN, font_size=70
        )
        eq3 = MathTex(
            r"x^{2}+\frac{3}{6}x=\frac{9}{6}", color=GREEN, font_size=70
        )
        eq4 = MathTex(
            r"x^{2}+\frac{1}{2}x=\frac{3}{2}", color=GREEN, font_size=70
        )
        eq5 = MathTex(
            r"x^{2}+\frac{1}{2}x+\left( \frac{1}{4} \right)^{2}=\frac{3}{2}+\left( \frac{1}{4} \right)^{2}", color=GREEN, font_size=70
        )
        eq6 = MathTex(
            r"\left( x+\frac{1}{4} \right)^{2}=\frac{25}{16}", color=GREEN, font_size=70
        )
        eq7 = MathTex(
            r"x+\frac{1}{4}=\pm \sqrt{\frac{25}{16}}", color=GREEN, font_size=70
        )
        eq8 = MathTex(
            r"x+\frac{1}{4}=\pm \frac{\sqrt{25}}{\sqrt{16}}", color=GREEN, font_size=70
        )
        eq9 = MathTex(
            r"x+\frac{1}{4}=\pm \frac{5}{4}", color=GREEN, font_size=70
        )
        eq10 = MathTex(
            r"x=-\frac{6}{4}\vee x=\frac{4}{4}", color=GREEN, font_size=70
        )
        eq11 = MathTex(
            r"x=-\frac{3}{2}\vee x=1", color=GREEN, font_size=70
        )
        eq12 = MathTex(
            r"S=\left\{ -\frac{3}{2} ,1\right\}", color=GREEN, font_size=70
        )


        ############
        equations = [eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12]

        # Posição inicial da primeira equação
        equations[0].move_to(ORIGIN)
        self.play(Write(equations[0]))
        self.wait(1)

        # Transformar de uma equação para a próxima
        for i in range(len(equations) - 1):
            self.play(ReplacementTransform(equations[i], equations[i + 1]))
            self.wait(2.5)

        # Deixar a última equação visível no final
        self.play(FadeOut(equations[-1]))
        self.wait(1)
        ############


        # EXPLICAÇÃO DAS SOLUÇÕES

        title1 = Text(
            "Solução de Uma Equação",
            font_size=65
        )
        descr1 = Text(
            "Qualquer valor que torna-a real",
            font_size = 40, color=GREEN
        )
        eq1 = MathTex(
            r"2",r"x^{2}",r"+2",r"x",r"-4=0",
            font_size=100, color=BLUE
        )
        eq1.move_to(DOWN*0.5)


        self.play(Write(title1))
        self.wait(1)
        self.play(title1.animate.to_corner(UP, buff=1))
        descr1.move_to(title1.get_bottom()+DOWN*0.7)
        self.play(Write(descr1))
        self.wait(1)
        self.play(Write(eq1))
        self.wait(1)

        # Substituição

        current_x = ValueTracker(1)
        x_value = always_redraw(lambda: MathTex(
            rf"x={current_x.get_value():.2f}", font_size=90
        ))
        always_redraw(lambda: x_value.to_corner(DOWN, buff= 0.3))
        
        self.play(Indicate(eq1[1]), Indicate(eq1[3]), run_time=1.5)
        self.wait(0.5)
        self.play(Write(x_value))
        self.wait(0.5)

        # Equações da Substituição

        eq1_sub = always_redraw(lambda: MathTex(
            rf"2\times {current_x.get_value():.2f}^{2} + "
            rf"2\times {current_x.get_value():.2f} - 4=0"
            if current_x.get_value() not in [0, 1] 
            else rf"2\times {int(current_x.get_value())}^{2} + 2\times {int(current_x.get_value())} - 4=0",
            font_size=90, color=BLUE
        ).move_to(DOWN * 0.5))


        self.play(ReplacementTransform(eq1, eq1_sub))
        self.wait(1)

        result_text = MathTex(
            r"\Leftrightarrow 0=0",
            font_size=90, color=YELLOW
        ).move_to(eq1_sub.get_bottom()+DOWN*0.8)

        self.play(Write(result_text))
        self.play(Circumscribe(result_text, color=BLUE))
        self.wait(1.5)
        self.play(Unwrite(result_text))
        self.wait(2)

        self.play(current_x.animate.set_value(0), run_time=2)
        self.wait(1)

        result_text = MathTex(
            r"\Leftrightarrow -4=0",
            font_size=90, color=YELLOW
        ).move_to(eq1_sub.get_bottom()+DOWN*0.8)
        
        cross = Cross(result_text, stroke_width=9)

        self.play(Write(result_text))
        self.wait(1)
        self.play(Create(cross))
        self.wait(1)
        self.play(FadeOut(result_text, cross, title1, descr1, eq1_sub, x_value))
        self.wait(1)

        eq1 = MathTex(
            r"2x^{2}+2x-4=0",
            font_size=100, color=BLUE
        )
        result = MathTex(
            r"S=\left\{ 1,-2 \right\}",
            font_size=100, color=YELLOW
        ).move_to(DOWN)

        self.play(Write(eq1))
        self.wait(1)
        self.play(eq1.animate.move_to(UP))
        self.wait(1)
        self.play(Write(result), run_time=2)
        self.play(Circumscribe(result))
        self.wait(2)
        self.play(Unwrite(eq1), Unwrite(result))

        # EXPLICAÇÃO DA RESOLUÇÃO

        self.wait(2)

        title = Text(
            "Métodos de Resolução",
            font_size=60)

        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.to_corner(UP, buff=0.8))

        form1 = MathTex(
            r"ax^{2}=0",
            font_size=100, tex_to_color_map={'a':YELLOW}
        )
        result = MathTex(
            r"S=\left\{ 0 \right\}",
            font_size=120, color=WHITE
        ).move_to(DOWN*2)

        self.wait(1)
        self.play(Write(form1))
        self.wait(1)
        self.play(Write(result))
        self.play(Circumscribe(result, color=BLUE))
        self.wait(2)
        self.play(FadeOut(result))
        self.wait(0.5)

        # Animação da prova

        ###########
        eq1 = MathTex(
            r"x^{2} = \frac{0}{", r"a", r"}",                  
            font_size=100
        )
        eq1[1].set_color(YELLOW)

        eq2 = MathTex(
            r"x^{2}=0", font_size=100
        )
        eq3 = MathTex(
            r"x=\pm \sqrt{0}", font_size=100
        )
        eq4 = MathTex(
            r"x=0", font_size=100
        )
        equations = [form1, eq1, eq2, eq3, eq4]

        # Transformar de uma equação para a próxima
        for i in range(len(equations) - 1):
            self.play(ReplacementTransform(equations[i], equations[i + 1]))
            self.wait(2.5)

        # Deixar a última equação visível no final
        self.play(Indicate(equations[-1]))
        self.play(FadeOut(equations[-1]))
        self.wait(1)
        ############


        form = MathTex(
            r"ax^{2}+c=0",
            font_size=100, tex_to_color_map={'a':YELLOW, 'c':BLUE}
        )

        self.play(Write(form))
        self.wait(1)
        self.play(FadeOut(form))
        self.wait(0.5)

        eq1 = MathTex(
            r"2x^{2}-8=0",                  
            font_size=100
        )
        eq2 = MathTex(
            r"2x^{2}=8",                  
            font_size=100
        )
        eq3 = MathTex(
            r"x^{2}=\frac{8}{2}",
            font_size=100
        )
        eq4 = MathTex(
            r"x^{2}=4",
            font_size=100
        )
        eq5 = MathTex(
            r"x=\pm \sqrt{4}",
            font_size=100
        )
        eq6 = Tex(
            r"$x=2$ ou $x=-2$",
            font_size=100
        )
        eq7 = MathTex(
            r"x=2\vee x=-2",
            font_size=100
        )
        eq8 = MathTex(
            r"S=\left\{ 2,-2 \right\}",
            font_size=100
        )

        equations = [eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8]
        self.play(Write(equations[0]))
        self.wait(2)

        # Transformar de uma equação para a próxima
        for i in range(len(equations) - 1):
            self.play(ReplacementTransform(equations[i], equations[i + 1]))
            self.wait(2)

        # Deixar a última equação visível no final
        self.play(Indicate(equations[-1]))
        self.play(FadeOut(equations[-1]))
        self.wait(1)
        ############

        self.play(Write(form))
        self.wait(2)

        eq1 = MathTex(
            r"a", r"x^{2}=-", r"c", font_size=100
        )
        eq2 = MathTex(
            r"x^{2}=-", r"\frac{c}{a}", font_size=100
        )
        eq3 = MathTex(
            r"x=\pm \sqrt{-\frac{c}{a}}", font_size=100
        )

        equations = [form,eq1,eq2,eq3]
        for i in range(len(equations) - 1):
            self.play(ReplacementTransform(equations[i], equations[i + 1]))
            self.wait(2)

        self.wait(0.5)
        self.play(Circumscribe(eq3))
        self.wait(0.5)
        self.play(FadeOut(eq3))

        self.wait(1)

        # Explicação 2

        form = MathTex(
            r"ax^{2}+bx=0",
            font_size=100, tex_to_color_map={'a':YELLOW, 'b':GREEN}
        )

        self.play(Write(form))
        self.wait(1)
        self.play(FadeOut(form))
        self.play(FadeOut(title))
        self.wait(0.5)


        lawtex = Text(
            "Lei do Anulamento do Produto",
            font_size=60)

        self.play(Write(lawtex), run_time=2)
        self.wait(1)
        self.play(lawtex.animate.to_corner(UP, buff=0.8))

        text = MathTex(
            r"a\times b=0",
            font_size=100
        )
        text2 = MathTex(
            r"a=0\vee b=0",
            font_size=100,
            color = GREEN)
        text2.move_to(text.get_bottom()+DOWN)

        self.play(Write(text))
        self.wait(1)
        self.play(Write(text2))
        self.play(Circumscribe(text2))
        self.wait(1)
        self.play(FadeOut(text, text2, lawtex))
        self.wait(1)


        self.play(Write(title))

        eq1 = MathTex(
            r"2x^{2}+4x=0", font_size=100
        )
        eq2 = MathTex(
            r"x(2x+4)=0", font_size=100
        )
        eq3 = MathTex(
            r"x=0\vee 2x+4=0", font_size=100
        )
        eq4 = MathTex(
            r"x=0\vee x=-2", font_size=100
        )
        eq5 = MathTex(
            r"S=\left\{ 0,-2 \right\}", font_size=100,
            color=YELLOW
        )

        self.play(Write(eq1))
        self.wait(2)

        equations = [eq1,eq2,eq3,eq4,eq5]
        for i in range(len(equations) - 1):
            self.play(ReplacementTransform(equations[i], equations[i + 1]))
            self.wait(2)
        
        self.play(Circumscribe(eq5, color=BLUE))

        self.wait(1)
        self.play(FadeOut(eq5))
        self.wait(1)

        text = MathTex(
            r"x=0\vee x=\frac{-b}{a}",
            font_size=100
        )

        self.play(Write(text))
        self.wait(0.5)
        self.play(Circumscribe(text))
        self.wait(1)
        self.play(FadeOut(text, title))
        self.wait(1)

        text_final = Tex(
            "Nos Próximos Vídeos...",
            color=BLUE,
            font_size=100
        )

        self.play(Write(text_final))
        self.play(ApplyWave(text_final))

        self.wait(3)
        self.play(Unwrite(text_final))
        self.wait(1)
