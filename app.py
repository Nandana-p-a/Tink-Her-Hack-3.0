from flask import Flask, request, redirect, url_for, session, jsonify, render_template
import os
import pandas as pd
from textblob import TextBlob
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SESSION_COOKIE_NAME'] = 'your_session_cookie_name'

# Spotify OAuth setup
sp_oauth = SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="user-library-read playlist-modify-public"
)

# Create a Spotipy client instance
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Load the music data dynamically
music_data = pd.read_csv('music_data.csv')  # Ensure music_data.csv is in the same directory

# Sentiment analysis function
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # Returns a float between -1 and 1
    if sentiment > 0.2:
        return "Happy"
    elif sentiment < -0.2:
        return "Sad"
    else:
        return "Calm"

# Function to recommend songs based on emotion
def recommend_songs(emotion):
    recommendations = music_data[music_data['emotion'].str.lower() == emotion.lower()]
    return recommendations[['title', 'artist', 'url']].to_dict(orient='records')

# Route to handle sentiment analysis based on text input
@app.route('/predict_emotion', methods=['POST'])
def predict_emotion():
    text_input = request.form['text']  # Get text input from form
    emotion = analyze_sentiment(text_input)
    return redirect(url_for('recommend_emotion', emotion=emotion))  # Redirect to recommendations

# Route to get song recommendations based on emotion
@app.route('/recommend_emotion/<emotion>', methods=['GET'])
def recommend_emotion(emotion):
    # Get song recommendations for the detected emotion
    recommendations = recommend_songs(emotion)
    
    # Return the list of recommended songs to the user, passing the emotion to the template
    return render_template('recommendations.html', songs=recommendations, emotion=emotion)

# Route to start Spotify authentication
@app.route("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

# Callback route after user grants permission on Spotify
@app.route("/callback")
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('recommend_spotify'))

# Route to recommend songs from Spotify based on emotion
@app.route('/recommend_spotify')
def recommend_spotify():
    if not session.get("token_info"):
        return redirect(url_for("login"))

    token_info = session.get("token_info")
    sp = spotipy.Spotify(auth=token_info["access_token"])
    
    # Use Spotify API to recommend songs based on the detected emotion
    emotion = "Happy"  # Example emotion; replace dynamically
    results = sp.search(q=emotion.lower(), type='track', limit=5)

    tracks = results['tracks']['items']
    song_list = [{'name': track['name'], 'artist': track['artists'][0]['name'], 'url': track['external_urls']['spotify']} for track in tracks]

    return render_template('recommendations.html', songs=song_list)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
