from flask import Flask,jsonify,request,abort
from pymongo import MongoClient
from pymongo.errors import WriteError
from bson.objectid import ObjectId
import hashlib,jwt
from functools import wraps
from datetime import datetime, timedelta
from flask_cors import CORS
from flask.json import JSONEncoder
import base64
try:
    client = MongoClient("mongodb+srv://gioele:Animaletto1.@animaletto.qy0pfrb.mongodb.net/test")
except:
    abort(505, "Errore nel contattare il server")
db = client["animalettodb"]
animali = db["post"]
utenti = db["user"]

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


app = Flask(__name__)
app.config["SECRET_KEY"]="b15af302e5f56b13fd72f5e693aa4abb"
app.json_encoder = CustomJSONEncoder
CORS(app, resources={r"/*": {'origins': "*"}})

#Da implementare
'''
    aggiungere il caricamento di foto per i post, puoi farlo solo quando hai il front, se no non è testabile
'''


#route implementate
'''
    Autenticazione JWT
    Visualizzazione post personali
    Ricerca dei post con filtri
    Pubblicazione dei post
    Cancellazione dei post 
    Registrazione
    Login
'''


def create_token(username):
    return jwt.encode({
        "username" : username,
        "expiration" : str(datetime.utcnow() + timedelta(minutes=30)),
        "alg":"HS256"
    },app.config["SECRET_KEY"])
    
def refresh_token(token):
    try:
        token=jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
        if datetime.strptime(token["expiration"],"%Y-%m-%d %H:%M:%S.%f") < datetime.utcnow():
            token = create_token(token["username"])
            token=jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
        return token
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return {"message":"errore creazione token"},500

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token=request.headers.get("Authorization")
        if token is None:
            return jsonify({"message":"token mancante"}),401
       
        #try:
            #payload=jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
        payload=refresh_token(token)
       # except:
        #    return jsonify({"message":"token non valido"}),403
        
        return func(payload,*args, **kwargs)
    return decorated
    


@app.route('/login',methods=["POST"])
def login():
    query={}
    query["username"]=request.form["username"]
    query["password"]=request.form["password"]    

    if query["username"]=="" or query["password"]=="":
       abort(400,"Stringhe vuote")

    
    query["password"]=hashlib.md5(query["password"].encode('utf-8')).hexdigest()
    if utenti.find_one(query) is None:
        abort(404,"Nessun utente con queste credenziali")

    token=create_token(query["username"])

    return jsonify({"token":token}),200

@app.route('/signin',methods=["POST"])
def signin():
    query={}
    query["username"]=request.form["username"]
    query["password"]=request.form["password"]    
    query["nome"]=request.form["nome"]
    query["cognome"]=request.form["cognome"] 
    query["email"]=request.form["email"] 
    query["cellulare"]=request.form["cellulare"] 
    if query["username"]=="" or query["password"]==""  or query["nome"]=="" or query["cognome"]=="":
        abort(400,"Stringhe vuote")

    try:
        if not utenti.find_one({"username":query["username"]}) is None:
            abort(409,"Utente già presente")
    except WriteError:
        abort(505, "Errore nel contattare il server")

    try:
        query["password"]=hashlib.md5(query["password"].encode('utf-8')).hexdigest()
        utenti.insert_one(query)
    except WriteError:
        abort("Errore nel contattare il server",500)

    return "ok", 200


@app.route('/')
def index():
    return 'Animalettiiiiiiii'


def ricerca(oldfiltro):
    filtro={}
    for key, value in oldfiltro.items():
        if not value is None:
            filtro[key]=value
    try:
        an= list(animali.find(filtro))
    except WriteError:
        abort(505, "Errore nel contattare il server")
    return an



@app.route('/getPost',methods=["GET"]) 
@token_required
def getPost(username):
    username=username["username"]
    '''
    restituisce tutti i post se non viene passato nessun parametro
    restituisce tutti i post o i post filtrati per: [razza,taglia,tipologia,vaccinato,regione]
    '''
    filtro={}
    filtro["regione"]=request.args.get("regione")
    filtro["tipologia"]=request.args.get("tipologia")
    filtro["taglia"]=request.args.get("taglia")
    filtro["vaccinato"]=request.args.get("vaccinato")
 

    animal=ricerca(filtro)

    if len(animal)==0 or animal is None:
       return jsonify({}),200
    ret=[]
    for an in animal:
        creatore=an["creatore"]
        if creatore is None:
            abort(404, "Nessun utente associato alla creazione del post")
        try:    
          user=utenti.find_one({"username":creatore})
        except WriteError:
            abort(500, "Errore nel contattare il server")
        if user is None:
            abort(404, "Nessun utente con l'username indicato ")
        an["creatore"]=user
        ret.append(an)
    ret.reverse()
    return jsonify(ret),200

@app.route('/publishPost',methods=["POST"]) 
@token_required
def publishPost(username):
    
    username=username["username"]

    '''
    Aggiunge un nuovo post associato all'utente
    '''
    query={}
    query["regione"]=request.form["regione"]
    query["tipologia"]=request.form["tipologia"]
    query["razza"]=request.form["razza"]
    query["taglia"]=request.form["taglia"]
    query["vaccinato"]=request.form["vaccinato"]
    query["anni"]=request.form["anni"]
    query["citta"]=request.form["citta"]
    query["colore"]=request.form["colore"]
    query["descrizione"]=request.form["descrizione"]
    query["nome_animale"]=request.form["nome_animale"]
    file =request.files["file"]
    file_str=base64.b64encode(file.read())
    query["file"]=file_str.decode('utf-8')
    
    try:
        if utenti.find_one({"username":username}) is None:
            abort(400,"errore creatore post")
    except WriteError:
        abort(505, "Errore nel contattare il server")
    query["creatore"]=username

    query["anni"]=int(query["anni"])
    try:
        animali.insert_one(query)
    except WriteError:
        abort("Errore nel contattare il server",500)

    return "ok",200

@app.route('/deletePost',methods=["POST"]) 
@token_required
def deletePost(username):
    '''
    Elimina un post con un determinato id (può solo chi l'ha creato).
    '''
    username=username["username"]
    try:
        result = animali.delete_one({'_id': ObjectId(request.form["id"])})
    except WriteError:
        abort(505, "Errore nel contattare il server")
    if result.deleted_count != 1:
        abort("Nessun post trovato", 404)
    return "ok", 200
    


@app.route('/getMyPost',methods=["GET"]) 
@token_required
def getMyPost(username):
    username=username["username"]
    '''
    restituisce tutti i post associati ad un utente, l'username del creatore è estratto dal token
    '''
    try:
        animal=list(animali.find({"creatore":username}))
    except WriteError:
        abort(505, "Errore nel contattare il server")
    if len(animal)==0 or animal is None:
        abort(404,"Nessun animale trovato o problemi nel contattare il server")
    ret=[]
    for an in animal:
        creatore=an["creatore"]
        if creatore is None:
            abort(404, "Nessun utente associato alla creazione del post")
        try:
            user=utenti.find_one({"username":creatore})
        except WriteError:
            abort(505, "Errore nel contattare il server")
        if user is None:
            abort(404, "Nessun utente con l'username indicato ")
        an["creatore"]=user
        ret.append(an)
    ret.reverse()
    return jsonify(ret),200


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)