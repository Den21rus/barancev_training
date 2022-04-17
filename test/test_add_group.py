# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.session.login(Group(username="Den21rus", password="Htc777@pux"))
    app.project.open_project_page()
    app.session.logout()