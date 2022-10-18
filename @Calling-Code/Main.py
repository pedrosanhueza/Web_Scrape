
## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time
import seaborn as sns
import matplotlib.pyplot as plt
import time

# from Projects._1_Billionaires import forbesBillionaires
# from Projects._2_BYUI_ClassCatalog import catalogBYUI
# from Projects._3_CountryCode import countryCode
# from Projects._4_FIFAWorldCup import FIFAWorldCup
# # from Projects._5_Financial Data import 
# from Projects._6_ForbesBillionaries import forbesBillionaires
# from Projects._7_ForbesUniversities import Forbes_Universities
# from Projects._8_IrvineSpectrumCenter import irvinespectrumcenter
from Projects._9_BYUI_JobBoard import BYUI_JobBoard
# from Projects._10_MutualAppFeedback import Mutual_App_Feedback
# from Projects._11_NewsCBS import cbsnews
# # from Projects._12_PoliticosChilenos import 
# from Projects._13_PoliticosEspanoles import DiputadosEspanoles
# from Projects._14_SINCAMMAGob import SINCAMMAGob
# from Projects._15_BYUI_SurplusStore import SurplusStore
# from Projects._16_USHouseRepresentatives import representatives
# from Projects.test import test

st.set_option('deprecation.showPyplotGlobalUse', False)

## ----------------------------------------- Beggin Side Bar ----------------------------------------------------------------------------- ##

options = (
   'Billionaires',
   'Class Catalog - BYUI',
   'Country Code',
   'FIFA World Cup',
   'Financial Data',
   'Forbes - Billionaries',
   'Forbes - Universities',
   'Irvine Spectrum Center',
   'Job Board - BYUI',
   'Mutual App Feedback',
   'News - CBS',
   'Politicos Chilenos',
   'Políticos Españoles',
   'SINCA MMA Gob',
   'Surplus Store - BYUI',
   'US House of Representatives',
   'test')

option = st.sidebar.selectbox('Web Scraping Projects', options)

## ----------------------------------------- Modules Variables ------------------------------------------------------------------------ ##
## data
## url - scrape
## url - website

projectOption = {
   'Billionaires':1,
   'Class Catalog - BYUI':2,
   'Country Code':3,
   'FIFA World Cup':4,
   'Financial Data':5,
   'Forbes - Billionaries':6,
   'Forbes - Universities':7,
   'Irvine Spectrum Center':8,
   'Job Board - BYUI':9,
   'Mutual App Feedback':10,
   'News - CBS':11,
   'Politicos Chilenos':12,
   'Políticos Españoles':13,
   'SINCA MMA Gob':14,
   'Surplus Store - BYUI':15,
   'US House of Representatives':16,
   'test':17
}

# st.write('You selected:', option)

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
if projectOption[option] == 1: #'Billionaires'
   st.write('Hola!')

## ----------------------------------------- Class Catalog - BYUI ------------------------------------------------------------------------ ##
# elif projectOption[option] == 2:
#    data = catalogBYUI.data
#    url = catalogBYUI.url
#    url_split = url.replace('https://','').split('/')[0]

#    tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Table', 'Code', 'Analysis'])

#    with tab1:
#       st.header(option)
#       col1, col2, col3 = st.columns(3)
#       col1.metric("Classes", data.shape[0], "1.2 °F")
#       col2.metric("Subjects", data.description.nunique(), "-8%")
#       col3.metric("Humidity", "86%", "4%")

#       st.image('@Calling-Code/Projects/CatalogBYUI/CatalogBYUI.png', caption='Website page')
      
#       # f"[{url_split}]({url}) website"
#    with tab2:
#       st.header(f"Data extracted from @@@")
#       # st.header(f"Data extracted from {url_split}")
#       st.dataframe(data)
#    with tab3:
#       st.header("Code")
#    with tab4:
#       st.header("Analysis")

# ## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
# elif projectOption[option] == 3:
#    data = countryCode.data
#    url = countryCode.url
#    url_split = url.replace('https://','').split('/')[0]

