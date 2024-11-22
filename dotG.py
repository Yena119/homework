import matplotlib.pyplot as plt

data = [90, 80, 70, 77, 58]
x = ['a', 'b', 'c', 'd', 'e']
plt.figure('그래프 이름')
plt.plot(x, data)
plt.scatter(x, data, color='red')
plt.title('Graph')
plt.grid()
plt.show()

