import pytest
import json
import logging
from src.core import Core


@pytest.mark.parametrize('input,output',[
    ('./tests/data/core/1.json',"100")
])
def test_core_1(input,output):
    with open(input,'r') as f:
        input_data = json.load(f)
    core = Core(logging)    
    assert {"predict":output} == core.run(input_data)