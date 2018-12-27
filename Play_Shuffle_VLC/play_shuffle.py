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

    #We create a randomlist to save the songs randomly
    randomlist = []
    #Now we change the predefined dictionary by a random list
    while len(randomlist) != len(library):
        #Here we use the function choice of the library random, for change the order of the titles
        randomsong = random.choice(list(library.keys()))
        assert isinstance(randomsong, str)

        if randomsong not in randomlist:
            randomlist.append(randomsong)
        else:
            pass
    assert randomsong in randomlist
    return randomlist


def MakeRandomPlayList (library):
    assert isinstance(library, dict)

    randomtitle = SelectRandomSong(library)
    #We return to convert our random list into a dictionary that will change its order, and we put the order
    playlist = dict((key + 1, value) for key, value in enumerate (randomtitle))

    assert isinstance(playlist, dict)
    assert isinstance(playlist[1],str)
   
    return playlist

print(MakeRandomPlayList(library))






