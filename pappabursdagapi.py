from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/generate_birthday_card', methods=['POST'])
def generate_birthday_card():
    data = request.get_json()
    name = data['name']
    message = f"""
    **************************************
    *                                    *
    *     Kjære {name},                   *
    *                                    *
    **************************************
    
    Jeg er sikkelig glad i deg og setter enormt stor pris på å ha deg som min far.
    Ja, jeg vil gjerne spise med deg på restaurant, men jeg kunne også tenkt meg noe annet.
    Derfor ønsker jeg å invitere deg med på en tur til et valgfritt sted, selvfølgelig innenfor rimelige grenser økonomisk sett.
    Vi kan begge spare 500 kr i måneden for å gjøre denne turen mulig.
    
    Håper du får en fantastisk bursdag!
    
    Med kjærlighet,
    [Ditt navn]
    """
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
