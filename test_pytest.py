#! /usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    print("----",some_data)
    assert some_data==42
