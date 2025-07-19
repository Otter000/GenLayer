# { "Depends": "py-genlayer:test" }

from genlayer import *

class NumberGuess(gl.Contract):
    secret_number: u8
    attempts: u32
    last_response: str

    def __init__(self):
        self.secret_number = u8(5)
        self.attempts = 0
        self.last_response = "The game has started! Guess the number from 1 to 10"

    @gl.public.write
    def guess(self, answer: int) -> None:
        self.attempts += 1
        if answer == self.secret_number:
            self.last_response = f"✅ Guessed by {self.attempts} attempts!"
        elif answer < self.secret_number:
            self.last_response = "🔺 Try more"
        else:
            self.last_response = "🔻 Try less"

    @gl.public.view
    def get_result(self) -> str:
        return self.last_response