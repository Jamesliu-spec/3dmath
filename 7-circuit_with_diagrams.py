from manim import *
import numpy as np
from manim import Succession

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class CircuitTheoryUltimate(Scene):
    """
    最终修正版：电路理论全部公式、定理、图形。
    所有数学符号使用 LaTeX 命令，无 Unicode，无多余 $ 符号。
    """
    def construct(self):
        # ---------- 配色与字体 ----------
        self.camera.background_color = "#1e1e2e"
        font = "SimHei"
        text_color = WHITE
        formula_color = YELLOW
        cursor_color = BLUE
        circuit_color = GREEN
        plot_color = ORANGE

        # ---------- 辅助绘图函数 ----------
        def draw_resistor(pos, width=0.8, height=0.4, label="R", color=circuit_color):
            start = pos + LEFT * width/2
            end = pos + RIGHT * width/2
            points = [start]
            n_segments = 6
            step = width / n_segments
            for i in range(1, n_segments):
                x = start[0] + i * step
                y_offset = height if i % 2 == 1 else -height
                points.append(np.array([x, pos[1] + y_offset, 0]))
            points.append(end)
            resistor = VMobject(stroke_color=color, stroke_width=3)
            resistor.set_points_smoothly(points)
            label_R = Text(label, font_size=20, color=color, font=font).next_to(resistor, DOWN, buff=0.1)
            return VGroup(resistor, label_R)

        def draw_capacitor(pos, width=0.6, height=0.5, label="C", color=circuit_color):
            left = pos + LEFT * width/2
            right = pos + RIGHT * width/2
            line1 = Line(left + UP*height/2, left + DOWN*height/2, color=color, stroke_width=3)
            line2 = Line(right + UP*height/2, right + DOWN*height/2, color=color, stroke_width=3)
            label_C = Text(label, font_size=20, color=color, font=font).next_to(VGroup(line1, line2), DOWN, buff=0.1)
            return VGroup(line1, line2, label_C)

        def draw_inductor(pos, width=0.8, height=0.4, label="L", color=circuit_color):
            points = [pos + LEFT * width/2]
            step = width / 8
            for i in range(1, 8):
                x = pos[0] - width/2 + i * step
                y_offset = height if i % 2 == 1 else -height
                points.append(np.array([x, pos[1] + y_offset, 0]))
            points.append(pos + RIGHT * width/2)
            inductor = VMobject(stroke_color=color, stroke_width=3)
            inductor.set_points_smoothly(points)
            label_L = Text(label, font_size=20, color=color, font=font).next_to(inductor, DOWN, buff=0.1)
            return VGroup(inductor, label_L)

        def draw_source(pos, label="V", color=WHITE):
            circle = Circle(radius=0.25, color=color, stroke_width=2)
            circle.move_to(pos)
            plus = Text("+", font_size=18, color=color, font=font).next_to(circle, UP, buff=0.05)
            minus = Text("-", font_size=18, color=color, font=font).next_to(circle, DOWN, buff=0.05)
            label_V = Text(label, font_size=20, color=color, font=font).next_to(circle, RIGHT, buff=0.2)
            return VGroup(circle, plus, minus, label_V)

        def draw_wire(start, end, color=circuit_color):
            return Line(start, end, color=color, stroke_width=2)

        def draw_ground(pos, color=WHITE):
            gnd_line = Line(pos, pos + DOWN*0.5, color=color)
            gnd_bars = VGroup(
                Line(pos + DOWN*0.3 + LEFT*0.2, pos + DOWN*0.3 + RIGHT*0.2, color=color),
                Line(pos + DOWN*0.45 + LEFT*0.3, pos + DOWN*0.45 + RIGHT*0.3, color=color)
            )
            return VGroup(gnd_line, gnd_bars)

        def draw_opamp(pos, label="Op-Amp", color=WHITE):
            tri = Polygon(pos + LEFT*0.6 + DOWN*0.4, pos + LEFT*0.6 + UP*0.4, pos + RIGHT*0.6, color=color, stroke_width=3)
            label_op = Text(label, font_size=18, color=color, font=font).next_to(tri, RIGHT, buff=0.1)
            return VGroup(tri, label_op)

        def draw_bjt(pos, label="Q", color=WHITE):
            circle = Circle(radius=0.2, color=color).move_to(pos + LEFT*0.3)
            line_c = Line(pos + RIGHT*0.3, pos + UP*0.3, color=color)
            line_e = Line(pos + RIGHT*0.3, pos + DOWN*0.3, color=color)
            label_Q = Text(label, font_size=18, color=color, font=font).next_to(circle, LEFT, buff=0.1)
            return VGroup(circle, line_c, line_e, label_Q)

        def draw_mosfet(pos, label="M", color=WHITE):
            line1 = Line(pos + LEFT*0.3 + UP*0.3, pos + LEFT*0.3 + DOWN*0.3, color=color)
            line2 = Line(pos + RIGHT*0.3 + UP*0.3, pos + RIGHT*0.3 + DOWN*0.3, color=color)
            line3 = Line(pos + LEFT*0.3, pos + RIGHT*0.3, color=color)
            label_M = Text(label, font_size=18, color=color, font=font).next_to(line1, LEFT, buff=0.1)
            return VGroup(line1, line2, line3, label_M)

        def draw_diode(pos, label="D", color=WHITE):
            triangle = Polygon(pos + LEFT*0.3 + UP*0.2, pos + LEFT*0.3 + DOWN*0.2, pos + RIGHT*0.3, color=color)
            line = Line(pos + RIGHT*0.3 + UP*0.2, pos + RIGHT*0.3 + DOWN*0.2, color=color)
            label_D = Text(label, font_size=18, color=color, font=font).next_to(triangle, UP, buff=0.1)
            return VGroup(triangle, line, label_D)

        def draw_ideal_opamp(pos, label="Op-Amp", color=WHITE):
            tri = Polygon(pos + LEFT*0.6 + DOWN*0.4, pos + LEFT*0.6 + UP*0.4, pos + RIGHT*0.6, color=color, stroke_width=3)
            pin_pos = Text("+", font_size=16, color=color, font=font).move_to(pos + LEFT*0.6 + UP*0.2)
            pin_neg = Text("-", font_size=16, color=color, font=font).move_to(pos + LEFT*0.6 + DOWN*0.2)
            label_op = Text(label, font_size=18, color=color, font=font).next_to(tri, RIGHT, buff=0.1)
            return VGroup(tri, pin_pos, pin_neg, label_op)

        def draw_transformer(pos, label="T", color=WHITE):
            left = pos + LEFT*0.5
            right = pos + RIGHT*0.5
            line1 = Line(left + UP*0.3, left + DOWN*0.3, color=color)
            line2 = Line(right + UP*0.3, right + DOWN*0.3, color=color)
            core = Rectangle(width=0.2, height=0.6, color=color).move_to(pos)
            label_T = Text(label, font_size=18, color=color, font=font).next_to(core, UP, buff=0.1)
            return VGroup(line1, line2, core, label_T)

        # ---------- 构建基本电路图 ----------
        def build_RLC_series():
            center = np.array([2.5, 0.2, 0])
            V_pos = center + LEFT*2 + UP*0.5
            R_pos = center + LEFT*0.2
            L_pos = center + RIGHT*0.7
            C_pos = center + RIGHT*0.0 + DOWN*0.3
            source = draw_source(V_pos, label="V_s")
            resistor = draw_resistor(R_pos, label="R")
            inductor = draw_inductor(L_pos, label="L")
            wire1 = draw_wire(V_pos + UP*0.3, R_pos + LEFT*0.4)
            wire2 = draw_wire(R_pos + RIGHT*0.4, L_pos + LEFT*0.4)
            wire3 = draw_wire(L_pos + RIGHT*0.4, C_pos + LEFT*0.3)
            gnd = draw_ground(C_pos + RIGHT*0.3 + DOWN*0.3)
            wire4 = draw_wire(C_pos + RIGHT*0.3, gnd[0].get_start())
            circuit = VGroup(source, resistor, inductor, wire1, wire2, wire3, wire4, gnd)
            circuit.move_to(center, aligned_edge=LEFT)
            return circuit

        def build_RC():
            center = np.array([2.5, 0.0, 0])
            V_pos = center + LEFT*2 + UP*0.5
            R_pos = center + LEFT*0.0
            C_pos = center + RIGHT*0.7
            source = draw_source(V_pos, label="V")
            resistor = draw_resistor(R_pos, label="R")
            capacitor = draw_capacitor(C_pos, label="C")
            wire1 = draw_wire(V_pos + UP*0.3, R_pos + LEFT*0.4)
            wire2 = draw_wire(R_pos + RIGHT*0.4, C_pos + LEFT*0.3)
            gnd = draw_ground(C_pos + RIGHT*0.3 + DOWN*0.3)
            wire3 = draw_wire(C_pos + RIGHT*0.3, gnd[0].get_start())
            circuit = VGroup(source, resistor, capacitor, wire1, wire2, wire3, gnd)
            circuit.move_to(center, aligned_edge=LEFT)
            return circuit

        def build_RL():
            center = np.array([2.5, 0.0, 0])
            V_pos = center + LEFT*2 + UP*0.5
            R_pos = center + LEFT*0.0
            L_pos = center + RIGHT*0.7
            source = draw_source(V_pos, label="V")
            resistor = draw_resistor(R_pos, label="R")
            inductor = draw_inductor(L_pos, label="L")
            wire1 = draw_wire(V_pos + UP*0.3, R_pos + LEFT*0.4)
            wire2 = draw_wire(R_pos + RIGHT*0.4, L_pos + LEFT*0.4)
            gnd = draw_ground(L_pos + RIGHT*0.3 + DOWN*0.3)
            wire3 = draw_wire(L_pos + RIGHT*0.4, gnd[0].get_start())
            circuit = VGroup(source, resistor, inductor, wire1, wire2, wire3, gnd)
            circuit.move_to(center, aligned_edge=LEFT)
            return circuit

        # ---------- 图形函数 ----------
        def draw_rc_curve():
            axes = Axes(x_range=[0, 5, 1], y_range=[0, 1.2, 0.2], axis_config={"color": GRAY}).shift(RIGHT*1.5 + DOWN*0.2)
            curve = axes.plot(lambda t: 1 - np.exp(-t), color=plot_color)
            return VGroup(axes, curve)

        def draw_phasors(center, Vm=3, Im=2, phi=np.pi/6):
            V_vec = Arrow(center, center + Vm * (RIGHT*np.cos(phi) + UP*np.sin(phi)), color=RED)
            I_vec = Arrow(center, center + Im * RIGHT, color=BLUE)
            angle = Arc(radius=0.5, start_angle=0, angle=phi, color=YELLOW)
            return VGroup(V_vec, I_vec, angle)

        def draw_resonance():
            axes = Axes(x_range=[0, 3, 0.5], y_range=[0, 1.5, 0.5], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            curve = axes.plot(lambda x: 1 / np.sqrt((1 - x**2)**2 + (0.3*x)**2), color=plot_color)
            return VGroup(axes, curve)

        def draw_bode_mag():
            axes = Axes(x_range=[0.1, 4, 0.5], y_range=[-40, 10, 10], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            curve = axes.plot(lambda x: 20*np.log10(1/np.sqrt(1 + (x/2)**2)), color=plot_color, x_range=[0.1,4])
            return VGroup(axes, curve)

        def draw_bode_phase():
            axes = Axes(x_range=[0.1, 4, 0.5], y_range=[-90, 0, 10], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            curve = axes.plot(lambda x: -np.degrees(np.arctan(x/2)), color=plot_color, x_range=[0.1,4])
            return VGroup(axes, curve)

        def draw_nyquist():
            circle = Circle(radius=1, color=BLUE, stroke_width=1).shift(RIGHT*2 + UP*0.5)
            points = [np.array([2,0.5,0]) + np.array([np.cos(t)*0.8, np.sin(t)*0.5, 0]) for t in np.linspace(0, np.pi, 50)]
            curve = VMobject(stroke_color=ORANGE, stroke_width=2)
            curve.set_points_smoothly(points)
            return VGroup(circle, curve)

        def draw_state_space():
            rect = Rectangle(width=2, height=1.5, color=WHITE).shift(RIGHT*2 + UP*0.5)
            label = Text("State Space\nx'=Ax+Bu\ny=Cx+Du", font_size=20, color=WHITE, font=font).move_to(rect)
            return VGroup(rect, label)

        def draw_three_phase():
            axes = Axes(x_range=[0, 2*np.pi, 0.5], y_range=[-1.2, 1.2, 0.5], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            curve1 = axes.plot(lambda t: np.sin(t), color=RED)
            curve2 = axes.plot(lambda t: np.sin(t - 2*np.pi/3), color=GREEN)
            curve3 = axes.plot(lambda t: np.sin(t - 4*np.pi/3), color=BLUE)
            return VGroup(axes, curve1, curve2, curve3)

        def draw_filter_response(f_type="lowpass"):
            axes = Axes(x_range=[0.1, 4, 0.5], y_range=[-40, 5, 10], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            if f_type == "lowpass":
                curve = axes.plot(lambda x: 20*np.log10(1/np.sqrt(1 + x**4)), color=plot_color, x_range=[0.1,4])
            elif f_type == "highpass":
                curve = axes.plot(lambda x: 20*np.log10(x**2/np.sqrt(1 + x**4)), color=plot_color, x_range=[0.1,4])
            elif f_type == "bandpass":
                curve = axes.plot(lambda x: 20*np.log10(x*np.sqrt(1 - x**2)/np.sqrt(1 + x**4)), color=plot_color, x_range=[0.1,4])
            else:
                curve = axes.plot(lambda x: 20*np.log10(abs(1 - x**2)/np.sqrt(1 + x**4)), color=plot_color, x_range=[0.1,4])
            return VGroup(axes, curve)

        def draw_coupled_inductors():
            L1 = draw_inductor(np.array([1.5, 0.2, 0]), label="L1")
            L2 = draw_inductor(np.array([3.5, 0.2, 0]), label="L2")
            line = DashedLine(np.array([1.8, 0.6, 0]), np.array([3.2, 0.6, 0]), color=WHITE)
            label_M = Text("M", font_size=18, color=WHITE, font=font).next_to(line, UP, buff=0.05)
            return VGroup(L1, L2, line, label_M)

        def draw_smith_chart():
            circle = Circle(radius=1, color=WHITE, stroke_width=1).shift(RIGHT*2 + UP*0.5)
            line1 = Line(circle.get_center() + LEFT*1, circle.get_center() + RIGHT*1, color=GRAY, stroke_width=0.5)
            line2 = Line(circle.get_center() + DOWN*1, circle.get_center() + UP*1, color=GRAY, stroke_width=0.5)
            return VGroup(circle, line1, line2)

        def draw_butterworth():
            axes = Axes(x_range=[0.1, 4, 0.5], y_range=[-40, 5, 10], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            curve1 = axes.plot(lambda x: 20*np.log10(1/np.sqrt(1 + x**(2*2))), color=plot_color, x_range=[0.1,4])
            curve2 = axes.plot(lambda x: 20*np.log10(1/np.sqrt(1 + x**(2*4))), color=RED, x_range=[0.1,4])
            return VGroup(axes, curve1, curve2)

        def draw_chebyshev():
            axes = Axes(x_range=[0.1, 4, 0.5], y_range=[-40, 5, 10], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            eps = 0.5
            curve = axes.plot(lambda x: 20*np.log10(1/np.sqrt(1 + eps**2 * np.cosh(2*np.arccosh(x))**2)), color=plot_color, x_range=[1,4])
            return VGroup(axes, curve)

        def draw_elliptic():
            axes = Axes(x_range=[0.1, 4, 0.5], y_range=[-40, 5, 10], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            curve = axes.plot(lambda x: 20*np.log10(1/np.sqrt(1 + 0.1*x**2 + 0.01*x**4)), color=plot_color, x_range=[0.1,4])
            return VGroup(axes, curve)

        def draw_root_locus():
            axes = Axes(x_range=[-3, 1, 1], y_range=[-2, 2, 1], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            poles = [(-1, 1), (-1, -1)]
            zeros = [(0, 0)]
            pole_dots = [Dot(axes.coords_to_point(p[0], p[1]), color=RED) for p in poles]
            zero_dots = [Dot(axes.coords_to_point(z[0], z[1]), color=BLUE) for z in zeros]
            branch1 = axes.plot(lambda x: np.sqrt(1 - (x+1)**2), color=GREEN, x_range=[-2, 0])
            branch2 = axes.plot(lambda x: -np.sqrt(1 - (x+1)**2), color=GREEN, x_range=[-2, 0])
            return VGroup(axes, *pole_dots, *zero_dots, branch1, branch2)

        def draw_pid_controller():
            rect1 = Rectangle(width=1.2, height=0.6, color=WHITE).shift(RIGHT*1.5 + UP*0.5)
            label1 = Text("PID", font_size=20, color=WHITE, font=font).move_to(rect1)
            arrow1 = Arrow(rect1.get_left(), rect1.get_left() + LEFT*0.5, color=WHITE)
            arrow2 = Arrow(rect1.get_right(), rect1.get_right() + RIGHT*0.5, color=WHITE)
            return VGroup(rect1, label1, arrow1, arrow2)

        def draw_nyquist_stability():
            axes = Axes(x_range=[-2, 2, 0.5], y_range=[-1.5, 1.5, 0.5], axis_config={"color": GRAY}).shift(RIGHT*1.5)
            point = Dot(axes.coords_to_point(-1, 0), color=RED, radius=0.08)
            label = Text("-1", font_size=18, color=RED, font=font).next_to(point, LEFT)
            circle = Circle(radius=0.5, color=ORANGE).shift(axes.coords_to_point(-1, 0))
            return VGroup(axes, point, label, circle)

        # ---------- 打字机设置 ----------
        cursor = VGroup(
            Line(UP * 0.4, DOWN * 0.4, color=cursor_color, stroke_width=6),
            Line(LEFT * 0.1, RIGHT * 0.1, color=cursor_color, stroke_width=2)
        )
        start_pos = np.array([-6.0, 3.2, 0])
        cursor.move_to(start_pos + np.array([0, -0.1, 0]))

        def blink_cursor(cursor, run_time=0.5):
            return Succession(
                cursor.animate.set_opacity(0).set_run_time(run_time/2),
                cursor.animate.set_opacity(1).set_run_time(run_time/2)
            )

        # ---------- 内容列表（全部使用 LaTeX 命令，无 Unicode，无多余 $） ----------
        content = [
            ("text", "CIRCUIT THEORY - ULTIMATE REFERENCE", YELLOW),
            ("text", "--- 1. Ohm's Law & Power ---", WHITE),
            ("formula", "V = I R", formula_color),
            ("formula", "P = V I = I^2 R = V^2 / R", formula_color),
            ("text", "--- 2. Kirchhoff's Laws ---", WHITE),
            ("formula", "\\text{KVL: }\\sum V_k = 0", formula_color),
            ("formula", "\\text{KCL: }\\sum I_k = 0", formula_color),
            ("text", "--- 3. Resistor Combinations ---", WHITE),
            ("formula", "\\text{Series: } R_{\\mathrm{eq}} = R_1 + R_2 + \\cdots", formula_color),
            ("formula", "\\text{Parallel: } 1/R_{\\mathrm{eq}} = 1/R_1 + 1/R_2 + \\cdots", formula_color),
            ("text", "--- 4. Y-\\Delta Transformation ---", WHITE),
            ("formula", "R_\\Delta = (R_a R_b + R_b R_c + R_c R_a) / R_a", formula_color),
            ("formula", "R_Y = R_{ab} R_{ac} / (R_{ab} + R_{bc} + R_{ca})", formula_color),
            ("text", "--- 5. Voltage Divider ---", WHITE),
            ("formula", "V_{\\mathrm{out}} = V_{\\mathrm{in}} \\frac{R_2}{R_1+R_2}", formula_color),
            ("text", "--- 6. Current Divider ---", WHITE),
            ("formula", "I_{\\mathrm{out}} = I_{\\mathrm{in}} \\frac{R_{\\mathrm{total}}}{R_{\\mathrm{branch}}}", formula_color),
            ("text", "--- 7. Capacitors ---", WHITE),
            ("formula", "I = C \\frac{dV}{dt}", formula_color),
            ("formula", "V = \\frac{1}{C} \\int I \\, dt", formula_color),
            ("formula", "E = \\frac{1}{2} C V^2", formula_color),
            ("formula", "\\text{Series: } 1/C_{\\mathrm{eq}} = 1/C_1 + 1/C_2 + \\cdots", formula_color),
            ("formula", "\\text{Parallel: } C_{\\mathrm{eq}} = C_1 + C_2 + \\cdots", formula_color),
            ("text", "--- 8. Inductors ---", WHITE),
            ("formula", "V = L \\frac{dI}{dt}", formula_color),
            ("formula", "I = \\frac{1}{L} \\int V \\, dt", formula_color),
            ("formula", "E = \\frac{1}{2} L I^2", formula_color),
            ("formula", "\\text{Series: } L_{\\mathrm{eq}} = L_1 + L_2 + \\cdots", formula_color),
            ("formula", "\\text{Parallel: } 1/L_{\\mathrm{eq}} = 1/L_1 + 1/L_2 + \\cdots", formula_color),
            ("text", "--- 9. RC Charging ---", WHITE),
            ("formula", "V_c(t) = V_s \\left(1 - e^{-t/(RC)}\\right)", formula_color),
            ("formula", "I(t) = \\frac{V_s}{R} e^{-t/(RC)}", formula_color),
            ("text", "--- 10. RC Discharging ---", WHITE),
            ("formula", "V_c(t) = V_0 e^{-t/(RC)}", formula_color),
            ("formula", "I(t) = -\\frac{V_0}{R} e^{-t/(RC)}", formula_color),
            ("text", "--- 11. RL Current Growth ---", WHITE),
            ("formula", "I_L(t) = \\frac{V_s}{R} \\left(1 - e^{-Rt/L}\\right)", formula_color),
            ("formula", "V_L(t) = V_s e^{-Rt/L}", formula_color),
            ("text", "--- 12. RL Current Decay ---", WHITE),
            ("formula", "I_L(t) = I_0 e^{-Rt/L}", formula_color),
            ("formula", "V_L(t) = -I_0 R e^{-Rt/L}", formula_color),
            ("text", "--- 13. RLC Series (Natural) ---", WHITE),
            ("formula", "s^2 + \\frac{R}{L}s + \\frac{1}{LC} = 0", formula_color),
            ("formula", "\\alpha = \\frac{R}{2L}, \\quad \\omega_0 = \\frac{1}{\\sqrt{LC}}", formula_color),
            ("formula", "\\text{Underdamped: } s = -\\alpha \\pm j\\sqrt{\\omega_0^2-\\alpha^2}", formula_color),
            ("formula", "\\text{Critically damped: } s = -\\alpha \\text{ (double)}", formula_color),
            ("formula", "\\text{Overdamped: } s = -\\alpha \\pm \\sqrt{\\alpha^2-\\omega_0^2}", formula_color),
            ("text", "--- 14. RLC Parallel ---", WHITE),
            ("formula", "\\frac{1}{RC} + \\frac{s}{L} + s^2 C = 0", formula_color),
            ("formula", "\\alpha = \\frac{1}{2RC}, \\quad \\omega_0 = \\frac{1}{\\sqrt{LC}}", formula_color),
            ("text", "--- 15. Network Theorems ---", WHITE),
            ("text", "Thevenin: $V_{\\mathrm{Th}} = V_{\\mathrm{oc}},\\; R_{\\mathrm{Th}} = V_{\\mathrm{oc}} / I_{\\mathrm{sc}}$", formula_color),
            ("text", "Norton: $I_{\\mathrm{N}} = I_{\\mathrm{sc}},\\; R_{\\mathrm{N}} = V_{\\mathrm{oc}} / I_{\\mathrm{sc}}$", formula_color),
            ("text", "Superposition: response = sum of individual sources", formula_color),
            ("text", "Substitution: any branch can be replaced by equivalent", formula_color),
            ("text", "Reciprocity: $V/I$ ratio unchanged when source and response swapped", formula_color),
            ("text", "Maximum Power Transfer: $Z_L = Z_{\\mathrm{Th}}^*$", formula_color),
            ("text", "Tellegen's Theorem: sum of branch powers = 0", formula_color),
            ("text", "Compensation Theorem: branch replaced by equivalent source", formula_color),
            ("text", "Millman's Theorem: parallel voltage sources combined", formula_color),
            ("text", "--- 16. AC Sinusoids ---", WHITE),
            ("formula", "V(t) = V_m \\sin(\\omega t + \\phi)", formula_color),
            ("formula", "I(t) = I_m \\sin(\\omega t + \\phi)", formula_color),
            ("text", "--- 17. RMS Values ---", WHITE),
            ("formula", "V_{\\mathrm{rms}} = \\frac{V_m}{\\sqrt{2}}", formula_color),
            ("formula", "I_{\\mathrm{rms}} = \\frac{I_m}{\\sqrt{2}}", formula_color),
            ("text", "--- 18. Phasor Representation ---", WHITE),
            ("formula", "\\mathbf{V} = V_m \\angle\\phi = V_m e^{j\\phi}", formula_color),
            ("formula", "\\mathbf{I} = I_m \\angle\\phi = I_m e^{j\\phi}", formula_color),
            ("text", "--- 19. Impedance ---", WHITE),
            ("formula", "Z = \\frac{\\mathbf{V}}{\\mathbf{I}} = R + jX", formula_color),
            ("formula", "Z_R = R,\\; Z_L = j\\omega L,\\; Z_C = -j/(\\omega C)", formula_color),
            ("text", "--- 20. Admittance ---", WHITE),
            ("formula", "Y = \\frac{1}{Z} = G + jB", formula_color),
            ("formula", "G = \\frac{R}{R^2+X^2},\\; B = -\\frac{X}{R^2+X^2}", formula_color),
            ("text", "--- 21. AC Power ---", WHITE),
            ("formula", "P_{\\mathrm{avg}} = V_{\\mathrm{rms}} I_{\\mathrm{rms}} \\cos\\phi", formula_color),
            ("formula", "Q = V_{\\mathrm{rms}} I_{\\mathrm{rms}} \\sin\\phi \\;\\text{(Reactive)}", formula_color),
            ("formula", "S = V_{\\mathrm{rms}} I_{\\mathrm{rms}} \\;\\text{(Apparent)}", formula_color),
            ("formula", "S = \\sqrt{P^2 + Q^2}", formula_color),
            ("text", "--- 22. Power Factor Correction ---", WHITE),
            ("text", "Add capacitors to reduce reactive power", formula_color),
            ("text", "pf = $\\cos\\phi = P/S$; improve by adding parallel capacitors", formula_color),
            ("text", "--- 23. Series Resonance ---", WHITE),
            ("formula", "\\omega_0 = \\frac{1}{\\sqrt{LC}}", formula_color),
            ("formula", "Q = \\frac{\\omega_0 L}{R} = \\frac{1}{\\omega_0 C R}", formula_color),
            ("formula", "\\mathrm{BW} = \\frac{\\omega_0}{Q}", formula_color),
            ("text", "--- 24. Parallel Resonance ---", WHITE),
            ("formula", "\\omega_0 = \\frac{1}{\\sqrt{LC}}", formula_color),
            ("formula", "Q = \\frac{R}{\\omega_0 L} = R \\omega_0 C", formula_color),
            ("formula", "\\mathrm{BW} = \\frac{\\omega_0}{Q}", formula_color),
            ("text", "--- 25. Impedance Transformation ---", WHITE),
            ("text", "$Q$ can be used to transform impedance", formula_color),
            ("text", "--- 26. Transformers ---", WHITE),
            ("formula", "\\frac{V_s}{V_p} = \\frac{N_s}{N_p}", formula_color),
            ("formula", "\\frac{I_s}{I_p} = \\frac{N_p}{N_s}", formula_color),
            ("text", "--- 27. Autotransformers ---", WHITE),
            ("text", "Single winding with tap", formula_color),
            ("text", "--- 28. Three-Phase Systems ---", WHITE),
            ("formula", "V_{\\mathrm{line}} = \\sqrt{3} V_{\\mathrm{phase}}", formula_color),
            ("formula", "P_{\\mathrm{total}} = \\sqrt{3} V_{\\mathrm{line}} I_{\\mathrm{line}} \\cos\\phi", formula_color),
            ("formula", "Q_{\\mathrm{total}} = \\sqrt{3} V_{\\mathrm{line}} I_{\\mathrm{line}} \\sin\\phi", formula_color),
            ("formula", "S_{\\mathrm{total}} = \\sqrt{3} V_{\\mathrm{line}} I_{\\mathrm{line}}", formula_color),
            ("text", "--- 29. Op-Amp Circuits ---", WHITE),
            ("text", "Inverting: $V_{\\mathrm{out}} = -\\frac{R_f}{R_{\\mathrm{in}}} V_{\\mathrm{in}}$", formula_color),
            ("text", "Non-inverting: $V_{\\mathrm{out}} = \\left(1+\\frac{R_f}{R_{\\mathrm{in}}}\\right) V_{\\mathrm{in}}$", formula_color),
            ("text", "Summing: $V_{\\mathrm{out}} = -R_f \\left(\\frac{V_1}{R_1}+\\frac{V_2}{R_2}+\\cdots\\right)$", formula_color),
            ("text", "Difference: $V_{\\mathrm{out}} = \\frac{R_2}{R_1}(V_2 - V_1)$", formula_color),
            ("text", "Integrator: $V_{\\mathrm{out}} = -\\frac{1}{RC} \\int V_{\\mathrm{in}}\\,dt$", formula_color),
            ("text", "Differentiator: $V_{\\mathrm{out}} = -RC \\frac{dV_{\\mathrm{in}}}{dt}$", formula_color),
            ("text", "Instrumentation Amplifier: high CMRR", formula_color),
            ("text", "Logarithmic Amplifier: $V_{\\mathrm{out}} \\propto \\ln(V_{\\mathrm{in}})$", formula_color),
            ("text", "Antilog Amplifier: $V_{\\mathrm{out}} \\propto \\exp(V_{\\mathrm{in}})$", formula_color),
            ("text", "Precision Rectifier", formula_color),
            ("text", "Peak Detector", formula_color),
            ("text", "--- 30. Coupled Inductors ---", WHITE),
            ("formula", "V_1 = L_1 \\frac{dI_1}{dt} + M \\frac{dI_2}{dt}", formula_color),
            ("formula", "V_2 = M \\frac{dI_1}{dt} + L_2 \\frac{dI_2}{dt}", formula_color),
            ("text", "Ideal Transformer: $V_1/V_2 = N_1/N_2,\\; I_1/I_2 = N_2/N_1$", formula_color),
            ("text", "$M = k\\sqrt{L_1 L_2},\\; k\\le 1$", formula_color),
            ("text", "--- 31. Transfer Function H(s) ---", WHITE),
            ("formula", "H(s) = \\frac{V_{\\mathrm{out}}(s)}{V_{\\mathrm{in}}(s)}", formula_color),
            ("text", "--- 32. Bode Plots ---", WHITE),
            ("text", "$20\\log_{10}|H(j\\omega)|$, angle vs $\\log_{10}\\omega$", formula_color),
            ("text", "--- 33. Nyquist Stability ---", WHITE),
            ("text", "Encircles $(-1,0)$ $\\Rightarrow$ unstable", formula_color),
            ("text", "--- 34. Nichols Chart ---", WHITE),
            ("text", "Magnitude vs phase on logarithmic scale", formula_color),
            ("text", "--- 35. Root Locus ---", WHITE),
            ("text", "Poles move with gain $K$", formula_color),
            ("text", "Rule: branches start at poles, end at zeros", formula_color),
            ("text", "--- 36. Laplace Transform ---", WHITE),
            ("formula", "\\mathcal{L}\\{f(t)\\} = \\int_0^\\infty f(t)e^{-st}\\,dt", formula_color),
            ("formula", "\\mathcal{L}\\left\\{\\frac{df}{dt}\\right\\} = sF(s) - f(0)", formula_color),
            ("formula", "\\mathcal{L}\\left\\{\\int f\\,dt\\right\\} = \\frac{F(s)}{s}", formula_color),
            ("text", "Initial Value Theorem: $\\lim_{s\\to\\infty} sF(s) = f(0^+)$", formula_color),
            ("text", "Final Value Theorem: $\\lim_{s\\to 0} sF(s) = \\lim_{t\\to\\infty} f(t)$", formula_color),
            ("text", "--- 37. Laplace for Circuits ---", WHITE),
            ("formula", "Z_R = R,\\; Z_L = sL,\\; Z_C = 1/(sC)", formula_color),
            ("text", "--- 38. Fourier Series ---", WHITE),
            ("formula", "f(t) = a_0 + \\sum_{n=1}^\\infty \\left[ a_n \\cos(n\\omega_0 t) + b_n \\sin(n\\omega_0 t) \\right]", formula_color),
            ("formula", "a_0 = \\frac{1}{T} \\int f(t)\\,dt", formula_color),
            ("formula", "a_n = \\frac{2}{T} \\int f(t)\\cos(n\\omega_0 t)\\,dt", formula_color),
            ("formula", "b_n = \\frac{2}{T} \\int f(t)\\sin(n\\omega_0 t)\\,dt", formula_color),
            ("text", "--- 39. Fourier Transform ---", WHITE),
            ("formula", "F(\\omega) = \\int_{-\\infty}^{\\infty} f(t)e^{-j\\omega t}\\,dt", formula_color),
            ("formula", "\\text{Parseval's Theorem: } \\int |f(t)|^2\\,dt = \\frac{1}{2\\pi}\\int |F(\\omega)|^2\\,d\\omega", formula_color),
            ("text", "--- 40. State Space Model ---", WHITE),
            ("formula", "\\dot{x} = A x + B u", formula_color),
            ("formula", "y = C x + D u", formula_color),
            ("text", "Controllability: $\\mathrm{rank}[B\\ AB\\ \\cdots\\ A^{n-1}B] = n$", formula_color),
            ("text", "Observability: $\\mathrm{rank}[C; CA; \\cdots; CA^{n-1}] = n$", formula_color),
            ("text", "--- 41. Two-Port Parameters ---", WHITE),
            ("formula", "\\text{Z: }[V] = [Z][I]", formula_color),
            ("formula", "\\text{Y: }[I] = [Y][V]", formula_color),
            ("formula", "\\text{H: }[V_1; I_2] = [H][I_1; V_2]", formula_color),
            ("formula", "\\text{ABCD: }[V_1; I_1] = [ABCD][V_2; -I_2]", formula_color),
            ("text", "S-parameters: scattering matrix", formula_color),
            ("text", "Conversion between parameters", formula_color),
            ("text", "--- 42. Transmission Lines (Lossless) ---", WHITE),
            ("formula", "V(z) = V^+ e^{-j\\beta z} + V^- e^{j\\beta z}", formula_color),
            ("formula", "I(z) = \\frac{V^+}{Z_0} e^{-j\\beta z} - \\frac{V^-}{Z_0} e^{j\\beta z}", formula_color),
            ("formula", "Z_0 = \\sqrt{\\frac{L}{C}},\\; \\beta = \\omega\\sqrt{LC}", formula_color),
            ("text", "VSWR = $\\frac{1+|\\Gamma|}{1-|\\Gamma|}$", formula_color),
            ("text", "Smith Chart: graphical impedance matching", formula_color),
            ("text", "--- 43. Lossy Transmission Lines ---", WHITE),
            ("formula", "\\gamma = \\sqrt{(R+j\\omega L)(G+j\\omega C)}", formula_color),
            ("formula", "Z_0 = \\sqrt{\\frac{R+j\\omega L}{G+j\\omega C}}", formula_color),
            ("text", "--- 44. Filters ---", WHITE),
            ("text", "Low-pass, High-pass, Band-pass, Band-stop, All-pass", formula_color),
            ("text", "Butterworth, Chebyshev, Elliptic filter responses", formula_color),
            ("text", "Active filter topologies: Sallen-Key, multiple feedback", formula_color),
            ("text", "Filter design: pole-zero placement", formula_color),
            ("text", "--- 45. z-Transform ---", WHITE),
            ("formula", "X(z) = \\sum_{n=-\\infty}^{\\infty} x[n] z^{-n}", formula_color),
            ("text", "Region of Convergence (ROC) matters", formula_color),
            ("text", "--- 46. Digital Signal Processing ---", WHITE),
            ("text", "Difference equation: $y[n] = \\sum_{k} a_k y[n-k] + \\sum_{k} b_k x[n-k]$", formula_color),
            ("text", "Digital filter design (IIR, FIR)", formula_color),
            ("text", "Impulse invariance, bilinear transform", formula_color),
            ("text", "--- 47. Feedback Control ---", WHITE),
            ("text", "Closed-loop transfer function: $T(s) = \\frac{G(s)}{1+G(s)H(s)}$", formula_color),
            ("text", "Steady-state error: $e_{ss} = \\lim_{s\\to 0} sE(s)$", formula_color),
            ("text", "Routh-Hurwitz stability criterion", formula_color),
            ("text", "Root Locus: poles move with gain $K$", formula_color),
            ("text", "Bode stability: gain and phase margins", formula_color),
            ("text", "PID controller: $K_p + \\frac{K_i}{s} + K_d s$", formula_color),
            ("text", "--- 48. Random Signals ---", WHITE),
            ("text", "Autocorrelation: $R_{xx}(\\tau) = E[x(t)x(t+\\tau)]$", formula_color),
            ("text", "Power Spectral Density: $S_{xx}(\\omega) = \\mathcal{F}\\{R_{xx}(\\tau)\\}$", formula_color),
            ("text", "Cross-correlation: $R_{xy}(\\tau) = E[x(t)y(t+\\tau)]$", formula_color),
            ("text", "Wiener-Khinchin theorem", formula_color),
            ("text", "--- 49. Nonlinear Circuits ---", WHITE),
            ("text", "Diode: $I = I_s\\left(e^{V/V_T} - 1\\right)$", formula_color),
            ("text", "Transistor: Ebers-Moll model", formula_color),
            ("text", "Piecewise-linear approximation", formula_color),
            ("text", "Small-signal analysis", formula_color),
            ("text", "--- 50. Advanced Topics ---", WHITE),
            ("text", "Switched-capacitor circuits", formula_color),
            ("text", "Chaotic circuits: Chua's circuit", formula_color),
            ("text", "Memristor: $M(q) = d\\varphi/dq$", formula_color),
            ("text", "Fractional-order circuits", formula_color),
            ("text", "Wave digital filters", formula_color),
            ("text", "Noise analysis: thermal, shot, flicker", formula_color),
            ("text", "Sensitivity analysis", formula_color),
            ("text", "Symbolic circuit analysis", formula_color),
            ("text", "Topological methods", formula_color),
            ("text", "Graph theory in circuits", formula_color),
            ("text", "--- 51. Additional Theorems ---", WHITE),
            ("text", "Kelvin's theorem", formula_color),
            ("text", "Thévenin with dependent sources", formula_color),
            ("text", "Norton with dependent sources", formula_color),
            ("text", "Source transformation", formula_color),
            ("text", "Star-mesh transformation", formula_color),
            ("text", "Foster's theorem", formula_color),
            ("text", "--- 52. END ---", GREEN),
        ]

        # ---------- 布局 ----------
        current_y = start_pos[1]
        line_spacing = 0.6
        max_lines_per_page = 10
        all_lines = VGroup()
        self.add(cursor)

        right_graphic = VGroup()

        # ---------- 主循环 ----------
        for i, (typ, text, color) in enumerate(content):
            if typ == "text":
                mob = Text(text, font=font, color=color, font_size=24)
            else:
                mob = MathTex(text, color=color, font_size=26)
            mob.align_to(start_pos, LEFT)
            mob.move_to(np.array([start_pos[0], current_y, 0]), aligned_edge=LEFT)

            self.play(FadeIn(mob, run_time=0.1))
            cursor.next_to(mob, RIGHT, buff=0.1)
            self.play(blink_cursor(cursor, run_time=0.1), run_time=0.1)

            # 根据内容更新右侧图形
            if "Ohm's Law" in text or "V = I R" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                circuit = build_RLC_series()
                circuit.shift(RIGHT*1.5)
                self.play(Create(circuit, run_time=0.6))
                right_graphic = circuit
            elif "RC Charging" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                circuit = build_RC()
                circuit.shift(RIGHT*1.5)
                self.play(Create(circuit, run_time=0.6))
                curve = draw_rc_curve()
                self.play(Create(curve))
                right_graphic = VGroup(circuit, curve)
            elif "RL Current Growth" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                circuit = build_RL()
                circuit.shift(RIGHT*1.5)
                self.play(Create(circuit, run_time=0.6))
                right_graphic = circuit
            elif "RLC Series" in text or "RLC Parallel" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                circuit = build_RLC_series()
                circuit.shift(RIGHT*1.5)
                self.play(Create(circuit, run_time=0.6))
                right_graphic = circuit
            elif "Phasor" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                phasors = draw_phasors(np.array([2.5, 0.5, 0]))
                self.play(Create(phasors))
                right_graphic = phasors
            elif "Resonance" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                res = draw_resonance()
                self.play(Create(res))
                right_graphic = res
            elif "Bode" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                bode = draw_bode_mag()
                self.play(Create(bode))
                right_graphic = bode
            elif "Nyquist" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                nyq = draw_nyquist()
                self.play(Create(nyq))
                right_graphic = nyq
            elif "State Space" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                ss = draw_state_space()
                self.play(Create(ss))
                right_graphic = ss
            elif "Three-Phase" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                tp = draw_three_phase()
                self.play(Create(tp))
                right_graphic = tp
            elif "Filters" in text or "Low-pass" in text or "High-pass" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                filt = draw_filter_response("lowpass")
                self.play(Create(filt))
                right_graphic = filt
            elif "Coupled Inductors" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                coup = draw_coupled_inductors()
                coup.shift(RIGHT*0.5)
                self.play(Create(coup))
                right_graphic = coup
            elif "Op-Amp" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                op = draw_opamp(np.array([2.5, 0.5, 0]))
                self.play(Create(op))
                right_graphic = op
            elif "Smith" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                smith = draw_smith_chart()
                self.play(Create(smith))
                right_graphic = smith
            elif "Butterworth" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                bw = draw_butterworth()
                self.play(Create(bw))
                right_graphic = bw
            elif "Chebyshev" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                ch = draw_chebyshev()
                self.play(Create(ch))
                right_graphic = ch
            elif "Elliptic" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                el = draw_elliptic()
                self.play(Create(el))
                right_graphic = el
            elif "BJT" in text or "Transistor" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                bjt = draw_bjt(np.array([2.5, 0.5, 0]))
                self.play(Create(bjt))
                right_graphic = bjt
            elif "MOSFET" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                mos = draw_mosfet(np.array([2.5, 0.5, 0]))
                self.play(Create(mos))
                right_graphic = mos
            elif "Diode" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                dio = draw_diode(np.array([2.5, 0.5, 0]))
                self.play(Create(dio))
                right_graphic = dio
            elif "Root Locus" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                rl = draw_root_locus()
                self.play(Create(rl))
                right_graphic = rl
            elif "PID" in text or "Feedback" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                pid = draw_pid_controller()
                self.play(Create(pid))
                right_graphic = pid
            elif "Nyquist Stability" in text:
                if right_graphic:
                    self.play(FadeOut(right_graphic))
                ns = draw_nyquist_stability()
                self.play(Create(ns))
                right_graphic = ns

            # 自动翻页
            if i > 0 and (i % max_lines_per_page == 0):
                shift_amount = line_spacing * max_lines_per_page
                self.play(
                    *[line.animate.shift(UP * shift_amount) for line in all_lines],
                    cursor.animate.shift(UP * shift_amount),
                    run_time=0.4
                )
                current_y -= shift_amount
                start_pos[1] -= shift_amount

            all_lines.add(mob)
            current_y -= line_spacing
            self.wait(0.05)

        # 结束光标闪烁
        for _ in range(3):
            self.play(blink_cursor(cursor, run_time=0.3), run_time=0.3)
        self.play(FadeOut(cursor))
        self.wait(2)