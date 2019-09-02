from z3 import *
s = Solver()
x = BitVec("x",32)
s.add(x&1==0)
s.add(((0x4D2 * x + 0x162E) / 0x112C ^ 0xABCDDCBA) == 0xABCDB8B9)
s.add(((0x91E * x + 0x2693) / 0x1E61 ^ 0x12336790) == 0x1233FC70)
print(s.check())
print(s.model())