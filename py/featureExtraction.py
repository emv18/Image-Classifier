# Load basic libraries.
from skimage.io import imread, imshow
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import copy, math
import createCSV

'''
folder_path = './Images/All Dogs/'
image_list = []
image_index = 1

while True:
    image_path = os.path.join(folder_path, f'perro{image_index}.jpg')
    
    if not os.path.isfile(image_path):
        break
    
    image = imread(image_path)
    image_list.append(image)
    
    image_index += 1
'''

# Load and show an image
# Samoyed Image
#image = imread('./Images/All Dogs/perro1.jpg')
# Pomeranian Image
image = imread('./Images/All Dogs/perro219.jpg')
# Xolitzquintle Image
#image = imread('./Images/All Dogs/perro438.jpg')
#imshow(image)

# Check the image shape 
image_shape= image.shape
'''
print("IMAGE SHAPE: ")
print(image_shape)
print('')

#print("IMAGE SHAPE: " + image.shape) 
# Watch the content of the image in grayscale
print("IMAGE:")
print(image)
print("")
'''

size = image.shape[0]*image.shape[1]

# ----------------------------------------- FEATURES AS VECTORS --------------------------------------------------
# Red channel values Feature
feature1_reds = image[:,:,0].ravel().tolist() #We get the red value of the rgb and save it in a 1D array
'''
print("REDS: ")
print(feature1_reds)
print('')
'''
# Red channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature1_reds, bins=256, range=(0, 256))
ax.set_title('Red Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Red Value')
plt.show()
'''


# Green channel values Feature
feature2_greens = image[:,:,1].ravel().tolist() #We get the green value of the rgb and save it in a 1D array
'''
print("GREENS: ")
print(feature2_greens)
print('')
'''
# Green channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature2_greens, bins=256, range=(0, 256))
ax.set_title('Green Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Green Value')
plt.show()
'''

# Blue channel values Feature
feature3_blues = image[:,:,2].ravel().tolist() #We get the green value of the rgb and save it in a 1D array
'''
print("BLUES: ")
print(feature3_blues)
print('')
'''
# Blue channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature3_blues, bins=256, range=(0, 256))
ax.set_title('Blue Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Blue Value')
plt.show()
'''

#Whites Feature
feature4_whites = image[((image[:,:,0] >= 230) & (image[:,:,1] >= 230) & (image[:,:,2] >= 230)) 
                     & ((image[:,:,0] <= 250) & (image[:,:,1] <= 250) & (image[:,:,2] <= 250))]
feature4_whites= feature4_whites.ravel().tolist()
'''
print("WHITES: ")
print(feature4_whites)
print('')
'''
# White channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature4_whites, bins=256, range=(0, 256))
ax.set_title('White Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('White Value')
plt.show()
'''

#Blacks Feature
feature5_blacks = image[((image[:,:,0] >= 0) & (image[:,:,1] >= 0) & (image[:,:,2] >= 0)) 
                     & ((image[:,:,0] <= 30) & (image[:,:,1] <= 30) & (image[:,:,2] <= 30))]
