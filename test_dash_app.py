from app import app
import dash_html_components as html
import dash_core_components as dcc

def test_header_present():
    layout = app.layout
    headers = [c for c in layout.children if isinstance(c, html.H1)]
    assert len(headers) == 1
    assert "Pink" in headers[0].children

def test_graph_present():
    layout = app.layout
    graphs = [
        c for c in layout.children
        if isinstance(c, dcc.Graph)
    ]
    assert len(graphs) >= 1  # checks the graph exists

def test_region_picker_present():
    layout = app.layout
    radios = [
        c for c in layout.children
        if isinstance(c, dcc.RadioItems)
    ]
    assert len(radios) == 1
    expected = {"north", "east", "south", "west", "all"}
    found = {opt["value"] for opt in radios[0].options}
    assert found == expected
