from app import app
import json

client = app.test_client()

def get_token():
    response = client.post('/login',data={'username': 'test', 'password': 'test'})
    data_json = json.loads(response.text)
    return data_json["token"] 


def test_signin():
    '''
    #Sono già presenti nel db, quindi non dà successo
    rv = client.post('/signin', data={'username': 'mattia_pulcino', 'password': 'pulcino', 'nome': 'Mattia', 'cognome': 'Di maria qualcosa'})
    assert rv.status_code == 200

    rv = client.post('/signin', data={'username': 'rakypazza01', 'password': 'rachele', 'nome': 'Rachele', 'cognome': 'Di maria'})
    assert rv.status_code == 200

    rv = client.post('/signin', data={'username': 'gioelino', 'password': 'albero', 'nome': 'Gioele', 'cognome': 'Modica'})
    assert rv.status_code == 200
    '''
    response = client.post('/signin',data={'username': 'utente1', 'password': '','nome': 'Mario', 'cognome': 'Rossi'})
    assert response.status_code == 400

    response = client.post('/signin' ,data={'username': 'gioelino', 'password': 'password', 'nome': 'Mario', 'cognome': 'Rossi'})
    assert response.status_code == 409

    response = client.post('/signin',data={})
    assert response.status_code == 400





def test_login():
    response = client.post('/login',data={'username': 'test', 'password': 'test'})
    assert response.status_code == 200


    response = client.post('/login', data={'username': 'utente_sconosciuto', 'password': 'albero'})
    assert response.status_code == 404


    response = client.post('/login', data={'username': 'gioelino', 'password': 'password_sbagliata'})
    assert response.status_code == 404

    response = client.post('/login',data={})
    assert response.status_code == 400



def test_getPost():
    response = client.get('/getPost?provincia=Pisa',headers={"Authorization":f'{get_token()}'})
    assert response.status_code==200

def test_getPost2():
    response = client.get('/getPost',headers={"Authorization":f'{get_token()}'})
    assert response.status_code==200


def test_getPost3():
    response = client.get('/getPost?provincia=Palermo',headers={"Authorization":f'{get_token()}'})
    assert response.status_code==404

def test_publishPost():
    data = {
        "provincia": "Milano",
        "tipologia": "Cane",
        "razza": "Pastore tedesco",
        "taglia": "Grande",
        "vaccinato": "True",
        "anni": "3",
        "citta": "Milano",
        "colore": "nero",
        "descrizione": "Bellissimo cane in cerca di casa",
        "nome_animale": "Rocky"
    }
    response = client.post("/publishPost",headers={"Authorization":f'{get_token()}'},data=data)
    assert response.status_code == 200

def test_deletePost():
    response = client.post('/deletePost',headers={"Authorization":f'{get_token()}'},data={'id': "63ecd1fa3fb90a8f48b9f641"})
    assert response.status_code == 403




