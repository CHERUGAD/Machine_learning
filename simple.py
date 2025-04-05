x= [1,2,3,4,5]
y= [2,3,4,5,6]
 
n= len(x)
m= len(y)

sum_x= sum(x)
sum_y= sum(y)
sum_x2= sum([i**2 for i in range(n)])
sum_xy= sum([x[i]*y[i] for i in range(n)])
#finding slope and intercept
m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2- sum_x2**2) 
mean_x= sum_x/n
mean_y= sum_y/n
c = mean_y - m*mean_x
print("Slope:", m)
print("Intercept:", c)
print("Equation of line: y = mx + c")
print(f"y = {m :.2f}x + {c:.2f}")
#predicting y for given x
x= 6
y= m*x + c
print(f"Predicted y:  {y:.2f}")
#plotting the line
import matplotlib.pyplot as plt
import numpy as np
x= np.array([1,2,3,4,5])
y= np.array([2,3,4,5,6])
plt.scatter(x,y, color= 'red')
plt.plot(x, m*x + c, color= 'blue')
plt.title('Linear Regression')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()