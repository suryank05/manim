from manim import *
class TransformTestFixed(Scene):
    def construct(self):
        sq = Square().set_color(RED)
        cir = Circle().set_color(GREEN)
        tr = Polygon(LEFT, UP * 2, RIGHT).set_color(BLUE)
        rec=Rectangle(color=YELLOW)
        
        self.play(
            ReplacementTransform(sq, cir),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(cir, tr),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(tr,rec),
        )
        self.wait()