# Step 1: Import sqlalchemy & sqlalchemy.orm
# Step 2: Create Engine
# Step 3: Create Declarative Base
# Step 4: Create Session Using sessionmaker() & Bind To Engine
# Step 5: Create Model Class With Base Parameter, Table Name & Column Mappings
# Step 6: Create Database & Tables Using Base.metadata.create_all() With Engine Parameter 
# Step 7: Create session Using Session() With Context Manager

# SQLAlchemy Modules
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

# Create Engine
engine = sa.create_engine("mysql+mysqlconnector://root:password@localhost:3306/Stratolog", echo=True)

# Create Declarative Base
Base = declarative_base()

# Create SessionMaker (similar to SessionFactory or EntityManagerFactory in JPA/Hibernate)
Session = sessionmaker(bind=engine)

# Model Class
class Guitar(Base):

    # Table Name
    __tablename__ = "guitars"
    # Column Mappings
    id = sa.Column(sa.Integer, primary_key=True)
    brand = sa.Column(sa.String(20), nullable=False)
    model = sa.Column(sa.String(20), nullable=False)
    year = sa.Column(sa.String(4), nullable=False)
    image = sa.Column(sa.String(255), nullable=False)

    def __repr__(self):
        return f"<Guitar(id={self.id}, brand={self.brand}, model={self.model}, year={self.year}, image={self.image})>"

def main() -> None:

    # Create Database & Tables
    Base.metadata.create_all(engine)

    # Create Guitar Object To Persist
    guitar = Guitar(brand="Jet", model="JS400HT", year="2024", image="asdfdf23asdfsdf")

    # Create Session With Context Manager
    with Session() as session:
        # Saving Guitar Object
        session.add(guitar)
        # Commit Changes
        session.commit()
        print(session.query(Guitar).all())

if __name__ == "__main__":
    main()