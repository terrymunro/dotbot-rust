import subprocess, dotbot

from typing import NamedTuple


# curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


class Rustup(dotbot.Plugin):
    """

    """

    _directive = "rustup"


    def can_handle(self, directive: str) -> bool:
        return self._directive == directive


    def handle(self, directive: str, data) -> bool:
        if not self.can_handle(directive):
            raise ValueError(f"rustup cannot handle directive {directive}")

        return False
