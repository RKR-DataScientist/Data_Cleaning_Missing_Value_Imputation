import pandas as pd
import numpy as np
## How to randomly sample a Pandas DataFrame
'''

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
                'age': [42, 52, 36, 24, 73],
                'preTestScore': [4, 24, 31, 2, 3],
                'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age',
                                           'preTestScore', 'postTestScore'])
print(); print(df)
    # Select a random subset of 2 without replacement
print(); print(df.take(np.random.permutation(len(df))[:2]))
    # Select a random subset of 4 without replacement
print(); print(df.take(np.random.permutation(len(df))[:4]))
    # random sample of df    
df1 = df.sample(3)
print(); print(df1)
'''


#How to drop ROW and COLUMN in a Pandas DataFrame
# Create a dataframe
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            'year': [2012, 2012, 2013, 2014, 2014],
            'reports': [4, 24, 31, 2, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print(); print(df)

    # Drop an observation (row)
print(); print(df.drop(['Cochice', 'Pima']))

    # Drop a variable (column) # Note: axis=1 denotes that we are referring to a column, not a row
print(); print(df.drop('reports', axis=1))

    # Drop a row if it contains a certain value (in this case, “Tina”)
print(); print(df[df.name != 'Tina'])

    # Drop a row by row number (in this case, row 3)
print(); print(df.drop(df.index[2]))

    # can be extended to dropping a range
print(); print(df.drop(df.index[[2,3]]))

    # dropping relative to the end of the DF.
print(); print(df.drop(df.index[-2]))

    # Keep top 3
print(); print(df[:3])

    # Drop bottom 3 
print(); print(df[:-3])




#How to JOIN and MERGE Pandas DataFrame?


# Create a dataframe
raw_data = {'subject_id': ['1', '2', '3', '4', '5'],
                'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
                'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
print(); print(df_a)

    # Create a second dataframe
raw_data = {'subject_id': ['4', '5', '6', '7', '8'],
                'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
                'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
print(); print(df_b)

    # Create a third dataframe
raw_data = {'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
                'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
print(); print(df_n)

    # Join the two dataframes along rows
df_new = pd.concat([df_a, df_b])
print(); print(df_new)

    # Join the two dataframes along columns
df = pd.concat([df_a, df_b], axis=1)
print(); print(df)

    # Merge two dataframes along the subject_id value
df = pd.merge(df_new, df_n, on='subject_id')
print(); print(df)

    # Merge two dataframes with both the left and right dataframes using the subject_id key
df = pd.merge(df_new, df_n, left_on='subject_id', right_on='subject_id')
print(); print(df)

    # Merge with outer join
df = pd.merge(df_a, df_b, on='subject_id', how='outer')
print(); print(df)

    # Merge with inner join
df = pd.merge(df_a, df_b, on='subject_id', how='inner')
print(); print(df)

    # Merge with right join
df = pd.merge(df_a, df_b, on='subject_id', how='right')
print(); print(df)

    # Merge with left join
df = pd.merge(df_a, df_b, on='subject_id', how='left')
print(); print(df)

    # Merge while adding a suffix to duplicate column names
df = pd.merge(df_a, df_b, on='subject_id', how='left', suffixes=('_left', '_right'))
print(); print(df)

    # Merge based on indexes
df = pd.merge(df_a, df_b, right_index=True, left_index=True)
print(); print(df)




#How to deal with missing values in a Pandas DataFrame?

# Create dataframe with missing values
raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
                'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
                'age': [42, np.nan, 36, 24, 73],
                'sex': ['m', np.nan, 'f', 'm', 'f'],
                'preTestScore': [4, np.nan, np.nan, 2, 3],
                'postTestScore': [25, np.nan, np.nan, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex',
                                           'preTestScore', 'postTestScore'])
print(); print(df)

    # Drop missing observations
df_no_missing = df.dropna()
print(); print(df_no_missing)

    # Drop rows where all cells in that row is NA
df_cleaned = df.dropna(how='all')
print(); print(df_cleaned)

    # Create a new column full of missing values
df['location'] = np.nan
print(); print(df)

    # Drop column if they only contain missing values
print(); print(df.dropna(axis=1, how='all'))

    # Drop rows that contain less than five observations
    # This is really mostly useful for time series
print(); print(df.dropna(thresh=5))

    # Fill in missing data with zeros
print(); print(df.fillna(0))

    # Fill in missing in preTestScore with the mean value of preTestScore
    # inplace=True means that the changes are saved to the df right away
df["preTestScore"].fillna(df["preTestScore"].mean(), inplace=True)
print(); print(df)

    # Fill in missing in postTestScore with each sex’s mean value of postTestScore
df["postTestScore"].fillna(df.groupby("sex")["postTestScore"].transform("mean"), inplace=True)
print(); print(df)

    # Select the rows of df where age is not NaN and sex is not NaN
print(); print(df[df['age'].notnull() & df['sex'].notnull()])
print(); print(df[df['age'].notnull() & df['sex'].notnull()].fillna(0))

























