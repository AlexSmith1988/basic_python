square = lambda x: x * x
cube = lambda x: square(x) * x
apply = lambda f, g: lambda x: f(g(x))

apply(print, apply(cube, square))(2)
