# Playlist_recommendation
Using knn to recommend playlists best suited for a song based on genre. 

This data used to train the knn model has three playlist :- 1. Hip-Hop Playlist 
                                                            2. Alternate Playlist
                                                            3. Pop Playlist 

These playlists are curated based on similar genre of music. Each playlist has 25 songs. 

Spotify keeps a track of 9 features of a song. Out of these, I chose the best 4 features to 
classify a song i.e Acousticness , Danceability , Energy and Speechiness. 

Danceability: Describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. The close to 1.0, the more danceable.

Speechiness: This detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audiobook, poetry), the closer to 1.0 the attribute value.

Energy: Represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. The closer to 1.0, the more intensity and activity.

Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. The closer to 1, the more acoustic the track.

Taking these features of a new input song, the song is recommended two of the three playlists.
My model has an accuracy of 0.87. This model can be extended to more data and can be used to recommend more number of playlists.
