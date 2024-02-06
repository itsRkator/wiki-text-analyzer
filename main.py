# app.py
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for search history
search_history = []

# Wikipedia API endpoint
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


def fetch_wikipedia_text(topic):
    # Function to fetch the text of a Wikipedia article based on the provided topic
    # Use Wikipedia API to get the content of the article
    params = {
        "action": "query",
        "format": "json",
        "titles": topic,
        "prop": "extracts",
        "exintro": True,
    }

    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()

    # Extract text content from the API response
    page_id = list(data["query"]["pages"].keys())[0]
    text = data["query"]["pages"][page_id].get("extract", "")

    return text


def analyze_word_frequency(text, n):
    # Function to analyze word frequency in the given text and return the top n frequent words
    # Tokenize the text into words
    words = text.split()

    # Calculate word frequency using a dictionary
    word_frequency = {}
    for word in words:
        word = word.lower()
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # Sort the dictionary by frequency in descending order
    sorted_word_frequency = sorted(
        word_frequency.items(), key=lambda x: x[1], reverse=True
    )

    # Return the top n frequent words
    return sorted_word_frequency[:n]


@app.route("/word_frequency", methods=["POST"])
def word_frequency_analysis():
    # Endpoint for word frequency analysis with data in the request body
    data = request.json  # Assuming the data is sent in JSON format

    # Check if 'topic' and 'n' are present in the request data
    if "topic" not in data or "n" not in data:
        return (
            jsonify({"error": "Missing required parameters in the request body"}),
            400,
        )

    topic = data["topic"]

    # Check if n is a valid integer
    try:
        n = int(data["n"])
    except ValueError:
        return jsonify({"error": 'Invalid value for parameter "n"'}), 400

    # Fetch Wikipedia text for the given topic
    text = fetch_wikipedia_text(topic)

    if not text:
        return (
            jsonify({"error": "Failed to fetch Wikipedia article for the given topic"}),
            400,
        )

    # Analyze word frequency
    top_words = analyze_word_frequency(text, n)

    # Store search history
    search_history.append({"topic": topic, "top_words": top_words})

    # Return the result in a structured format
    return jsonify({"topic": topic, "top_words": top_words})


@app.route("/search_history", methods=["GET"])
def search_history_endpoint():
    # Endpoint to retrieve search history
    return jsonify(search_history)


if __name__ == "__main__":
    app.run(debug=True)
