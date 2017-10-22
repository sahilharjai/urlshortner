import numpy as np
import pandas as pd
import pickle

filename= '/home/sahil/Desktop/urlshortner/urlshortner/shortner/best_model.sav'

best_model = pickle.load(open(filename, 'rb'))

print(best_model.feature_importances_)

def pred(my_list):
    ans=np.asarray(my_list)
    value= best_model.predict_proba(ans)
    return(value)
    # if value[0]==0:
	   #  print('Safe')
    # else:
	   #  print('Phishing')