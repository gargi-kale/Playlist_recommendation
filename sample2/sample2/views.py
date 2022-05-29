from django.http import HttpResponse
from django.shortcuts import render
import joblib
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier
from scipy import stats
import random 
import numpy as np

client_id='563f86d9ae474e1387b5fe497bc1bcd7'
client_secret='a157b170e49f4330aed7782fbedf1ea8'
client_credentials=SpotifyClientCredentials(client_id,client_secret)
sp=spotipy.Spotify(client_credentials_manager=client_credentials)
df=pd.read_csv('playlistdata.csv')
scaler=StandardScaler()
scaler.fit(df.drop('class',axis=1))

def home(request):
    return render(request,"home.html")

def result(request):
    knn=joblib.load('Knn_model_1.sav')
    take_input=request.GET['input']
    meta=sp.track(take_input)
    name=meta['name']
    artist = meta['album']['artists'][0]['name']
    features=sp.audio_features(take_input)
    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    speechiness = features[0]['speechiness']
    temp={'acousticness':[acousticness],'danceability':[danceability],'energy':[energy],'speechiness':[speechiness]}
    track_info=pd.DataFrame(temp,columns=df.columns[:-1])
    normalized=scaler.transform(track_info)
    normalized_features=pd.DataFrame(normalized,columns=df.columns[:-1])
    fin=knn.predict(normalized_features)[0]
    recommendations=[]
    recommendations.append(fin)
    #Finding the next common label point to recommend 
    l=knn.kneighbors(normalized_features,return_distance=False)
    l=l[0].tolist()
    label_points=[]
    for i in l:
        temp1=df['class'][i]
        if temp1!=fin:
            label_points.append(temp1)
    def next_recommendation(m):
        n=list(stats.find_repeats(m).values)
        d=list(stats.find_repeats(m).counts)
        if n==[]:
            return random.choice(m)
        else:
            return int(n[d.index(max(d))])
    second_recommendation=-1
    if label_points!=[]:
        second_recommendation=next_recommendation(label_points)
    else:
        t=[]
        for i in [1,2,3]:
            if i!=fin:
                t.append(i)
        second_recommendation=random.choice(t)
    #Creating list of the recommendations
    recommendations.append(second_recommendation)
    playlist_names=[]
    for i in recommendations:
        if i==1:
            s="/images/hiphop_image.jpeg"
            playlist_names.append(s)
        elif i==2:
            s1="/images/alternate_image.jpeg"
            playlist_names.append(s1)
        elif i==3:
            s2="/images/pop_imagefinal.jpeg"
            playlist_names.append(s2)
    return render(request,"result.html",{'ans':playlist_names[0],'ans2':playlist_names[1],'song_name':name})

