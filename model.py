import pandas as pd
import pylab as pl
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

def abs_error(actual, pred): 
    return np.abs(pred-actual)

df = pd.read_csv('output_clean_under200.csv')

#split train , test
train ,test = train_test_split(df,test_size = 0.2)

df_x_train = train.iloc[:,1:]
df_x_test = test.iloc[:,1:]
df_y_train = train.iloc[:,0]
df_y_test = test.iloc[:,0]

#MLP model
MLP = MLPRegressor(solver = 'lbfgs' , hidden_layer_sizes = (30,100,100,100,50) , random_state = 1)
MLP.fit(df_x_train,df_y_train)
MLPpred = MLP.predict(df_x_test)
print 'MLP MAE : ', np.mean(abs_error(MLPpred,df_y_test))

#RandomForest model
RF = RandomForestRegressor()
RF.fit(df_x_train,df_y_train)
RFpred = RF.predict(df_x_test)
print 'RF MAE : ', np.mean(abs_error(RFpred,df_y_test))

#LinearRegression model
lm=LinearRegression()
lm.fit(df_x_train,df_y_train)
lmpred=lm.predict(df_x_test)
print 'LR MAE : ', np.mean(abs_error(lmpred,df_y_test))

#dump the model
joblib.dump(RF,'RFmodel.pkl')