### EDA

def uniqueness_overview(df, columns=None):
    """Print number of unique and proportion of unique 
       values per column of a pd.DataFrame.
       Args:
           df (pd.DataFrame): data frame
           columns (list(str)): columns compute
    """
    if columns is None:
        columns = df.columns
    for column in columns:
        uniques = len(df[column].value_counts())
        print("col. {0:8}: {1:6} uniques values ({2:2.2f}%) ".format(column, uniques, (uniques / len(df[column])) * 100, ))


