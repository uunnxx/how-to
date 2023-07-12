class Email:
    def __init__(self, address):
        self._email = address

    def _set_email(self, value):
        if '@' not in value:
            print("This is not an email address.")
        else:
            self._email = value

    def _get_email(self):
        return self._email

    def _del_email(self):
        print("Erase this email attribute!")
        del self._email

    # The interface provides the public attribute email
    email = property(_get_email, _set_email, _del_email, 'This property contains the email.')


print()
m1 = Email("kp1@othermail.com")
print(m1.email)

m1.email = "kp2@othermail.com"
print(m1.email)

m1.email = "kp2.com"
del m1.email


class Email2:
    def __init__(self, address):
        self._email = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            print("This is not an email address.")
        else:
            self._email = value

    @email.deleter
    def email(self):
        print("Erase this email attribute!")
        del self._email

    # The interface provides the public attribute email
    # email = property(_get_email, _set_email, _del_email, 'This property contains the email.')


print()
m2 = Email2("kp1@othermail.com")
print(m2.email)

m2.email = "kp2@othermail.com"
print(m2.email)

m2.email = "kp2.com"
del m2.email
