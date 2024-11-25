from Flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Skin Analysis API!'})

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    # İşleme ve model entegrasyonu burada yapılacak
    return jsonify({'result': 'Analysis result will appear here!'}), 200

if __name__ == '__main__':
    app.run(debug=True)