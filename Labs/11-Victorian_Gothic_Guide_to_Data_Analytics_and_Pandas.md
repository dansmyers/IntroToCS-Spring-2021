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
[*Project-Based R Companion to Introductory Statistics*](https://www.taylorfrancis.com/books/mono/10.1201/9780429292002/project-based-companion-introductory-statistics-chelsea-myers?context=ubx&refId=262ee6fc-50b7-4b79-a116-d508a2270467).
She has &ndash; let's call it &ndash; a *fascination* with weird and morbid 19th Century data sets, which is one of her many excellent qualities.

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





