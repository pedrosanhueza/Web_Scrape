# catalogBYUI

import requests
import pandas as pd

url_display = 'https://www.byui.edu/catalog#/courses'

url = 'https://byui.kuali.co/api/v1/catalog/courses/6102e778ef84b869ba4eb375?q='

response = requests.get(url)

responseObject = response.json()

df = pd.DataFrame(responseObject)

df = pd.concat([df, df.subjectCode.apply(pd.Series)], axis=1).drop(['subjectCode','__passedCatalogQuery','_score'], axis=1)

def str_num(word):
    for letter in word:
        if letter.isdigit():
            idx = word.index(letter)
            code = word[idx:]
            break
    return code

df['course-id'] = df.__catalogCourseId.apply(lambda x: str_num(x))

df.columns = [
    'catalogCourseId',
    'dateStart',
    'pid',
    'id',
    'title',
    'catalogActivationDate',
    'name',
    'description',
    'subjectCode-id',
    'linkedGroup',
    'course-id'
]

data = df

# ----------------------- TEST -----------------------

script_1 = '''
url = 'https://byui.kuali.co/api/v1/catalog/courses/6102e778ef84b869ba4eb375?q='

response = requests.get(url)

responseObject = response.json()

df = pd.DataFrame(responseObject)

df = pd.concat([df, df.subjectCode.apply(pd.Series)], axis=1).drop(['subjectCode','__passedCatalogQuery','_score'], axis=1)

df.columns = [
    'catalogCourseId',
    'dateStart',
    'pid',
    'id',
    'title',
    'catalogActivationDate',
    'name',
    'description',
    'subjectCode-id',
    'linkedGroup'
]

data = df

data.to_csv('BYUI_catalog.csv', index=False)
'''