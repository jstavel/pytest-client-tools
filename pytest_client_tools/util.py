# SPDX-FileCopyrightText: Red Hat
# SPDX-License-Identifier: MIT

import dataclasses
import functools
import pathlib


@dataclasses.dataclass
class SavedFile:
    path: pathlib.Path
    remove_at_start: bool = False


@functools.total_ordering
class Version:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            parts = args[0].split(".")
            self._bits = [int(p) for p in parts]
        else:
            self._bits = [int(p) for p in args]

    def __lt__(self, other):
        if not isinstance(other, Version):
            return False
        return self._bits < other._bits

    def __eq__(self, other):
        if not isinstance(other, Version):
            return False
        return self._bits == other._bits

    def __str__(self):
        return ".".join([str(i) for i in self._bits])

    def __repr__(self):
        return f"Version({self.__str__()})"
