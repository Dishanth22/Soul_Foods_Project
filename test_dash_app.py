from app import app
import dash_html_components as html
import dash_core_components as dcc

def test_header_present():
    layout = app.layout
    # Look for an H1 component
    headers = [c for c in layout.children if isinstance(c, html.H1)]
    assert len(headers) == 1
    assert "Pink" in headers[0].children

def test_graph_present():
    layout = app.layout
    graphs = [
        c for c in layout.children 
        if isinstance(c, dcc.Graph)
    ]
    assert len(graphs) >= 1

def test_region_picker_present():
    layout = app.layout
    radios = [
        c for c in layout.children
        if isinstance(c, dcc.RadioItems)
    ]
    assert len(radios) == 1
    # Test options
    expected = {"north", "east", "south", "west", "all"}
    found = {opt["value"] for opt in radios[0].options}
    assert expected == found
