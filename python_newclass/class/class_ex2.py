class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def fromTuple(cls, tup):
        return cls(tup[0], tup[1])

    @classmethod
    def fromDictionary(cls, dic):
        return cls(dic["email"], dic["passwrod"])


new = User("test1@test.com", "11111")
new2 = User("test2@test.com", "22222")

USER = User.fromTuple(("user@test.com", "1234"))

print(new.email, new.password)
print(new2)
print(USER.email, USER.password)
