from pydantic import BaseModel

class TagBase(BaseModel):
    name: str

class CreateTag(TagBase):
    pass

class UpdateTag(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        org_mode = True