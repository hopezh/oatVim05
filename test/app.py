import glob

from dash import (
    Dash,
    callback,
    callback_context,
    dcc,
    dash_table,
    html,
    Input,
    Output,
    State,
)
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

import numpy as np
import pandas as pd

from util.footer import footer
from util.components import create_fig
from util.components import create_fig_annotated
from util.components import source_data_table


# oat: get a list of csv in data folder
# csv_list = sorted(glob.glob("./data/*.csv"))
csv_list = sorted(glob.glob("./data_test/*.csv"))
# print(csv_list)


# oat: init dash app -----------------------------------------------------------
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
    ],
)

# oat: create app layout -------------------------------------------------------
app.layout = dbc.Container(
    [
        # o: 1. title
        dbc.Row(
            [
                dbc.Col(
                    html.H2("qela test"),
                )
            ],
            # className="h-20",
        ),
        # o: 2. content
        dbc.Row(
            [
                # o: 2.1 1st row: inputs and submit button
                dbc.Row(
                    [
                        # o: 2.1.1 left column: inputs
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    id="csv_selector",
                                    multi=False,
                                    options=csv_list,
                                    value=csv_list[0],
                                    placeholder="Select a csv file",
                                ),
                                dcc.Checklist(
                                    id="show_name",
                                    options=["show name"],
                                    value=[],
                                ),
                                # html.Div(id="checklist_status"),
                            ],
                            width=12,
                            lg=11,
                        ),
                        # o: 2.1.2 right column: submit button
                        dbc.Col(
                            [
                                dbc.Button(
                                    id="submit-button",
                                    children="Submit",
                                    n_clicks=0,
                                    color="primary",
                                ),
                            ],
                            width=12,
                            lg=1,
                        ),
                    ]
                ),
                # o: 2.2 2nd row: graph
                dbc.Row(
                    [dcc.Graph(id="chart", figure={})],
                    # className="h-50",
                ),
                # o: 2.3 3rd row: source data table
                dbc.Row(
                    [source_data_table(csv_list[0])],
                    # className="h-50",
                ),
            ],
            # className="h-60",
            # className="ms-1",
        ),
        # o: 3. footer
        dbc.Row(
            [dbc.Col(footer)],
            # className="h-20",
        ),
    ],
    fluid=True,
    style={"height": "100vh"},
)


# o: cb to update chart  -------------------------------------------------------
@app.callback(
    Output("chart", "figure"),
    [
        # Input("submit-button", "n_clicks"),
        Input("csv_selector", "value"),
        Input("show_name", "value"),
    ],
)
def update_graph(csv_selected, show_name):
    if not csv_selected:
        raise PreventUpdate
    elif csv_selected and not show_name:
        print("csv selected:", csv_selected, "\n")
        # create layout
        fig = create_fig(csv_selected)
        return fig
    elif csv_selected and show_name:
        fig = create_fig_annotated(csv_selected)
        return fig


# o: cb to update source data table --------------------------------------------
@app.callback(
    Output("table_source_data", "data"), 
    [
        Input("csv_selector", "value"),
    ]
)
def update_source_data_table(csv_selected):
    if not csv_selected:
        raise PreventUpdate
    else:
        df = pd.read_csv(csv_selected)
        data = df.to_dict("records")
        return data


# run server -------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(
        debug=True,
        # port=8050,
    )
