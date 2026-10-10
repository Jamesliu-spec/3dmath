from manim import *
from manim import Surface
from perlin_noise import PerlinNoise 
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class perlinnoise(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        title = Text("柏林噪声地形动画演示", font_size=48, font="SimHei").to_edge(UP).shift(UP * 0.3)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.add_fixed_in_frame_mobjects(title)

        noise_gen = PerlinNoise(octaves=4, seed=50)

        def terrain_surface(u, v):
            noise_val = noise_gen([u / 3.0, v / 3.0])
            height = (noise_val + 0.5) * 1.5 + 0.5
            return np.array([u, v, height])

        terrain = Surface(
            terrain_surface,
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.8,
            stroke_width=0.5,
        )

        terrain.set_color_by_gradient(BLUE, GREEN, YELLOW)

        self.play(Write(title), Create(axes))
        self.play(Create(terrain), run_time=3)
        self.wait(1)

        self.play(Rotate(terrain, angle=PI, axis=OUT), run_time=5)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()