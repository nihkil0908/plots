import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models.tools import HoverTool
from bokeh.plotting import figure, curdoc

df = pd.read_csv('https://raw.githubusercontent.com/nihkil0908/plots/master/nik.csv')
#print(df)
#df.columns.tolist()
#sample = df.sample(31)
source = ColumnDataSource(df)
#print(df['Rank'])
p = figure()
p.circle(x='Rank', y='Population',
         source=source,
        size=15, color='green')
hover = HoverTool()
hover.tooltips=[
    ('Attack Date', '@Rank'),
    ('Attacking Aircraft', '@Population'),
    ('Tons of Munitions', '@State'),
    ('Type of Aircraft', '@Postal')
]
df.to_json(orient='index')
p.add_tools(hover)
show(p)
curdoc().add_root(p)
