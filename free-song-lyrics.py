import lyricsgenius
api_key = "GqkMcDsl9kh1XQmWdS5vAMI_Cozz93AlzaRoLjYpfMHKyio3xEm34cOEx-xe4O-V"
genius = lyricsgenius.Genius(api_key)
name = input("Enter Artist Name : ")
artist = genius.search_artist(name)
song = input("Type your song for Lyrics : ")
song = artist.song(song)
print(song.lyrics)