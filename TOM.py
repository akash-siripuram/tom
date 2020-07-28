import streamlit as st
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



d=pd.read_excel("Mann.xlsx")

st.write("The shape is ",d.shape)

#cl=st.selectbox("Select the number of clusters",[2,3,4,5,6,7,8,9,10])
a=st.number_input("Enter the Last Period last digit",value=2,step=1)
b=st.number_input("Enter the Last Price last digit",value=2,step=1)
c=st.number_input("Enter the Next Period last digit(You want to predict)",value=2,step=1)
g,r=0,0


if a is None or b is None or c is None:
		st.print("")
else:
	if st.button("Get Result"):	
		with st.spinner('In Progress...'):
			for i in range(2,11):
				kmeans = KMeans(n_clusters=i, random_state=0).fit(d)
				a=kmeans.predict([[a,b,c]])
				if a[0]%2==0:
					g=g+1
				else:
					r=r+1


if g>r:
	st.success("Next is green")
else:
	st.error("Next is Red")

















