import json
import pandas as pd
import plotly.express as px

import dash
from dash import dcc, html, Input, Output

# Load data
df = pd.read_csv("data/data_cdsh.csv")
with open("data/california-counties.geojson") as f:
    counties = json.load(f)

# Grouping options
group_options = {
    "Ethnicity": ["Black", "White", "Hispanic", "Asian", "Native_American", "Other_missing"],
    "Age": ["17_and_Under", "18-64", "65_and_Over"],
    "Gender": ["Female", "Male"],
}

# Initialize app
app = dash.Dash(__name__)
app.title = "California Health and Human Services Programs"

# Layout
app.layout = html.Div([
    html.H1("California Health and Human Services Programs"),
    
    html.Div([
        html.Label("Program:"),
        dcc.Dropdown(df["Program"].unique(), id="program", value="CalFresh"),
        
        html.Label("Year:"),
        dcc.Dropdown(df["Year"].unique(), id="year", value=2021),
        
        html.Label("View by:"),
        dcc.Dropdown(["Person", "Ethnicity", "Age", "Gender"], id="view", value="Person"),
    ], style={"width": "30%", "display": "inline-block", "verticalAlign": "top"}),

    dcc.Graph(id="map"),

    html.Div([
        html.Label("County:"),
        dcc.Dropdown(["All"] + sorted(df["County"].unique()), id="county", value="All"),

        html.Label("Breakdown:"),
        dcc.Dropdown(["Ethnicity", "Age", "Gender"], id="bar_group", value="Ethnicity")
    ], style={"width": "30%", "display": "inline-block", "verticalAlign": "top"}),

    dcc.Graph(id="bar"),
])

# Callbacks
@app.callback(
    Output("map", "figure"),
    Input("program", "value"),
    Input("year", "value"),
    Input("view", "value"),
)

def update_map(program, year, view):
    dff = df[(df["Program"] == program) & (df["Year"] == year)]

    if view == "Person":
        dff["value"] = dff["Person"]
        color_title = "People"
    else:
        group = group_options[view]
        dff["value"] = dff[group].sum(axis=1) / dff["Person"]
        color_title = f"% {view}"

    fig = px.choropleth(
        dff,
        geojson=counties,
        locations="County",
        featureidkey="properties.name",
        color="value",
        color_continuous_scale="Viridis",
        scope="usa",
        labels={"value": color_title},
        title=f"{program} in {year} – {view}",
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig

@app.callback(
    Output("bar", "figure"),
    Input("program", "value"),
    Input("county", "value"),
    Input("bar_group", "value"),
)

def update_bar(program, county, group_type):
    dff = df[df["Program"] == program]
    if county != "All":
        dff = dff[dff["County"] == county]

    group_cols = group_options[group_type]
    dff = dff.groupby("Year")[group_cols].sum().reset_index()
    dff = pd.melt(dff, id_vars="Year", value_vars=group_cols, var_name=group_type, value_name="Count")

    fig = px.bar(dff, x="Year", y="Count", color=group_type, barmode="stack",
                title=f"{group_type} Breakdown by Year – {county if county != 'All' else 'California'}")
    return fig

# Run server
if __name__ == "__main__":
    app.run(debug=True)