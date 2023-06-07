

from .IGenericRepository import IGenericRepository
from typing import TypeVar,List
from Models.Context import Session, Base, Schema
from flask import json


Entity = TypeVar('Entity')


class GenericRepository(IGenericRepository):
    
    def __init__(self, db:Session, modelType:type(Entity), schema: Schema):
        self.db= db
        self.modelType= modelType
        self.schema = schema
    
    
    
    
    def getAllData(self) -> List[Entity]:
        data = self.db.query(self.modelType).all()
        return [self.schema.load(self.schema.dump(item)) for item in data]
    
    
    
    
    def getDataByIDOne(self, ID: str) -> List[Entity]:
        result= self.db.query(self.modelType).filter_by(ID= ID).first()
        return self.schema.dump(result)
    
    
    
    
    def getDataByID(self, ID: str) -> Entity:
         return self.db.query(self.modelType).filter_by(ID= ID).first()
    
    
    
    
    
    def addData(self, data: Entity) -> Entity:
        self.db.add(data)
        self.db.commit()
        self.db.refresh(data)
        return data
    
    
    
    
    def updateData(self, entity: Entity) -> Entity:
        self.db.commit()
        self.db.refresh(entity)
        return entity
    
    
    
    
    
    def delete(self, ID: int) -> None:
        self.db.query(self.modelType).filter_by(ID=ID).delete()
        self.db.commit()
    
    
    
    
    
    def delete(self, ID: str) -> None:
        self.db.query(self.modelType).filter(ID=ID).delete()
        self.db.commit()
    
    
    
    
    def delete(self, entity: Entity) -> None:
       self.db.delete(entity)
       self.db.commit()
    
    
    