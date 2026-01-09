import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Titanic-Dataset.csv")
df = pd.DataFrame(data)

#univariate 
# numerical cols
# for age
print(df["Age"].describe())

age = df["Age"].plot(kind="hist",bins=20)
plt.show()

age_dist = df["Age"].plot(kind="kde")
plt.show()

print(df["Age"].skew())

# identify outliers
out = df["Age"].plot(kind="box")
plt.show()

print(df['Age'].isnull().sum())
per = df['Age'].isnull().sum()/len(df["Age"])

# Fare
print(df["Fare"].describe())
df["Fare"].plot(kind="hist")
plt.show()
print(df["Fare"].skew())
print(df[df["Fare"]>300])
print(df['Fare'].isnull().sum())

# categorical columns
print(df['Survived'].value_counts())
survive = df['Survived'].value_counts().plot(kind="pie",autopct="%0.1f%%")
plt.show()
print(df["Survived"].isnull().sum())
df['Pclass'].value_counts().plot(kind="bar")
plt.show()

print(df['Sex'].value_counts())
df['Sex'].value_counts().plot(kind="pie",autopct="%0.1f%%")
plt.show()

print(df['SibSp'].value_counts())
df['SibSp'].value_counts().plot(kind="pie",autopct="%0.1f%%")
plt.show()

print(df['Parch'].value_counts())
df['Parch'].value_counts().plot(kind="pie",autopct="%0.1f%%")
plt.show()

#bivariate
#choose main column and bivariate it with all columns

#survived and pclass
print(pd.crosstab(df['Survived'],df["Pclass"],normalize="columns")*100)

#survived and gender
print(pd.crosstab(df['Survived'],df["Sex"],normalize="columns")*100)

#survived and embarked
print(pd.crosstab(df['Survived'],df["Embarked"],normalize="columns")*100)

#gender and embarked
print(pd.crosstab(df['Sex'],df["Embarked"],normalize="columns")*100)

#pclass and embarked
print(pd.crosstab(df['Pclass'],df["Embarked"],normalize="columns")*100)

#survived and age
print(df[df["Survived"]==1]['Age'].plot(kind="kde",label="Survived"))
print(df[df["Survived"]==0]['Age'].plot(kind="kde",label="Survived"))
plt.legend()
plt.show()

#feature engineering
print(df[df["SibSp"]==8])

print(df[df["Ticket"]=="CA. 2343"])

df["Family_size"] = df["SibSp"] + df["Parch"] + 1
df["ind_fare"] = df["Fare"]/df["Family_size"]
print(df["ind_fare"])

def family_type(size):
    if size==1:
        return "Single"
    elif size<=4:
        return "Small"
    else:
        return "Large"
    
df["Family_type"] = df["Family_size"].apply(family_type)
print(df["Family_type"])

print(pd.crosstab(df["Family_type"],df["Survived"],normalize="index")*100)

df["surname"] = df["Name"].str.split(",").str.get(0)
print(df["surname"])    

df["title"] = df["Name"].str.split(",").str.get(1).str.strip().str.split(" ").str.get(0)

df["title"] = df["title"].replace({
    "Mlle":"Miss",
    "Ms.":"Miss.",
    "Mme":"Mrs",
    "Lady":"Royal",
    "Countess":"Royal",
    "Capt":"Officer",
    "Col":"Officer",
    "Don":"Royal",
    "Jonkheer":"Royal",
    "Dona":"Royal"
})
print(df["title"].value_counts())

print(df["Cabin"].value_counts().head(15))
print(df["Cabin"].fillna("M",inplace=True))
print(df["Cabin"].isnull().sum())

df["deck"] = df["Cabin"].str[0]
print(df["deck"])

print(pd.crosstab(df["deck"],df["Pclass"]))
pd.crosstab(df["deck"],df["Survived"],normalize="index").plot(kind="bar",stacked=True)
plt.show()

