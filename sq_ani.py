from manim import *
from manim_physics import *
class Test_Ani(SpaceScene):
    def construct(self):
        sq=Circle(radius=0.5,color=YELLOW).shift(UP)
        sq.shift(DOWN+RIGHT)

        grd=Line([-4,-2,0],[4,-2,0])
        self.add(grd)
        self.play(Create(sq))
        self.make_rigid_body(sq)
        self.make_static_body(grd)
        self.wait(4)


