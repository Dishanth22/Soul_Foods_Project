import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load cleaned data
df = pd.read_csv("formatted_sales.csv")

# Convert and sort dates
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize Dash app
app = Dash(__name__)

# App Layout
app.layout = html.Div(
    children=[
        html.H1(
            children="Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#E91E63",
                "fontFamily": "Arial",
                "marginTop": "20px",
            },
        ),

        html.Div(
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontSize": "20px", "marginRight": "10px"}
                ),
                dcc.RadioItems(
                    id="region-picker",
                    options=[
                        {"label": region.capitalize(), "value": region}
                        for region in ["all", "north", "south", "east", "west"]
                    ],
                    value="all",
                    inline=True,
                    style={
                        "fontSize": "18px",
                        "padding": "10px",
                        "marginBottom": "20px",
                    },
                ),
            ],
            style={"textAlign": "center"},
        ),

        dcc.Graph(
            id="sales-line-chart",
            style={"width": "90%", "margin": "auto"},
        ),
    ],
    style={"backgroundColor": "#FFF0F5", "paddingBottom": "40px"},
)

# Callback to update graph based on region
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-picker", "value")
)
def update_graph(selected_region):

    # Filter data by region (unless "all")
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Create the line chart
    fig = px.line(
        filtered_df,
        x="date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time — {selected_region.capitalize()} Region",
        labels={"date": "Date", "Sales": "Total Sales ($)"},
    )

    fig.update_layout(
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFF0F5",
        font=dict(color="#880E4F", size=14)
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)
