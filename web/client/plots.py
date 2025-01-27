import json
import plotly as py
import plotly.express as px
import pandas as pd


def prob_graph(labels, pred):
    data = pd.DataFrame(pred, labels, columns=["probability"])
    fig = px.bar(data_frame=data, x=data.index, y="probability",
                 color="probability", title="옷 분류별 확률")
    graphJSON = json.dumps(fig, cls=py.utils.PlotlyJSONEncoder)
    return graphJSON