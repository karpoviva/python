from model.group import Group


def test_delete_group(app):
    if app.group.count_group() == 0:
        app.group.create(Group(name="test"))
    app.group.open_home_page()
    app.group.delete_first_group()
