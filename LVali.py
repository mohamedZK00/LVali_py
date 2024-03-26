import pickle
import numpy as np
import sys


loaded_model = pickle.load(open('gbR94.sav', 'rb'))

vpr = loaded_model.predict(np.array([sys.argv[1],sys.argv[2],sys.argv[3]]).reshape(1,-1))
#rint('grade_student',vpr)
predicted_grade = {"vpr": round(vpr[0], 1)}
max_grade=100
predicted_percentage = round((predicted_grade["vpr"] / max_grade) * 100, 1)
formatted_result = "Student grade : {:.1f}%".format(predicted_percentage)
print(formatted_result)







