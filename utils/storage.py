async def save_to_storage(client, message, storage_channel):
    # Forward the file to the storage channel
    forwarded_message = await message.forward(storage_channel)
    return forwarded_message
