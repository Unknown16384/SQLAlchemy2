from session import Connection
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

class BaseTable(DeclarativeBase):
    __abstract__ = True
class Orders(BaseTable):
    __tablename__ = 'Orders'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Product_ID = Column(Integer, ForeignKey('Products.ID'))
    Quantity = Column(Integer)
    Date = Column(DateTime,  server_default=func.now())
    Product = relationship('Products', backref='Order')
class Products(BaseTable):
    __tablename__ = 'Products'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Supplier_ID = Column(Integer, ForeignKey('Suppliers.ID'))
    Name = Column(String(50))
    Amount = Column(Integer)
    Supplier = relationship('Suppliers', backref='Order')
class Suppliers(BaseTable):
    __tablename__ = 'Suppliers'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50))
    Foo = Column(String, nullable=True)

if __name__ == '__main__':
    connect = Connection(sql_type='SQLite', db_name='mydb')
    engine = connect.engine
    session = connect.session
#    BaseTable.metadata.drop_all(engine)
    BaseTable.metadata.create_all(engine)

    data = [Suppliers(Name='Alfa'), Suppliers(Name='Beta', Foo='comment'),
            Products(Supplier_ID=1, Name='Merch1', Amount=10), Products(Supplier_ID=1, Name='Merch2', Amount=5),
            Products(Supplier_ID=2, Name='Air', Amount=999),
            Orders(Product_ID=1, Quantity=1), Orders(Product_ID=1, Quantity=3), Orders(Product_ID=2, Quantity=1), Orders(Product_ID=3, Quantity=0)]
    session.add_all(data)
    session.commit()

    for row in session.query(Orders):
        print(f'{row.Date}: {row.Product.Name}, {row.Quantity}')