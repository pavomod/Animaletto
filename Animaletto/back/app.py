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




class CustomJSONEncoder(JSONEncoder): #converte in stringa gli objectID 
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)


try:
    client = MongoClient("qui va il link con le credenziali") #connessione al server mongo
except:
    abort(505, "Errore nel contattare il server")
db = client["animalettodb"]
animali = db["post"] #documento degli annunci
utenti = db["user"] #documento degli utenti registrati
app = Flask(__name__)
app.config["SECRET_KEY"]="qui va la chiave" #chaive di codifica del token jwt
app.json_encoder = CustomJSONEncoder
CORS(app, resources={r"/*": {'origins': "*"}}) #formato e domini accettati, impostato su all per debug



#route implementate
'''
    Registrazione
    Login
    Autenticazione JWT
    Visualizzazione post personali
    Ricerca dei post con filtri
    Pubblicazione dei post
    Cancellazione dei post 

'''


def create_token(username): 
    '''
    Crea un token di autenticazione formato dall'username e la data di scadenza (30 min)
    '''
    return jwt.encode({
        "username" : username,
        "expiration" : str(datetime.utcnow() + timedelta(minutes=30)),
        "alg":"HS256"
    },app.config["SECRET_KEY"])
    
def refresh_token(token):
    '''
    Ogni 30' viene refreshato il token dell'utente con la nuova data di scadenza.
    '''
    try:
        token=jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
        if datetime.strptime(token["expiration"],"%Y-%m-%d %H:%M:%S.%f") < datetime.utcnow():
            token = create_token(token["username"])
            token=jwt.decode(token,app.config["SECRET_KEY"],algorithms="HS256")
        return token
    except (RuntimeError, KeyError):
        return {"message":"errore creazione token"},500

def token_required(func): 
    '''
    Funzione wrap che prima di permettere l'uso di un metodo verifica la presenza e la validità del token
    '''
    @wraps(func)
    def decorated(*args, **kwargs):
        token=request.headers.get("Authorization")
        if token is None:
            return jsonify({"message":"token mancante"}),401
        payload=refresh_token(token)
        return func(payload,*args, **kwargs)
    return decorated
    


@app.route('/login',methods=["POST"])
def login():
    '''
    Effettua il login dell'utente assegnando un token di autenticazione in caso di corrispondenza con il DB.
    '''
    query={}
    query["username"]=request.form["username"]
    query["password"]=request.form["password"]    

    if query["username"]=="" or query["password"]=="":
       return {"message":"Stringhe vuote"},400

    
    query["password"]=hashlib.md5(query["password"].encode('utf-8')).hexdigest()
    if utenti.find_one(query) is None:
        return {"message":"Nessun utente con queste credenziali"},404

    token=create_token(query["username"])
    log("L'utente ["+query["username"]+"] ha effettuato l'accesso.")
    #modifica appena implementata
    token=str(token)
    token=token[1:]
    token = token.replace("'", "")
    return jsonify({"token":token}),200

@app.route('/signin',methods=["POST"])
def signin():
    '''
    Registra un utente solo se l'username non è già presente nel DB
    '''
    query={}
    query["username"]=request.form["username"]
    query["password"]=request.form["password"]    
    query["nome"]=request.form["nome"]
    query["cognome"]=request.form["cognome"] 
    query["email"]=request.form["email"] 
    query["cellulare"]=request.form["cellulare"] 
    if query["username"]=="" or query["password"]==""  or query["nome"]=="" or query["cognome"]=="":
        return {"message":"Stringhe vuote"},400
    try:
        if not utenti.find_one({"username":query["username"]}) is None:
            return {"message":"Utente gia presente"},409
    except WriteError:
        return {"message":"Errore nel contattare il server"},505

    try:
        query["password"]=hashlib.md5(query["password"].encode('utf-8')).hexdigest()
        utenti.insert_one(query)
    except WriteError:
        return {"message":"Errore nel contattare il server"},505
    log("L'utente ["+query["username"]+"] e stato registrato.")
    return {"message":"ok"}, 200


@app.route('/')
def index():
    '''
    Inutile, ma è la prima route che ho creato per provare flask
    '''
    return {"message":'Animalettiiiiiiii'},202


def ricerca(oldfiltro):
    '''
    Query al db con filtro per ricerca di annunci. 
    Restituisce una lista di dizionari.
    '''
    filtro={}
    for key, value in oldfiltro.items():
        if not value is None:
            filtro[key]=value
    try:
        an= list(animali.find(filtro))
    except WriteError:
        return {"message":"Errore nel contattare il server"},505
    return an



@app.route('/getPost',methods=["GET"]) 
@token_required
def getPost(username):
    '''
    Restituisce tutti i post se non viene passato nessun parametro
    Restituisce tutti i post o i post filtrati per: [razza,taglia,tipologia,vaccinato,regione]
    '''
    username=username["username"]

    
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
            return {"message":"Erorre username creatore"},404
        try:    
          user=utenti.find_one({"username":creatore})
        except WriteError:
            return {"message":"Errore nel contattare il server"},500
        if user is None:
            return {"message":"Errore username creatore"},404
        an["creatore"]=user
        ret.append(an)
    ret.reverse()
    
    return jsonify(ret),200

@app.route('/publishPost',methods=["POST"]) 
@token_required
def publishPost(username):
    '''
    Carica un annuncio sul db nella tabella POST associandogli l'username del creatore.
    L'username viene estratto dal token.
    '''
    username=username["username"]

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
            return {"message":"Errore username creatore"},400
    except WriteError:
        return {"message":"Errore nel contattare il server"},500
    query["creatore"]=username

    query["anni"]=int(query["anni"])
    try:
        animali.insert_one(query)
    except WriteError:
        return {"message":"Errore nel contattare il server"},500
    
    log("L'utente ["+username+"] ha pubblicato un post.")
    return {"message":"ok"},200

@app.route('/deletePost',methods=["POST"]) 
@token_required
def deletePost(username):
    '''
    Elimina un post con un determinato ID.
    '''
    username=username["username"]
    try:
        result = animali.delete_one({'_id': ObjectId(request.form["id"])})
    except WriteError:
        return {"message":"Errore nel contattare il server"},500
    if result.deleted_count != 1:
        return {"message":"Nessun post trovato"},404
    log("L'utente ["+username+"] ha eliminato il post ["+request.form["id"]+"].")
    return {"message":"ok"}, 200
    


@app.route('/getMyPost',methods=["GET"]) 
@token_required
def getMyPost(username):
    '''
    Restituisce tutti i post associati ad un utente, l'username del creatore è estratto dal token
    '''
    username=username["username"]
    
    try:
        animal=list(animali.find({"creatore":username}))
    except WriteError:
        return {"message":"Errore nel contattare il server"},500
    if len(animal)==0:
        return {"message":"Nessun post trovato"},404
    ret=[]
    
    for an in animal:
        creatore=an["creatore"]
        if creatore is None:
            return {"message":"Errore username creatore post"},404
        try:
            user=utenti.find_one({"username":creatore})
        except WriteError:
            return {"message":"Errore nel contattare il server"},500
        if user is None:
            return {"message":"Errore username creatore post"},404
        an["creatore"]=user
        ret.append(an)
    ret.reverse()
    
    return jsonify(ret),200

def log(message):
    '''
    Aggiunge una stringa nel file di log con data e ora corrente.
    '''
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")


if __name__ == '__main__':
    '''
    Host impostato su 0.0.0.0 nel caso del deploy online del back. [Es. pythoneverywhere da errore con 127.0.0.1]
    '''
    app.run(host="0.0.0.0",port=5000,debug=True)
