from passlib.context import CryptContext

from core.event.produce_event import produce_event

from core.utils.settings import settings
from core.model.account_model import AccountAvroOut, AccountAvroIn
from core.model.otp_model import OTPAvroOut
from core.model.device_model import DeviceAvroOut
from core.enums.account_enums import OTPPurpose

from core.utils.init_log import logger


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    logger.info('Generating password hash.')
    return pwd_context.hash(password)


async def create_new_account(data: AccountAvroIn) -> None:
    # Hash password
    password_hash = get_password_hash(password=data.password)
    
    # Create otp avro obj
    otp_obj = OTPAvroOut(
        firstname=data.firstname,
        email=data.email,
        phone_number=data.phone_number,
        purpose=OTPPurpose.email_verification.value
    )

    # Create account dict
    account_dict = data.model_dump(exclude={'password', 'confirm_password', 'device'})
    account_dict.update({'hashed_password': password_hash, "active_device_count": 1, "active_devices": [data.device.device_id]})
    
    # Create account avro obj
    account_obj = AccountAvroOut(**account_dict)

    # Create device avro obj
    device_obj = DeviceAvroOut(
        account_email=data.email,
        device_name=data.device.device_name,
        device_id=data.device.device_id,
        device_serial_number=data.device.device_serial_number,
        device_model=data.device.device_model,
        is_active=data.device.is_active,
        ip_address=data.device.ip_address,
        platform=data.device.platform,
        screen_info=data.device.screen_info
    )    

    # Serialize data
    account_event = account_obj.serialize()
    otp_event = otp_obj.serialize()
    device_event = device_obj.serialize()
    
    # Emit events
    logger.info('Emitting generate otp event')
    logger.info('Emitting add role to account event')
    logger.info('Emitting add new device event')
    await produce_event(value=otp_event, topic=settings.api_otp_topic)
    await produce_event(value=account_event, topic=settings.api_role_topic)
    await produce_event(topic=settings.api_device_topic, value=device_event)    

