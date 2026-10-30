import numpy as np

a = np.array([10, 20, 30])
b = np.array([2, 5, 10])

print("Arithmetic:")
print("Add:", np.add(a, b))
print("Subtract:", np.subtract(a, b))
print("Multiply:", np.multiply(a, b))
print("Divide:", np.divide(a, b))
print("Power:", np.power(a, 2))
print("Mod:", np.mod(a, b))

x = np.array([0, np.pi/2, np.pi])

print("\nTrigonometric:")
print("Sin:", np.sin(x))
print("Cos:", np.cos(x))
print("Tan:", np.tan(x))

c = np.array([1, 10, 100])

print("\nExponential and Logarithmic:")
print("Exponential:", np.exp(c))
print("Log:", np.log(c))
print("Log10:", np.log10(c))

print("\nComparison:")
print("Greater:", np.greater(a, b))
print("Less:", np.less(a, b))
print("Equal:", np.equal(a, b))

d = np.array([1.2, 2.7, 3.5])

print("\nRounding:")
print("Round:", np.round(d))
print("Floor:", np.floor(d))
print("Ceil:", np.ceil(d))

e = np.array([-10, 20, -30])

print("\nAbsolute and Sign:")
print("Absolute:", np.abs(e))
print("Sign:", np.sign(e))

p = np.array([5, 6, 7])
q = np.array([3, 2, 1])
print("\nBitwise:")
print("AND:", np.bitwise_and(p, q))
print("OR:", np.bitwise_or(p, q))
print("XOR:", np.bitwise_xor(p, q))
print("NOT:", np.bitwise_not(p))