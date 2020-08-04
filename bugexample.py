from typing import Generic, TypeVar, List, get_type_hints
from pydantic.generics import GenericModel
from pydantic import ValidationError


T = TypeVar('T')

class InnerT(GenericModel, Generic[T]):
    inner: T

class OuterT(GenericModel, Generic[T]):
    outer: T
    nested: List[InnerT[T]]

class BaseOuterT(GenericModel, Generic[T]):
    outer: T
    nested: InnerT[T]

# o1 = OuterT[int](**{"outer": 1, "nested": [{"inner": "2"}]})
print("output2\n")
o2 = OuterT[int](**{"outer": 1, "nested": [{"inner": "a"}]})

# try:
#     print(o4 = BaseOuterT[int](**{"outer": 1, "nested": {"inner": "a"}}))
# except ValidationError as ve:
#     # print(ve)
#     pass

# print("output1\n")
# print(o1)  # Output 1
print(o2)  # Output 2

# print(get_type_hints(o1))
print(get_type_hints(o2))
# print(type(o1.nested[0]))
print(type(o2.nested[0]))

print("output3\n")
o3 = BaseOuterT[int](**{"outer": 1, "nested": {"inner": "2"}})
print(o3)
print(get_type_hints(o3))
print(type(o3.nested))

# print(o3.nested.__concrete__)
# print(o3.nested.__annotations__)
# print(o3.nested.__custom_root_type__)
# print(o3.nested.__fields__)
# print("\n")
# print(o2.nested[0].__concrete__)
# print(o2.nested[0].__annotations__)
# print(o2.nested[0].__custom_root_type__)
# print(o2.nested[0].__fields__)


