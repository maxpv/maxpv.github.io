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
        
    max_column_width = str(len(max(columns, key=len)))
    for column in columns:
        uniques = len(df[column].value_counts())
        s="col. {0:"+max_column_width+"}: {1:6} uniques values ({2:2.2f}%)"
        print(s.format(column, uniques, (uniques / len(df[column])) * 100, ))
