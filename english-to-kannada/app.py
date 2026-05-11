from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

LANGUAGES = {
    'kn': 'Kannada',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ml': 'Malayalam',
    'bn': 'Bengali',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'zh': 'Chinese',
    'ar': 'Arabic'
}

@app.route('/')
def home():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()

        text = data.get('text', '').strip()
        target = data.get('target', 'kn').strip().lower()

        if not text:
            return jsonify({'error': 'Please enter some text'}), 400

        if target not in LANGUAGES:
            return jsonify({'error': 'Invalid language'}), 400

        translator = GoogleTranslator(source='en', target=target)
        translated = translator.translate(text)

        return jsonify({
            'success': True,
            'original': text,
            'translated': translated,
            'target': target,
            'target_name': LANGUAGES[target]
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)