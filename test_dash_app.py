from app import app
from dash import html, dcc

# Recursive search helper
def find_all(component, component_type):
    found = []

    # If the component itself is the target
    if isinstance(component, component_type):
        found.append(component)

    # If the component has children, search inside them
    if hasattr(component, "children"):
        children = component.children

        if isinstance(children, list):
            for child in children:
                found.extend(find_all(child, component_type))
        elif children is not None:
            found.extend(find_all(children, component_type))

    return found


def test_header_present():
    layout = app.layout
    headers = find_all(layout, html.H1)
    assert len(headers) == 1
    assert "Pink Morsel Sales Visualiser" in headers[0].children


def test_graph_present():
    layout = app.layout
    graphs = find_all(layout, dcc.Graph)
    assert len(graphs) == 1
    assert graphs[0].id == "sales-line-chart"


def test_region_picker_present():
    layout = app.layout
    radios = find_all(layout, dcc.RadioItems)
    assert len(radios) == 1  # there is exactly one region picker

    radio = radios[0]
    assert radio.id == "region-picker"

    expected_values = {"all", "north", "south", "east", "west"}
    actual_values = {opt["value"] for opt in radio.options}

    assert actual_values == expected_values
