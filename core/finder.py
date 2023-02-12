from playwright.sync_api import sync_playwright as pupe
from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionMediaProperties as Props

def fetch_url(title: str, artist: str) -> str: # media_data: Props
    '''
    Fetch a media url.
    '''
    
    # artist, title = media_data.artist, media_data.title
    
    with pupe() as tear:
        
        # Init browser
        # browser = tear.firefox.launch(headless = False)
        
        browser = tear.chromium.launch_persistent_context('./context', headless = True)
        
        page = browser.new_page()
        page.set_viewport_size({'width': 800, 'height': 1200})
        
        # Send query
        page.goto(f'https://www.youtube.com/results?search_query={artist} {title}')
        page.wait_for_load_state()
                
        # Get first element    
        url = page.evaluate('document.querySelector("#contents a").href')
        
        browser.close()
        
        return url

# EOF