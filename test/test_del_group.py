

def test_delete_group(app):
    app.group.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()