import pytest
from app import app

@pytest.fixture
def dash_app():
    return app

def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text

def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio = dash_duo.find_element("#region-picker")
    assert radio is not None
