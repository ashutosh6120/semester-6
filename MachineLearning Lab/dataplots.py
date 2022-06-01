#scatter plot
import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x, y)
plt.show()



#boxplot
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)
data = np.random.normal(100, 20, 200)
fig = plt.figure(figsize =(10, 7))
plt.boxplot(data)
plt.show()


#heat maps
import matplotlib.pyplot as plt
import numpy as np
a = np.random.random((16, 16))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()


#contour plot
import matplotlib.pyplot as plt
import numpy as np
feature_x = np.linspace(-5.0, 3.0, 70)
feature_y = np.linspace(-5.0, 3.0, 70)
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
fig, ax = plt.subplots(1, 1)
Z = X ** 2 + Y ** 2
# plots filled contour plot
ax.contourf(X, Y, Z)
ax.set_title('Filled Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')
plt.show()




#3d surface plots
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
x= np.outer(np.linspace(-3, 3, 32), np.ones(32))
y= x.copy().T # transpose
z= (np.sin(x **2) + np.cos(y **2) )
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, z)
plt.show()
