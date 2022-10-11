# 정적 변화가 없다?
from typing import overload


class Calc:
    @staticmethod # @어노테이션
    def add(a,b):
        print(a+b)
    def diff(s,a,b):
        print("diff 3개짜리")
    @staticmethod
    @overload
    def diff(s,a):
        print("diff 2개짜리")
