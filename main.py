import core
import json
import winsound
import threading

# Settings
ps1 = '\033[94m|>\033[0m'
tracks: list = json.load(open('tracks.json'))

# play = lambda file: winsound.PlaySound(file, winsound.SND_FILENAME)

play = lambda file: threading.Thread(target = winsound.PlaySound,
                                     args = [file, winsound.SND_FILENAME]).start()

def like() -> None:
    '''
    Save the current track.
    '''
    
    # Get playing media
    cur = core.media.fetch()
    data = {'title': cur.title, 'artist': cur.artist}
    print(ps1, f'track \033[91m{cur.title}\033[0m ({cur.artist}):', end = ' ')
    
    # Check if not already liked
    if data in tracks:
        play('reject.wav')
        return print('Already liked')
    
    # Add to tracks
    tracks.append(data)
    open('tracks.json', 'w').write(json.dumps(tracks, indent = 3))
    print('Done')
    
    # Play confirmation sound
    play('confirm.wav')

# Run binder
print(ps1, 'Running')
core.binder.run({'<ctrl>+<alt>+l': like})

# EOF