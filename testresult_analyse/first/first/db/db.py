from  collections import namedtuple

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

Base = declarative_base()
ENGINE = None
SESSION = None

class TestResult(Base):
    __tablename__ = 'testresult'

    name = Column(String,primary_key=True)
    traceback = Column(String)

    def __init__(self,name,traceback):
        self.name = name

        self.traceback = traceback



def init_db():
    print 'first init global para first.'
    global ENGINE,SESSION
    ENGINE =  create_engine("sqlite:///test.db",echo=True)
    SESSION = scoped_session(sessionmaker(bind=ENGINE)) 
    if SESSION == None:
        print "session initialization fails"
        sys.exit(1)

    return SESSION

def create_db():
    engine = create_engine("sqlite:///test.db",echo=True)
    Base.metadata.create_all(engine)

class Action:

    def set(self,session,data):
        print data.name,data.traceback
        tr = TestResult(data.name,data.traceback)
        session.add(tr)
        session.commit()



def test1():
    init_db()
    action = Action()
    session = SESSION()
    Data = namedtuple('Data',['name','traceback'])

    action.set(session,Data(name="test",traceback="traceback maded up"))
if __name__ == '__main__':
    session = init_db()
    action = Action()
    Data = namedtuple('Data',['name','traceback'])
    action.set(session,Data(name="test",traceback="traceback maded up"))
