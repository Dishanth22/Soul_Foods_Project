import pytest
from dash import Dash
from app import app

# Dash provides an internal test client we can use without Selenium
@pytest.fixture
def test_client():
    return app.test_client()

def test_header_present():
    response = app.test_client().get("/")
    assert b"Pink Morsel Sales Visualiser" in response.data

def test_graph_present():
    response = app.test_client().get("/")
    # check ID of line chart
    assert b"id=\"sales-line-chart\"" in response.data

def test_region_picker_present():
    response = app.test_client().get("/")
    # check ID of region radio buttons
    assert b"id=\"region-picker\"" in response.data
