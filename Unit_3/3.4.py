class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, illegal_character, position):
        self.illegal_character = illegal_character
        self.position = position

    def __str__(self):
        return f"The username contains an illegal character '{self.illegal_character}' at position {self.position}."


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short. It must be at least 3 characters long."


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long. It must be at most 16 characters long."


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character."


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    # Check username
    if not all(c.isalnum() or c == '_' for c in username):
        for i, c in enumerate(username):
            if not c.isalnum() and c != '_':
                raise UsernameContainsIllegalCharacter(c, i)
    if len(username) < 3:
        raise UsernameTooShort
    if len(username) > 16:
        raise UsernameTooLong

    # Check password
    mandatory_characters = {'uppercase': False, 'lowercase': False, 'digit': False, 'special': False}
    for c in password:
        if c.isupper():
            mandatory_characters['uppercase'] = True
        elif c.islower():
            mandatory_characters['lowercase'] = True
        elif c.isdigit():
            mandatory_characters['digit'] = True
        elif c in string.punctuation:
            mandatory_characters['special'] = True

    for char_type, is_present in mandatory_characters.items():
        if not is_present:
            if char_type == 'uppercase':
                raise PasswordMissingUppercase
            elif char_type == 'lowercase':
                raise PasswordMissingLowercase
            elif char_type == 'digit':
                raise PasswordMissingDigit
            elif char_type == 'special':
                raise PasswordMissingSpecial

    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong, PasswordMissingCharacter) as e:
            print(e)


if __name__ == "__main__":
    main()
