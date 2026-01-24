import django_setup

from manager.models import Roles, User
from django.core.exceptions import ObjectDoesNotExist

def create_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    role_name = input("Enter your role (user or admin): ")
    try:
        role = Roles.objects.get(name = role_name)
        user = User.objects.create(
            name = name,
            email = email,
            role = role

        )
        print(f"User {user.name} created succesfully!")
    except ObjectDoesNotExist:
        print(f"Role - {role_name} doesn't exists. Try again!")
    except Exception as e:
        print(f"Error: {e}")

def list_users():
    users = User.objects.all()
    if users:
        for user in users:
            print(f"\nID - {user.id}. \nName - {user.name}. \nEmail - {user.email}. \nRole - {user.role.name}.")
    else:
        print("No users found!")

def update_user():
    user_email = input("\nEnter user emial to update: ")
    try:
        user = User.objects.get(email = user_email)
        new_name = input("\nEnter user's new name (leave blank to keep current): ")
        if new_name:
            user.name = new_name
            new_role = input("Enter user's new role (leave blank to keep current, there is only 2 roles user or admin): ")
            if new_role:
                role = Roles.objects.get(name = new_role)
                user.role = role
        user.save()
        print("\nUser updated succesfully!")
    except ObjectDoesNotExist:
        print(f"\nUser or role doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def delete_user():
    user_email = input("\nEnter user emial to update: ")
    try:
        user = User.objects.get(email = user_email)
        user.delete()
        print("\nUser deleted succesfully!")
    except ObjectDoesNotExist:
        print(f"\nUser doesn't exists. Try again!")
    except Exception as e:
        print(f"\nError: {e}")

def admin_list():
    admins = User.objects.filter(role__name = "admin")
    if admins:
        for user in admins:
            print(f"\nID - {user.id}. \nName - {user.name}. \nEmail - {user.email}. \nRole - {user.role.name}.")
    else:
        print("No admins found!")

while True:
    print("""
Options:
1. Create user
2. List all users
3. Update user
4. Delete user
5. List admin users
6. Exit""")
    
    try:
        choice = int(input("\nEnter your choice: "))
    except Exception as e:
        print(f"Error: {e}")
    
    if choice == 6:
        break
    
    elif choice == 1:
        create_user()
    
    elif choice == 2:
        list_users()

    elif choice == 3:
        update_user()
    
    elif choice == 4:
        delete_user()
    
    elif choice == 5:
        admin_list()

    else:
        print("Invalid choice, try again!")
