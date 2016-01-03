# -*- coding: utf-8 -*-

# import sqlalchemy
# from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Stock(Base):

    """docstring for Stock"""
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    company = Column(String)

    # init repr 預設方法 init 若無設定則全部都為columns
    # def __init__(self, name):
    #     self.name = name

    # def __repr__(self):
    #     return "<Stock('%s')>" % (self.name)

    def __init__(self):
        super(Stock, self).__init__()
