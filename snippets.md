## Keras

```python
def get_imagenet_classes():
    CLASS_INDEX_PATH = 'https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json'
    fpath = get_file('imagenet_class_index.json',
                     CLASS_INDEX_PATH,
                     file_hash='c2c37ea517e94d9795004a39431a14cb')
    with open(fpath) as f:
        return [values[1] for key, values in json.load(f).items()]
```

Usage:
```
# Example
get_imagenet_classes()[0:5]
# Output: ['tench', 'goldfish', 'great_white_shark', 'tiger_shark', 'hammerhead']
```
-----

```python
# forked from: gist.github.com/stared/dfb4dfaf6d9a8501cd1cc8b8cb806d2e
class PlotLosses(keras.callbacks.Callback):
    def __init__(self, skip=5, refresh_rate=5, figsize=(17,10), zoom_delta=7):
        self.skip = skip
        self.refresh_rate=5
        self.figsize=figsize
        self.fig = plt.figure()
        self.zoom_delta = zoom_delta
        
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []

        self.logs = []

    def on_epoch_end(self, epoch, logs={}):
        last_loss = logs.get('loss')
        last_val_loss = logs.get('val_loss')

        self.x.append(self.i)
        self.losses.append(last_loss)
        self.val_losses.append(last_val_loss)
        self.i += 1
        
        if((self.i % self.refresh_rate == 0 and self.i > self.skip) or self.i == self.skip):
            clear_output(wait=True)
            fig = plt.figure(figsize=self.figsize)
            ax = fig.add_subplot(2, 1, 1)
            ax.plot(self.x[self.skip:], self.losses[self.skip:], label="loss")
            ax.plot(self.x[self.skip:], self.val_losses[self.skip:], label="val_loss")
            plt.title("{0:.4} loss & {1:.4} validation loss (epoch={2})".format(last_loss, last_val_loss, self.i))
            plt.legend()
            
            if(self.i > 100):
                axins = zoomed_inset_axes(ax, 2, loc=7)
                axins.plot(self.x[self.skip:], self.losses[self.skip:])
                axins.plot(self.x[self.skip:], self.val_losses[self.skip:])
                last_epochs = slice(self.i-self.zoom_delta-1,self.i-1)
                axins.set_xlim(last_epochs.start, last_epochs.stop)
                min_y = min(min(self.losses[last_epochs]), min(self.val_losses[last_epochs]))
                max_y =  max(max(self.losses[last_epochs]), max(self.val_losses[last_epochs]))
                axins.set_ylim(min_y, max_y)
                mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec="0.5")

            plt.show()
```

Usage:
```
model2.fit(X_train, y_train, (...), callbacks=[PlotLosses()])
```

## EDA

```python
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
```

----

```python
def corr_sub_plot(ax, df, title=""):
    corr = df.corr()
    avg_corr = corr.values[np.triu_indices_from(corr.values,1)].mean()
    ax.set_title(title+" ({0:.4})".format(avg_corr))
    
    labels = corr.columns
    if len(corr.columns) > 15:
        labels=range(1,len(corr.columns),4)

    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_yticks(np.arange(len(df.columns)))
    ax.set_yticklabels(df.columns)
    ax.set_xticklabels(df.columns)
    return ax.imshow(corr, interpolation="nearest", cmap=colmap, vmin=-1, vmax=1)
```

Usage:
```python
corr_sub_plot(ax[0,0], train.iloc[features_array], title="First subplot")
corr_sub_plot(ax[0,1], train.iloc[features_array2], "Second subplot")
cax = corr_sub_plot(ax[1,0], train.iloc[features_array3], "Third subplot")

# To normalize plots' colors 
f.colorbar(cax, ax=ax.ravel().tolist()) 
```

-----

## Feature engineering

```python
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
```

-----
