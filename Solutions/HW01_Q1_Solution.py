# -*- coding: utf-8 -*-
"""
File:   HW01_Q1_Solution.py
Author: Connor McCurley
Date:   09/05/2018
Desc:   This file demonstrates the concept of polynomial regression.
"""

""" =======================  Import dependencies ========================== """
from IPython import get_ipython
get_ipython().magic('reset -sf')
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
    plt.figure()   
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
N_train = 10 #number of training samples to generate
N_test = 50 #number of test samples to generate
gVar = .1 #variance of error distribution
maxM =  10 #Max regression model order

"""======================== Generate true function ======================== """
#We would not know this in practice!!!
true_x = np.arange(l,u,0.001)  #get equally spaced points in the xrange
true_t = np.sinc(true_x) #compute the true function value

""" =======================  Generate Training Data ======================= """
train_data = np.array(generateUniformData(N_train, l, u, gVar)).T
train_x = train_data[:,0]
train_t = train_data[:,1]

""" ======================== Generate Test Data =========================== """
test_data = np.array(generateUniformData(N_test, l, u, gVar)).T
test_x = test_data[:,0]
test_t = test_data[:,1]
    
""" ========================  Train the Model ============================= """
w = fitdata(train_x,train_t,3) #regression weights

#Get estimated labels of training data
X_train = np.array([train_x**m for m in range(w.size)]).T #generate feature vectors
est_train_t = X_train@w #get estimated labels

#Plot data
plotData(train_x,train_t,true_x,true_t,train_x,est_train_t,['Training Data', 'True Function', 'Estimated\nPolynomial'])
print(w)
   

"""========================================================================="""
""" ===== Run model fitting and testing over varying model orders  ======== """
"""========================================================================="""
#initialize error vectors
erms_train = np.zeros((maxM,1))
erms_test = np.zeros((maxM,1))

for M  in range(1,(maxM+1)):
    #fit regression model
    w = fitdata(train_x,train_t,M) #regression weights
    
    #generate feature vectors
    X_train = np.array([train_x**m for m in range(w.size)]).T #generate feature vectors
    X_test = np.array([test_x**m for m in range(w.size)]).T #generate feature vectors

    #estimate labels
    est_train_t = X_train@w #get estimated labels of training data
    est_test_t = X_test@w #get estimated labels of test data
    
    #calculate instantaneous error
    inst_error_train = (est_train_t - train_t)
    inst_error_test = (est_test_t - test_t)
    
    #calculate rms error
    erms_train[M-1,0] = math.sqrt((inst_error_train.T@inst_error_train)/N_train) #get error for training data
    erms_test[M-1,0] = math.sqrt((inst_error_test.T@inst_error_test)/N_test) #get error for test data

#Plot the error vs model order    
plt.figure()
p1 = plt.plot(np.arange(1,(maxM+1)),erms_train, marker='o', color='b', fillstyle='none')
p2 = plt.plot(np.arange(1,(maxM+1)),erms_test, marker='o', color='r', fillstyle='none')
plt.ylim(0,1)
plt.xlabel("Model Order")
plt.ylabel("Erms")
plt.title("Polynomial Regression Error for Varying Model Orders")
plt.legend(("Training Error","Test Error"))
plt.show()



