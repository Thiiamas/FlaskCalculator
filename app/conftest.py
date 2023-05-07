import pytest
from flask import Flask, render_template,request
from app import create_app

app = create_app()
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client