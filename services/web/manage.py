from flask.cli import FlaskGroup

from api_sf2 import app, db, Char, Facts

# Database creation

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.commit()

if __name__ == "__main__":
    cli()


# Data Inserts 

## Inserts fighters
fighters = [{'name': 'ryu'}, {'name': 'ken'}, {'name': 'honda'}, {'name': 'chunli'}, {'name': 'blanka'}, {'name': 'zangief'}, {'name': 'guile'}, {'name': 'dhalsim'}, {'name': 'thawk'}, {'name': 'cammy'}, {'name': 'feilong'}, {'name': 'deejay'}, {'name': 'balrog'}, {'name': 'vega'}, {'name': 'sagat'}, {'name': 'bison'}, {'name': 'akuma'}]

for fg in fighters:
    db.session.add(Char(**fg))
db.session.commit()

## Inserts facts
fact= [
{'char_id': '1', 'text': 'He wanders the world with the desire for complete mastery of his martial art, and takes both his travels and training seriously' },
{'char_id': '1', 'text': 'Ryu carries around a large, white duffel bag containing items important to his travels, such as clothing, plane tickets, passports, and local currency' },
{'char_id': '2', 'text': 'While Ryu is the more serious and stoic of the two, Ken is the complete opposite - stylish, unorthodox and unpredictable' },
{'char_id': '3', 'text': 'His signature move is the Hyaku Retsu Harite (lit., Hundred Violent Sumo Hands; commonly referred to as the Hundred Hand Slap)' },
{'char_id': '4', 'text': 'Her name in Mandarin stands for spring beauty' },
{'char_id': '5', 'text': 'Only one fighter appeared to not be human' },
{'char_id': '6', 'text': 'Was going to be called Vodka Gobalsky' },
{'char_id': '7', 'text': 'Guile leaves his country and family to enter the World Warrior tournament to avenge the death of his friend Charlie, who was killed by Bison' },
{'char_id': '8', 'text': 'Dhalsim originally had six arms' },
{'char_id': '9', 'text': 'He is a Native American from Mexico whose ancestral homeland was taken over by Shadaloo, forcing him into exile' },
{'char_id': '10', 'text': 'Cammy is the second female character toappear in the Street Fighter series' },
{'char_id': '11', 'text': 'Although he is a famous martial arts movie actor, he still takes his time to appear at underground fighting areas to find a worthy opponent to spar with ' },
{'char_id': '12', 'text': 'He is a Jamaican kickboxer who has made enormous strides in fame in the Street Fighter world not just as a fighter, but also as a world famous musician and recording artist' },
{'char_id': '13', 'text': 'Balrog is clearly the visual reference of professional boxer Mike Tyson' },
{'char_id': '14', 'text': 'Vega imagined as a traditional armored, sword-bearing knight, but was eventually developed into a figure with a Spanish ninja feel' },
{'char_id': '15', 'text': 'He is the "Emperor of Muay Thai" and a former member of Shadaloo, where he acted as a personal bodyguard for M. Bison' },
{'char_id': '16', 'text': 'Due to his Psycho Power, Bison is able to survive after death and move into a fresh body' },
{'char_id': '17', 'text': 'Rarely displays any sign of emotions or humanity' }
]

for fc in fact:
    db.session.add(Facts(**fc))
db.session.commit()