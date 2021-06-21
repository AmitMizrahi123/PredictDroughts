import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC


#### DF Clening ###
df = pd.read_csv('files/merge.csv', index_col=0)
df['Week'] = pd.to_datetime(df['Week'])
set_year = df['Week'].dt.year.to_list()
set_month = df['Week'].dt.month.to_list()
set_day = df['Week'].dt.day.to_list()
df.insert(0, "Year", set_year, None)
df.insert(1, "Month", set_month, None)
df.insert(2, "Day", set_day, None)
encoding_columns = pd.get_dummies(df['LEVEL'], prefix="Level")
df = df.join(encoding_columns)

print(df)

### Start ML ###
X = df[df.columns[(df.columns != 'LEVEL') & (df.columns != 'Week') & (df.columns != 'State') & (df.columns != 'Postal Code') & (df.columns != 'GeoId')]]
y = df[['LEVEL']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

def ML_Algo(model):
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test) * 100
    return score

score_list = []

models = ["LogisticRegression", "KNeighborsClassifier", "DecisionTreeClassifier", "RandomForestClassifier", "SVC"]

lg = LogisticRegression()
lg_score = ML_Algo(lg)
score_list.append(lg_score)

knn = KNeighborsClassifier(n_neighbors=5)
knn_score = ML_Algo(knn)
score_list.append(knn_score)

dtc = DecisionTreeClassifier()
dtc_score = ML_Algo(dtc) 
score_list.append(dtc_score)

rfc = RandomForestClassifier()
rfc_score = ML_Algo(rfc)
score_list.append(rfc_score)

svc = SVC()
svc_score = ML_Algo(svc)
score_list.append(svc_score)

data = {
    "Model": models,
    "Score": score_list
}

score_df = pd.DataFrame(data)
print(score_df)