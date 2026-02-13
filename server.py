"""
Flask server for the Emotion Detection application.
Provides:
- GET /emotionDetector?textToAnalyze=<text>
- GET /
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the emotion of the provided text and return a formatted response.
    The text is provided as a query parameter named 'textToAnalyze'.
    If the dominant emotion is None (e.g., blank/invalid input), returns an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detection(text_to_analyze)

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    if dominant is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

@app.route("/")
def render_index_page():
    """
    Render the homepage for the Emotion Detection web app.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
