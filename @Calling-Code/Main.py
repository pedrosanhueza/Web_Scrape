## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st
import streamlit.components.v1 as components # embed website
import pandas as pd # panel data

from datetime import datetime, timedelta
import time

import pytz
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px
from plotly.figure_factory import create_distplot

import os

st.set_option('deprecation.showPyplotGlobalUse', False)

## ----------------------------------------- Introduction ----------------------------------------------------------------------------- ##

st.markdown('''
<h1 style="font-size:40px;text-align:center;">
   Hi!
</h1>
<p style="font-size:20px;text-align:center;">
   Here is a list of projects where I extract (live) data from various websites, and share the scraping code.
   With the data, I do a simple analysis.
   <br>
   Regression models, predictory ML/AI, EDA, and more ...
</p>
''',unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,3,1])
with col1:
    st.write(' ')
with col2:
   st.image('@Calling-Code/Pictures/Me_sticker.png', caption='Profile Sticker') 
with col3:
    st.write(' ')

st.markdown('''
<p style="font-size:20px;text-align:center;">
   Projects are listed in the drop down bar. Each project has:
   <sup> 1 </sup> A code source, an
   <sup> 2 </sup> embedded website or the website hyperlink, and a
   <sup> 3 </sup> table with data extracted.
</p>
''',unsafe_allow_html=True)

st.markdown('''
<p style="font-size:12px;text-align:left;color:rgba(192,192,192,0.3);">
         (1) Some projects extracted underlying data through requests, API, and/or Web Drivers. <br>
         (2) Not all websites allow embedding. <br>
         (3) Display extractiong underlying HTML and, with it, data stored in a database. <br>
</p>
''',unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.5,3,1.5])
with col1:
    st.write(' ')
with col2:
   st.image('@Calling-Code/Pictures/API_call_3.gif') 
with col3:
    st.write(' ')
   
st.markdown('''<hr>''',unsafe_allow_html=True)



## ----------------------------------------- Beggin Side Bar ----------------------------------------------------------------------------- ##

projectOption = {
   'TEST':1,
   'BYU-Idaho Class Catalog':2,
   'Phone Country Code':3,
   'Fifa Soccer 2022':4,
   'Stocks - ADVFN':5,
   'Billionaires - Forbes':6,
   'Universities - Forbes':7,
   'Irvine Spectrum Center - Stores':8,
   'BYU-Idaho Student Employment':9,
   'Mutual App Feedback':10,
   'News - CBS':11,
   'Politicos Chilenos':12,
   'Políticos Españoles':13,
   'SINCA MMA Gob':14,
   'Surplus Store - BYUI':15,
   'Representatives - USA':16,
   'Boat Trader':17}

projects = tuple(projectOption.keys())

project = st.selectbox('Select project: ', projects)

## ----------------------------------------- General Variables ------------------------------------------------------------------------ ##

project_order = list(projectOption.values())

IdahoTz = pytz.timezone('US/Mountain') 
timeZoneMountain = datetime.now(IdahoTz)
currentTimeInRexburg = timeZoneMountain.strftime("%Y-%m-%d")
YesterdayTimeInRexburg = (timeZoneMountain - timedelta(1)).strftime("%Y-%m-%d")

## ----------------------------------------- TEST ------------------------------------------------------------------------ ##
if projectOption[project] == 1:
   st.write(project)

   url1 = 'https://www.boattrader.com/boat-dealers/'
   url5 = 'https://www.irvinespectrumcenter.com/shopping/stores'
   url7 = 'https://www.cbsnews.com/world/'
   url11= 'https://web.byui.edu/SurplusList/'
   url12= 'https://www.byui.edu/catalog#/courses'


   components.iframe(f"{url1}", width=350, height=500, scrolling=True)
   components.iframe(f"{url5}", width=350, height=500, scrolling=True)
   components.iframe(f"{url7}", width=350, height=500, scrolling=True)
   components.iframe(f"{url11}",width=350, height=500, scrolling=True)
   components.iframe(f"{url12}",width=350, height=500, scrolling=True)

