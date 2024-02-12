import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
def predict_model(i):
    dataset=pd.read_csv('soil.csv')
    dataset=dataset.dropna()
    x=dataset.iloc[:,1].values
    y=dataset.iloc[:,-1].values
    x=x.reshape(-1,1)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    classifier=KNeighborsClassifier(n_neighbors=5)
    classifier.fit(x_train,y_train)
    result=classifier.predict([[i]])
    return result[0]













