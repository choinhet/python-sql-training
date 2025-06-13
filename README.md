# Python and SQL training

## Intro

This training does not aim in diving deep in the smallest concepts and well-known 
and distributed knowledge of programming basics, such as for-loops,
if statements, and so on. 

The main idea is to provide you challenges so that you can look for required concepts
yourself and start building the most important programming foundation: 'Googling' (Or 'GPTing')

I'd recommend that you type all the code by yourself so you don't get fooled by the
idea that you already got everything while if you were on a plane, you'd be useless.

Typing should help with memorizing. Giving your brain more time to process the information
it's currently soaking.

## Starters

Let's start with SQL, the almighty database and data manipulation language.
Its concepts are widely spread even when not directly applied to SQL code.
I want you to initially take a grasp on the following concepts:

- Granularity
- Attributes/Measures/Constants
- Star Schema
- The OLAP cube

Go ahead and give those a proper search, watch a video or two about them.
After you thought you understood everything, come back here and let's start the training.

### SQL Training

#### Store Sales

Suppose we have to keep track of the sales across multiple stores. Those stores share multiple
products. And each store has a bunch of sales every day. You have one huge table
with the following columns:

Date, Value, ProductId, ProductName, StoreId, StoreName, Category, Subcategory, 
State, Street, Country;

Theoretical Questions:

- Which are the columns that have the biggest variance across the data?
- What is the difference of storing a column that varies in comparison to one that is constant most of the time?
- How could we optimize the storage?

Code time!

##### Lesson 01

Create an optimized structure for that storage! We have a big table stored as a CSV in
`python_sql_training/lesson_01/resources/big.parquet`.

Guidelines:

You should use Python's duckdb interface. It's super simple. 
It's a library that allows us to manipulate data in an SQL manner within Python.
I'll give you an example of how that works, by having the worst way of stealing resources
from the database: the select all.

This script can be found at: `python_sql_training/lesson_01/example.py`
To run it, check the `RUNNING_SCRIPTS.md` file.

```py
import duckdb

if __name__ == "__main__":
    duckdb.query(
        """
        select *
        from read_parquet('resources/big.parquet')
        """
    ).show()
```

The output should be saved in `lesson_01/resources` folder. There is an example of 
a bad solution at: `python_sql_training/lesson_01/bad_solution.py`. This should be
used as an example on where and how to save the optimized data. Be aware you
can use multiple queries if you want.

There is an acceptable solution in the solution folder.

##### Lesson 02

For this lesson, we'll be using the concepts of the star schema.
The queries should be easy to create.

There is an acceptable solution in the solution folder.

##### Assignment

Using the solution for Lesson 01, answer the following questions:

- Which are the total sales by store?
- Which are the total sales by product?
 
##### Lesson 03

Let's use some different concepts. Go ahead and search a bit about window functions.
We'll explore some cool use cases for it.

There is an acceptable solution in the solution folder.

##### Assignment

Using the solution for Lesson 01, answer the following questions:

- Which is the total share by store?
- ...