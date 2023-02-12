from typing import Callable
import pynput.keyboard as kbd

def run(hotkeys: dict[str: Callable]) -> None:
    '''
    Run binder.
    '''
    
    with kbd.GlobalHotKeys(hotkeys) as ln:
        ln.join()