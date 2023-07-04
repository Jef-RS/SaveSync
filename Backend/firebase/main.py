import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

diretório = os.path.dirname(__file__)
name_arq = os.path.basename(diretório)
diretório_raiz = diretório[:-8]


# Initialize the Firebase app
cred = credentials.Certificate(f"{diretório_raiz}firebase/firebase.json")
firebase_admin.initialize_app(cred)

# Get a Firestore client
db = firestore.client()

# Specify the collection and document data
collection_name = "users"
document_data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30
}

# Add the document to the collection
db.collection(collection_name).add(document_data)

