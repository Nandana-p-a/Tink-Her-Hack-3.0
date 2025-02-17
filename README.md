# Tink-Her-Hack-3.0
# EchoMood 🎯


## Basic Details
### Team Name: Tech Divas


### Team Members
- Member 1: Nandana P A- Muthoot Institute of Technology and Science 
- Member 2: Jeslia Jobi- Muthoot Institute of Technology and Science 
- Member 3: Parvathi Krishna- Muthoot Institute of Technology and Science 

### Project Description
EchoMood is a web app that recommends music based on your emotions. It uses Flask for the backend and TextBlob for sentiment analysis. Users type a sentence describing their mood, and the app suggests songs from a local database or Spotify. Personalized recommendations are available via Spotify login.

### The Problem statement
Traditional music recommendation systems lack the ability to adapt dynamically to a user’s real-time emotional state. They often rely on historical listening patterns, which may not align with how the user currently feels. This limitation creates a gap for users seeking emotionally resonant music in the moment.

### The Solution
This project offers an Emotion-Based Music Recommendation System, a web application that detects a user’s mood through text input and recommends songs tailored to their emotions. By integrating a local music dataset and Spotify’s API, the system delivers personalized playlists dynamically matched to the user’s detected emotional state (e.g., Happy, Sad, Neutral, Angry). It provides a seamless user experience and bridges the gap between emotional needs and music discovery.

## Technical Details
### Technologies/Components Used
For Software:
- Languages used : Python, HTML, CSS
- Frameworks used : Flask
- Libraries used : Spotipy, TextBlob, Pandas, os, jsonify, Session
- Tools used : Sotipy Developer Dashboard, Text Editor/IDE, Python Package Manager


### Implementation
1.Emotion Detection :

-Analyzes user input text using TextBlob for sentiment analysis.
-Detects emotions such as Happy, Sad, Neutral, and Angry.

2.Music Recommendation :

-Uses a local music dataset (music_data.csv) to recommend songs based on emotions.
-Integrates with the Spotify API to fetch personalized playlists dynamically.

3.Web Application :

-Developed using Flask to provide a seamless user interface for input, authentication, and recommendations.
-Renders dynamic HTML templates (index.html, recommendations.html).

4.Spotify Integration :

-Implements OAuth 2.0 authentication to log in users via Spotify.
-Retrieves personalized song recommendations through Spotify's API.

4.Session Handling :

-Stores detected emotions and user authentication details in the Flask session for streamlined flow across routes.

# Installation
1. pip install flask spotipy textblob pandas
2. music_data.csv
3. Client ID, Client Secret, and configure the Redirect URI from Spotify Development Dashboard


# Run
python app.py 

# Screenshots (Add at least 3)
Home Page:
https://github.com/Nandana-p-a/Tink-Her-Hack-3.0/blob/0903b074f314b7929eeab98ababe057935818441/EchoMood%20Images/Home%20page.jpg

Emotion Detection:
https://github.com/Nandana-p-a/Tink-Her-Hack-3.0/blob/0903b074f314b7929eeab98ababe057935818441/EchoMood%20Images/Emotion%20detection.jpg

Song Recomendations:
https://github.com/Nandana-p-a/Tink-Her-Hack-3.0/blob/0903b074f314b7929eeab98ababe057935818441/EchoMood%20Images/Song%20recommendations.jpg


# Build Photos
Refer 'EchoMood Images' Folder: 
https://github.com/Nandana-p-a/Tink-Her-Hack-3.0/tree/0903b074f314b7929eeab98ababe057935818441/EchoMood%20Images

### Project Demo
# Video
https://github.com/Nandana-p-a/Tink-Her-Hack-3.0/blob/6de8b4c20655eac6b7fbd8a89c4d1dffefda22e1/Video/Video.mp4


---
Made with ❤ at TinkerHub
