from pydantic import BaseModel, ConfigDict
from datetime import datetime
#from typing import Optional

class ItemBase(BaseModel):
    name: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)