import numpy as np

mylist = [1,2,3,]
x = np.array(mylist)
print(x)

y = np.array([[1,2,3],[4,5,6]])
print(y)

print(y.shape)

n = np.arange(0, 30, 2)
m = n.reshape(5, 3)
print(m)

o = np.linspace(0, 4, 4)
o.resize(2,2)
print(o)

print(np.ones((3, 2)))
print(np.zeros((3, 2)))
print(np.eye(4))

print(np.diag(n))

print(np.array([1, 2, 3]) * 3)
print(np.repeat([1, 2, 3], 3))

p = np.ones([2, 3])
v = np.vstack([p+1, 4*p])
print(v)

h = np.hstack([4*p, p+1])
print(h)



x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** 2)
print(x.dot(y))

z = np.array([y, y**2])
print(z)
print(z.T)
print(z.shape)
print(z.T.shape)
print(z.dtype)

l = z.astype('a')
print(z.dtype)

a = np.array([-4, -2, 1, 3, 5])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())
print(a.argmax())
print(a.argmin())

s = np.arange(1, 13)**2
print(s)

print(s[0])
print(s[1:5])
print(s[-4::-2])

r = np.arange(36)
r.resize((6,6))
print(r)

# print(r[2, 2])
# print(r[3, 3:6])
# print(r[:2, :-1])
# print(r[-1, ::2])
# print(r[r > 30])

r2 = r[:3, :3]
print(r2)

r2[:] = 0
print(r2)

print(r)

r_copy = r.copy()
print(r_copy)

r_copy[:] = 10
print(r_copy)
print(r)

test = np.random.randint(0, 10, (4, 3))
print(test)

for row in test:
    print(row)
print('\n')    

for i in range(len(test)):
    print(test[i])
print('\n')    

for i, row in enumerate(test):
    print('row', i, 'is', row)

test2 = test ** 2
print(test2)

for i, j in zip(test, test2):
    print(i,'+',j,'=',i+j) 


