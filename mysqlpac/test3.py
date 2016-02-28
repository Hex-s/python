from sqlalchemy import create_engine,Column
from sqlalchemy.types import String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#连接数据库的路径
db_connect_string = 'mysql+pymysql://root:123@localhost/test?charset=utf8'
#create_engine() 返回一个数据库引擎,echo=True 显示每条执行的SQL语句，生产环境下可以关闭
engine = create_engine(db_connect_string)
#sessionmaker()生成一个数据库会话
db_session = sessionmaker(bind = engine)
#session可以视为当前数据库的连接
session = db_session()

#对象的基类
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

query = session.query(User)
query1 = session.query(User.id)
#print(query.statement)
#for name in query:
#	print(name)

#最多返回n条数据
#print(query.limit(2).all())

#从第n+1条数据开始返回
#print(query.offset(1).all())
#users = query1.order_by(User.name).all()
#for user in users:
#	print(user.name)

#print(query1.filter(User.id == 1).scalar())
#print(query.filter(or_(User.id == 1, User.id == 2)).all())
#print(query.filter('id=1 or id=2').all())
#print(query.filter(User.id.in_((1, 2))).all())
#print(query.filter('id in (1,2)').all())

#print(query1.filter(not_(User.name == None)).all())

#print(query.count())

#print(session.query('count(*)').select_from(User).scalar())

#print(session.query('count(*)').filter(User.id>2).scalar())
#session.query(User).filter(User.id == '6').update({User.name:'Lily'})

#query.filter(User.id == '6').delete()

#print(query.get('1').name)
session.query("insert into user values('5','lily')")

session.commit()
session.close() 