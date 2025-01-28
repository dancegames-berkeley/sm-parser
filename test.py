import dataclasses
import orjson

@dataclasses.dataclass
class Nested:
    awa: str

@dataclasses.dataclass
class Test():
    test: str
    awa: Nested

t = [Test('test', Nested('awa'))]

print(orjson.dumps(t))