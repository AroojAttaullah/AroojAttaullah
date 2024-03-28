import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset from seaborn
titanic_df = sns.load_dataset('titanic')

# Display basic information about the dataset
print("Basic information about the Titanic dataset:")
print(titanic_df.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the Titanic dataset:")
print(titanic_df.head())

# Visualizations
plt.figure(figsize=(14, 6))

# Survival Count
plt.subplot(1, 2, 1)
sns.countplot(x='survived', data=titanic_df, palette='Set1')
plt.title('Survival Count (0 = Not Survived, 1 = Survived)')
plt.xlabel('Survival Status')
plt.ylabel('Count')

# Passenger Class Distribution
plt.subplot(1, 2, 2)
sns.countplot(x='pclass', data=titanic_df, palette='Set2')
plt.title('Passenger Class Distribution')
plt.xlabel('Passenger Class')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(titanic_df['age'], bins=10, kde=True, color='skyblue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Fare Distribution
plt.figure(figsize=(10, 6))
sns.histplot(titanic_df['fare'], bins=10, kde=True, color='salmon')
plt.title('Fare Distribution')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.show()

# Gender Distribution
plt.figure(figsize=(6, 6))
titanic_df['sex'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()Basic information about the Titanic dataset: <class 'pandas.core.frame.DataFrame'> RangeIndex: 891 entries, 0 to 890 Data columns (total 15 columns): # Column Non-Null Count Dtype --- ------ -------------- ----- 0 survived 891 non-null int64 1 pclass 891 non-null int64 2 sex 891 non-null object 3 age 714 non-null float64 4 sibsp 891 non-null int64 5 parch 891 non-null int64 6 fare 891 non-null float64 7 embarked 889 non-null object 8 class 891 non-null category 9 who 891 non-null object 10 adult_male 891 non-null bool 11 deck 203 non-null category 12 embark_town 889 non-null object 13 alive 891 non-null object 14 alone 891 non-null bool dtypes: bool(2), category(2), float64(2), int64(4), object(5) memory usage: 80.7+ KB None First few rows of the Titanic dataset: survived pclass sex age sibsp parch fare embarked class \ 0 0 3 male 22.0 1 0 7.2500 S Third 1 1 1 female 38.0 1 0 71.2833 C First 2 1 3 female 26.0 0 0 7.9250 S Third 3 1 1 female 35.0 1 0 53.1000 S First 4 0 3 male 35.0 0 0 8.0500 S Third who adult_male deck embark_town alive alone 0 man True NaN Southampton no False 1 woman False C Cherbourg yes False 2 woman False NaN Southampton yes True 3 woman False C Southampton yes False 4 man True NaN Southampton no True 

<ipython-input-20-82d474065a52>:21: FutureWarning: Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect. sns.countplot(x='survived', data=titanic_df, palette='Set1') <ipython-input-20-82d474065a52>:28: FutureWarning: Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect. sns.countplot(x='pclass', data=titanic_df, palette='Set2') 

￼

