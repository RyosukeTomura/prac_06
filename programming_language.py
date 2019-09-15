class ProgrammingLanguage:

#like most init functions, create the fields and set them to the parameters passed in
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)

    #which returns True/False if the programming language is dynamically typed or not
    def is_dynamic(self):
        return self.typing == "Dynamic"


