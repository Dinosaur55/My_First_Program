import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

# Start timing
start_time = time.time()

msg="Helloworld, I am Dinosaur55"
print(msg)

# Generate a random number between 1 and 8
print(np.random.randint(1,9))

# Generate a vector [1,2,3,4,5]
v = np.array([1,2,3,4,5])
u = np.linspace(1,5,5)
w = range(5)
x = list(range(1,5,2))
print(v)
print(v[0])
print(v[1:3])
print(v[:2])
print(v[:5])
print(v[1:])

print(u)
print(w)
print(x)
print(x[1])


# Generate a matrix [[1,2,3],[4,5,6],[7,8,9]]
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
# Output m(1,2) = 2
print(m[0,1])
print(m[1][2])

# Draw a sine wave
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()

# End timing and print total time
end_time = time.time()
total_time = end_time - start_time
print(f"\nTotal execution time: {total_time:.4f} seconds")
