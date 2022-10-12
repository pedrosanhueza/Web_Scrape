
## ----------------------------------------- Import -------------------------------------------------------------------------------------- ##
import streamlit as st
import pandas as pd

# from Projects import SurplusStore      #1
from Projects.CatalogBYUI import catalogBYUI       #2
from Projects import countryCode   #3
from Projects.FIFA_World_Cup import FIFAWorldCup    #4
# from Projects import SurplusStore    #5
# from Projects import SurplusStore    #6
# from Projects import SurplusStore    #7
# from Projects import SurplusStore    #8
# from Projects import SurplusStore    #9
# from Projects import SurplusStore    #10
# from Projects import SurplusStore    #11
# from Projects import SurplusStore    #12
# from Projects import SurplusStore    #13
# from Projects import SurplusStore    #14
from Projects import SurplusStore    #15
from Projects import representatives    #16
# from Projects import SurplusStore    #17


st.write('# Web Analysis')
st.write('''
    __Author__ : Pedro Sanhueza \n
    Description: Web Scraping EDA
    ''')

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
   # data = SurplusStore.data
   # url = SurplusStore.url
   # url_split = url.replace('https://','').split('/')[0]
   st.write('Billionaires')

## ----------------------------------------- Class Catalog - BYUI ------------------------------------------------------------------------ ##
elif projectOption[option] == 2:
   data = catalogBYUI.data
   url = catalogBYUI.url
   url_split = url.replace('https://','').split('/')[0]

   tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Table', 'Code', 'Analysis'])

   with tab1:
      st.header(option)
      col1, col2, col3 = st.columns(3)
      col1.metric("Classes", data.shape[0], "1.2 °F")
      col2.metric("Subjects", data.description.nunique(), "-8%")
      col3.metric("Humidity", "86%", "4%")

      st.image('@Calling-Code/Projects/CatalogBYUI/CatalogBYUI.png', caption='Website page')
      
      # f"[{url_split}]({url}) website"
   with tab2:
      st.header(f"Data extracted from @@@")
      # st.header(f"Data extracted from {url_split}")
      st.dataframe(data)
   with tab3:
      st.header("Code")
   with tab4:
      st.header("Analysis")

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 3:
   data = countryCode.data
   url = countryCode.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 4:
   st.header(option)
   data = FIFAWorldCup.data
   countries = ('All Countries',) + tuple(data.Country.unique())
   country_selected = st.sidebar.selectbox("Countries",countries)

   st.write(country_selected)

   data_main = data.copy()

   if country_selected == 'All Countries':
      data_main = data.copy()
   else:
      data_main = data[data.Country == country_selected]

   Players_avg = round(data_main.shape[0] / (data.shape[0] / data.Country.nunique())  - 1,2)
   Age_avg = round(data.HT.mean() / data[data.Country == country_selected].AGE.mean() - 1,2)
   HT_avg = round(data.HT.mean() / data[data.Country == country_selected].HT.mean()   - 1,2)
   WT_avg = round(data.HT.mean() / data[data.Country == country_selected].WT.mean()   - 1,2)
   BMI_avg = round(data.HT.mean() / data[data.Country == country_selected].BMI.mean() - 1,2)

   tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Table', 'Code', 'Analysis'])

   with tab1:
      col2, col3, col4, col5, col6 = st.columns(5)
      col2.metric("Players",    round(data_main.shape[0]), str(Players_avg) + '%')
      col3.metric("Age Avg",    round(data_main.AGE.mean()), str(Age_avg) + "%")
      col4.metric("Height Avg", round(data_main.HT.mean()), str(HT_avg)  + "%")
      col5.metric("Weight Avg", round(data_main.WT.mean()), str(WT_avg)  + "%")
      col6.metric("BMI Avg",    round(data_main.BMI.mean()), str(BMI_avg) + "%")

   with tab2:
      st.dataframe(data_main)
   with tab3:
      st.header(option)
   with tab4:
      st.header(option)
   
   page_bg_img = '''
   <style>
   body {
   background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
   background-size: cover;
   }
   </style>
   '''

   st.markdown(page_bg_img, unsafe_allow_html=True)
## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 15:
   data = SurplusStore.data
   url = SurplusStore.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
elif projectOption[option] == 16: 
   data = representatives.data
   url = representatives.url
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Billionaires ------------------------------------------------------------------------ ##
else:
   data = pd.DataFrame({'a':range(10)})
   url = "EXAMPLE.ORG"
   url_split = url.replace('https://','').split('/')[0]

## ----------------------------------------- Tables ----------------------------------------------------------------------------------- ##

# tab1, tab2, tab3, tab4 = st.tabs(['Page', 'Table', 'Code', 'Analysis'])

# with tab1:
#    st.header(option)
#    # image = Image.open('Projects/CatalogBYUI/CatalogBYUI.png')
#    # st.image(image, caption='Website page')
#    # f"[{url_split}]({url}) website"

# with tab2:
   
#    st.header(f"Data extracted from @@@")

#    # st.header(f"Data extracted from {url_split}")

#    st.dataframe(data)

# with tab3:
#    st.header("Code")

# with tab4:
#    st.header("Analysis")
