import random
import numpy as np
import csv
import pandas as pd
import random

def randwaka():
  dtype=[("waka","str"),("name","str"),("mean","str")]
  waka_num=4
  data = np.zeros(waka_num,dtype=dtype)

  f=pd.read_csv("waka.csv",header=None,names=["name","waka","meaning"],encoding="shift-jis")
  i=random.randint(0,3)

  return f.loc[i],i