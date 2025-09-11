weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
print(weekly_playlist[1])
weekly_playlist_length = len(weekly_playlist)
print("This playlist has:",weekly_playlist_length,"songs.")


weekly_playlist.append("drivers license")#add it to the playlist.
weekly_playlist.insert(0,"Bohemian Rapsody")#add at the beginning of the playlist.
weekly_playlist.remove("Good 4 u")#Take it out of the playlist.
print(weekly_playlist.index("Levitating"),"- Commercial break!")
print("Songs by Harry Styles:", "As It Was")
weekly_playlist.reverse() #for the Throwback Thursday.
new_weekly_playlist = ["As It Was", "Blinding Lights", "Bohemian Rapsody", "Good 4 u", "Heat Waves", "Levitating"] #songs in alphabetical order.

#new_weekly_playlist_length = len(new_weekly_playlist)
#print("This new playlist has:",new_weekly_playlist_length,"songs.")


print(weekly_playlist)
print(new_weekly_playlist)