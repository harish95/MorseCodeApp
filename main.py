from flask import Flask, render_template, request


app = Flask(__name__)


MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}
def TextToMorse(text):
    morse_code = ""
    for word in text:
        if word.upper() in MORSE_CODE_DICT.keys():
            morse_code += MORSE_CODE_DICT[word.upper()]
        else:
            morse_code += ' '
    return morse_code

@app.route("/", methods = ["POST","GET"])
def home():
    morse_code = ""
    if request.method == "POST":
        text = request.form['input']
        morse_code = TextToMorse(text)

    return render_template('index.html',morse_code=morse_code)


if __name__ == '__main__':
    app.run(debug=True)