# ## ----------------------------------------- FIFA World Cup ------------------------------------------------------------------------ ##
# elif projectOption[option] == 4:
#    st.header(option)

#    data = FIFAWorldCup.data

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

# ## ----------------------------------------- Job Board - BYUI ------------------------------------------------------------------------ ##
elif projectOption[option] == 9:

   st.write('''
   # BYU-I
   ## Job Board
   ''')

   st.markdown('''
   # BYU-I
   ## Job Board
   **Author**: Pedro Sanhueza
   ''')

   data = BYUI_JobBoard.data
   
   d = str(datetime.today().strftime("%Y-%m-%d"))

   KPI1_jobs = round(1-(400/data.shape[0]),2)

   KPI1_1_max = round(1-(data.payRate.median()/data.payRate.max()),2)

   jobs_not_online = data[~data.title.str.contains('Online')].shape[0]

   KPI1, KPI1_1, KPI2 = st.columns(3)

   KPI1.metric('Jobs Published', f"{data.shape[0]}")

   KPI1_1.metric("Highest Pay Rate Job", f"${data.payRate.max()}")

   KPI2.metric("Departments Recluting", f"{data.departmentName.nunique()}")

   today = data[data.dateUpdated == time.strftime("%Y-%m-%d")].shape[0]

   yesterday = data[data.dateUpdated == (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")].shape[0]

   KPI3, KPI4, KPI_K = st.columns(3)

   KPI3.metric("Departments hiring", f"{data.departmentName.nunique()}")

   try:
      KPI4.metric("Jobs posted today",today, f'{round((today/yesterday)-1,2)}% of yesterday')
   except:
      KPI4.metric("Jobs posted today",today, f'0% of yesterday')

   KPI_K.metric("Jobs not Online", f"{jobs_not_online}")

   tab1, tab2, tab3, tab4 = st.tabs(['Highest Paid Jobs','Jobs not online','Table','Code'])

   with tab1:
      col1, col2, col3 = st.columns(3)

      with col1:
         st.write('')
      with col2:
         st.write(data.payRate.max())
      with col3:
         st.write('')

   with tab2:
      jobs_to_remove = ['TA','Custodian','Online','Grounds']
      jobs_to_remove_str = '|'.join(jobs_to_remove)   
      st.write('Personalised Table')
      data_p = data[~data.title.str.contains(jobs_to_remove_str)].sort_values('payRate', ascending=False)[['title','payRate','workSchedule','URL']]
      st.dataframe(data_p)
      
      sns.kdeplot(data.payRate, shade=True, color="g", bw=0.94, alpha=0.5, cut=0)
      fig1 = plt.show()
      st.pyplot(fig1)

   with tab3:
      st.dataframe(BYUI_JobBoard.data)

   with tab4:
      st.code(BYUI_JobBoard.script1)

   sns.kdeplot(data.payRate, shade=True, color="g", bw=0.94, alpha=0.5, cut=0)

   fig1 = plt.show()

   st.pyplot(fig1)

   if st.button('Personalised Table'):
      jobs_to_remove = ['TA','Custodian','Online','Grounds']
      jobs_to_remove_str = '|'.join(jobs_to_remove)   
      st.write('Personalised Table')
      data_p = data[~data.title.str.contains(jobs_to_remove_str)].sort_values('payRate', ascending=False)[['title','payRate','workSchedule','URL']]
      st.table(data_p)

   if st.button("ballons"):
      st.balloons()
   
   if st.button("info"):
      st.info('This is a purely informational message', icon="ℹ️")
   



# ## -----------------------------------------  ------------------------------------------------------------------------ ##
# elif projectOption[option] == 15:
#    data = SurplusStore.data
#    url = SurplusStore.url
#    url_split = url.replace('https://','').split('/')[0]

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
# elif projectOption[option] == 16: 
#    data = representatives.data
#    url = representatives.url
#    url_split = url.replace('https://','').split('/')[0]

# ## -----------------------------------------  ------------------------------------------------------------------------ ##
# else:
#    data = pd.DataFrame({'a':range(10)})
#    url = "EXAMPLE.ORG"
#    url_split = url.replace('https://','').split('/')[0]

