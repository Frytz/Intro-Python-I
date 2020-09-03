# Print "Hello, world!" to your terminal




class Hello:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f"{self.name}")

hello = Hello("Hello World")
print(hello)
