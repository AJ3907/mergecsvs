Python 2.7 was used. I Have merged according to inner join.

How to run?

1) go to the directory containing the csvs. (You can also specify the path in the code.)
2) in command line type: python merge.py <common_column_name> ( eg. : merge.py email)
3) output.csv will be generated.

Assumption:

In case of csv files with multiple columns other than 1 column("email"):
Suppose two csvs have email, Value1 and email, Value1 as their columns, then I assume, both the value1 columns will have same values in both the csvs corresponding to their email column, as in merging I will skip the same columns in the second csv.

I have handled the situation in case two rows have same email in a csv and have different values, by indexing using list of list.
