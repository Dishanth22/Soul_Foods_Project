dcc.RadioItems(
    id="region-picker",
    options=[
        {"label": region.capitalize(), "value": region}
        for region in ["all", "north", "south", "east", "west"]
    ],
    value="all"
)
