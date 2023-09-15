import json

def convert_to_json(song_recommendations):
    songs = []
    for i, recommendation in enumerate(song_recommendations, start=1):
        recommendation = recommendation.strip()
        if " - " not in recommendation or " : " not in recommendation:
            print(f"Ignoring invalid recommendation at line {i}: {recommendation}")
            continue
        song_artist, genre = recommendation.split(" : ", 1)
        song, artist = song_artist.split(" - ", 1)
        song_data = {
            "id": str(i),
            "song": song.strip(),
            "artist": artist.strip(),
            "genre": genre.strip()
        }
        songs.append(song_data)
    
    json_data = {
        "songs": songs
    }
    return json.dumps(json_data, indent=4)

# Read song recommendations from text file
file_path = "data/songs.txt"
with open(file_path, "r") as file:
    recommendations = file.readlines()

# Convert recommendations to JSON format
json_result = convert_to_json(recommendations)

# Write JSON result to a new file
output_file_path = "recommendations.json"
with open(output_file_path, "w") as output_file:
    output_file.write(json_result)

print("JSON file created successfully.")
