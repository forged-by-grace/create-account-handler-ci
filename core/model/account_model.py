from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field, EmailStr
from typing import Optional, List
from core.utils.settings import settings
from core.model.device_model import Device

class PasswordAvro(AvroBaseModel):
    password: str = Field(description="Alphanumeric string representing the account password")
    confirm_password: str = Field(description="Alphanumeric string representing the account password")    
  

class AccountAvroIn(PasswordAvro):    
    email: EmailStr = Field(description="An email string. This is the user's email address. It will be validated before use.", 
                            json_schema_extra={'email':'joe@example.com'},
                            examples=['johndoe@example.com'])
    firstname: str = Field(description="A string. This is the user's first name.",
                           examples=['John'])
    lastname: str = Field(description="A string. This is the user's lastname.",
                          examples=['Doe'])
    phone_number: str = Field(description="A string. This is the user's mobile or contact number. This will be validated before use.",
                              examples=['915 1234 789'])
    country_code: str = Field(description="A string. This is the user's country code.",
                              examples=['+234'])
    country: str = Field(description="A string. This is the user's country of residence. e.g. Nigeria", 
                         examples=['Nigeria'])
    username: Optional[str] = Field('ID used to retrieve the account username')
    device: Device = Field(description='A dict used to track the device info')   
    display_pics: Optional[str] = Field(description='Account display image',)
    

class AccountAvroOut(AvroBaseModel):
    email: EmailStr = Field(description="An email string. This is the user's email address. It will be validated before use.", 
                            json_schema_extra={'email':'joe@example.com'},
                            examples=['johndoe@example.com'])
    firstname: str = Field(description="A string. This is the user's first name.",
                           examples=['John'])
    lastname: str = Field(description="A string. This is the user's lastname.",
                          examples=['Doe'])
    phone_number: str = Field(description="A string. This is the user's mobile or contact number. This will be validated before use.",
                              examples=['915 1234 789'])
    country_code: str = Field(description="A string. This is the user's country code.",
                              examples=['+234'])
    country: str = Field(description="A string. This is the user's country of residence. e.g. Nigeria", 
                         examples=['Nigeria'])
    username: Optional[str] = Field('ID used to retrieve the account username')
    display_pics: Optional[str] = Field(description='Account display image',)
    hashed_password: str = Field(description='Account password hashed')
    version: int = Field(default=settings.account_model_version, 
                         description="A string. This represents the version of database schema")
    disabled: bool = Field(default=True, 
                           description="A boolean. This is used to disable a user's account")
    email_verified: bool = Field(default=False, 
                                 description="A boolean used to check the verification state of the account's email")
    phone_verified: bool = Field(default=False, 
                                 description="A boolean used to check the verification state of the user's phone number")
    is_active: bool = Field(default=False, description="A boolean used to verify the login state of the account")
    active_device_count: int = Field(description='An integer representing the number of active devices connecting to a single account')
    active_devices: List[str] = Field(description='A list showing all active account devices')
