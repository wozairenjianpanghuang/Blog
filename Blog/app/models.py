#与当前项目相关的模型文件，即所有的实体类在此编写
from . import db

class Category(db.Model):
  __tablename__ = "category"
  id = db.Column(db.Integer,primary_key=True)
  cate_name = db.Column(db.String(50),nullable=False)
  #增加与Topic之间的关联关系以及反向引用
  topics = db.relationship('Topic',backref='category',lazy="dynamic")

class BlogType(db.Model):
  __tablename__ = 'blogtype'
  id = db.Column(db.Integer,primary_key=True)
  type_name = db.Column(db.String(20),nullable=False)
  # 增加与Topic之间的关联关系和反向引用
  topics = db.relationship('Topic',backref='blogType',lazy="dynamic")

class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer,primary_key=True)
  loginname = db.Column(db.String(50),nullable=False)
  uname = db.Column(db.String(30),nullable=False)
  email = db.Column(db.String(200),nullable=False)
  url = db.Column(db.String(200))
  upwd=db.Column(db.String(30),nullable=False)
  is_author=db.Column(db.SmallInteger,default=0)
  #增加与Topic之间的关联关系和反向引用
  topics = db.relationship('Topic',backref='user',lazy='dynamic')
  #增加与Reply之间的关联关系和反向引用
  replies = db.relationship('Reply',backref='user',lazy="dynamic")
  #增加与Topic之间的关联关系和反向引用(多对多)
  voke_topics=db.relationship(
    'Topic',
    secondary='voke',
    backref=db.backref('voke_users',lazy='dynamic'),
    lazy='dynamic'
  )

class Topic(db.Model):
  __tablename__ = "topic"
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(
    db.String(200),nullable=False)
  pub_date = db.Column(
    db.DateTime,nullable=False)
  read_num = db.Column(db.Integer,default=0)
  content = db.Column(db.Text,nullable=False)
  images = db.Column(db.Text)

  #关系：一(Category)对多(Topic)的关系
  category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
  #关系:一(BlogType)对多(Topic)的关系
  blogtype_id = db.Column(db.Integer,db.ForeignKey('blogtype.id'))
  #关系:一(User)对多(Topic)的关系
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
  #定义与Reply之间的关联关系和反向引用
  replies = db.relationship('Reply',backref='topic',lazy="dynamic")

class Reply(db.Model):
  __tablename__ = 'reply'
  id = db.Column(db.Integer,primary_key=True)
  content = db.Column(db.Text,nullable=False)
  reply_time = db.Column(db.DateTime)
  # 关系:一(Topic)对多(Reply)的关系
  topic_id = db.Column(db.Integer,db.ForeignKey('topic.id'))
  # 关系:一(User)对多(Reply)的关系
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

Voke = db.Table(
  'voke',
  db.Column('id',db.Integer,primary_key=True),
  db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
  db.Column('topic_id',db.Integer,db.ForeignKey('topic.id'))
)


