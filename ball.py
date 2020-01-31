from vector import Vector
import pyglet
from math import atan2, sin, cos

ball_image = pyglet.image.load('ball.png')


class Ball(pyglet.sprite.Sprite):
    def __init__(self, radius, posn, windowWidth, windowHeight):
        super(Ball, self).__init__(pyglet.image.load('ball.png'), posn[0], posn[1])

        self.radius = radius
        self.posn = posn
        self.velocity = Vector([0, 0])
        self.acceleration = Vector([0, -5])
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.kick_speed = 60

        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2

    def updateSpritePosn(self):
        self.x = self.posn[0]
        self.y = self.posn[1]

    def move(self):
        self.velocity = self.velocity + self.acceleration
        self.posn = self.posn + self.velocity

        if self.posn[1] - self.image.anchor_y < 0:
            self.posn[1] = self.image.anchor_y
            self.velocity.mirror(axis=1)

        if self.posn[1] + (self.height - self.image.anchor_y) > self.windowHeight:
            self.posn[1] = self.windowHeight - self.image.anchor_y
            self.velocity.mirror(axis=1)

        if self.posn[0] - self.image.anchor_x < 0:
            self.posn[0] = self.image.anchor_x
            self.velocity.mirror(axis=0)

        if self.posn[0] + (self.width - self.image.anchor_x) > self.windowWidth:
            self.posn[0] = self.windowWidth - (self.image.width - self.image.anchor_x)
            self.velocity.mirror(axis=0)

        self.updateSpritePosn()
        direction = 1 if self.velocity[0] > 0 else -1
        self.rotation += direction * (abs(self.velocity[0]))
        # self.rotation += cmp(self.velocity[0], 0) * (abs(self.velocity[0]))

    def kick(self, newVelocity):
        self.velocity = newVelocity

    def intersects(self, other):
        return (self.posn + other.posn.scale(-1)).norm() < self.radius + other.radius

    def kick(self, x, y):
        if (self.posn[0] - x)**2 + (self.posn[1] - y)**2 < self.radius ** 2:
            forceAngle = atan2(self.posn[1] - y, self.posn[0] - x)
            self.velocity = Vector([self.kick_speed * cos(forceAngle), self.kick_speed * sin(forceAngle)])
