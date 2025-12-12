import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load cleaned data
df = pd.read_csv("formatted_sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize Dash app
app = Dash(__name__)

# ------------------------
# APP LAYOUT
# ------------------------
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f8",
        "padding": "20px",
        "fontFamily": "Arial",
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "40px",
            },
        ),

        html.Div(
            style={"width": "60%", "margin": "0 auto", "textAlign": "center"},
            children=[
                html.H3("Filter by Region:", style={"color": "#34495e"}),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All Regions", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "30px"},
                ),
            ],
        ),

        dcc.Graph(id="sales-line-chart"),
    ],
)

# ------------------------
# CALLBACK FOR FILTERING
# ------------------------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="Sales",
        title=f"Pink Morsel Sales ({selected_region.title() if selected_region != 'all' else 'All Regions'})",
        labels={"date": "Date", "Sales": "Total Sales ($)"},
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f8",
        title_font_size=24,
        xaxis=dict(showgrid=True, gridcolor="#e0e0e0"),
        yaxis=dict(showgrid=True, gridcolor="#e0e0e0"),
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
