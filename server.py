"""Flask web application for emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector as detect_emotion

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the submitted text and return its emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze")
    result = detect_emotion(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Testo non valido! Riprova!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
