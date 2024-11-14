from flask import Flask, jsonify, request, send_from_directory
from typing import List, Optional
from dataclasses import dataclass
from math import ceil

app = Flask(__name__)

# Endpoint para las imágenes de personajes
@app.route('/ApiDBZ/personajes/<path:filename>')
def serve_personaje_image(filename):
    return send_from_directory('static/images/personajes', filename)

# Endpoint para las imágenes de planetas
@app.route('/ApiDBZ/planetas/<path:filename>')
def serve_planeta_image(filename):
    return send_from_directory('static/images/planetas', filename)

# Endpoint para las imágenes de transformaciones
@app.route('/ApiDBZ/transformaciones/<path:filename>')
def serve_transformacion_image(filename):
    return send_from_directory('static/images/transformaciones', filename)

@dataclass
class Planet:
    id: int
    name: str
    isDestroyed: bool
    description: str
    image: str

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'isDestroyed': self.isDestroyed,
            'description': self.description,
            'image': self.image,
        }

@dataclass
class Transformation:
    id: int
    name: str
    image: str
    ki: str
    #canon: bool

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'ki': self.ki,
            #'canon': self.canon,
        }

@dataclass
class Character:
    id: int
    name: str
    ki: str
    maxKi: str
    race: str
    gender: str
    description: str
    image: str
    affiliation: str
    originPlanet: Planet
    transformations: List[Transformation]

    def to_dict(self, full = False):
        character_dict = {
            'id': self.id,
            'name': self.name,
            'ki': self.ki,
            'maxKi': self.maxKi,
            'race': self.race,
            'gender': self.gender,
            'description': self.description,
            'image': self.image,
            'affiliation': self.affiliation,
        }
        if full:
            character_dict['originPlanet'] = self.originPlanet.to_dict()
            character_dict['transformations'] = [t.to_dict() for t in self.transformations]
        return character_dict

