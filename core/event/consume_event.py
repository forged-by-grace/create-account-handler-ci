from core.helper.consumer_helper import consume_event
from core.model.account_model import AccountAvroIn
from core.utils.settings import settings
from core.helper.account_helper import create_new_account
from core.utils.init_log import logger


async def consume_create_new_account_event():
    # consume event
    consumer = await consume_event(topic=settings.api_account_topic, group_id=settings.api_account_create_group)
    
    try:
        # Consume messages
        async for msg in consumer:  
            # Deserialize event
            account_data = AccountAvroIn.deserialize(data=msg.value)
            
            # Create account
            logger.info('Creating account...')
            await create_new_account(data = account_data)
    except Exception as err:
        logger.error(f'Failed to create account with error: {str(err)}')
    finally:
        logger.warning('Consumer is stopping.')
        await consumer.stop()

