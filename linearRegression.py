import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline

X = np.random.uniform(-100,1220,15420) #for random values in list X
					# X is also independent variable
y = X*3+5 				#y is the dependent variable

plt.show(X,y)				# scatter plot of data

b0 = np.random				#provide random values to b0 
b1 = np.random				#provide random values to b1

mean_X = np.mean(X)			#calculation of mean of X
mean_y = np.mean(y) 			#calculation of mean of y

num = 0
den = 0

for i in range(len(X)):			#loop to calculate the numerator and denomenator
    num += (X[i] - mean_X) * (y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

b1 = num/den				#formula to calculate slope
b0 = mean_y - (b1*mean_X)		#formula to calculate y intercept

h = b1*X + b0				
print(h)

print(y)
