from model.group import Group

def test_modify_group_name(app, db, check_ui):
    if app.group.count == 0:
        app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
 #   app.open_home_page()
 #   if app.group.count() == 0:
 #       app.group.create(Group(name="test"))
 #   app.group.modify_first_group(Group(header="New header"))



