import subprocess, dotbot

from typing import NamedTuple


class Cargo(dotbot.Plugin):
    """

    """

    _directive = "cargo"


    def can_handle(self, directive: str) -> bool:
        return self._directive == directive


    def handle(self, directive: str, data) -> bool:
        if not self.can_handle(directive):
            raise ValueError(f"{self._directive} cannot handle directive {directive}")

        return False
