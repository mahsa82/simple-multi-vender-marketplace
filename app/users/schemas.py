from pydantic import BaseModel, EmailStr, Field, field_validator


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128, description="password of the user")
    password_confirm: str = Field(min_length=8, max_length=128, description="confirm password of the user")

    @field_validator("password_confirm")
    def check_password_match(cls, password_confirm, validation):
        if not (password_confirm == validation.data.get("password")):
            raise ValueError("password doesnt match.")
        return password_confirm
