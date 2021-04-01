import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()




# clean_doc=pickle.load(open('clean_doc.obj','rb'))
tfidf= pickle.load(open('Tfidfmodels.pkl','rb'))
model=pickle.load(open('kmeanmodel.pkl','rb'))
df_news_papers= pd.read_csv('https://raw.githubusercontent.com/npatos/datamining_assignment_4/main/combined_news_papers_fetched_data.csv')
      
# front end elements of the web page 
html_temp = """ 
<div style ="background-color:gray;padding:13px"> 
<h1 style ="color:white;text-align:center;">NEWS CLASSIFICATION APP</h1> 
</div> 
""" 
st.markdown(html_temp, unsafe_allow_html = True) 
default_value_goes_here = ""
article = st.text_area("Enter Your article title here", default_value_goes_here)
result =""
df_news_papers= pd.read_csv('https://raw.githubusercontent.com/npatos/datamining_assignment_4/main/combined_news_papers_fetched_data.csv')
df_news_papers["News_Page"] = le.fit_transform(df_news_papers[["News_Page"]])  
# when 'Predict' is clicked, make the prediction and store it 
if st.button("Predict"): 
  pred = model.predict(tfidf.transform([article]))
  if pred==1:
    st.write('Entertainment')   
    pred= int(pred)
    data_pred = df_news_papers.loc[(df_news_papers['News_Page'] == pred)]
    st.dataframe(data_pred['Source_URL'].unique())
  elif pred==0:
    st.write('Business')
    term="Business"
    pred= int(pred)
    data_pred = df_news_papers.loc[(df_news_papers['News_Page'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.dataframe(data_pred['Source_URL'].unique())
  elif pred==2:
    st.write('Politics') 
    pred= int(pred)
    term="Politics"
    pred= int(pred)
    data_pred = df_news_papers.loc[(df_news_papers['News_Page'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.dataframe(data_pred['Source_URL'].unique())
  elif pred==3:
    st.write('Sport')
    pred= int(pred)
    term='Sport'
    data_pred = df_news_papers.loc[(df_news_papers['News_Page'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.dataframe(data_pred['Source_URL'].unique())

