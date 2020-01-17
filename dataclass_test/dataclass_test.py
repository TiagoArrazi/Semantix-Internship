from dataclasses import dataclass


@dataclass
class DataClassFoo:
    alpha: str
    beta: str


x = DataClassFoo('a', 'b')
