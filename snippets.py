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
        
### Feature engineering

# This is not optimal for large datasets
from sklearn.base import BaseEstimator, TransformerMixin
class CyclicClockTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        print(type(X[0][0]))
        seconds = np.array([(d.minute * 60 + d[0].hour*60*60) for d in pd.DatetimeIndex(X)])
        sec_cos = np.sin(2*np.pi*seconds/24*60*60)
        sec_sin = np.cos(2*np.pi*seconds/24*60*60)
        return [sec_cos, sec_sin]
