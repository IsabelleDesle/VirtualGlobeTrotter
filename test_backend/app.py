from flask import Flask, request, jsonify
from flask_cors import CORS
import string

app = Flask(__name__)
CORS(app) 

@app.route('/change-background', methods=['POST'])
def change_background():
    data = request.json
    user_input = data.get('input', '').lower().translate(str.maketrans('', '',
                                    string.punctuation))

    if user_input == "cat":
        image_url = "https://th.bing.com/th/id/R.094ee0d312d6fb870f22e4e57a69bdd7?rik=394J%2fneqvGt7zQ&riu=http%3a%2f%2fimages4.fanpop.com%2fimage%2fphotos%2f16000000%2fBeautiful-Cat-cats-16096437-1280-800.jpg&ehk=7Ul0qN8DJPOyACXqdst%2bSeHYBg6ESI9MPS%2fjVm2XumU%3d&risl=&pid=ImgRaw&r=0"
    elif user_input == "hamster":
        image_url = "https://th.bing.com/th/id/R.5ff640be0c346801233c8cf6ac5ac168?rik=5yBo%2bDwxX%2bhmSA&pid=ImgRaw&r=0"
    else:
        image_url = "https://th.bing.com/th/id/OIP.W07rYmz1_ou1WpPaTlLnhgHaHI?rs=1&pid=ImgDetMain"

    return jsonify({"background_image": image_url})

if __name__ == "__main__":
    app.run(debug=True)
