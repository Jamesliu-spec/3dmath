from manim import *
import os

config.tex_template.tex_compiler = "latex"
config.tex_template.add_to_preamble("\\usepackage{amsmath,amssymb}")

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class PythagoreanTheorem(Scene):
    def construct(self):
        # --- 标题 ---
        title = Text("勾股定理", font_size=48, font="SimHei", color=BLUE)
        subtitle = MathTex("a^2 + b^2 = c^2", font_size=30, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.2)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(VGroup(title, subtitle).animate.to_edge(UP).scale(0.7))
        self.wait(0.5)

        # --- 直角三角形（缩小） ---
        a_len = 1.8
        b_len = 2.4
        c_len = 3.0

        A = np.array([0, 0, 0])
        B = np.array([a_len, 0, 0])
        C = np.array([0, b_len, 0])

        side_a = Line(A, B, color=RED, stroke_width=6)
        side_b = Line(A, C, color=GREEN, stroke_width=6)
        side_c = Line(B, C, color=BLUE, stroke_width=6)

        offset = LEFT * 2.5 + DOWN * 1.2
        triangle = VGroup(side_a, side_b, side_c)
        triangle.shift(offset)

        self.play(Create(side_a), Create(side_b), run_time=1)
        self.play(Create(side_c), run_time=1)
        self.wait(0.5)

        # --- 顶点标签 ---
        label_A = MathTex("A", font_size=24).next_to(A + offset, DL, buff=0.3)
        label_B = MathTex("B", font_size=24).next_to(B + offset, DR, buff=0.3)
        label_C = MathTex("C", font_size=24).next_to(C + offset, UL, buff=0.3)
        labels = VGroup(label_A, label_B, label_C)
        self.play(Write(labels))
        self.wait(0.5)

        # --- 边长标注（亮色、稍大） ---
        a_label = MathTex("a = 1.8", font_size=28, color="#FF6666").next_to(
            (A + B) / 2 + offset, DOWN, buff=0.6
        )
        b_label = MathTex("b = 2.4", font_size=28, color="#66FF66").next_to(
            (A + C) / 2 + offset, LEFT, buff=0.6
        )
        c_label = MathTex("c = 3.0", font_size=28, color="#66AAFF").next_to(
            (B + C) / 2 + offset, UR, buff=0.6
        )
        side_labels = VGroup(a_label, b_label, c_label)
        self.play(Write(side_labels))
        self.wait(1)

        # --- 公式动画（字体不变） ---
        formula1 = MathTex("a^2 + b^2 = c^2", font_size=32, color=YELLOW)
        formula2 = MathTex("1.8^2 + 2.4^2 = 3^2", font_size=32, color=YELLOW)
        formula3 = MathTex("3.24 + 5.76 = 9", font_size=32, color=YELLOW)
        formula4 = MathTex("9 = 9", font_size=32, color=GREEN)

        formulas = [formula1, formula2, formula3, formula4]
        for f in formulas:
            f.shift(RIGHT * 4.5 + UP * 0.5)

        self.play(Write(formula1))
        self.wait(0.8)
        self.play(TransformMatchingShapes(formula1, formula2))
        self.wait(0.8)
        self.play(TransformMatchingShapes(formula2, formula3))
        self.wait(0.8)
        self.play(TransformMatchingShapes(formula3, formula4))
        self.wait(1)

        # --- 检查标记 ---
        check = Text("成立！", font_size=30, color=GREEN, font="SimHei")
        check.next_to(formula4, DOWN, buff=0.5)
        self.play(Write(check))
        self.wait(1)

        # --- 正方形面积演示 ---
        self.play(FadeOut(formula4), FadeOut(check))
        self.wait(0.3)

        # 红色正方形（a边）
        sq_a = Square(
            side_length=a_len,
            color=RED,
            fill_color=RED,
            fill_opacity=0.35,
            stroke_width=3
        )
        sq_a.move_to(A + offset + np.array([a_len/2, -a_len/2 - 0.2, 0]))

        # 绿色正方形（b边）- 亮色
        sq_b = Square(
            side_length=b_len,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.4,
            stroke_width=3
        )
        sq_b.move_to(A + offset + np.array([-b_len/2 - 0.25, b_len/2, 0]))

        # 蓝色正方形（c边）
        sq_c = Square(
            side_length=c_len,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.35,
            stroke_width=3
        )
        angle = np.arctan2(b_len, a_len)
        sq_c.rotate(angle)
        mid_c = (B + C) / 2 + offset
        normal = np.array([-b_len, a_len, 0]) / c_len
        sq_c.move_to(mid_c + normal * 0.5)

        area_a_label = MathTex("a^2 = 3.24", font_size=22, color="#FF6666")
        area_a_label.next_to(sq_a, DOWN, buff=0.25)

        area_b_label = MathTex("b^2 = 5.76", font_size=22, color="#66FF66")
        area_b_label.next_to(sq_b, LEFT, buff=0.25)

        area_c_label = MathTex("c^2 = 9", font_size=22, color="#66AAFF")
        area_c_label.next_to(sq_c, UP, buff=0.25)

        self.play(Create(sq_a), Create(sq_b), run_time=1.5)
        self.play(Write(area_a_label), Write(area_b_label))
        self.wait(0.5)
        self.play(Create(sq_c), run_time=1.5)
        self.play(Write(area_c_label))
        self.wait(1)

        # --- 汇总 ---
        summary = VGroup(
            MathTex("3.24 + 5.76 = 9", font_size=30, color=YELLOW),
            Text("勾股定理成立！", font_size=30, color=GREEN, font="SimHei")
        )
        summary.arrange(DOWN, buff=0.3)
        summary.shift(RIGHT * 4 + DOWN * 2.5)
        self.play(Write(summary))
        self.wait(2)

        # --- 结束 ---
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
        end_text = Text("谢谢观看！", font_size=42, font="SimHei", color=BLUE)
        self.play(Write(end_text))
        self.wait(2)