from math import sin, cos, ceil
import sys
A = 0.0
B = 0.0
print("\x1b[2J")
while True:
  b = [' ' for _ in range(1760)]
  z = [0.0 for _ in range(1760)]
  i = 0.0
  j = 0.0
  while j < 6.28:
    while i < 6.28:
      c = sin(i)
      d = cos(j)
      e = sin(A)
      f = sin(j)
      g = cos(A)
      h = d + 2
      D = 1 / (c * h * e + f * g + 5)
      l = cos(i)
      m = cos(B)
      n = sin(B)
      t = c * h * g - f * e
      x = int(40 + 30 * D * (l * h * m - t * n))
      y = int(12 + 15 * D * (l * h * n + t * m))
      o = int(x + 80 * y)
      N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
      if (22 > y and y > 0 and x > 0 and 80 > x and D > z[o]) :
          z[o] = D
          b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
      i += 0.02
    j += 0.07
  print("\x1b[H")
  for cur in range(1760):
    sys.stdout.write(b[cur] if (cur % 80 != 0) else '\n')

  A += 0.007
  B += 0.002