feature5_blacks= feature5_blacks.ravel().tolist()
'''
print("BLACKS: ")
print(feature5_blacks)
print('')
'''
# Black channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature5_blacks, bins=256, range=(0, 256))
ax.set_title('Black Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Black Value')
plt.show()
'''

#Browns Feature
feature6_browns = image[((image[:,:,0] >= 20) & (image[:,:,1] >= 50) & (image[:,:,2] >= 90)) 
                     & ((image[:,:,0] <= 220) & (image[:,:,1] <= 190) & (image[:,:,2] <= 140))]
feature6_browns= feature6_browns.ravel().tolist()
'''
print("BROWNS: ")
print(feature6_browns)
print('')
'''
# Brown channel values Feature
'''
fig, ax = plt.subplots(figsize=(6,3))
ax.hist(feature6_browns, bins=256, range=(0, 256))
ax.set_title('Brown Channel Histogram')
ax.set_xlabel('Pixels')
ax.set_ylabel('Brown Value')
plt.show()
'''
#print(feature.shape) 
#print(feature)
#print(feature6_browns)

# This piece of code was made to create a csv file for each feature

createCSV.create_csv(feature1_reds, 'red_features.csv')
createCSV.create_csv(feature2_greens, 'green_features.csv')
createCSV.create_csv(feature3_blues, 'blue_features.csv')
createCSV.create_csv(feature4_whites, 'white_features.csv')
createCSV.create_csv(feature5_blacks, 'black_features.csv')
createCSV.create_csv(feature6_browns, 'brown_features.csv')

'''
columns = {
    'reds': feature1_reds,
    'greens': feature2_greens,
    'blues': feature3_blues,
    'whites': feature4_whites,
    'blacks': feature5_blacks,
    'browns': feature6_browns
}
createCSV.create_csv(columns, 'all_features.csv')
'''



'''
# ----------------------------------------- FEATURES AS MATRIX MULTINOMINAL REGRESSION --------------------------------------------------
features= [feature1_reds, feature2_greens, feature3_blues, feature4_whites, feature5_blacks, feature6_browns]
x_train = np.array(features)
y_train = ['Xolitzquintle', 'Pomeranian', 'Samoyed']

def sigmoid(z):
    """
    Compute the sigmoid of z

    Parameters
    ----------
    z : array_like
        A scalar or numpy array of any size.

    Returns
    -------
     g : array_like
         sigmoid(z)
    """
    z = np.clip(z, -500, 500)           # protect against overflow
    g = 1.0/(1.0+np.exp(-z))

    return g

def compute_cost_logistic_reg(X, y, w, b, lambda_ = 1):
    """
    Computes the cost over all examples
    Args:
    Args:
      X (ndarray (m,n): Data, m examples with n features
      y (ndarray (m,)): target values
      w (ndarray (n,)): model parameters  
      b (scalar)      : model parameter
      lambda_ (scalar): Controls amount of regularization
    Returns:
      total_cost (scalar):  cost 
    """

    m,n  = X.shape
    cost = 0.
    for i in range(m):
        z_i = np.dot(X[i], w) + b                                      #(n,)(n,)=scalar, see np.dot
        f_wb_i = sigmoid(z_i)                                          #scalar
        cost +=  -y[i]*np.log(f_wb_i) - (1-y[i])*np.log(1-f_wb_i)      #scalar
             
    cost = cost/m                                                      #scalar

    reg_cost = 0
    for j in range(n):
        reg_cost += (w[j]**2)                                          #scalar
    reg_cost = (lambda_/(2*m)) * reg_cost                              #scalar
    
    total_cost = cost + reg_cost                                       #scalar
    return total_cost    

def compute_gradient_logistic_reg(X, y, w, b, lambda_): 
    """
    Computes the gradient for linear regression 
 
    Args:
      X (ndarray (m,n): Data, m examples with n features
      y (ndarray (m,)): target values
      w (ndarray (n,)): model parameters  
      b (scalar)      : model parameter
      lambda_ (scalar): Controls amount of regularization
    Returns
      dj_dw (ndarray Shape (n,)): The gradient of the cost w.r.t. the parameters w. 
      dj_db (scalar)            : The gradient of the cost w.r.t. the parameter b. 
    """
    m,n = X.shape
    dj_dw = np.zeros((n,))                            #(n,)
    dj_db = 0.0                                       #scalar

    for i in range(m):
        f_wb_i = sigmoid(np.dot(X[i],w) + b)          #(n,)(n,)=scalar
        err_i  = f_wb_i  - y[i]                       #scalar
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err_i * X[i,j]      #scalar
        dj_db = dj_db + err_i
    dj_dw = dj_dw/m                                   #(n,)
    dj_db = dj_db/m                                   #scalar

    for j in range(n):
        dj_dw[j] = dj_dw[j] + (lambda_/m) * w[j]

    return dj_db, dj_dw  

