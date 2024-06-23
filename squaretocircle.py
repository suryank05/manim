from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()
        tri=Triangle()
        rec=Rectangle()

        #Showing shapes
        self.play(Create(square))
        self.play(FadeOut(square))
        self.play(Transform(circle,tri))
        
        
       
        self.play(FadeOut(tri))      