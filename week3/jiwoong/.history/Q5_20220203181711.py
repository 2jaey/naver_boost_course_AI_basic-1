import numpy as np

xy = np.array([[1.,2.,3.,4.,5.,6.],
            [10.,20.,30.,40.,50.,60.]])
x_train = xy[0]
y_train = xy[1]

#Q3
print(x_train,x_train.shape)
print(y_train,y_train.shape)

beta_gd = np.random.uniform(0,1,1)
bias = np.random.uniform(0,1,1)

#Q4
print(beta_gd,bias)

learning_rate = 0.01

def difference(y,x,b,a):
    return (y-b*x-a)


for i in range(1000):
    error = difference(y_train,x_train,beta_gd,bias) ** 2
    bias -= -2 *learning_rate * np.mean(difference(y_train,x_train,beta_gd,bias) )
    beta_gd -= -2* learning_rate * np.mean(difference(y_train,x_train,beta_gd,bias) * x_train)
    
    if i%100 == 0:
        print("Epoch ([:10d]/10000 error: [:10f], beta_gd:[:10f]".format(i,error,beta_gd.item(),bias.item()))