# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.login(Group(username="Den21rus", password="Htc777@pux"))
    app.open_project_page()
    app.logout()