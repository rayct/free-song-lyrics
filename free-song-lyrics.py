import lyricsgenius
api_key = "3-7CABwvkETjlrkkkjQ-_Kx15Tk5o6u4s1WJ797CRwwbx10yeG4EQI5sYH2_CIF0"
genius = lyricsgenius.Genius(api_key)
name = input("Enter Artist Name : ")
artist = genius.search_artist(name)
song = input("Type your song for Lyrics : ")
song = artist.song(song)
print(song.lyrics)