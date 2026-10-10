class User:
  def __init__(self, first_name, last_name, location, hobby):
    self.first_name = first_name
    self.last_name = last_name
    self.location = location
    self.hobby = hobby
    self.login_attempts = 0

  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0

  def describe_user(self):
    print(f"The user's full name is {self.first_name.title()} {self.last_name.title()}.\nThis user lives in {self.location.title()}.\nThis user's hobby is {self.hobby}.")

  def greet_user(self):
    print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

elia = User("elia", "ghazal", "lebanon", "coding")
elia.describe_user()
elia.greet_user()

george = User("george", "khayat", "lebanon", "basketball")
george.describe_user()
george.greet_user()

elia.increment_login_attempts()
elia.increment_login_attempts()
elia.increment_login_attempts()
elia.increment_login_attempts()
print(elia.login_attempts)
elia.reset_login_attempts()
print(elia.login_attempts)

class Admin(User):

  def __init__(self, first_name, last_name, location, hobby):
    super().__init__(first_name, last_name, location, hobby)
    self.privileges = ["can add post", "can delete post", "can ban user"]

  def show_privileges(self):
    for privilege in self.privileges:
      print(privilege)

brian = Admin("Brian", "smith", "USA", "football")
brian.show_privileges()

class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin2(User):

  def __init__(self, first_name, last_name, location, hobby):
    super().__init__(first_name, last_name, location, hobby)
    self.privileges = Privileges()

sam = Admin2("sam", "winchester", "Texas", "researching")
sam.privileges.show_privileges()
