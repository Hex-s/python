from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func, or_, not_

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True,autoincrement=True)
    name = Column(String(20))
    
engine = create_engine('mysql+pymysql://root:123@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()

#-------insert-----
#user1 = User(id='1',name='a')
#user2 = User(id='2',name='b')
#user3 = User(id='3',name='c')
#session.add(user2)
#session.add(user3)

#-------select-------
query = session.query(User)
#print(query.statement)
#print(type(query))   <class 'sqlalchemy.orm.query.Query'>
#for user in query:
#	print(user.name)

#print(query.all()) #[<__main__.User object at 0x1035e1278>, <__main__.User object at 0x1035e12e8>, <__main__.User object at 0x1035d4358>]

#print(query.first().name)

#print(query.filter(User.id == '2').first().name)
#print(query.get('2').name)
#print(query.filter("id='2'").first().name)

qu = session.query(User.name)
#print(qu.all())  #[('a',), ('b',), ('c',)]
#print(qu.limit(2).all())
#print(qu.offset(1).all())
#print(qu.order_by("id desc").all())
#print(session.query(User.id).order_by(User.name.desc(),User.id).all())
#print(qu.filter(User.id=='5').scalar())
#print(session.query('id').select_from(User).filter("id='1'").scalar())
#print(qu.filter(User.id > '1', User.name != 'b').scalar())
#print(qu.filter(or_(User.id == 1, User.id == 2)).all())
#print(qu.filter(User.id.in_((1, 2))).all())

q = session.query(User.id)
#print(q.filter(User.name == None).scalar())
#print(q.filter('name is null').scalar())
#print(q.filter(not_(User.name == None)).all())

#print(q.count())
#print(session.query(func.count('*')).select_from(User).scalar())
#print(session.query(func.count('1')).select_from(User).scalar())
#print(session.query(func.sum(User.id)).scalar())
#print(session.query(func.now()).scalar())
#print(session.query(func.current_timestamp()).scalar())
#print(session.query(func.md5(User.name)).filter(User.id == 1).scalar())

q2 = session.query(User).filter(User.id == '6').all()
if q2:
	print("has")
else:
    print("None")	

session.commit()
session.close()
