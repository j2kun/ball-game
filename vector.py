class Vector:
   def __init__(self, coords):
      self.coords = coords
      self.dimension = len(coords)

   def scale(self, constant):
      return Vector([constant * x for x in self.coords])

   def add(self, other):
      # zip is a special function which produces a list of pairs
      # allowing one to simultaneously iterate through two lists.
      return Vector([x+y for (x,y) in zip(self.coords, other.coords)])

   def norm(self):
      return sum(x*x for x in self.coords) ** 0.5

   def mirror(self, axis=0, friction=0.2):
      self.coords[axis] = -self.coords[axis] + friction * self.coords[axis]

   def __repr__(self):
      return str(self.coords)

   def __add__(self, other):
      return self.add(other)

   def __sub__(self, other):
      return Vector([x-y for (x,y) in zip(self.coords, other.coords)])

   def __neg__(self, other):
      return Vector([-y for y in self.coords])

   def __getitem__(self, index):
      return self.coords[index]

   def __setitem__(self, index, value):
      self.coords[index] = value

