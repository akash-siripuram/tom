import streamlit as st
import numpy as np
from sklearn import preprocessing
import pandas as pd
#from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split



d=pd.read_excel("Mann.xlsx")
#st.write("The shape is ",d.shape)
d1=d[:4571]
d2=d[4571:9142]
d3=d[9142:13713]
d4=d[13713:18284]
d5=d[18284:22855]
d6=d[22855:27426]
d7=d[27426:]
lis=[d1,d2,d3,d4,d5,d6,d7]
#cl=st.selectbox("Select the number of clusters",[2,3,4,5,6,7,8,9,10])
a=st.number_input("Enter the Last Period last digit",value=2,step=1)
b=st.number_input("Enter the Last Price last digit",value=2,step=1)
c=st.number_input("Enter the Next Period last digit(You want to predict)",value=2,step=1)
g,r=0,0

p=-1
j=1
if a is None or b is None or c is None:
		st.print("")
else:
	s_type=st.selectbox("Type",["Normal","Reverse"])
	if s_type =="Normal":
		if st.button("Classify"):
			with st.spinner('In Progress...'):
				clf = svm.SVC()
				for i in lis:
					X=i[['A','B','C']]
					y=i['Y']
					X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
					#st.write("The shape is ",d.shape)
					clf.fit(X_train,y_train)
					p=clf.predict([[a,b,c]])
					if p==0:
						r=r+1
						#st.write("RED",j)
						j=j+1
					elif p==1:
						g=g+1
						#st.write("GREEN",j)
						j=j+1
				if r>g:
					st.error("Next is RED {}".format((r/7)*100))
				else:
					st.success("Next is GREEN {}".format((g/7)*100))
				with st.spinner('Checking Violet In Progress...'):
					clf = svm.SVC()
					d=pd.read_excel("violet.xlsx")
					#st.write("The shape is ",d.shape)
					d1=d[:1857]
					d2=d[1857:3714]
					d3=d[3714:5571]
					d4=d[5571:7428]
					d5=d[7428:9285]
					d6=d[9285:11142]
					d7=d[11142:]
					lis=[d1,d2,d3,d4,d5,d6,d7]
					v,o=0,0
					for i in lis:
						X=i[['A','B','C']]
						y=i['Y']
						X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
						#st.write("The shape is ",d.shape)
						clf.fit(X_train,y_train)
						p=clf.predict([[a,b,c]])
						if p==0:
							o=o+1
							#st.write("Other",j)
							j=j+1
						elif p==1:
							v=v+1
							#st.write("Violet",j)
							j=j+1
					if v>o:
						st.success("Next is Violet {}".format((v/7)*100))
					else:
						st.warning("Next is Other Color {}".format((o/7)*100))	
	elif s_type=="Reverse":
		if st.button("Classify"):
				with st.spinner('In Progress...'):
					clf = svm.SVC()
					for i in lis:
						X=i[['A','B','C']]
						y=i['Y']
						X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
						#st.write("The shape is ",d.shape)
						clf.fit(X_train,y_train)
						p=clf.predict([[a,b,c]])
						if p==0:
							g=g+1
							#st.write("GREEN",j)
							j=j+1
						elif p==1:
							r=r+1
							#st.write("RED",j)
							j=j+1
					if r>g:
						st.error("Next is RED {}".format((r/7)*100))
					else:
						st.success("Next is GREEN {}".format((g/7)*100))	
					with st.spinner('Checking Violet In Progress...'):
						clf = svm.SVC()
						d=pd.read_excel("violet.xlsx")
						st.write("The shape is ",d.shape)
						d1=d[:1857]
						d2=d[1857:3714]
						d3=d[3714:5571]
						d4=d[5571:7428]
						d5=d[7428:9285]
						d6=d[9285:11142]
						d7=d[11142:]
						lis=[d1,d2,d3,d4,d5,d6,d7]
						v,o=0,0
						for i in lis:
							X=i[['A','B','C']]
							y=i['Y']
							X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
							#st.write("The shape is ",d.shape)
							clf.fit(X_train,y_train)
							p=clf.predict([[a,b,c]])
							if p==0:
								o=o+1
								#st.write("Other",j)
								j=j+1
							elif p==1:
								v=v+1
								#st.write("Violet",j)
								j=j+1
						if v>o:
							st.success("Next is Violet {}".format((v/7)*100))
						else:
							st.warning("Next is Other Color {}".format((o/7)*100))				
