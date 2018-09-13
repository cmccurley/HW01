# -*- coding: utf-8 -*-
"""
Description: This script acts as starter code for question 1 of HW01 for 
Foundations of Machine Learning, Fall 2018.  This code demonstrates one way of
generating samples from an underlying distribution with added Gaussian noise.

Portions of this code are intentionally missing. It is up to the student to 
fill them in!  Hint: not everything you need is in this file. It is up to the
student to add the necessary code to complete this assignment.

"""

""" =======================  Import dependencies ========================== """

import numpy as np
import math 
import matplotlib.pyplot as plt

plt.close('all')

""" ======================  Function definitions ========================== """

def generateUniformData(N, l, u, gVar):
	'''generateUniformData(N, l, u, gVar): Generate N uniformly spaced data points 
    in the range [l,u) with zero-mean Gaussian random noise with variance gVar'''
	# x = np.random.uniform(l,u,N)
	step = (u-l)/(N);
	x = np.arange(l+step/2,u+step/2,step)
	e = np.random.normal(0,gVar,N)
	t = np.sinc(x) + e
	return x,t

def plotData(x1,t1,x2,t2,x3=None,t3=None,legend=[]):
    '''plotData(x1,t1,x2,t2,x3=None,t3=None,legend=[]): Generate a plot of the 
       training data, the true function, and the estimated function'''
    p1 = plt.plot(x1, t1, 'bo') #plot training data
    p2 = plt.plot(x2, t2, 'g') #plot true value
    if(x3 is not None):
        p3 = plt.plot(x3, t3, 'r') #plot training data

    #add title, legend and axes labels
    plt.ylabel('t') #label x and y axes
    plt.xlabel('x')
    
    if(x3 is None):
        plt.legend((p1[0],p2[0]),legend)
    else:
        plt.legend((p1[0],p2[0],p3[0]),legend)
        
def fitdata(x,t,M):
    X = np.array([x**m for m in range(M+1)]).T
    w = np.linalg.inv(X.T@X)@X.T@t
    return w
        

""" ======================  Variable Declaration ========================== """

l = 0 #lower bound on x
u = 10 #upper bound on x
N = 50 #number of samples to generate
gVar = .25 #variance of error distribution
M =  3 #regression model order
""" =======================  Generate Training Data ======================= """
data_uniform  = np.array(generateUniformData(N, l, u, gVar)).T

x1 = data_uniform[:,0]
t1 = data_uniform[:,1]

x2 = np.arange(l,u,0.001)  #get equally spaced points in the xrange
t2 = np.sinc(x2) #compute the true function value
    
""" ========================  Train the Model ============================= """

w = fitdata(x1,t1,M) 
x3 = np.arange(l,u,0.001)  #get equally spaced points in the xrange
X = np.array([x3**m for m in range(w.size)]).T
t3 = X@w #compute the predicted value

plotData(x1,t1,x2,t2,x3,t3,['Training Data', 'True Function', 'Estimated\nPolynomial'])
print(w)


""" ======================== Generate Test Data =========================== """


"""This is where you should generate a validation testing data set.  """
   


""" ========================  Test the Model ============================== """

""" This is where you should test the validation set with the trained model """



