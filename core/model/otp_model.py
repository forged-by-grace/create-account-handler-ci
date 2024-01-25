from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field, EmailStr

class OTPPurposeAvro(AvroBaseModel):
    purpose: str = Field(description='The purpose of the OTP')


class OTPAvro(OTPPurposeAvro):
   otp: str = Field(description="verified otp")


class OTPAvroOut(OTPPurposeAvro):
    firstname: str = Field(description="A string. This is the user's first name.",
                           examples=['John'])
    email: EmailStr = Field(description="An email string. This is the user's email address. It will be validated before use.", 
                            examples=['johndoe@example.com'])
    phone_number: str = Field(description="A string. This is the user's mobile or contact number. This will be validated before use.",
                              examples=['915 1234 789'])
