# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.create_group(Group(name="new", header="test", footer="new test group"))
        app.return_to_group_page()
        app.logout()


def test_add_empty_group(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.return_to_group_page()
        app.logout()