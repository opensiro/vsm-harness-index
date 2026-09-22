from math_utils import clamp

assert clamp(5, 1, 10) == 5
assert clamp(-4, 1, 10) == 1
assert clamp(14, 1, 10) == 10

try:
    clamp(1, 4, 3)
except ValueError:
    pass
else:
    raise AssertionError("lower > upper must raise ValueError")

print("ok")
