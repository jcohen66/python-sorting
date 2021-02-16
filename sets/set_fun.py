mystring = "This is awesome"
print(mystring)

# Set of unique chars but unordered
mystring_set = set(mystring)
print(mystring_set)
for c in mystring_set:
    print(c, end=" ")

# List of unique chars but now in default order
mystring_list = list(mystring_set)
print(mystring_list)


mylist = ["c", "c", "a", "b"]
mynewlist = list(set(mylist))
# Note the new order.
print(mynewlist)

# this is the set of permissions before vchange:
original_permission_set = {"is_admin", "can_post_entry", "can_view_entry", "can_view_settings"}

# this is new set of permissions
new_permission_set = {"can_edit_settings", "is_member", "can_view_entry", "can_edit_entry"}

# now permissions to add will be:
x = new_permission_set.difference(original_permission_set)
print(x)

# As you can see can_edit_entry is in both sets so we dont need
# to worry about handling it

# now permissions to remove will be:
x = original_permission_set.difference(new_permission_set)
print(x)

# and basically it's also true; we switched admin to member, and add
# more permission on settings; and removed the post-entry permission

