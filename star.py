import turtle
turtle.colormode(255)
from myFunctionfile import*
bob = turtle.Turtle()
bob.speed(0)
bob.shape('turtle')
turtle.bgcolor('black')

jump(bob,-1000,0)
for times in range(30):
    funky(bob)
    bob.forward(100)

bob.left(180)
bob.forward(1600)
bob.left(180)
jump(bob,0,-85)
bob.left(180)
bob.forward(1050)
bob.left(180)
bob.color('orange')

for times in range(35):
    funky2(bob)
    bob.forward(100)


bob.left(180)
bob.forward(1600)
bob.left(180)


jump(bob,0,-170)

bob.left(180)
bob.forward(1600)
bob.left(180)
bob.color('orange')

for times in range(35):
    funky2(bob)
    bob.forward(100)

jump(bob,0,-85)
bob.left(180)
bob.forward(1250)
bob.left(180)

for times in range(30):    
    funky(bob)
    bob.forward(100)
#secondloop

jump(bob,0,-255)
bob.left(180)
bob.forward(1050)
bob.left(180)
bob.color('orange')

for times in range(30):
    funky2(bob)
    bob.forward(100)


bob.left(180)
bob.forward(1600)
bob.left(180)


jump(bob,0,-255)

bob.left(180)
bob.forward(1000)
bob.left(180)
bob.color('orange')

for times in range(30):
    funky2(bob)
    bob.forward(100)

jump(bob,0,-170)


bob.left(180)
bob.forward(1050)
bob.left(180)
for times in range(31):    
    funky(bob)
    bob.forward(100)

#thirdloop


jump(bob,0,-340)
bob.left(180)
bob.forward(1050)
bob.left(180)
bob.color('orange')

for times in range(30):
    funky2(bob)
    bob.forward(100)


bob.left(180)
bob.forward(1600)
bob.left(180)


jump(bob,0,-340)

bob.left(180)
bob.forward(1000)
bob.left(180)
bob.color('orange')

for times in range(20):
    funky2(bob)
    bob.forward(100)

jump(bob,0,-255)

bob.left(180)
bob.forward(1050)
bob.left(180)
for times in range(20):    
    funky(bob)
    bob.forward(100)

#fourthloop

jump(bob,0,-425)
bob.left(180)
bob.forward(1650)
bob.left(180)
bob.color('orange')

for times in range(30):
    funky2(bob)
    bob.forward(100)


bob.left(180)
bob.forward(1600)
bob.left(180)


jump(bob,0,-425)

bob.left(180)
bob.forward(1000)
bob.left(180)
bob.color('orange')

for times in range(20):
    funky2(bob)
    bob.forward(100)

jump(bob,0,-340)


bob.left(180)
bob.forward(1050)
bob.left(180)
for times in range(20):    
    funky(bob)
    bob.forward(100)
#5th loop. at this loop, the design goes upwards

jump(bob,-1050,85)

for times in range(30):
    funky(bob)
    bob.forward(100)

jump(bob,-1000,85)
for times in range(20):
    funky(bob)
    bob.forward(100)

jump(bob,-1050,0)
bob.color('orange')
for times in range(20):
    funky2(bob)
    bob.forward(100)


jump(bob,-1050,85)

for times in range(20):
    funky2(bob)
    bob.forward(100)

jump(bob,-1000,170)
for times in range(20):
    funky(bob)
    bob.forward(100)


jump(bob,-1050,170)
bob.color('orange')
for times in range(20):
    funky2(bob)
    bob.forward(100)

jump(bob,-1000,255)
for times in range(20):
    funky(bob)
    bob.forward(100)

jump(bob,-1050,255)
bob.color('orange')
for times in range(20):
    funky2(bob)
    bob.forward(100)

jump(bob,-1000,340)
for times in range(20):
    funky(bob)
    bob.forward(100)

jump(bob,-1050,340)
bob.color('orange')
for times in range(20):
    funky2(bob)
    bob.forward(100)

jump(bob,-1000,425)
for times in range(20):
    funky(bob)
    bob.forward(100)
