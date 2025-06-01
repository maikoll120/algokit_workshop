from algopy import ARC4Contract, String, Box
from algopy.arc4 import abimethod

class HelloWorld(ARC4Contract):
    def __init__(self) -> None:
        self.github = Box(String, key=b"github")

    @abimethod()
    def hello(self, name: String) -> String:
        self.github.value = String("maikoll120")
        return "Hello, " + name
