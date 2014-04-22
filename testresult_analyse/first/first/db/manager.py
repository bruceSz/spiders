from collections import namedtuple

from db import Action
from db import init_db
from db import create_db

TestRet = namedtuple('TestRet',['name','traceback'])
class Manager:
    def __init__(self):
        self.driver = Action() 
        create_db()
        self.session = init_db()

    def set_data(self,name,value):

        tr = TestRet(name=name,traceback=value)
        self.driver.set(self.session,tr)


if __name__ == '__main__':
    manager = Manager()
    manager.set_data('test','test result maded up')
