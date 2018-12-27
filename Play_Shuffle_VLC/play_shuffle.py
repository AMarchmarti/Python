import random
library = {"California_Uber_Alles.mp3":{"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys","location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party":{"track-number": 1, "artist": "Chastity Belt", "album": "No regrets","location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":{"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly","location": "./biblioteca/King_Kunta.mp3"}}

def CheckSelectRandomSong (song, library):
    
    assert isinstance(song, str)
    assert isinstance(library, dict)
    #We check that the selected song is in the library
    if song not in library:
        return False
    
    return True

def CheckRandomSong (musiclist):

    assert isinstance(musiclist, dict)

    songslist = list(musiclist.values())
    #We check that the songs do not repeat themselves
    for song in songslist:
        if songslist.count(song) > 1:
            return False
    return True

def SelectRandomSong (library):

    #We need the title of the song, then we extract of the library the title and create a list.
    titlelist = list(library.keys())
    #We create a randomlist to save the songs randomly
    randomlist = []

    while len(randomlist) < len(titlelist):

        randomsong = random.choice(titlelist)
        assert isinstance(randomsong, str)

        if randomsong not in randomlist:
            randomlist.append(randomsong)
        else:
            pass
    assert randomsong in randomlist
    return randomlist


def MakeRandomPlayList (library):
    assert isinstance(library, dict)

    randomsongs = SelectRandomSong(library)
    playlist = dict((key, value) for key, value in enumerate (randomsongs))

    assert isinstance(playlist, dict)
    assert isinstance(playlist[0],str)
   
    return playlist

print(MakeRandomPlayList(library))






