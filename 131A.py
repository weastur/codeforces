import io
import os
import sys

input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
out = sys.stdout.write

s = inp().decode()
if s.isupper():
    print(s.lower())
elif s[0].islower() and (len(s) == 1 or s[1:].isupper()):
    print(s[0].upper() + s[1:].lower())
else:
    print(s)