## ----------------------------------------- Class Catalog - BYUI ------------------------------------------------------------------------ ##
if projectOption[project] == 2:
   from Projects._2_BYUI_ClassCatalog import catalogBYUI
   url = catalogBYUI.url_display
   data = catalogBYUI.data
   script_1 = catalogBYUI.script_1

   st.markdown(f'''
   <br><p style="font-size:20px;text-align:left;color:black;">
      Extracting data from: 
      <a style="color:#4F9ACF; padding:7px 10px;" target="_blank" href = '{url}'> Class Catalog - BYUI </a>
   </p><br>
   ''',unsafe_allow_html=True)

   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("See Website 👨🏻‍💻"):
      components.iframe(f"{url}",width=1000, height=500, scrolling=True)
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
      
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'Class_Catalog_BYUI.csv',
         mime      =    'text/csv',)
      
      st.dataframe(data)
   
   st.markdown(f'''
      <br>
         <p style="font-size:20px;text-align:Center;color:black;"> Description: </p>
         <p style="font-size:12px;text-align:Center;color:black;">
            Simple
         </p>
      <br>
   ''',unsafe_allow_html=True)

   

# ## ----------------------------------------- # Country Code ------------------------------------------------------------------------ ##
if projectOption[project] == 3:
   from Projects._3_CountryCode import countryCode
   
   url = countryCode.url
   
   st.write(url)

   data = countryCode.data
   st.dataframe(data)

# ## ----------------------------------------- FIFA World Cup ------------------------------------------------------------------------ ##
if projectOption[project] == 4:
   from Projects._4_FIFAWorldCup import FIFAWorldCup
   st.write(FIFAWorldCup.url)
   data = FIFAWorldCup.data
   st.dataframe(data)

#    data_main = data.copy()
   
#    countries = ('All Countries',) + tuple(data.Country.unique())
#    country_selected = st.sidebar.selectbox("Countries",countries)

#    positions = ('All Positions',) + tuple(data.POS.unique())
#    position_selected = st.sidebar.selectbox("Positions",positions)

#    if country_selected != 'All Countries':
#       data_main = data[data.Country == country_selected]
#       url_pic_country = data_main.Country_logo.iloc[0]

#    if position_selected != 'All Positions':
#       data_main = data[data.POS == position_selected]
#       url_pic_country = data_main.Country_logo.iloc[0]

#    if (country_selected != 'All Countries') and (position_selected != 'All Positions'):
#       data_main = data[(data.POS == position_selected) & (data.Country == country_selected)]
   
#    if (country_selected == 'All Countries') and (position_selected != 'All Positions'):
#       data_main = data[data.POS == position_selected]
   
#    url_pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Easports_fifa_logo.svg/800px-Easports_fifa_logo.svg.png'
   
#    st.image(f"{url_pic}",width=400)

#    Players_avg = round(1 - data_main.shape[0] / (data.shape[0] / data.Country.nunique())  - 1,2)
#    Age_avg =     round(1 - data.AGE.mean() / data[data.Country == country_selected].AGE.mean(),2)
#    HT_avg =      round(1 - data.HT.mean()  / data[data.Country == country_selected].HT.mean() ,2)
#    WT_avg =      round(1 - data.WT.mean()  / data[data.Country == country_selected].WT.mean() ,2)
#    BMI_avg =     round(1 - data.BMI.mean()  / data[data.Country == country_selected].BMI.mean(),2)

#    tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Table', 'Code', 'Analysis'])

#    with tab1:
#       col2, col3, col4, col5, col6 = st.columns(5)
#       if country_selected == 'All Countries':
#          col2.metric("Players",    round(data_main.shape[0]))
#          col3.metric("Age Avg",    round(data_main.AGE.mean()))
#          col4.metric("Height Avg", round(data_main.HT.mean()))
#          col5.metric("Weight Avg", round(data_main.WT.mean()))
#          col6.metric("BMI Avg",    round(data_main.BMI.mean()))
#       else:
#          col2.metric("Players",    round(data_main.shape[0]), str(Players_avg) + '%')
#          col3.metric("Age Avg",    round(data_main.AGE.mean()), str(Age_avg) + "%")
#          col4.metric("Height Avg", round(data_main.HT.mean()), str(HT_avg)  + "%")
#          col5.metric("Weight Avg", round(data_main.WT.mean()), str(WT_avg)  + "%")
#          col6.metric("BMI Avg",    round(data_main.BMI.mean()), str(BMI_avg) + "%")

