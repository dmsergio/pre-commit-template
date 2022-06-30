"""
Sample class to try pre-commit tool.
"""


class Greeting:
    """
    Class to say 'hello' or 'bye' to self.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def hello(self) -> str:
        """Method to say 'hello' to self.

        Returns:
            Hello message.
        """
        return f"Hello {self.name}!"

    def bye(self) -> str:
        """Method to say 'bye' to self.

        Returns:
            Bye message.
        """
        return f"Bye {self.name}!"
