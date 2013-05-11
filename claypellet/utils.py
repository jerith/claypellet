

class Rect(object):
    def __init__(self, origin, size):
        self.origin = tuple(origin)
        self.size = tuple(size)

    @property
    def x(self):
        return self.origin[0]

    @property
    def y(self):
        return self.origin[1]

    @property
    def w(self):
        return self.size[0]

    @property
    def h(self):
        return self.size[1]

    @property
    def area(self):
        return self.w * self.h

    @classmethod
    def from_grect(cls, grect):
        return cls((grect.origin.x, grect.origin.y),
                   (grect.size.w, grect.size.h))

    def get_box(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)

    def copy(self, offset):
        return type(self)(self.origin, self.size)

    def move(self, offset):
        return type(self)((self.x + offset[0], self.y + offset[1]), self.size)
