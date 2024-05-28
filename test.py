from pickle import *

model = load(open("model.pkl","rb"))
model.predict()