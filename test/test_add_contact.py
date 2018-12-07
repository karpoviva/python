# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(fname="Albert", sname="Ivanovich", lname="Petrov", address="Nikolaevskiy avenu",
                               email="nik0007@sina.com", tel="+79994447878"))

