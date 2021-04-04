import json
import plotly
from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
import pandas as pd
import numpy as np



app = Flask(__name__)


# TODO: import CSV and Perform ETL
# TODO: Prepare plotly visualizations for Dashboard
# TODO: adjust Index page
# TODO: running the app and preparing the port
# TODO: Adjusting README.md for Instructions for running the app

@app.route('/')
@app.route('/index')
def index():
    # extract data needed for visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)

    count = list(df.iloc[:, 4:].groupby('related').count().iloc[:, 1])
    message_type = ['Not Related', 'Related']

    # create visuals
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=message_type,
                    y=count
                )
            ],

            'layout': {
                'title': 'Counts of Related/Not-related messages',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Type"
                }
            }
        }
    ]

    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    # render web page with plotly graphs
    return render_template('index.html', ids=ids, graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)