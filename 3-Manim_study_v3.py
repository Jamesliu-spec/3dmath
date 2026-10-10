from manim import *
import random

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_rate = 60

class Rotating3DSystem(ThreeDScene):
    def construct(self):
       axes = ThreeDAxes()
       title = Text("3D坐标系演示",font_size=48,font="SimHei").to_edge(UP).shift(UP*0.3)
       self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES) 
       self.add_fixed_in_frame_mobjects(title)

       blocks = VGroup()
       for i in range (5):
           for j in range(5):
                height = random.random()*1.5 + 0.5
                block = Prism(dimensions=[0.6,0.6,height])
                
                if height < 1.0:
                    color = BLUE
                elif height < 1.5:
                    color = GREEN
                else:
                    color = YELLOW
                block.set_color(color)
                block.move_to([i-2,j-2,0])
                blocks.add(block)
       self.play(Write(title),Create(axes),Create(blocks))
       self.wait(5)
       
       self.play(blocks.animate.set_color(RED), run_time=1.5)
       self.wait(0.5)
       
       self.play(blocks.animate.set_color(GREEN), run_time=1.5)
       self.wait(0.5)
       
       self.play(Rotate(blocks,angle=PI,axis=OUT), run_time=5)
       self.wait(0.5)

       self.play(blocks.animate.set_color(ORANGE), run_time=1.5)
       self.wait(0.5)

       self.play(blocks.animate.set_color(PURPLE), run_time=1.5)
       self.wait(0.5)

       self.begin_ambient_camera_rotation(rate=0.2)
       self.play(blocks.animate.set_color(TEAL), run_time=2)
       self.wait(1)
       self.stop_ambient_camera_rotation()

config.preview = True
scene = Rotating3DSystem()
scene.render()