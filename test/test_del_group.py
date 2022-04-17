from model.group import Group

def test_delete_first_group(app):
    app.session.login(Group(username="Den21rus", password="Htc777@pux"))
    app.project.deleted_first_group()
    app.session.logout()