#          st.image(f"{url_pic_country}",width=400)

#    with tab2:
#       if (country_selected != 'All Countries' or position_selected != 'All Positions'):
#          st.dataframe(data_main.drop('Country_logo', axis=1))
#       else:
#          st.dataframe(data.drop('Country_logo', axis=1))
#    with tab3:
#       st.header('Code for live data extraction')
#       st.write('Runs every time you load the page and updates the table')
#       st.code(FIFAWorldCup.script, language="python")
#    with tab4:
#       st.header(option)

## ----------------------------------------- Financial Data ------------------------------------------------------------------------ ##
# if projectOption[project] == 5:
#    # from Projects._5_Financial Data import 
#    st.write(.url)
#    data = .data
#    st.dataframe(data)

## ----------------------------------------- Forbes Billionaires ------------------------------------------------------------------------ ##
if projectOption[project] == 6:
   from Projects._6_ForbesBillionaries import forbesBillionaires
   st.write(forbesBillionaires.url_main)
   data = forbesBillionaires.data
   st.dataframe(data)

## ----------------------------------------- Forbes Universities ------------------------------------------------------------------------ ##
if projectOption[project] == 7:
   from Projects._7_ForbesUniversities import Forbes_Universities
   st.write(Forbes_Universities.url_main)
   data = Forbes_Universities.data
   st.dataframe(data)

## ----------------------------------------- Irvine Spectrum Center ------------------------------------------------------------------------ ##
if projectOption[project] == 8:
   from Projects._8_IrvineSpectrumCenter import irvinespectrumcenter
   st.write(irvinespectrumcenter.url_main)
   data = irvinespectrumcenter.data
   st.dataframe(data)

# ## ----------------------------------------- Job Board - BYUI ------------------------------------------------------------------------ ##
# if projectOption[project] == 9:
   # from Projects._9_BYUI_JobBoard import BYUI_JobBoard
#    st.write(project)
   
#    st.markdown('''
#    <p style="text-align:right;">
#       Author: Pedro Sanhueza
#    </p>
   
#    <center>
#       <h1 style="color:#214491;font-size: 90px;">
#          BYU-I
#          <br>
#          Job Board 
#       </h1>
#    </center>
   
#    <br>
#   ''',unsafe_allow_html=True)

#    data = BYUI_JobBoard.data
   
#    d = str(datetime.today().strftime("%Y-%m-%d"))

#    KPI1_jobs = round(1-(400/data.shape[0]),2)

#    KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

#    today_data = data[data.dateUpdated >= currentTimeInRexburg]

#    today = today_data.shape[0]

#    yesterday_data = data[data.dateUpdated == (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")]

#    yesterday = yesterday_data.shape[0]

#    KPI1, KPI2, KPI3, KPI4 = st.columns(4)

#    KPI1.metric('Jobs Published', f"{data.shape[0]}")

#    KPI2.metric("Departments Recluting", f"{data.departmentName.nunique()}")

#    KPI3.metric("Jobs Posted Today",today)

#    KPI4.metric("Highest Pay Rate Job", f"${data.payRate.max()}")

#    st.markdown('''
#    <br>
#    <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#       Highest Paid Jobs
#    </p>
#    <br>
#    ''',unsafe_allow_html=True)

#    Njobs = st.slider('Select a range of jobs', 1, 10, 5)

#    data_topPayRate = data.sort_values('payRate', ascending=False).head(Njobs)[['title','payRate','departmentName','managerName','URL']]
   
#    data_topPayRate.columns = ['Job Title','Hourly Wage','Department','Employer','Application Link']

#    st.dataframe(data_topPayRate.reset_index().drop('index',axis=1))

#    if today > 0:

#       st.markdown(f'''
#       <br>
#       <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#          Jobs Posted Today
#       </p>
#       <p style="text-align:center;color:#4F9ACF;">
#          {currentTimeInRexburg}
#       </p>
#       <br>
#       ''',unsafe_allow_html=True)

#       st.dataframe(today_data[['title','payRate','departmentName','managerName','URL']].sort_values('payRate',ascending=False))
#    elif yesterday > 0:
#       st.markdown(f'''
#       <br>
#       <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#          Jobs Posted Yesterday
#       </p>
#       <p style="text-align:center;color:#4F9ACF;">
#          {YesterdayTimeInRexburg}
#       </p>
#       <br>
#       ''',unsafe_allow_html=True)

