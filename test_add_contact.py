# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(fname="Albert", sname="Ivanovich", lname="Petrov", address="Nikolaevskiy avenu",
                            email="nik0007@sina.com", tel="+79994447878"))
    app.logout()

