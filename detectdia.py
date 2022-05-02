import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm

class Diabetes():
	
	def __init__(self):

		dataset = pd.read_csv('diabetes.csv')

		X =dataset.drop(columns='Outcome',axis=1)
		Y =dataset['Outcome']
		self.Standard_data = StandardScaler()
		self.Standard_data.fit(X)
		standardized_data=self.Standard_data.transform(X)
		X=standardized_data
		Y=dataset['Outcome']
		X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
		self.classifier = svm.SVC(kernel='linear')
		self.classifier.fit(X_train, Y_train)

	def detectf(self,preg,glucose,bp,skinthick,insulin,bmi,dpf,age):
		input_data = (preg,glucose,bp,skinthick,insulin,bmi,dpf,age)

		input_data_as_numpy_array = np.asarray(input_data)

		input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

		std_data = self.Standard_data.transform(input_data_reshaped)


		prediction = self.classifier.predict(std_data)


		if (prediction[0] == 0):
		  return False
		else:
		  return True

if __name__=="__main__":
	x=Diabetes()
	x.find()