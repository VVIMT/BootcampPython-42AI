from vector import Vector

v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector([10.35, -13.50, 2.0, -3.64])
v3 = 4
v4 = 7
v5 = Vector(1)
v6 = [8]
v7 = [19]
v8 = Vector([35])

print("v1 + v2: " + str(v1 + v2))
print("\nv2 + v1: " + str(v2 + v1))
print("\nv6 + v2: " + str(v6 + v2))
print("\nv2 + v6: " + str(v2 + v6))
print("\nv1 + v5: " + str(v1 + v5))
print("\nv1 + v8: " + str(v1 + v8))
print("\nv5 + v8: " + str(v5 + v8))
print("\nv8 + v5: " + str(v8 + v5))
print("\n")