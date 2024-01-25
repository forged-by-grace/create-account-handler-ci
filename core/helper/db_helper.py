from core.connection.db_connection import account_col

from core.model.account_model import AccountInDB

from pydantic import EmailStr


async def get_account_by_email(email: EmailStr):
    """    
    This is used to retrieve an account from the database using email.
    @params {email} - The email registered to the account to be retrieved.
    @returns {object} - A dict containing the account data
    
    """
    
    # Filter
    query = {"email": email}

    # Query
    response = await account_col.find_one(filter=query)

    # Check if response is None
    if not response:
        return None
    
    # Deserialize
    account_obj = AccountInDB(**response)

    return account_obj


async def get_account_by_id(id: str):
    """
    This is used to retrieve accounts from the database using the id.
    @params {id} - The id registered to the account.
    @returns {object} - A dict containing the account data
    """

    # Filter
    query = {"_id": id}

    # Query
    response = await account_col.find_one(filter=query)

    # Check if response is None
    if not response:
        return None
    
    # Deserialize
    account_obj = AccountInDB(**response)

    return account_obj


async def get_account_by_phone_number(phone_number: str):
    """
    This is used to retrieve accounts from the database using the id.
    @params {phone_number} - The phone number registered to the account.
    @returns {object} - A dict containing the account data
    """
    
    # query
    query = {"phone_number": phone_number}

    # Query
    response = await account_col.find_one(filter=query)

    # Check if response is None
    if not response:
        return None
    
    # Deserialize
    account_obj = AccountInDB(**response)

    return account_obj

