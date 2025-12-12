import pandas as pd
from process_sales import clean_and_transform

def test_clean_and_transform():
    sample = {
        "product": ["Pink Morsel", "Blue Morsel"],
        "quantity": [10, 5],
        "price": [2, 3],
        "date": ["2023-01-01", "2023-01-02"],
        "region": ["North", "South"]
    }

    df = pd.DataFrame(sample)
    result = clean_and_transform(df)

    assert len(result) == 1
    assert result.iloc[0]["Sales"] == 20
    assert list(result.columns) == ["Sales", "date", "region"]
