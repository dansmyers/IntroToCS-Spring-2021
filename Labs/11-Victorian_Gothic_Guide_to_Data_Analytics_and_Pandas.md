# The Victorian Gothic Guide to Data Analytics and Pandas

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Caspar_David_Friedrich_-_Abtei_im_Eichwald_-_Google_Art_Project.jpg/2560px-Caspar_David_Friedrich_-_Abtei_im_Eichwald_-_Google_Art_Project.jpg" width="50%" />

>*The Abby in the Oakwood*, Caspar David Friedrich (1809-10)

## Description

Pandas is a Python framework for data analytics. In this lab, you'll work through three small projects that will illustrate what it can do. Along the way, we'll also learn a little
about Python-based plotting frameworks and review some statistical concepts.

By the end of this lab, you will be familiar with:

- Loading data from a CSV file into a Pandas dataframe.
- Basic dataframe manipulations: Selecting a column, selecting subsets, creating new columns.
- Generating cross tabulations and frequency tables for comparing categorical data.
- Creating bar plots from a frequency table.
- Creating histograms from a dataframe.
- Calculating the mean and five number summary of a dataframe.

At the end of this lab, you'll submit **three Python programs and three PDF plots** to the assignment on Canvas.

The three labs we're going to complete were originally designed by my wife Chelsea for her book,
[*Project-Based R Companion to Introductory Statistics*](https://www.taylorfrancis.com/books/mono/10.1201/9780429292002/project-based-companion-introductory-statistics-chelsea-myers?context=ubx&refId=262ee6fc-50b7-4b79-a116-d508a2270467). She has &ndash; let's call it &ndash; a *fascination* with weird and morbid 19th Century data sets, which is one of her many excellent qualities.

## Pandas Background



## Get the Data

The three CSV files are posted to Canvas. Download them all, then upload them to your Mimir workspace using the `File ---> Upload` menu.

The three files will upload to your top-level workspace directory. Start by making a subdirectory for this lab and moving the files to it.

```
mkdir CMS_120/Lab_11

cd CMS_120/Lab_11

mv ../../Titanic.csv .

mv ../../Lister.csv .

mv ../../Ohio.csv .
```

The `mv` command moves a file. Here, `..` refers to the parent directory, so the path `../../Titanic.csv` refers to a file named `Titanic.csv` that is two levels up in the
directory hierarchy. The second `.` refers to the current working directory, which will be `CMS_120/Lab_11` in this example. In words, the command takes the file `Titanic.csv`
from two levels up and moves it to the current working directory.

Type `ls` and verify that the three files have appeared in your current directory.

## The *Titanic* Dataset

<img src="http://4.bp.blogspot.com/-B_jEnnLjgI0/U-_r3-pZr6I/AAAAAAAA3lM/UzMzMqlDSsQ/s1600/1977114_10152475439781112_174145227163964287_n.jpg" width="50%" />

In the early hours of April 15, 1912, the "unsinkable" ship *RMS Titanic* sank when it struck an iceberg, killing more than half of the passengers and crew aboard. The `Titanic.csv` dataset contains demographic information for 889 of those passengers as well as a record of whether or not each passenger survived. Our first goal is to explore the functionality of Pandas by opening and modifying the *Titanic* dataset.


### Load the Data Set

Create a new Python file called `titanic.py` and put the following code inside it:

```
"""
Analyze the Titanic data set with Pandas
"""

import pandas as pd
import numpy as np

# Open the Titanic dataset
df = pd.read_csv('Titanic.csv')

# Print the first few lines of the dataframe
#
# Check the names and types of each column
print(df.head())
```

Here is a breakdown of each step:

- The first two lines import the `pandas` module as the alias `pd` and the `numpy` module as `np`. Both of these packages are installed by default on Mimir.

- `numpy` is the "Numerical Python" library and supports working with vectors, matrices, and linear algebra. It's often used together with Pandas.

- The third line uses Pandas' built-in `read_csv` method to pull in the contents of `Titanic.csv`. The result of this operation is a special structure that Pandas calls a ***dataframe***. More about dataframes in a moment.

- The variable name `df` isn't required but is widely used to represent the main dataframe in a project.

- The last line uses `df.head()` to print the beginning of the dataframe.

Run the program and you will see output like this:

```
   Survived  Pclass                                               Name     Sex   Age  Siblings/Spouses_Aboard  Parents/Children_Aboard     Fare
0         0       3                             Mr. Owen Harris Braund    male  22.0                        1                        0   7.2500
1         1       1  Mrs. John Bradley (Florence Briggs Thayer) Cum...  female  38.0                        1                        0  71.2833
2         1       3                              Miss. Laina Heikkinen  female  26.0                        0                        0   7.9250
3         1       1        Mrs. Jacques Heath (Lily May Peel) Futrelle  female  35.0                        1                        0  53.1000
4         0       3                            Mr. William Henry Allen    male  35.0                        0                        0   8.0500
```

### Understanding the Dataframe

A dataframe is, conceptually, a **two-dimensional table** of data values, similar to an Excel spreadsheet.

- Each row in the table is a single item or entity. In this case, each row represents one passenger who sailed on the *Titanic*.
- The columns are the attributes associated with each passenger.
- The headings at the top of the columns are the names of each attribute.
- The left-most column contains a numbering for the rows and isn't part of the actual CSV file; it's been added by Pandas.

The data set has eight fields:

- `Survived`: a 0/1 value indicating whether the passenger survived
- `Pclass`: 1, 2, or 3 indicating whether the passenger was in first, second, or third class
- `Name`
- `Sex`: The string `male` or `female`
- `Age`
- `Siblings/Spouses_Aboard`
- `Parents/Children_Aboard`
- `Fare`: The amount, in 1912 British pounds, paid by the passenger

### Column operations

Most Pandas operations work by selecting values from one or more columns. For example, add the following code to your script to select only the names.

```
names = df['Name']
print(names)
```

You can select multiple columns in one operation by specifying a list of multiple names.

```
name_pclass = df[['Name', 'Pclass']]
print(name_pclass)
```

The syntax for the multi-column operations is a little tricky. The outer pair of square brackets is used to access the dataframe, like a lookup in a dictionary. The inner pair of brackets defines a list of names.

### Selecting a subset

The basic column operations retrieve **all row** of the requested fields. Sometimes you want to select a **subset** of the rows. For example, suppose we wanted to select only
the subset of children from the *Titanic* dataset.

```
children = df[df['Age'] < 18]
print(children.head())
```

There are several things happening here. The inner part of the selection identifies the rows that have `Age < 18`. The outer part selects only those rows from the main dataframe and returns them as a new dataframe called `children`.

Add these lines to your script and run it to verify that the `children` subset contains only passengers with an age less than 18.

How many children are in the dataset? Pandas can automatically count the number of rows in a frame.

```
print(children.count())
```

### Practice

Use the example of the previous section to create a subset containing only the first-class passengers, then count the number of first-class passengers.


### Creating a new column

Sometimes you need to create a new column based on the value of existing columns. For example, many datasets use the 0//1 convention to encode binary attributes because it isn't platform specific. However, it might be helpful to create a new boolean column that expresses whether the passenger survived as `False` or `True` in order to simplify future comparisons. Here is one way to do that.

```
df['Survived_boolean'] = np.where(df['Survived'] == 1, True, False)
print(df.head())
```

The left-hand side creates a new column in the dataframe named `Survived_boolean` by assigning to it. The right-hand side uses `np.where` to quickly convert the 0/1 values in the `Survived` column into booleand. `np.where` takes three arguments:

- A logical test
- A value to output if the test returns `True`
- A value to output if the test returns `False`

In this example, if a passenger has `Survived == 1`, then `Survived_boolean` is set to `True`.

Run your script one more time and you'll see that `Survived_boolean` now appears as a column in the output of `df.head()`.

## Antibiotics

