from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize translator
translator = GoogleTranslator(source='en', target='kn')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()

        if not text:
            return jsonify({'error': 'Please enter some text to translate'}), 400

        translated = translator.translate(text)
        return jsonify({
            'success': True,
            'original': text,
            'translated': translated
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)