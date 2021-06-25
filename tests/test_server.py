from fastapi.testclient import TestClient
from server import app
import json
import pytest
import logging
client = TestClient(app)


@pytest.mark.parametrize('input,output', [
    ('./tests/data/core/1.json', './tests/data/output/1.json')
])
def test_read_main(input, output):
    with open(input, 'r') as f:
        input_data = json.load(f)
    with open(output, 'r') as f:
        output_data = json.load(f)
    logging.info(f"{input_data}")
    res = client.post("/", json=input_data)

    assert res.status_code == 200
    assert res.json() == output_data
