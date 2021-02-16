from enum import Enum, IntEnum, Flag, IntFlag

class MyEnum(Enum):
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"

class MyIntEnum(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3

# Now we can do things like

MyEnum.FIRST    # <MyEnum.FIRST: 'first'>

# it has value and nanme attributes, which are handy:

MyEnum.FIRST.value      # 'first'
MyEnum.FIRST.name       # 'FIRST'

# additionally we can do things like:

MyEnum('first')         # <MyEnum.FIRST: 'first'>, get enum by value

MyIntEnum.ONE == 1      # True
MyEnum.FIRST.value == 'first'

MyEnum('FIRST')         # ValueError