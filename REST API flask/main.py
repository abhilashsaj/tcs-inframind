from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import random 

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
# import pandas as pd

from sklearn.multiclass import OneVsRestClassifier
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection

from flask_cors import CORS
	
# from sklearn.ensemble import BaggingClassifier
# from sklearn.ensemble import ExtraTreesClassifier
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.ensemble import VotingClassifier
# from sklearn.metrics import roc_curve, roc_auc_score

app = Flask(__name__)
CORS(app)
api = Api(app)

class OpenAPI(Resource):

	def get(self):
		# response.headers["X-Total-Count"] = "1"
		return {'post_meal': bool(random.getrandbits(1)),
			'blood_sugar_level': random.randint(0,400),
	        'breaths_per_minute': random.randint(10,30),
	        'is_running': bool(random.getrandbits(1)),
	        'breath_shortness_severity': random.randint(0,10),
	        'cough_frequency': random.randint(0,10),
	        'cough_severity': random.randint(0,10),
	        
	        'blood_pressure_sys': random.randint(50,250),
	        'blood_pressure_dia': random.randint(50,250),
	        'heart_rate': random.randint(60,200),
	        'cholestorol': random.randint(60,200),
	        'oxygen_saturation': random.randint(90,100)
	        }


	def post(self):
		return {'post_meal': bool(random.getrandbits(1)),
		'blood_sugar_level': random.randint(0,400),
        'breaths_per_minute': random.randint(10,30),
        'is_running': bool(random.getrandbits(1)),
        'breath_shortness_severity': random.randint(0,10),
        'cough_frequency': random.randint(0,10),
        'cough_severity': random.randint(0,10),
        
        'blood_pressure_sys': random.randint(50,250),
        'blood_pressure_dia': random.randint(50,250),
        'heart_rate': random.randint(60,200),
        'cholestorol': random.randint(60,200),
        'oxygen_saturation': random.randint(90,100)
        }
        

class PredictionModels(Resource):

	def get(self):
		post_meal = bool(request.form['post_meal'])
		blood_sugar_level = int(request.form['blood_sugar_level'])
		breaths_per_minute = int(request.form['breaths_per_minute'])
		is_running = bool(request.form['is_running'])
		breath_shortness_severity = int(request.form['breath_shortness_severity'])
		cough_frequency = int(request.form['cough_frequency'])
		cough_severity = int(request.form['cough_severity'])
		blood_pressure_sys = int(request.form['blood_pressure_sys'])
		blood_pressure_dia = int(request.form['blood_pressure_dia'])
		heart_rate = int(request.form['heart_rate'])
		cholestorol = int(request.form['cholestorol'])
		oxygen_saturation = int(request.form['oxygen_saturation'])


		loaded_model = pickle.load(open('diabetes_prediction_model.sav', 'rb'))
		# loaded_model.predict([100,True])
		diabetes = "No"
		if(loaded_model.predict([[blood_sugar_level,post_meal]]) == 0):
			diabetes="No"
		elif(loaded_model.predict([[blood_sugar_level,post_meal]]) == 0):
			diabetes="PreDiabetes"
		else:
			diabetes="Yes"

		loaded_model = pickle.load(open("bronchi.sav", 'rb'))

		bronchi = "No"
		if(loaded_model.predict([[breaths_per_minute, breath_shortness_severity, cough_frequency,cough_severity]]) == 0):
			bronchi="No"
		else:
			bronchi="Yes"

		loaded_model = pickle.load(open("hypoxemia.sav", 'rb'))
		hypoxemia = "No"
		if(loaded_model.predict([[int(oxygen_saturation)]]) == 0):
			hypoxemia="No"
		else:
			hypoxemia="Yes"

		loaded_model = pickle.load(open("asthma.sav", 'rb'))
		asthma = "No"
		if(loaded_model.predict([[oxygen_saturation, heart_rate,breaths_per_minute] ]) == 0):
			asthma="No"
		else:
			asthma="Yes"

		loaded_model = pickle.load(open("CHD.sav", 'rb'))
		chd = "No"
		if(loaded_model.predict([[blood_pressure_sys,blood_pressure_dia, heart_rate,cholestorol] ]) == 0):
			chd="No"
		else:
			chd="Yes"

		return {"diabetes": diabetes, "bronchi": bronchi,"hypoxemia":hypoxemia, "asthma":asthma, "chd": chd}

	def post(self):		
		post_meal = bool(request.form['post_meal'])
		blood_sugar_level = int(request.form['blood_sugar_level'])
		breaths_per_minute = int(request.form['breaths_per_minute'])
		is_running = bool(request.form['is_running'])
		breath_shortness_severity = int(request.form['breath_shortness_severity'])
		cough_frequency = int(request.form['cough_frequency'])
		cough_severity = int(request.form['cough_severity'])
		blood_pressure_sys = int(request.form['blood_pressure_sys'])
		blood_pressure_dia = int(request.form['blood_pressure_dia'])
		heart_rate = int(request.form['heart_rate'])
		cholestorol = int(request.form['cholestorol'])
		oxygen_saturation = int(request.form['oxygen_saturation'])


		loaded_model = pickle.load(open('diabetes_prediction_model.sav', 'rb'))
		# loaded_model.predict([100,True])
		diabetes = "No"
		if(loaded_model.predict([[blood_sugar_level,post_meal]]) == 0):
			diabetes="No"
		elif(loaded_model.predict([[blood_sugar_level,post_meal]]) == 0):
			diabetes="PreDiabetes"
		else:
			diabetes="Yes"

		loaded_model = pickle.load(open("bronchi.sav", 'rb'))

		bronchi = "No"
		if(loaded_model.predict([[breaths_per_minute, breath_shortness_severity, cough_frequency,cough_severity]]) == 0):
			bronchi="No"
		else:
			bronchi="Yes"

		loaded_model = pickle.load(open("hypoxemia.sav", 'rb'))
		hypoxemia = "No"
		if(loaded_model.predict([[int(oxygen_saturation)]]) == 0):
			hypoxemia="No"
		else:
			hypoxemia="Yes"

		loaded_model = pickle.load(open("asthma.sav", 'rb'))
		asthma = "No"
		if(loaded_model.predict([[oxygen_saturation, heart_rate,breaths_per_minute] ]) == 0):
			asthma="No"
		else:
			asthma="Yes"

		loaded_model = pickle.load(open("CHD.sav", 'rb'))
		chd = "No"
		if(loaded_model.predict([[blood_pressure_sys,blood_pressure_dia, heart_rate,cholestorol] ]) == 0):
			chd="No"
		else:
			chd="Yes"

		return {"diabetes": diabetes, "bronchi": bronchi,"hypoxemia":hypoxemia, "asthma":asthma, "chd": chd}


api.add_resource(OpenAPI, "/")
api.add_resource(PredictionModels, "/prediction_models")

if __name__ == "__main__":
	# app.run(debug=True)
	app.run(host="0.0.0.0", port=5000, debug=True)


