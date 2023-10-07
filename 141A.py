import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

a, b = bytearray(inp()) + bytearray(inp()), bytearray(inp())
print("YES" if sorted(a) == sorted(b) else "NO")
