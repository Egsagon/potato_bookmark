import asyncio

from winsdk.windows.media.control import GlobalSystemMediaTransportControlsSessionManager as media_manager, \
                                         GlobalSystemMediaTransportControlsSessionMediaProperties as media_props

async def get_info_async():
    
    # Get current session
    sessions = await media_manager.request_async()
    current_session = sessions.get_current_session()
    
    # Return data
    if current_session:    
        return await current_session.try_get_media_properties_async()

def fetch() -> media_props:
    '''
    Fetch raw data from the current track.
    '''
    
    return asyncio.run(get_info_async())

# EOF