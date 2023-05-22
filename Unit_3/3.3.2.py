class UnderAge(Exception):
    def __str__(self):
        return "Your age is less than 18. In a few years, you'll be able to reach Ido's birthday!"

def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)

send_invitation("John", 17)
send_invitation("Alice", 20)
