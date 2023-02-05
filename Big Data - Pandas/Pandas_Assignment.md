**Q1. How do you load a CSV file into a Pandas DataFrame?**

Ans. 

	import pandas as pd
	pd.DataFrame
	df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
	print(df)



**Q2. How do you check the data type of a column in a Pandas DataFrame?**

Ans.

	type(df['Name'])
	df.dtypes

**Q3. How do you select rows from a Pandas DataFrame based on a condition?**

Ans. We can use operators like > , < >= , <= , != , =

	 df_new = df.loc[df['Age'] < 10]


**Q4. How do you rename columns in a Pandas DataFrame?**

Ans. Using rename() funnction

	 df.rename (columns = {'Age' : 'AgeOfPerson'}, inplace = True)

**Q5. How do you drop columns in a Pandas DataFrame?**

Ans. Using drop function
	 
	 df.drop('Pclass', axis=1, inplace=True)

**Q6. How do you find the unique values in a column of a Pandas DataFrame?**

Ans. Using unique() function
	
	 df.Sex.unique()

**Q7. How do you find the number of missing values in each column of a Pandas DataFrame?**

Ans. Using isnull() fucntion followed by sum() function

	 df.isnull().sum()

**Q8. How do you fill missing values in a Pandas DataFrame with a specific value?**

Ans. Using fillna() function

	 df.fillna('0000', inplace=True)

**Q9. How do you concatenate two Pandas DataFrames?**

Ans. 

	df_concat=[df1,df2]
	result = pd.concat(df_concat)

**Q10. How do you merge two Pandas DataFrames on a specific column?**

Ans. Using merge() function

	 df1.merge(df2[['Grade', 'Name']], on = 'Name', how = 'left')


**Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?**

Ans. df_new.groupby('Name').aggregate({"Age":['max', 'min']})

**Q12. How do you pivot a Pandas DataFrame?**

Ans. The pivot() function is used to reshaped a given DataFrame organized by given index / column values

	 df.pivot('PassengerId','Name', 'Age')

**Q13. How do you change the data type of a column in a Pandas DataFrame?**

Ans. DataFrame.astype() method is used to cast pandas object to a specified dtype. We can use dictionary to convert specific columns to another data types. 

	df = pd.DataFrame({
		'A': [1, 2, 3, 4, 5],
		'B': ['a', 'b', 'c', 'd', 'e'],
		'C': [1.1, '1.0', '1.3', 2, 5]})
		convert_dict = {'A': int,
					'C': float
					}
	 
	df = df.astype(convert_dict)
	print(df.dtypes)

**Q14. How do you sort a Pandas DataFrame by a specific column?**

Ans. Using sort_values() fucntion

	 df_new.sort_values('Age')

**Q15. How do you create a copy of a Pandas DataFrame?**

Ans.  Using copy() function

	  df_cpy = df.copy()

**Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?**

Ans. eval() to Filter by Multiple Conditions. 	
	 
	 df1= df[df.eval("Age <10 & Name.str.startswith('A').values")]


**Q17. How do you calculate the mean of a column in a Pandas DataFrame?**


Ans.

		df['Age'].mean()
		
**Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?**

Ans.

	    df['Age'].std()

**Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?**

Ans. By using corr() function we can get the correlation between two columns in the dataframe.

**Q20. How do you select specific columns in a DataFrame using their labels?**

Ans. df[['Name','Age']]

**Q21. How do you select specific rows in a DataFrame using their indexes?**

Ans. We can either use loc() or iloc() depdending on requirement

	 df.iloc[1:10]
	 df.loc[1:10]

**Q22. How do you sort a DataFrame by a specific column?**

Ans. Using sort_values() fucntion

	 df_new.sort_values('Age')

**Q23. How do you create a new column in a DataFrame based on the values of another column?**

Ans. You can add/append a new column to the DataFrame based on the values of another column using df.assign(), df.apply(), and, np.where() functions and return a new Dataframe after adding a new column.

	e.g df['new_column'] = df['Age']

**Q24. How do you remove duplicates from a DataFrame?**

Ans. Using drop_duplicates() method

	 df.drop_duplicates()

**Q25. What is the difference between .loc and .iloc in Pandas?**

Ans. df.iloc() - Will give value according to system index

	 df.loc() - will give the value according the index column which we have set
