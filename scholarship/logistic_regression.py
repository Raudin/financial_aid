# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# File system manangement
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn import metrics
# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Suppress warnings
import warnings

warnings.filterwarnings('ignore')


def classify(directory):
    # Get the Data
    import io

    # Training data
    train = pd.read_csv(f'{directory}/Train.csv')

    # Testing data
    test = pd.read_csv(f'{directory}/pending.csv')


    """TRAIN DATA """

    # Drop Gender
    train = train.drop(["gender"], axis=1)

    # Prepocessing Data

    train['Family_background'] = train['family_background'] \
    .replace({'Orphan': 5, 'Single-orphan': 3, 'Non-orphan': 1})
    train[['family_background', 'Family_background']]


    train['grade'] = train['KCPE'] \
    .replace({'A': 4,'B': 3, 'C': 2, 'D': 1,'E': 0})
    train[['KCPE', 'grade']]


    train['grade1'] = train['KCSE'] \
    .replace({'A': 6,'B': 5, 'C': 3, 'D': 1,'E': 0})
    train[['KCSE', 'grade1']]
        
        
    train['Aid'] = train['aid'] \
    .replace({'Work-study': 2, 'Scholarship': 1, 'Bursary': 3})
    train[['aid', 'Aid']]

    train['county_code'] = train['county'] \
    .replace({
        "Mombasa": 0,
        "Kwale": 0,
        "Kilifi": 0,
        "Tana River": 0,
        "Lamu": 4,
        "Taita-Taveta": 0,
        "Garissa": 0,
        "Wajir": 0,
        "Mandera": 4,
        "Marsabit": 4,
        "Isiolo": 0,
        "Meru": 0,
        "Tharaka-Nithi": 0,
        "Embu": 0,
        "Kitui": 0,
        "Machakos": 0,
        "Makueni": 0,
        "Nyandarua": 0,
        "Nyeri": 0,
        "Kirinyaga": 0,
        "Murang'a": 0,
        "Kiambu": 0,
        "Turkana": 4,
        "West Pokot": 4,
        "Samburu": 4,
        "Trans-Nzoia": 0,
        "Uasin Gishu": 0,
        "Elgeyo-Marakwet": 0,
        "Nandi": 0,
        "Baringo": 0,
        "Laikipia": 0,
        "Nakuru": 0,
        "Narok": 0,
        "Kajiado": 0,
        "Kericho": 0,
        "Bomet": 0,
        "Kakamega": 0,
        "Vihiga": 0,
        "Bungoma": 0,
        "Busia": 0,
        "Siaya": 0,
        "Kisumu": 0,
        "Homa Bay": 0,
        "Migori": 0,
        "Kisii": 0,
        "Nyamira": 0,
        "Nairobi.": 0,
    })
    train[['county', 'county_code']]

    train['Refugee_or_immigrant'] = train['refugee_or_immigrant'] \
    .replace({'Yes': 2, 'No': 1})
    train[['refugee_or_immigrant', 'Refugee_or_immigrant']]


    train['Sponsor'] = train['sponsor'] \
    .replace({'Yes': 1, 'No': 3})
    train[['sponsor', 'Sponsor']]

    train['Extra-curricular'] = train['extra-curricular'] \
    .replace({'True': 1, 'False': 0})
    train[['extra-curricular', 'Extra-curricular']]


    train['Leadership'] = train['leadership'] \
    .replace({'True': 2, 'False': 0})
    train[['leadership', 'Leadership']]

    train['Disabled'] = train['disabled'] \
    .replace({'Yes': 7, 'No': 1})
    train[['disabled', 'Disabled']]

    """LOGISTIC REGRESSION """

    lr = LogisticRegression()
    columns = ['Sponsor','Disabled','Refugee_or_immigrant','Family_background','grade1','grade','Aid','county_code', 'Extra-curricular','Leadership']

    lr.fit(train[columns], train["accepted"] )


    X = train[columns]
    y = train['accepted']

    train_X, val_X, train_y, val_y = train_test_split(
        X, y, test_size=0.30, random_state=0)

    lr = LogisticRegression()
    lr.fit(train_X, train_y,)
    predictions = lr.predict(val_X)
    accuracy = accuracy_score(val_y, predictions)
    print(accuracy)

    from sklearn.metrics import classification_report
    print(classification_report(val_y,predictions))


    """TEST DATA MANIPULATION"""
    test['Family_background'] = test['family_background'] \
    .replace({'Orphan': 5, 'Single-orphan': 3, 'Non-Orphan': 1})
    test[['family_background', 'Family_background']]

    test['grade'] = test['KCPE'] \
    .replace({'A': 4,'B': 3, 'C': 2, 'D': 1,'E': 0})
    test[['KCPE', 'grade']]

    test['grade1'] = test['KCSE'] \
    .replace({'A': 6,'B': 5, 'C': 3, 'D': 1,'E': 0})
    test[['KCSE', 'grade1']]

    test['Aid'] = test['aid'] \
    .replace({'Work-study': 2, 'Scholarship': 1, 'Bursary': 3})
    test[['aid', 'Aid']]

    test['county_code'] = test['county'] \
    .replace({
        "Mombasa": 0,
        "Kwale": 0,
        "Kilifi": 0,
        "Tana River": 0,
        "Lamu": 4,
        "Taita-Taveta": 0,
        "Garissa": 0,
        "Wajir": 0,
        "Mandera": 4,
        "Marsabit": 4,
        "Isiolo": 0,
        "Meru": 0,
        "Tharaka-Nithi": 0,
        "Embu": 0,
        "Kitui": 0,
        "Machakos": 0,
        "Makueni": 0,
        "Nyandarua": 0,
        "Nyeri": 0,
        "Kirinyaga": 0,
        "Murang'a": 0,
        "Kiambu": 0,
        "Turkana": 4,
        "West Pokot": 4,
        "Samburu": 4,
        "Trans-Nzoia": 0,
        "Uasin Gishu": 0,
        "Elgeyo-Marakwet": 0,
        "Nandi": 0,
        "Baringo": 0,
        "Laikipia": 0,
        "Nakuru": 0,
        "Narok": 0,
        "Kajiado": 0,
        "Kericho": 0,
        "Bomet": 0,
        "Kakamega": 0,
        "Vihiga": 0,
        "Bungoma": 0,
        "Busia": 0,
        "Siaya": 0,
        "Kisumu": 0,
        "Homa Bay": 0,
        "Migori": 0,
        "Kisii": 0,
        "Nyamira": 0,
        "Nairobi.": 0,
    })
    test[['county', 'county_code']]

    test['Refugee_or_immigrant'] = test['refugee_or_immigrant'] \
    .replace({'Yes': 2, 'No': 1})
    test[['refugee_or_immigrant', 'Refugee_or_immigrant']]

    test['Sponsor'] = test['sponsor'] \
    .replace({'Yes': 1, 'No': 3})
    test[['sponsor', 'Sponsor']]

    test['Extra-curricular'] = test['extra-curricular'] \
    .replace({'True': 1, 'False': 0})
    test[['extra-curricular', 'Extra-curricular']]

    test['Leadership'] = test['leadership'] \
    .replace({'True': 2, 'False': 0})
    test[['leadership', 'Leadership']]

    test['Disabled'] = test['disabled'] \
    .replace({'Yes': 7, 'No': 1})
    test[['disabled', 'Disabled']]


    lr = LogisticRegression()
    newcolumns = ['Sponsor','Disabled','Refugee_or_immigrant','Family_background','grade1','grade','Aid','county_code', 'Extra-curricular','Leadership']
    lr.fit(X,y)
    predictions_test = lr.predict(test[newcolumns])

    submission_df = pd.DataFrame({'id': test['id'],
                                    'accepted': predictions_test})

    # Place the File into outputs.csv for it to be read in the view and saved in the db
    submission_df.to_csv(f'{directory}/outputs.csv')
