# -*- coding: utf-8 -*-
from model.group import Group


def test_case(app):
    app.session.login(Group(username="Den21rus", password="Htc777@pux"))
    app.project.open_project_page()
    app.session.logout()