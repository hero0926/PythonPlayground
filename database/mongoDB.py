# 몽고디비

from distutils.log import warn as printf
from random import randrange as rand
from pymongo import Connection, errors
from ushuffle_dbU import DBNAME, randName, FIELDS, tformat, cformat

COLLECTION = 'users'
class MongoTest(object) :
  def __init__(self) :
    try :
      cxn = Connection()
    except errors.AutoReconnect :
      raise RuntimeError()
    self.db = cxn[DBNAME]
    self.users = self.db[COLLECTION]


  def insert(self) :
    self.users.insert(
      dict(login=who, userid=uid, projid=rand(1,5) for who, uid in randName())
    )

  def update(self) :
    fr = rand(1,5)
    to = rand(1,5)
    i = -1
    for i, user in enumerate(self.users.find({'projid' : fr})) :
      self.users.update(user, {'$set' : {'projid' : to}})
    return fr, to, i+1


  def delete(self) :
    rm = rand(1,5)
    i = -1
    for i, user in enumerate(self.users.find({'projid' : rm})) :
      self.users.remove(user)
    return rm, i+1


  def dbDump(self) :
    for user in self.users.find() :
      printf(''.join(map(tformat, (user[l] for k in FIELDS))))

  def finish(self) :
    self.db.connection.disconnect()


def main() :
  try :
    mongo = MongoTest()
  except RuntimeError :
    print("MONGODB SERVER ERROR")
    return


  mongo.insert()
  mongo.dbDump()

  fr, to, num = mongo.update()
  fr, to, num = mongo.update()
  mongo.dbDump()

  rm, num = mongo.delete()
  mongo.dbDump()

  mongo.db.drop_collection(COLLECTION)
  mongo.finish()
