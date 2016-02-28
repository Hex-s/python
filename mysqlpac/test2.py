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

#------insert------
#new_user = User(id='4',name='marry')
#session.add(new_user)

#------select------
query = session.query(User)
#print(query)
#print(query.statement)

#--全部信息--
#for user in query:
#	print(user.name)

#--最多返回n条记录--
users = query.limit(10).all()
for user in users:
	print(user.name)

#--返回一个类似列表的对象--
#print(query.all())	

#--返回第一条数据，记录不存在是返回None--
#print(query.first().name)

#记录不存在或是返回多行是抛出异常
#print(query.one().name)

#-------where-------
#---获取多行---
#users = query.filter(User.id != '1').all()
#for user in users:
#	print(iuser.name)

#--主键获取--
print(query.get('2').name)


session.commit()
session.close()    

