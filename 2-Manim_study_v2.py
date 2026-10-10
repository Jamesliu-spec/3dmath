from manim import *

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class Rotating3DSystem(ThreeDScene):
    def construct(self):
       axes = ThreeDAxes()
       cube = Cube(side_length=2,fill_color=BLUE,fill_opacity=0.7)
       title = Text("3D坐标系演示",font_size=48,font="SimHei").to_edge(UP).shift(UP*0.3)
       self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES) 
       self.add_fixed_in_frame_mobjects(title)
       self.play(Write(title),Create(axes),Create(cube))
       self.wait(1)
       
       self.play(cube.animate.set_color(RED), run_time=1.5)
       self.wait(0.5)
       
       self.play(cube.animate.set_color(GREEN), run_time=1.5)
       self.wait(0.5)
       
       self.play(Rotate(cube,angle=PI,axis=UP), run_time=5)
       self.wait(0.5)

       self.play(cube.animate.set_color(ORANGE), run_time=1.5)
       self.wait(0.5)

       self.play(cube.animate.set_color(PURPLE), run_time=1.5)
       self.wait(0.5)

       self.begin_ambient_camera_rotation(rate=0.2)
       self.play(cube.animate.set_color(TEAL), run_time=2)
       self.wait(1)
       self.stop_ambient_camera_rotation()

config.preview = True
scene = Rotating3DSystem()
scene.render()