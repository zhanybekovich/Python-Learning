# positional parameters
def birthday1(name, age):
    print("Happy Birthday", name, "!", "You are", age, "years old, aren't you?")

def birthday2(name="Ivanov", age=1):
    print("Happy Birthday", name, "!", "You are", age, "years old, aren't you?")

birthday1("Ivanov", 1)
#birthday1("Ivanov")
birthday1(name="Ivanov", age=1)
birthday1(age=1, name="Ivanov")

birthday2()
birthday2(name="Kate")
birthday2(age=12)
birthday2(name="Kate", age=12)
birthday2("Kate", 12)
