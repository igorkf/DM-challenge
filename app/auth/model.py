from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'fullname': 'João da Silva',
                'email': 'teste@teste.com',
                'password': 'umasenha'
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'email': 'teste@teste.com',
                'password': 'umasenha'
            }
        }
