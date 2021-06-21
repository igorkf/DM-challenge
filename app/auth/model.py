from pydantic import BaseModel, Field, EmailStr


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'exemplo': {
                'email': 'teste@teste.com',
                'password': 'umasenha'
            }
        }
