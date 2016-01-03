# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import SETTINGS
from Models.stock import Stock

class Stock_add(object):

    """docstring for stock_add"""

    def add(self, new_id, name, company):
        # check the id is not repeat        
        engine = create_engine(
            SETTINGS.engine_connect)

        Session = sessionmaker(bind=engine)
        session = Session()
        row = session.query(Stock).filter(Stock.id == new_id).first()

        if row:
        	raise Exception('stock id repeat') 

        else:
            # 新增 id to database


    def __init__(self):
        super(Stock_add, self).__init__()


# , echo=True
