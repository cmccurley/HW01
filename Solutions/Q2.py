# -*- coding: utf-8 -*-
"""
File:   starterQ2.py
Author: Connor McCurley
Date:   09/05/2018
Desc:   This file demonstrates the concepts of Maximum Likelihood (ML) and 
        Maximum A Priori (Map) by estimating the mean of a known Gaussian 
        distribution using a Gaussian Likelihood and a Gaussian Prior.
"""

""" =======================  Import dependencies ========================== """
#from IPython import get_ipython
#get_ipython().magic('reset -sf')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


plt.close('all')
""" ======================  Variable Declaration ========================== """

#True distribution mean and variance
trueMu = 4
trueVar = 1

#Initial prior distribution mean and variance
priorMu = 10
priorVar = 1

#Initial data likelihood mean and variance
likeMu = trueMu
likeVar = trueVar

numDraws = 200 #Number of draws from the true distribution

#Initialize vectors and matrices
draw =  np.zeros((numDraws,1))
muML = np.zeros((1,numDraws))
muMAP = np.zeros((1,numDraws))
varMAP = np.zeros((1,numDraws))

"""========================== Plot the true distribution =================="""
#plot true Gaussian function
step = 0.01
l = -20
u = 20
x = np.arange(l+step/2,u+step/2,step)
plt.figure(0)
p1 = plt.plot(x, norm(trueMu,trueVar).pdf(x), color='b')
plt.title('"True" Distribution')

"""========================= Perform ML and MAP Estimates =================="""
#Calculate posterior and update prior for the given number of draws

for samp in range (0,numDraws):
    draw[samp,0] = np.random.normal(likeMu,likeVar,1) #Draw from the known Gaussian distribution
    
    #Compute the ML mean estimate
    muML[0,samp] = np.sum(draw[:,0])/(samp+1)
    
    #Compute the MAP mean and variance estiamtes
    muMapComp1 = ((likeVar)/((samp*priorVar)+(likeVar)))*priorMu;
    muMAPComp2 = ((samp*priorVar)/((samp*priorVar)+(likeVar)))*muML[0,samp]
    muMAP[0,samp] = muMapComp1 + muMAPComp2
    varMAP[0,samp] = (priorVar*likeVar)/(likeVar+(priorVar*samp))

    #Update new prior as the previous iteration's posterior
    priorMu = muMAP[0,samp]
    priorVar = varMAP[0,samp]

    plt.figure(0)
    
    

"""======================== Plot mean estimates over time =================="""
#Plot convergence of ML mean
plt.figure(1)
plt.plot(range(0,numDraws),muML[0,:], linestyle='-', color='b')
plt.plot(range(0,numDraws),muMAP[0,:], linestyle='--', color='g')
plt.plot([0, numDraws+1],[trueMu, trueMu], linestyle='-.', color='r')
plt.legend(("ML Mean", "MAP Mean", "True Mean"))    
plt.xlabel("Iteration")
plt.ylabel("Mean Value")
plt.title("Convergence of Mean Estimates to True Mean")
    
"""============================ Get estimate errors ========================"""
#Get final estimated values
finalML = muML[0,-1]
finalMAP = muMAP[0,-1]

#Find errors of converged means
errorML = np.abs((trueMu-finalML)*100)/trueMu
errorMAP = np.abs((trueMu-finalMAP)*100)/trueMu

#Display final errors
print("Percent error from ML solution: ", errorML)
print("Percent error from MAP solution: ", errorMAP)

   







