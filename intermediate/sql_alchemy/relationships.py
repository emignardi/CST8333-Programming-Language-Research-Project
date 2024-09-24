from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/sqlalchemy")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    posts = relationship('Post', back_populates="user")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(200))
    userId = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship('User', back_populates="posts")

Base.metadata.create_all(engine)

user1 = User(name="Eric", email="randomemail@gmail.com")
user2 = User(name="John", email="random@gmail.com")
user3 = User(name="Norma", email="random@gmail.com")
user4 = User(name="Tadoe", email="random@gmail.com")
user5 = User(name="Bubs", email="random@gmail.com")
user6 = User(name="Leon", email="random@gmail.com")
post1 = Post(title="Post 1", content="Thisdfasdf asdfasdfs", user=user1)
post2 = Post(title="Post 2", content="Thisdfasdf asdfasdfs", user=user2)
post3 = Post(title="Post 3", content="Thisdfasdf asdfasdfs", user=user3)

posts_with_users = session.query(Post, User).join(User).all()
for post, user in posts_with_users:
    print(f"{post.title} {user.name}")

# session.add(user1)
# session.add(user2)
# session.add(user3)
session.add_all([user1, user2, user3, post1, post2, post3])
session.commit()

user = session.query(User).filter(User.name == "Eric").first()
print(user.email)

# eric = session.query(User).filter(User.name == "Eric").first()
# eric2 = session.query(User).filter_by(name = "Eric").first()
# if eric is not None:
#     session.delete(eric)
#     session.commit()