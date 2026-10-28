from dataclasses import dataclass


@dataclass(frozen=True)
class Site:
    name = str