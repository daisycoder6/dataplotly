#######
# Side-by-side heatmaps for Sitka, Alaska,
# Santa Barbara, California and Yuma, Arizona
# using a shared temperature scale.
######
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

dfframe = pd.read_csv('results.csv')

ecg = dfframe[dfframe['Conditions']=='ecg']
resp = dfframe[dfframe['Conditions']=='resp']
pace = dfframe[dfframe['Conditions']=='pace']

ecgdata = ecg['ch1'].append([ecg['ch2'],ecg['ch3'],ecg['ch4'],ecg['ch5']])
respdata = resp['ch1'].append([resp['ch2'],resp['ch3'],resp['ch4'],resp['ch5']])
pacedata = pace['ch1'].append([pace['ch2'],pace['ch3'],pace['ch4'],pace['ch5']])


trace1 = go.Histogram(
    x=ecgdata,
 
)
trace2 = go.Histogram(
    x=respdata
)
trace3 = go.Histogram(
    x=pacedata
)

fig = tools.make_subplots(rows=2, cols=3,
    subplot_titles=('ECG','Resp', 'Pace'),
    shared_yaxes = True,  # this makes the hours appear only on the left
)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)

fig['layout'].update(      # access the layout directly!
    title='Noise Data Conditions'
)
pyo.plot(fig, filename='AllThree.html')
