import sqlalchemy as sa

engine = sa.create_engine("mysql+mysqlconnector://root:password@localhost:3306/Stratolog", echo=True)
connection = engine.connect()

metadata = sa.MetaData()

guitar_table = sa.Table(
    "guitar",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("brand", sa.String(20), nullable=False),
    sa.Column("model", sa.String(20), nullable=False),
    sa.Column("year", sa.String(4), nullable=False),
    sa.Column("image", sa.String(200), nullable=False),
)

def insert_guitar(brand: str, model: str, year: str, image: str):
    query = guitar_table.insert().values(brand=brand, model=model, year=year, image=image)
    connection.execute(query)

def select_guitar():
    query = guitar_table.select()
    result = connection.execute(query)
    return result.fetchall()

def main() -> None:
    metadata.create_all(engine)
    insert_guitar("Jet", "JT-300", "2024", "asdfb4352asdfasdf234tasdf")
    connection.commit()
    print(select_guitar())
    connection.close()

if __name__ == "__main__":
    main()

# class Guitar(Base):

#     __tablename__ = "guitar"
#     id = Column("id", Integer, primary_key=True)
#     brand = Column("brand", String(20), nullable=False)
#     model = Column("model", String(20), nullable=False)
#     year = Column("year", String(4), nullable=False)
#     image = Column("image", LargeBinary(length=(2**32)-1), nullable=False)

#     def __init__(self, brand, model, year, image):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.image = image
    
#     def __str__(self):
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Image: {self.image}"
    

# connection = engine.connect()

# Session = sessionmaker(bind=engine)
# session = Session()

# guitar1 = Guitar(100, "Jet", "JT-300", "2024", "asdfb4352asdfasdf234tasdf")
# guitar2 = Guitar(100, "Jet", "JS-400HT", "2024", "asdfb4352asdfaasdfsdf234tasdf")

# session.add(guitar1)
# session.add(guitar2)
# session.commit()