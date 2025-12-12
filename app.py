import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("formatted_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "Sales": "Total Sales ($)"}
)

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children="Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(id="sales-line-chart", figure=fig),
    html.Div(
        children=("Sales before and after the Pink Morsel price increase on "
                  "15 January 2021."),
        style={"textAlign": "center", "marginTop": "20px"}
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
