# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(fname="Albert", sname="Ivanovich", lname="Petrov", address="Nikolaevskiy avenu",
                               email="nik0007@sina.com", tel="+79994447878"))
    app.session.logout()
