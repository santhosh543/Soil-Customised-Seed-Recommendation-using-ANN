import numpy as np
import sklearn

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to the crop predict API"

@app.route('/predict', methods = ['POST'])
def predict():
	model = pickle.load(open('Crop_pred_rand_forest.pkl' ,'rb'))
	
	try:
		moisture = float(request.form['moisture'])
		nitrogen = float(request.form['nitrogen'])
		phosphorous = float(request.form['phosphorous'])
		potassium = float(request.form['potassium'])
		
		test_vector = np.asanyarray([moisture, nitrogen, phosphorous, potassium])
		test_vector = np.reshape(test_vector,(1,4))
		reverse_mapping = ['Barley','Corn-Field for silage','Corn-Field for stover','Millet','Potato','Sugarcane']
		reverse_mapping = np.asarray(reverse_mapping)
		a = model.predict(test_vector)
		#hell yeah this corresponds to barley
		#prediction = reverse_mapping[a]

		# give to model and predict

		#hell yeah this corresponds to barley
		# prediction = reverse_mapping[a]

		c=0
		for ix in range(a.shape[0]):
		    if a[ix].any() == 1:
		        ans = c
		    c+=1

		#print reverse_mapping[ans]
		#print((moisture, nitrogen, phosphorous, potassium))
	

		res = reverse_mapping[ans]

		return jsonify({'result' : res })
	except Exception as e:
		print(e)
		return jsonify({'error' : 'Wrong Parameters' })

if __name__ == '__main__':
	app.run(port = 8080, debug = True)