# Sample data
SAMPLE_CHARACTERS = [
    Character(
        id = 1,
        name = "Goku",
        ki = "60.000.000",
        maxKi = "90 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "El protagonista de la serie, conocido por su gran poder y personalidad amigable...",
        image = "https://dragonball-api.com/characters/goku_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 1,
                name = "Goku SSJ",
                image = "https://dragonball-api.com/transformaciones/goku_ssj.webp",
                ki = "3 Billion",
            ),
            Transformation(
                id = 2,
                name = "Goku SSJ2",
                image = "https://dragonball-api.com/transformaciones/goku_ssj2.webp",
                ki = "6 Billion",
            ),
            Transformation(
                id = 3,
                name = "Goku SSJ3",
                image = "https://dragonball-api.com/transformaciones/goku_ssj3.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 4,
                name = "Goku SSJ4",
                image = "https://dragonball-api.com/transformaciones/goku_ssj4.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 5,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/goku_ssjb.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 6,
                name = "Goku Ultra Instinc",
                image = "https://dragonball-api.com/transformaciones/goku_ultra.webp",
                ki = "24 Billion",
            )
        ]
    ),
    Character(
        id = 2,
        name = "Vegeta",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 3,
        name = "Gohan",
        ki = "45.000.000",
        maxKi = "40 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Son Gohanda en su tiempo en España, o simplemente Gohan en Hispanoamérica, es uno de los personajes principales de los arcos argumentales de Dragon Ball Z, Dragon Ball Super y Dragon Ball GT. Es un mestizo entre saiyano y humano terrícola. Es el primer hijo de Son Goku y Chi-Chi, hermano mayor de Son Goten, esposo de Videl y padre de Pan.",
        image = "https://dragonball-api.com/characters/gohan.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [
            Transformation(
                id = 12,
                name = "Gohan SSJ",
                image = "https://dragonball-api.com/transformaciones/gohan_ssj-removebg-preview.webp",
                ki = "4.700.000.000",
            ),
            Transformation(
                id = 13,
                name = "Gohan SSJ2",
                image = "https://dragonball-api.com/transformaciones/Gohan_joven_ssj2.webp",
                ki = "10.200.000.000",
            ),
            Transformation(
                id = 14,
                name = "Gohan Ultimate",
                image = "https://dragonball-api.com/transformaciones/gohan_ultimate.webp",
                ki = "43.000.000.000",
            ),
            Transformation(
                id = 15,
                name = "Gohan Beast",
                image = "https://dragonball-api.com/transformaciones/beast_gohan___dragon_ball_super_super_hero_by_rmrlr2020_dfbqvta-pre.webp",
                ki = "25.6 Septillion",
            )
        ]
    ),
    Character(
        id = 4,
        name = "Broly",
        ki = "7 Quadrillion",
        maxKi = "11.2 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Broly es un Saiyajin que posee un poder gigantesco e incontrolable, el cual se manifiesta en toda su magnitud cuando se convierte en el Super Saiyajin Legendario. Incluso cuando apenas era un bebé su nivel de poder alcanzaba cifras inmensas que provocaban asombro y preocupación entre los de su raza",
        image = "https://dragonball-api.com/characters/Broly_DBS_Base.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 16,
                name = "Broly SSJ Legendary",
                image = "https://dragonball-api.com/transformaciones/Broly_Super_Saiyajin_Legendario_1.webp",
                ki = "11.2 Septillion",
            )
        ]
    ),
    Character(
        id = 5,
        name = "Trunks",
        ki = "50.000.000",
        maxKi = "37.4 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/Trunks_Buu_Artwork.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [
            Transformation(
                id = 17,
                name = "Trunks SSJ",
                image = "https://dragonball-api.com/transformaciones/trunks_ssj_removebg-preview.webp",
                ki = "905.000.000",
            ),
            Transformation(
                id = 18,
                name = "Trunks SSJ2",
                image = "https://dragonball-api.com/transformaciones/trunks ssj2.webp",
                ki = "18.000.000.000",
            ),
            Transformation(
                id = 19,
                name = "Trunks SS3",
                image = "https://dragonball-api.com/transformaciones/trunks ssj3.webp",
                ki = "1.25 Billion",
            ),
            Transformation(
                id = 20,
                name = "Trunks Rage",
                image = "https://dragonball-api.com/transformaciones/trunks ssj iracundo.webp",
                ki = "17.5 Quintillion",
            )
        ]
    ),
    Character(
        id = 6,
        name = "Goten",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 7,
        name = "Bardock",
        ki = "450.000",
        maxKi = "180.000.000",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 8,
        name = "Raditz",
        ki = "1.500",
        maxKi = "1.500",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Army of Frieza",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 9,
        name = "Nappa",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 10,
        name = "Turles",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 11,
        name = "Gine",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 12,
        name = "Paragus",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 13,
        name = "Rey Vegeta",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    ),
    Character(
        id = 14,
        name = "Son Pan",
        ki = "54.000.000",
        maxKi = "19.84 Septillion",
        race = "Saiyan",
        gender = "Male",
        description = "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Vegeta SSJ",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ (2).webp",
                ki = "330.000.000",
            ),
            Transformation(
                id = 8,
                name = "Vegeta SSJ2",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJ2.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 10,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 11,
                name = "Vegeta Mega Instinc Evil",
                image = "https://dragonball-api.com/transformaciones/vegeta mega instinto.webp",
                ki = "19.84 Septillion",
            )
        ]
    )
]

# Routes
@app.route('/characters', methods=['GET'])
def get_all_characters():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    
    total_items = len(SAMPLE_CHARACTERS)
    total_pages = ceil(total_items / limit)
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    
    # Get paginated items
    paginated_items = SAMPLE_CHARACTERS[start_idx:end_idx]
    
    return jsonify({
        'items': [char.to_dict() for char in paginated_items],
        'meta': {
            'totalItems': total_items,
            'itemCount': len(paginated_items),
            'itemsPerPage': limit,
            'totalPages': total_pages,
            'currentPage': page
        },
        'links': {
            'first': f"/characters?page=1&limit={limit}",
            'previous': f"/characters?page={page-1}&limit={limit}" if page > 1 else None,
            'next': f"/characters?page={page+1}&limit={limit}" if page < total_pages else None,
            'last': f"/characters?page={total_pages}&limit={limit}"
        }
    })

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = next((c for c in SAMPLE_CHARACTERS if c.id == character_id), None)
    if not character:
        return jsonify({'error': 'Character not found'}), 404
    return jsonify(character.to_dict(full = True))

if __name__ == '__main__':
    app.run(debug=True)