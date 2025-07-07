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
y = list([1,2,3,4,5])
print(f"v={v}")
print(f"v[0]={v[0]}")
print(f"v[1:3]={v[1:3]}")
print(f"v[:2]={v[:2]}")
print(f"v[1:]={v[1:]}")

print(f"u={u}")
print(f"w={w}")
print(f"x={x}")
print(f"y={y}")
print(f"x[1]={x[1]}")


# Generate a matrix [[1,2,3],[4,5,6],[7,8,9]]
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"m={m}")
# Output m(1,2) = 2
print(f"m[0,1]={m[0,1]}")
print(f"m[1][2]={m[1][2]}")

# Draw a sine wave
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()

# End timing and print total time
end_time = time.time()
total_time = end_time - start_time
print(f"\nTotal execution time: {total_time:.4f} seconds")