#       st.dataframe(yesterday_data[['title','payRate','departmentName','managerName','URL']].sort_values('payRate',ascending=False))

#    st.markdown('''
#    <br>
#    <p style="font-size:40px;text-align:center;color:#4F9ACF;">
#       Pay Rate Distribution
#    </p>
#    <br>
#    ''',unsafe_allow_html=True)

#    col1, col2 = st.columns([4,1])

#    with col2:
#       job_type = st.radio("Job Type", ('All','Online','On-Campus'))
      
#       if job_type == 'Online':
#          data_isOnline = data[data.isOnline == True]
#       elif job_type == 'On-Campus':
#          data_isOnline = data[data.isOnline == False]
#       else:
#          data_isOnline = data.copy()

#    with col1:   
#       sns.kdeplot(data_isOnline.payRate, shade=True, color="#214491", bw=0.8, alpha=0.5, cut=0)
#       fig1 = plt.show()
#       st.pyplot(fig1)

#    tab1, tab2 = st.tabs(['Data','Code'])

#    with tab1:
#       columns_ls = st.multiselect(
#       '',
#       data.columns,
#       ['title', 'payRate','managerName'])

#       st.dataframe(data[columns_ls])

#       @st.cache
#       def convert_df(df):
#          # IMPORTANT: Cache the conversion to prevent computation on every rerun
#          return df.to_csv().encode('utf-8')

#       csv = convert_df(data)

#       file_name = 'BYUI_jobBoard_' + str(time.strftime("%Y-%m-%d"))

#       st.download_button(
#          label = "Download data as CSV",
#          data = csv,
#          file_name = file_name,
#          mime = 'text/csv')

#    with tab2:

#       st.markdown(f'''
#       <br>
#       <p style="font-size:20px;text-align:center;color:#4F9ACF;">
#          🐍 Source Code
#       </p>
#       <a style="color:#4F9ACF; padding:7px 10px;"
#          target="_blank" 
#          href = 'https://github.com/pedrosanhueza/Web_Scrape/blob/main/BYUI_JobBoard/Job_board-Code/API-call-JobBoard.ipynb'>
#          GitHub Repository
#       </a>
#       <br>
#       ''',unsafe_allow_html=True)

#       st.code(BYUI_JobBoard.script1, language='python')
   
   # with tab1:
   #    col1, col2, col3 = st.columns(3)

   #    with col1:
   #       st.write('')
   #    with col2:
   #       st.write(data.payRate.max(), 12,13)
   #    with col3:
   #       st.write('')

   # with tab2:
   #    jobs_to_remove = ['TA','Custodian','Online','Grounds']
   #    jobs_to_remove_str = '|'.join(jobs_to_remove)   
   #    st.write('Personalised Table')
   #    data_p = data[~data.title.str.contains(jobs_to_remove_str)].sort_values('payRate', ascending=False)[['title','payRate','workSchedule','URL']]
   #    st.dataframe(data_p)
      
   #    sns.kdeplot(data.payRate, shade=True, color="g", bw=0.94, alpha=0.5, cut=0)
   #    fig1 = plt.show()
   #    st.pyplot(fig1)

   # with tab3:
   #    st.dataframe(BYUI_JobBoard.data)

   # with tab4:
   #    st.code(BYUI_JobBoard.script1)

   # sns.kdeplot(data.payRate, shade=True, color="g", bw=0.8, alpha=0.5, cut=0)

   # fig1 = plt.show()

   # st.pyplot(fig1)

   # if st.button('Personalised Table'):
   #    jobs_to_remove = ['TA','Custodian','Online','Grounds']
   #    jobs_to_remove_str = '|'.join(jobs_to_remove)   
   #    st.write('Personalised Table')
   #    data_p = data[~data.title.str.contains(jobs_to_remove_str)].sort_values('payRate', ascending=False)[['title','payRate','workSchedule','URL']]
   #    st.table(data_p)

   # if st.button("ballons"):
   #    st.balloons()
   
   # if st.button("info"):
   #    st.info('This is a purely informational message', icon="ℹ️")

## ----------------------------------------- Mutual App Feedback ------------------------------------------------------------------------ ##
   
