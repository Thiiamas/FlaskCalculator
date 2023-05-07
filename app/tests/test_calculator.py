import os
import tempfile
import xmltojson
import json

import pytest

def test_simple_Addition(client):
    response = client.post("/",data=dict(Input1=1, Input2=1,Operation="+"))
    print("print")
    print(response.data)
    assert b"<p>The calculation for 1.0 + 1.0 is: 2.0</p>" in response.data

def test_simple_Multiplication(client):
    client.get("/")
    response = client.post("/",data=dict(Input1=2, Input2=1,Operation="*"))
    print("print")
    print(client.get('/').data)
    assert b"<p>The calculation for 2.0 * 1.0 is: 2.0</p>" in response.data

def test_simple_Division(client):
    response = client.post("/",data=dict(Input1=4, Input2=2,Operation="/"))
    print("print")
    print(response.data)
    assert b"<p>The calculation for 4.0 / 2.0 is: 2.0</p>" in response.data