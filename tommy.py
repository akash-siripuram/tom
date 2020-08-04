import streamlit as st
import numpy as np
from sklearn import preprocessing
import pandas as pd
#from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import sklearn



s_type=st.selectbox("Type",["Emerd"])
#st.write("The shape is ",d.shape)
#cl=st.selectbox("Select the number of clusters",[2,3,4,5,6,7,8,9,10])
a=st.number_input("Enter the Last Period last digit",value=2,step=1)
b=st.number_input("Enter the Last Price last digit",value=2,step=1)
#c=st.number_input("Enter the Next Period last digit(You want to predict)",value=2,step=1)
g,r=0,0

p=-1
j=1
if a is None or b is None:
		st.print("")
else:
	
	if s_type=="Emerd":
		if st.button("Classify"):
			with st.spinner('In Progress...'):
				d=pd.read_excel("Emerd_n.xlsx")
				clf = svm.SVC()
				#clf = DecisionTreeClassifier(random_state=0)
				X=d[['A','B','C']]
				y=d['D']
				X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)
				for i in range(0,5):
				#st.write("The shape is ",d.shape)
					clf.fit(X_train,y_train)
					#st.write("You selected ",s_type)
					p=clf.predict([[a,b,a+1]])
					if p==0:
						r=r+1
						#st.error("Next is RED")
					elif p==1:
						g=g+1
						#st.success("Next is GREEN")							
				if g>r:
					st.success("Next is GREEN")
				elif r>g:
					st.error("Next is RED")

