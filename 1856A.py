import io
import os
import sys

if os.environ.get("LOCAL_JUDGE") is None:
    input_buffer = io.BytesIO(os.read(0, os.fstat(0).st_size))
    inp = lambda: input_buffer.readline().rstrip(b"\n").rstrip(b"\r")
else:
    inp = input
out = []

t = inp()
for _ in range(int(t)):
    n = int(inp())
    a = list(map(int, inp().split()))
    if sorted(a) == a:
        out.append(0)
    else:
        for i in range(n - 2, -1, -1):
            if a[i] > a[i + 1]:
                out.append(max(a[:i + 1]))
                break

sys.stdout.write("\n".join(map(str, out)))
