import Song
class Playlist:
    """List of class variables:
        userId = Spotify userId of playlist -- dec in function __init__
        songs = List of songs in playlist -- dec in function __init__
     """
    #class constructor
    def __init__(self, userId, songs =[]):
        self.userId = userId 
        self.songs = songs

    def add (self, song):
        self.songs.append(song)
    
    def __str__(self):
        string = ""
        for song in self.songs:
            string += str(song) + "\n"
        return string

    # == overload
    def __eq__(self, other):
        for song in self.songs:
            if not (song in other.songs):
                return False
        return True
    
    def __neq__(self,other):
        return not (self == other)

    #returns true if parameter in playlist, false otherwise
    def has(self, song):
        if song in self.songs:
            return True
        return False 
    
    #Param: other playlist to compare
    #Returns: sharedSongs {list of song objects present in both playlists} ; sharedArtists {set of artists shared by both profiles}
    #         artistCount {number of songs with matching artists}
    def compare(self, other):
        sharedSongs = Playlist("none",[])
        sharedArtists = set()
        artistsCount = 0
        artistPairs = []
        for song in self.songs:
            if song in other.songs:
                sharedSongs.add(song)
            else:
                for track in other.songs:
                    if song.artists == track.artists:
                        if not (track in artistPairs):
                            for artist in song.artists:
                                sharedArtists.add(artist)
                            artistPairs.append(track)
                            artistsCount+=1
        return (sharedSongs, sharedArtists, artistsCount)
    

