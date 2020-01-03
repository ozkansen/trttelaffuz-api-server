from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequestKeyError

from lib.trttelaffuz import TrtTelaffuz

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        try:
            q = request.form["q"]
        except BadRequestKeyError:
            q = None
    else:
        q = request.args.get("q")

    if q == None:
        return jsonify({
            "q": "",
            "detail": "Aranacak kelimeyi 'q' parametresine "
                      "POST metodu ile veya adres satırının sonuna"
                      "'q' parametresi ile gönderiniz."
        })

    search_keyword = TrtTelaffuz(q).return_dict_data()
    return jsonify(search_keyword)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
