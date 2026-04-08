from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)  # 'Flask' avec F majuscule

# Liste statique des formations
formations = [
    {
        'id': 1,
        'titre': 'DevOps Fundamentals',
        'duree': '40 heures',
        'niveau': 'Débutant',
        'technologies': ['Docker', 'CI/CD', 'Git']
    },
    {
        'id': 2,
        'titre': 'Python Avancé',
        'duree': '35 heures',
        'niveau': 'Intermédiaire',
        'technologies': ['Python', 'Flask', 'SQLAlchemy']
    },
    {
        'id': 3,
        'titre': 'Kubernetes pour Développeurs',
        'duree': '45 heures',
        'niveau': 'Avancé',
        'technologies': ['Kubernetes', 'Docker', 'Helm']
    },
    {
        'id': 4,
        'titre': 'AWS Cloud Practitioner',
        'duree': '30 heures',
        'niveau': 'Débutant',
        'technologies': ['AWS', 'EC2', 'S3']
    }
]

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html', 
                         titre="Bienvenue sur FormationHub",
                         date=datetime.now().strftime("%d/%m/%Y"))

@app.route('/formations')
def liste_formations():
    """Page listant toutes les formations"""
    return render_template('formations.html', 
                         formations=formations,
                         titre="Nos Formations")

@app.route('/formation/<int:id>')
def detail_formation(id):
    """Page détail d'une formation"""
    formation = next((f for f in formations if f['id'] == id), None)
    if formation:
        return render_template('formation_detail.html', 
                             formation=formation,
                             titre=formation['titre'])
    return "Formation non trouvée", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)