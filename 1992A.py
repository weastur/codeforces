import io
import os
import sys

out = []
if "LOCAL" not in os.environ:
    input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
    input = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")  # noqa

for _ in range(int(input())):
    a = list(map(int, input().split()))
    for _ in range(5):
        a.sort()
        a[0] += 1
    out.append(a[0] * a[1] * a[2])

sys.stdout.write("\n".join(map(str, out)))
