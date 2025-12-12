from app import app
from dash import html, dcc

def find_components(component, component_type):
    found = []
    if isinstance(component, component_type):
        found.append(component)
    children = getattr(component, "children", None)
    if isinstance(children, list):
        for child in children:
            found.extend(find_components(child, component_type))
    elif children is not None:
        found.extend(find_components(children, component_type))
    return found

def test_header_present():
    layout = app.layout
    headers = find_components(layout, html.H1)
    assert len(headers) >= 1
    assert "Pink Morsel Sales Visualiser" in headers[0].children

def test_graph_present():
    layout = app.layout
    graphs = find_components(layout, dcc.Graph)
    assert len(graphs) == 1
    assert graphs[0].id == "sales-line-chart"

def test_region_picker_present():
    layout = app.layout
    radios = find_components(layout, dcc.RadioItems)
    assert len(radios) == 1
    assert radios[0].id == "region-picker"