def gradient_descent(X, y, w_in, b_in, alpha, r_lambda, num_iters): 
    """
    Performs batch gradient descent
    
    Args:
      X (ndarray (m,n)   : Data, m examples with n features
      y (ndarray (m,))   : target values
      w_in (ndarray (n,)): Initial values of model parameters  
      b_in (scalar)      : Initial values of model parameter
      alpha (float)      : Learning rate
      r_lambda (float)     : Regularization rate
      num_iters (scalar) : number of iterations to run gradient descent
      
    Returns:
      w (ndarray (n,))   : Updated values of parameters
      b (scalar)         : Updated value of parameter 
    """
    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    w = copy.deepcopy(w_in)  #avoid modifying global w within function
    b = b_in
    
    for i in range(num_iters):
        # Calculate the gradient and update the parameters
        dj_db, dj_dw = compute_gradient_logistic_reg(X, y, w, b, r_lambda)   

        # Update Parameters using w, b, alpha and gradient
        w = w - alpha * dj_dw               
        b = b - alpha * dj_db               
      
        # Save cost J at each iteration
        if i<100000:      # prevent resource exhaustion 
            J_history.append( compute_cost_logistic_reg(X, y, w, b, r_lambda) )

        # Print cost every at intervals 10 times or as many iterations if < 10
        if i% math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]}   ")
        
    return w, b, J_history

#x_train = np.random.rand(7,2)
#y_train = np.array([0, 0, 0, 1, 1, 1, 1])

w_in = x_train.shape[1]
b_in = 0.5

alph = 0.1
r_lambda = 0.7
iters = 10000

w_out, b_out, _ = gradient_descent(x_train, y_train, w_in, b_in, alph, r_lambda, iters) 

def y_change(y, cl):
    """
    Creates an independent y vector that only holds 1's for
    the selected class and zero for the rest
    
    Args:
      y (ndarray (m,)) : target values
      cl (scalar)      : The class we are studying.
      
    Returns:
      y_pr (ndarray (n,))   : Array holding only 1's for the 
                              analyzed class.
    """
    y_pr=[]
    for i in range(0, len(y)):
        if y[i] == cl:
            y_pr.append(1)
        else:
            y_pr.append(0)
    return y_pr

def find_param(X, y):
    """
    Creates the w_i vector for the given class.
    
    Args:
      X (ndarray (m,n)    : Data, m examples with n features
      y (ndarray (m,))    : Target values
      
    Returns:
      theta_list (ndarray (n,)) : This is a matrix that will hold a row for the w values
                                  for every i class. 
    """
    w_in = x_train.shape[1]
    b_in = 0.5

    alph = 0.1
    r_lambda = 0.7
    iters = 1000

    y_uniq = list(set(y.flatten()))
    theta_list = []
    for i in y_uniq:
        y_tr = pd.Series(y_change(y, i))
        # y_tr = y_tr[:, np.newaxis]
        np.array(y_tr)[:, np.newaxis]
        print(f"\n\nWe will find the weights for class: {i}")
        theta1, _ , _ = gradient_descent(x_train, y_train, w_in, b_in, alph, r_lambda, iters) 
        theta_list.append(theta1)
    return theta_list

def predict(theta_list, X, y):
    y_uniq = list(set(y.flatten()))
    y_hat = [0]*len(y)
    for i in range(0, len(y_uniq)):
        y_tr = y_change(y, y_uniq[i])
        # y1 = sigmoid(x, theta_list[i])
        y1 = sigmoid(np.dot(X, theta_list[i]))
        for k in range(0, len(y)):
            if y_tr[k] == 1 and y1[k] >= 0.5:
                y_hat[k] = y_uniq[i]
    return y_hat

# Create an 11 by 3 random matrix
x_train = np.random.rand(11,3)
y_train = np.array([0,  0, 0, 1, 1, 1, 1, 2, 2, 2, 2])

theta_list = find_param(x_train, y_train)

y_hat = predict(theta_list, x_train, y_train)
print(y_hat)
'''