if projectOption[project] == 10:
   import altair as alt
   from Projects._10_MutualAppFeedback import Mutual_App_Feedback
   
   data = Mutual_App_Feedback.data
   logo = Mutual_App_Feedback.logo
   scrpt_1 = Mutual_App_Feedback.script_1
   fig1 = Mutual_App_Feedback.fig_1

   st.markdown(f'''
   <center>
      <br>
      <img src="{logo}">
      <br>
      <br>
      <br>
   </center>
   ''',unsafe_allow_html=True)

   tab1, tab2, tab3 = st.tabs(["Analysis 🧐", "Script 🐍","Table 🥩"])

   with tab1:
      col1, col2, col3, col4 = st.columns(4)
      col1.metric("Total Suggestions", f"{data.id.count()}")
      col2.metric("Suggestions Completed",f"{data.status.str.contains('Close').sum()}")
      col3.metric("New Features",f"{data.status.str.contains('Released').sum()}")
      col4.metric("Highest Interact Month", f"{data.date_created_month.value_counts().index[0]}")

   with tab2:
      st.markdown('''
         <center>
            <h1 style="color:black; font-size:30px;">
               Getting the date from one page
            </h1>
         </center>
         <br>
      ''',unsafe_allow_html=True)
      st.code(scrpt_1)
   with tab3:
      st.dataframe(data)

## ----------------------------------------- News CBS ------------------------------------------------------------------------ ##
if projectOption[project] == 11:
   from Projects._11_NewsCBS import cbsnews
   st.write(cbsnews.url)
   data = cbsnews.data
   st.dataframe(data)

## ----------------------------------------- Politicos Chilenos - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 12:
   from Projects._12_PoliticosChilenos.camara_diputados import url_main
   st.write(url_main)

   from Projects._12_PoliticosChilenos.camara_diputados import data_simple   
   data_1 = data_simple
   st.dataframe(data_1)

   # if st.button('Run Complete table'):
   #    from Projects._12_PoliticosChilenos.camara_diputados import data
   #    data_2 = data
   #    st.dataframe(data_2)

## ----------------------------------------- Politicos Españoles - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 13:
   from Projects._13_PoliticosEspanoles import DiputadosEspanoles
   st.write(DiputadosEspanoles.url_main)
   data = DiputadosEspanoles.data
   st.dataframe(data)

## ----------------------------------------- Politicos Españoles - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 14:
   from Projects._14_SINCAMMAGob import SINCAMMAGob
   st.write(SINCAMMAGob.url_main)
   data = SINCAMMAGob.data
   st.dataframe(data)

