import simplejson
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@172.16.2.133:3306/trade?charset=utf8", convert_unicode=True)
meta = MetaData()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)
    def to_dict(model_instance, query_instance=None):
        if hasattr(model_instance, '__table__'):
            return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
        else:
            cols = query_instance.column_descriptions
            return { cols[i]['name'] : model_instance[i]  for i in range(len(cols)) }
    def to_json(self):
        return dict(id=self.id, name=self.name, fullname=self.fullname, password=self.password,
                registered_on=self.registered_on.isoformat())

    # def __init__(self, id, name, fullname, password):
    #     self.id = id
    #     self.name = name
    #     self.fullname = fullname
    #     self.password = password
    def __init__(self, *values):
        self.some_sequence = values

    def to_json_all(self):
          return {
            'id': object.id,
            'name': object.name,
            'fullname': object.fullname,
            'password': object.password,
        }

def encode_json(object):
    if isinstance(object, User):
        return object.__dict__

        # or, alternatively ...
        return {
            'id': object.id,
            'name': object.name,
            'fullname': object.fullname,
            'password': object.password,
        }

    raise TypeError('Cannot serialize object of type %s' % type(object))

def populate(session):
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(ed_user)
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])
    session.commit()


class UserBean(object):
    def __init__(self, id, name, fullname, password):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.password = password


def encode_json_bean(object):
    if isinstance(object, UserBean):
        return object.__dict__

        # or, alternatively ...
        return {
            'id': object.id,
            'name': object.name,
            'fullname': object.fullname,
            'password': object.password,
        }

    raise TypeError('Cannot serialize object of type %s' % type(object))
# user_table = Table('user', meta)
# insp = Inspector.from_engine(engine)
# insp.reflecttable(user_table, None)
# print insp.get_columns(table_name="user", schema="trade")
# print insp.__getattribute__()


Session = sessionmaker(bind=engine)
session = Session()
# Put some data.
# populate(session)
# Query
rset = session.query(User).all()
# userInstance = User()
# print rset.to_json()
# print  ([('id'+':'+str(orderInfo.id), orderInfo.name, orderInfo.age, orderInfo.create_time, orderInfo.update_time, orderInfo.version)  for orderInfo in orderInfos])
# print  ([(id=user1.id, name=user1.name, fullname=user1.fullname, password=user1.password)  for user1 in rset]))
result = []
for row in session.query(User).all():
    userbean = UserBean(id=row.id, name=row.name, fullname=row.fullname,password=row.password)
    result.append(userbean)

print  "result===", result
print "result=", simplejson.dumps(result, default=encode_json_bean)
# print "result=", simplejson.dumps(result, default=encode_json)

# result = []
# keys = []
# for obj in rset:
#     instance = inspect(obj)
#     items = instance.attrs.items()
#     data = instance.attrs._data
#     print instance
#     print items
#     print data
















