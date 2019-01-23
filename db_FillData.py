from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, CatalogItem


def addUsers():
    user1 = User(name="name 1", email="email1@gmail.com")
    session.add(user1)


def addCategories():
    category1 = Category(user_id="1", name="category 1")
    category2 = Category(user_id="1", name="category 2")
    category3 = Category(user_id="1", name="category 3")
    session.add(category1)
    session.add(category2)
    session.add(category3)


def addItems():
    item1 = CatalogItem(category_id="1",
                        name="item 1", description="item info")
    item2 = CatalogItem(category_id="1", name="item 2",
                        description="item info")
    item3 = CatalogItem(category_id="1", name="item 3",
                        description="item info")
    item4 = CatalogItem(category_id="2", name="item 1",
                        description="item info")
    item5 = CatalogItem(category_id="2", name="item 2",
                        description="item info")
    item6 = CatalogItem(category_id="2", name="item 3",
                        description="item info")
    item7 = CatalogItem(category_id="3", name="item 1",
                        description="item info")
    item8 = CatalogItem(category_id="3", name="item 2",
                        description="item info")
    item9 = CatalogItem(category_id="3", name="item 3",
                        description="item info")
    session.add(item1)
    session.add(item2)
    session.add(item3)
    session.add(item4)
    session.add(item5)
    session.add(item6)
    session.add(item7)
    session.add(item8)
    session.add(item9)


engine = create_engine('postgresql://catalog:catalog123@localhost/itemcatalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
addUsers()
addCategories()
addItems()
session.commit()
