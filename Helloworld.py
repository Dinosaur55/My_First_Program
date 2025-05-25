import numpy as np

msg="Helloworld, I am Dinosaur55"
print(msg)

# Generate a random number between 1 and 8
print(np.random.randint(1,9))

# Generate a vector [1,2,3,4,5]
v = np.array([1,2,3,4,5])
u = np.array(range(1,6))
w = np.linspace(1,5,5)
print(v)
print(u)
print(w)

# Generate a matrix [[1,2,3],[4,5,6],[7,8,9]]
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
# Output m(1,2) = 2
print(m[0,1])