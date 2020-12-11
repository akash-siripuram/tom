
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
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
# from pycricbuzz import Cricbuzz
# c=Cricbuzz()
# matches=c.matches()
# for match in matches:
# 	st.write(match)
# 	if (match['mchstate'] != "nextlive"):
# 		  st.write(c.livescore(match['id']))
# 		  st.write(c.commentary(match['id']))
# 		  st.write(c.scoreboard(match['id']))			   
a_type=st.selectbox("Type",["LR","DT","ADABOOST [Recommended]","SVM"])
#st.write("The shape is ",d.shape)
#cl=st.selectbox("Select the number of clusters",[2,3,4,5,6,7,8,9,10])
st.write("This is Version 1")
g,r=0,0

p=-1
j=1
rr=st.radio("Select the cell",("1","2","3","4"))
if a_type=="LR":
	if rr=="1":
		st.write("hello")
					
	if rr=="2":
		a=st.number_input("Enter the Last fist color",value=1,step=1)
		b=st.number_input("Enter the Last second",value=1,step=1)
		c=st.number_input("Enter the last third color",value=1,step=1)
		e=st.number_input("Enter the last fourth color",value=1,step=1)
		f=st.number_input("Enter the last fifth color",value=1,step=1)
		if st.button("Predict 2nd"):
			with st.spinner('In Progress.....'):
				d=pd.read_excel("rd6.xlsx")
				#clf = svm.SVC(kernel="")
				#clf = DecisionTreeClassifier(random_state=0)
				X=d[['A','B','C','D','E']]
				y=d['Y']
				X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)

				#st.write("The shape is ",d.shape)
				clf = LogisticRegression(random_state=0).fit(X, y)
				#st.write("You selected ",s_type)

				p=clf.predict([[a,b,c,e,f]])
				if p%2==0:
					#r=r+1
					st.success("Next is GREEN")
				elif p%2==1:
					#g=g+1
					st.error("Next is RED")
	if rr== "3":
		a=st.number_input("Enter the Last fist color",value=1,step=1)
		b=st.number_input("Enter the Last second",value=1,step=1)
		if st.button("Predict 3rd"):
			with st.spinner('In Progress....'):
				d=pd.read_excel("rd3.xlsx")
				#clf = svm.SVC(kernel="")
				#clf = DecisionTreeClassifier(random_state=0)
				X=d[['A','B']]
				y=d['Y']
				X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)

				#st.write("The shape is ",d.shape)
				clf = LogisticRegression(random_state=0).fit(X, y)
				#st.write("You selected ",s_type)

				p=clf.predict([[a,b]])
				if p%2==0:
					#r=r+1
					st.success("Next is GREEN")
				elif p%2==1:
					#g=g+1
					st.error("Next is RED")
					
	if rr=="4":	
		a=st.number_input("Enter the Last fist color",value=1,step=1)
		b=st.number_input("Enter the Last second",value=1,step=1)
		c=st.number_input("Enter the last third color",value=1,step=1)
		if st.button("Predict 4th"):
			with st.spinner('In Progress..'):
				d=pd.read_excel("rd4.xlsx")
				#clf = svm.SVC(kernel="")
				#clf = DecisionTreeClassifier(random_state=0)
				X=d[['A','B','C']]
				y=d['Y']
				X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)

				#st.write("The shape is ",d.shape)
				clf = LogisticRegression(random_state=0).fit(X, y)
				#st.write("You selected ",s_type)

				p=clf.predict([[a,b,c]])
				if p%2==0:
					#r=r+1
					st.success("Next is GREEN")
				elif p%2==1:
					#g=g+1
					st.error("Next is RED")					
				#if g>r:
					#st.success("Next is GREEN - {} %".format((g/5)*100))
				#else:
					#st.error("Next is RED - {} %".format((r/5)*100))
elif a_type=="ADABOOST [Recommended]":
	a=st.number_input("Enter the Last Period last digit",value=1,step=1)
	b=st.number_input("Enter the Last Price last digit",value=1,step=1)
	with st.spinner('In Progress...'):
			d=pd.read_excel("Emerd_n.xlsx")
			clf = DecisionTreeClassifier(random_state=0)
			X=d[['A','B','C']]
			y=d['Y']
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)

			#st.write("The shape is ",d.shape)
			abc = AdaBoostClassifier(n_estimators=100,learning_rate=3,base_estimator=clf)
			# Train Adaboost Classifer
			model = abc.fit(X_train, y_train)
			#Predict the response for test dataset
			y_pred = model.predict([[a,b,a+1]])
			p=y_pred[0]

			if p==0:
				#r=r+1
				st.error("Next is RED")
			elif p==1:
				#g=g+1
				st.success("Next is GREEN")							
			#if g>r:
				#st.success("Next is GREEN - {} %".format((g/5)*100))
			#else:
				#st.error("Next is RED - {} %".format((r/5)*100))


elif a_type=="SVM":
	if st.button("Classify"):
		a=st.number_input("Enter the Last Period last digit",value=1,step=1)
		b=st.number_input("Enter the Last Price last digit",value=1,step=1)
		with st.spinner('In Progress...'):
			d=pd.read_excel("Emerd_n.xlsx")
			clf = svm.SVC(kernel="")
			#clf = DecisionTreeClassifier(random_state=0)
			X=d[['A','B','C']]
			y=d['Y']
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)

			#st.write("The shape is ",d.shape)
			clf.fit(X_train,y_train)
			#st.write("You selected ",s_type)

			p=clf.predict([[a,b,a+1]])
			if p==0:
				#r=r+1
				st.error("Next is RED")
			elif p==1:
				#g=g+1
				st.success("Next is GREEN")							
			#if g>r:
				#st.success("Next is GREEN - {} %".format((g/5)*100))
			#else:
				#st.error("Next is RED - {} %".format((r/5)*100))
elif a_type=="DT":
	a=st.number_input("Enter the Last Period last digit",value=2,step=1)
	b=st.number_input("Enter the Last Price last digit",value=2,step=1)
	if st.button("Classify"):
		with st.spinner('In Progress...'):
			d=pd.read_excel("Emerd_n.xlsx")
			#clf = svm.SVC()
			clf = DecisionTreeClassifier(random_state=0)
			X=d[['A','B','C']]
			y=d['Y']
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.001)

			#st.write("The shape is ",d.shape)
			clf.fit(X,y)
			#st.write("You selected ",s_type)

			p=clf.predict([[a,b,a+1]])
			if p==1:
				#r=r+1
				st.error("Next is RED")
			elif p==0:
				#g=g+1
				st.success("Next is GREEN")						
			#if g>r:
				#st.success("Next is GREEN - {} %".format((g/5)*100))
			#else:
				#st.error("Next is RED - {} %".format((r/5)*100))