## -----------------------------------------  ------------------------------------------------------------------------ ##
if projectOption[project] == 15:
   from Projects._15_BYUI_SurplusStore import SurplusStore

   st.write(SurplusStore.url)
   data = SurplusStore.data

   st.markdown('''
      <p style="text-align:right;">
         Author: Pedro Sanhueza
      </p>

      <center>
         <h1 style="color:#214491;font-size: 90px;">
            BYU-I
            <br>
            Surplus Store
         </h1>
      </center>

      <br>
   ''',unsafe_allow_html=True)

   highest_price = '$' + str( round(data.Price.max(),2))
      
   price_mean = '$' + str( round(data.Price.mean(),2) )

   excellent_items = str(data[data.Condition == 'Excellent'].shape[0]) + ' Items'

   KPI1, KPI2, KPI3, KPI4 = st.columns(4)
  
   KPI1.metric('Items in Store', f"{data.shape[0]}")

   KPI2.metric('Higher Price Item', f"{highest_price}")

   KPI3.metric('Average Price', f"{price_mean}")

   KPI4.metric('Excellent Condition', f"{excellent_items}")

   st.dataframe(data)

   # names = data['Condition'].value_counts().reset_index()['index']

   # values = data['Condition'].value_counts().reset_index()['Condition']
   
   st.line_chart(data[['Condition']])

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
if projectOption[project] == 16:
   st.write(project)
   from Projects._16_USHouseRepresentatives import representatives

   # data = representatives.rows
   # st.dataframe(data)
   data = representatives.data
   st.dataframe(data)



   # st.markdown('''
   #    <p style="text-align:right;">
   #       Author: Pedro Sanhueza
   #    </p>

   #    <center>
   #       <h1 style="color:#214491;font-size: 90px;">
   #          UNITED STATES
   #          <br>
   #          HOUSE of
   #          <br>
   #          REPRESENTATIVES
   #       </h1>
   #    </center>

   #    <br>
   # ''',unsafe_allow_html=True)

   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       <b> Part 1/3: </b>
   #       Web Scraping Data Extraction 🐍
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

   # st.code(representatives.script1, language='python')
   
   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       Code Extraction Output
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

   # st.dataframe(data)

   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       <b> Part 2/3: </b>
   #       Explanatory Data Analysis
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

   # data_melt_committee = data.copy()
   # data_melt_committee[[0,1,2,3,4,5]] = data['Committee Assignment'].str.split('|',expand=True)
   # data_melt_committee.drop('Committee Assignment',axis=1, inplace=True)
   # data_melt_committee = data_melt_committee.melt(id_vars=['District','Name','Party','Office Room','Phone','State'],value_name='Committee Assignment')
   # data_melt_committee = data_melt_committee[~data_melt_committee['Committee Assignment'].isnull()].drop('variable',axis=1)

   # KPI1,KPI2,KPI3,KPI4,KPI5 = st.columns(5)
   # KPI1.metric('Districts', f"{data.District.nunique()}")
   # KPI2.metric('Representatives', f"{data.Name.nunique()}")
   # KPI3.metric('Parties', f"{data.Party.nunique()}")
   # KPI4.metric('Committees', f"{data_melt_committee['Committee Assignment'].nunique()}")
   # KPI5.metric('States', f"{data.State.nunique()}")

   # newnames = {'R':'Republicans','D':'Democrats'}
   # fig = px.pie(data['Party'].replace(newnames),names='Party',color='Party',color_discrete_map={'Republicans':'Red','Democrats':'Blue'})
   # fig.update_traces(textfont_size=22,textinfo='percent+value')
   # fig.update_layout(legend=dict(
   #  orientation="h",
   #  yanchor="bottom",
   #  y=1.02,
   #  xanchor="right",
   #  x=0.67))
   # st.plotly_chart(fig,use_container_width=True)

   # st.bar_chart(data.State.value_counts().reset_index(), y='State',x='index')

   # party_group = st.radio("Representative Members by State",('Both','Republicans','Democrats'), horizontal=True)

   # if party_group == 'Republicans':
   #    fig = px.bar(data[data.Party=='R'],x='State',color='Party',color_discrete_map={'R': 'red'},width=900,height=400,labels={'count': 'Amount'})
   #    fig.update_layout(xaxis={'categoryorder':'total descending'})
   #    fig.update_xaxes(tickangle=-45)
   #    newnames = {'R':'Republicans'}
   #    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   #    st.plotly_chart(fig)

   # elif party_group == 'Democrats':
   #    fig = px.bar(data[data.Party=='D'],x='State',color='Party',color_discrete_map={'D': 'Blue'},width=900,height=400,labels={'count': 'Amount'})
   #    fig.update_layout(xaxis={'categoryorder':'total descending'})
   #    fig.update_xaxes(tickangle=-45)
   #    newnames = {'D':'Democrats'}
   #    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   #    st.plotly_chart(fig)
   
   # elif party_group == 'Both':
   #    fig = px.bar(data,x='State',color='Party',color_discrete_map={'R': 'red','D': 'blue'},width=900,height=400,labels={'count': 'Amount'})
   #    fig.update_layout(xaxis={'categoryorder':'total descending'})
   #    fig.update_xaxes(tickangle=-45)
   #    fig.update_yaxes(title=None)
   #    newnames = {'R':'Republicans','D':'Democrats'}
   #    fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   #    st.plotly_chart(fig)

   # fig = px.bar(data,x='State',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1000, height=800,barmode="group")
   # fig.update_layout(xaxis={'categoryorder':'total descending'})
   # st.plotly_chart(fig)


   # fig = px.bar(data, x='District', color='Party', color_discrete_map={'D': 'Blue', 'R':'Red'},width=1200, height=400)
   # fig.update_layout(xaxis={'categoryorder':'total descending'})
   # newnames = {'R':'Republicans','D':'Democrats'}
   # fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
   # fig.update_xaxes(tickangle=45)
   # st.plotly_chart(fig)

   # fig = px.bar(
   #    data_melt_committee,
   #    y='Committee Assignment',
   #    color='Party',
   #    color_discrete_map={'D': 'Blue', 'R':'Red'},
   #    orientation='h',
   #    title="Representatives per Party grouped by Committee",
   #    width=1200, height=400)
   # fig.update_layout(yaxis={'categoryorder':'total descending'})
   # newnames = {'R':'Republicans','D':'Democrats'}
   # st.plotly_chart(fig)

   # order = {'District':['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th' ,'11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st','32nd','33rd','34th','35th','36th','37th','38th','39th','40th','41st','42nd','43rd','44th','45th','46th','47th','48th','49th','50th','51st','52nd','53rd','At Large', 'Delegate','Resident Commissioner']}
   # fig = px.bar(data,x='District',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1300, height=800,category_orders=order,facet_col="Party")
   # fig.update_layout(xaxis={'categoryorder':'total descending'})
   # newnames = {'R':'Republicans','D':'Democrats'}
   # fig.for_each_trace(lambda t: t.update(name = newnames[t.name])) # Interactive graph does not show up on GitHub
   # st.plotly_chart(fig)

   # fig = px.bar(data,x='District',color='Party',color_discrete_map={'D': 'Blue', 'R':'Red'},title="Committee Members per Party",width=1400, height=800,barmode="group",category_orders=order)
   # fig.update_xaxes(tickangle=45)
   # st.plotly_chart(fig)

   # st.markdown('''
   # <center>
   #    <p style="font-size:30px;">
   #       <b> Part 3/3: </b>
   #       Conclusion
   #    </p>
   # </center>
   # ''',unsafe_allow_html=True)

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
# else:
#    data = pd.DataFrame({'a':range(10)})
#    url = "EXAMPLE.ORG"
#    url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Politicos Chilenos - Camara Diputados ------------------------------------------------------------------------ ##
if projectOption[project] == 17:
   from Projects._17_BoatTrader import BoatTrader
   
   url = BoatTrader.url_main # https://www.boattrader.com/boat-dealers/
   data = BoatTrader.data
   script_1 = BoatTrader.script_1
   
   st.markdown('''
   <center>
      <img src='https://boattrader.com/static/img/tol-design/btol/bt-inc-release/boattrader-logo.png' alt="Logo">
   </center>
   ''',unsafe_allow_html=True)

   st.markdown(f'''
   <h1 style="font-size:40px;text-align:center;"> Description: </h1>
   <p style="font-size:20px;text-align:center;">
      I was asked to gather all 2400+ boat dealers and contact information for owner, sale manager, general manager and/or marketing manager listed on
         <a href="{url}"> boattrader.com</a>. 
      They wanted me to extract the Enter Name, Title, Email, Mailing Address and Phone for each dealer and position at dealership (not all applied, not all are listed),
      and to enter it into an Excel or Google Sheet (whichever I prefer).
      <br><br>
      I send a test list of 20 to ensure project is on the right track. It took me about 25 minutes to write the code, clean the data, and send the result.
      <br><br>
      Here is the result, code, and analysis:
   </p>
   ''',unsafe_allow_html=True)
   
   with st.expander("Code Used 🐍"):
      st.code(script_1,language="python")
   with st.expander("See Website 👨🏻‍💻"):
      st.markdown(f'''<a href={url}>{url}</a>''',unsafe_allow_html=True)
      col1, col2, col3 = st.columns([1,3,1])
      with col1:
         st.write(' ')
      with col2:
         components.iframe(f"{url}", width=350, height=500, scrolling=True)
      with col3:
         st.write(' ')
   with st.expander("Data Extracted 🕸"):
      st.write("Table containing data extracted from website")
   with st.expander("Analysis 🧐"):
      st.write(" ")
      
      st.download_button(
         label     =    "Download data as CSV",
         data      =    data.to_csv().encode('utf-8'),
         file_name =    'BoatTrader_dealers.csv',
         mime      =    'text/csv',)
      
      st.dataframe(data)

   x = data.groupby('state').aggregate('count').reset_index()[['state','id']].sort_values('id', ascending=False).rename(columns={"id": "count"})
   st.bar_chart(x, x='state', y='id')

# ---------
