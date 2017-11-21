import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle



def pred(my_list):
    #print(my_list.shape())
    filename= '/home/sahil/Desktop/urlshortner/urlshortner/shortner/best_model.sav'
    #r=open(filename,'rb')
    #filename=filename.encode('utf-8')
    best_model = pickle.load(open(filename,'rb'),encoding='latin1')
    list2=[]
    list2.append(my_list)
    ans=np.asarray(list2)
    #ans.reshape(-1,1)

    value= best_model.predict_proba(ans)
    return value
    # if value[0]==1:
	   #  print('Phishing')
    # else:
	   #  print('Safe')