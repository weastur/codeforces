import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

m = {
    b'Tetrahedron': 4,
    b'Cube': 6,
    b'Octahedron': 8,
    b'Dodecahedron': 12,
    b'Icosahedron': 20,
}
ans = 0
for _ in range(int(inp())):
    ans += m[inp()]
print(ans)
