import json

from flask import Flask, Response, request
from utilizatori.functii import adauga_un_utilizator_flask, listeaza_toti_utilizatorii_flask, sterge_un_utilizator_flask
from produse.functii import adauga_un_produs_flask, listeaza_tote_produsele_flask, sterge_un_produs_flask
from comenzi.functii import adauga_o_comanda_flask, listeaza_toate_comenzile_flask, sterge_o_comanda_flask
app = Flask("Marketplace API")


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    return Response(status=200, response=json.dumps({"message": f"Hello, I'm A user: {user_id}"}))


@app.route("/put_user", methods=["POST"])
def put_user():
    message = json.loads(request.data)
    user_name = message.get("user_name")
    email_address = message.get("email_address")
    if not user_name or not email_address:
        return Response(status=503, response=json.dumps({"message": "user_name or email_address is missing"}))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=503, response=json.dumps(
            {"message": "user_name must be longer than 1 character and less than 50 characters"}))
    id_utilizator = adauga_un_utilizator_flask(user_name, email_address)
    return Response(status=200, response=json.dumps({"message": f"User: {id_utilizator} has been successfully added"}))

@app.route("/list_users", methods=["GET"])
def list_users():
    response = listeaza_toti_utilizatorii_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_toti_utilizatorii_flask()))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask(user_id)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/put_product", methods=["POST"])
def put_product():
    message = json.loads(request.data)
    product_name = message.get("product_name")
    product_price = message.get("product_price")
    if not product_name or not product_price:
        return Response(status=503, response=json.dumps({"message": "product_name or product_price is missing"}))
    id_produs = adauga_un_produs_flask(product_name, product_price)
    return Response(status=200, response=json.dumps({"message": f"product: {id_produs} has been successfully added"}))


@app.route("/list_produs", methods=["GET"])
def list_produs():
    response = listeaza_tote_produsele_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_tote_produsele_flask()))


@app.route("/delete_product/<string:id_product>", methods=["DELETE"])
def delete_product(id_product):
    status, message = sterge_un_produs_flask(id_product)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/put_comand", methods=["POST"])
def put_comand():
    message = json.loads(request.data)
    id_product = message.get("id_product")
    product_quantity = message.get("product_quantity")
    if not id_product or not product_quantity:
        return Response(status=503, response=json.dumps({"message": "product_id or product_quantity is missing"}))
    id_produs = adauga_o_comanda_flask(id_product, product_quantity)
    return Response(status=200, response=json.dumps({"message": f"product: {id_produs} has been successfully added"}))


@app.route("/list_comenzi", methods=["GET"])
def list_comenzi():
    response = listeaza_toate_comenzile_flask()
    print(response)
    return Response(status=200, response=json.dumps(listeaza_toate_comenzile_flask()))


@app.route("/delete_comand/<string:id_comand>", methods=["DELETE"])
def delete_comand(id_comand):
    status, message = sterge_o_comanda_flask(id_comand)
    return Response(status=status, response=json.dumps({"message": message}))

if __name__ == "__main__":
    app.run()

