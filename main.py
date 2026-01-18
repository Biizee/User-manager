import django_setup

from manager.models import Roles, User


#!--Creating roles
#admin_role = Roles.objects.create(
#    name = "admin"
#)

#admin_role = Roles.objects.create(
#    name = "user"
#)

#!--Finding roles by id
admin_role = Roles.objects.get(id = 1)
user_role = Roles.objects.get(id = 2)

#!--Creating users with roles
#first_user = User.objects.create(
#    name = "Сергій",
#    email = "poczta1@gmail.com",
#    role = user_role
#
#)
#
#second_user = User.objects.create(
#    name = "Степан",
#    email = "poczta2@gmail.com",
#    role = admin_role
#
#)

#!--Finding users by id
first_user = User.objects.get(id = 1)
second_user = User.objects.get(id = 2)

#!--Printing users name and roles
print(first_user.name + " має роль - " + first_user.role.name)
print(second_user.name + " має роль - " + second_user.role.name)


#!--Changing user role and printing new role
second_user.role_id = "2"
second_user.save()
print(second_user.name + " має роль - " + second_user.role.name)
