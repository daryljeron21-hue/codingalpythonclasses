from abc import ABC, abstractmethod

class absClass(ABC):

    def print(self, x):
        print("Passed value: ",x)

    @abstractmethod
    def task(self):
        print("We are inside absClass")

class test_class(absClass):
        def task(self):
            print("We are insisde test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)
