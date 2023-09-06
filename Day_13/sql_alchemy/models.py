from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR, Date
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///person.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Person(Base):
    __tablename__ = 'pets'
    ssn = Column("ssn", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    dob = Column("dob", String)
    email = Column("email", String)
    phone = Column("phone", String)
    address = Column("address", String)
    city = Column("city", String)
    state = Column("state", String)
    zipcode = Column("zipcode", String)
    country = Column("country", String)

    def __init__(self, ssn, first_name, last_name, gender, age, dob, email, phone, address, city, state, zipcode, country):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
    
    def __repr__(self):
        return f"{self.ssn}: {self.first_name} {self.last_name} {self.gender} {self.age}"   
    
Base.metadata.create_all(bind=engine)

person1 = Person(00000000, "John", "Doe", "M", 25, "1995-01-01", "john.doe@gmail.com", "123-456-7890", "123 Main St", "New York", "NY", "10001", "USA")
person2 = Person(11111111, "Jane", "Doe", "F", 25, "1995-01-01", "jane.doe@gmail.com", "123-456-7890", "123 Main St", "New York", "NY", "10001", "USA")
session.add(person1)
session.add(person2)
session.commit()
