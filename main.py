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
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
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
        ki = "",
        maxKi = "",
        race = "Saiyan",
        gender = "Male",
        description = "",
        image = "",
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
                id = 7,
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 8,
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 9,
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 10,
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 11,
                name = "",
                image = "",
                ki = "",
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
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 8,
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 9,
                name = "",
                image = "",
                ki = "",
            ),
            Transformation(
                id = 10,
                name = "",
                image = "",
                ki = "",
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
        description = "Es el hijo de Bardock y Gine, y hermano mayor de Son Goku. Él es uno de los pocos saiyanos que sobrevivieron a la destrucción del Planeta Vegeta, y formaba parte del equipo de Vegeta. Es el primer antagonista de Dragon Ball Z.",
        image = "https://dragonball-api.com/characters/Raditz_artwork_Dokkan.webp",
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
        ki = "",
        maxKi = "",
        race = "Saiyan",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
           
        ]
    ),
    Character(
        id = 10,
        name = "Turles",
        ki = "",
        maxKi = "",
        race = "",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 11,
        name = "Gine",
        ki = "",
        maxKi = "",
        race = "Saiyan",
        gender = "Female",
        description = "",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 12,
        name = "Paragus",
        ki = "",
        maxKi = "",
        race = "Saiyan",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 13,
        name = "Rey Vegeta",
        ki = "",
        maxKi = "",
        race = "Saiyan",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant...",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 14,
        name = "Son Pan",
        ki = "",
        maxKi = "",
        race = "",
        gender = "Female",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 15,
        name = "Bra",
        ki = "",
        maxKi = "",
        race = "Saiyan",
        gender = "Female",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 16,
        name = "Chaoz",
        ki = "",
        maxKi = "",
        race = "",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 17,
        name = "Chi-Chi",
        ki = "0",
        maxKi = "0",
        race = "Human",
        gender = "Female",
        description = "Esposa de Goku y madre de Gohan. Es la princesa del Monte Fry-pan siendo la hija de la fallecida reina de esta montaña y el Rey Gyuma, ella terminaría conociendo a Son Goku cuando era tan solo una niña para años más tarde durante su adolescencia ser su esposa y convertirse en la estricta pero amorosa madre de Gohan y Goten.",
        image = "https://dragonball-api.com/characters/ChiChi_DBS.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 18,
        name = "Ox-Satán",
        ki = "0",
        maxKi = "0",
        race = "Human",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 19,
        name = "Maestro Roshi",
        ki = "500.000",
        maxKi = "350.000.000",
        race = "Human",
        gender = "Male",
        description = "Maestro de artes marciales y mentor de Goku. Conocido bajo el nombre de Muten Rosh, fue en su momento el terrícola más fuerte de la Tierra, y mucha gente lo recuerda como el \"Dios de las Artes Marciales\", pero antes de poder ostentar dicho título tuvo que trabajar y estudiar las artes marciales con su maestro Mutaito y su eterno rival Tsuru-Sen'nin.",
        image = "https://dragonball-api.com/characters/roshi.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 20,
        name = "Maestro Karin",
        ki = "",
        maxKi = "",
        race = "Human",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 21,
        name = "Krilin",
        ki = "1.000.000",
        maxKi = "1 Billion",
        race = "Human",
        gender = "Male",
        description = "Amigo cercano de Goku y guerrero valiente, es un personaje del manga y anime de Dragon Ball. Es uno de los principales discípulos de Kame-Sen'nin, Guerrero Z, y el mejor amigo de Son Goku. Es junto a Bulma uno de los personajes de apoyo principales de Dragon Ball, Dragon Ball Z y Dragon Ball Super. Aparece en Dragon Ball GT como personaje secundario. En el Arco de Majin Boo, se retira de las artes marciales, optando por formar una familia, como el esposo de la Androide Número 18 y el padre de Marron.",
        image = "https://dragonball-api.com/characters/Krilin_Universo7.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 22,
        name = "Mr. Satán",
        ki = "450",
        maxKi = "5.000",
        race = "Human",
        gender = "Male",
        description = "Luchador humano famoso por llevarse el mérito de las victorias de los Guerreros Z.",
        image = "https://dragonball-api.com/characters/Mr_Satan_DBSuper.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 23,
        name = "Oob",
        ki = "",
        maxKi = "",
        race = "Human",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 24,
        name = "Ten Shin Han",
        ki = "2.400.000",
        maxKi = "80.000.000",
        race = "Human",
        gender = "Male",
        description = "Maestro de las artes marciales y miembro de los Z Fighters.  Es un personaje que aparece en el manga y en el anime de Dragon Ball, Dragon Ball Z, Dragon Ball GT y posteriormente en Dragon Ball Super.",
        image = "https://dragonball-api.com/characters/Tenshinhan_Universo7.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 25,
        name = "Yajirobe",
        ki = "",
        maxKi = "",
        race = "Human",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 26,
        name = "Yamcha",
        ki = "1.980.000",
        maxKi = "4.000.000",
        race = "Human",
        gender = "Male",
        description = "Luchador que solía ser un bandido del desierto.",
        image = "https://dragonball-api.com/characters/Final_Yamcha.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 27,
        name = "Android 8",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Male",
        description = "El Androide Número 8, es un androide creado por el Dr. Gero y el Dr. Frappé como una de las armas secretas del Ejército del Listón Rojo, siendo el encargado de la seguridad de la Torre Músculo en sus últimos niveles. Tiene una fuerza muy superior a la de un humano corriente así como un tamaño y físico aterradores.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 28,
        name = "Android 9",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Male",
        description = "El Androide Número 9, es un androide mecánico miembro del Ejército de los Pantalones Rojos construido por el Dr. Gero del Ejército del Listón Rojo en el videojuego Dragon Ball Online.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 29,
        name = "Android 13",
        ki = "195.000.000",
        maxKi = "562.500.000",
        race = "Android",
        gender = "Male",
        description = "Android 13 es un androide peligroso que aparece en la película \"El Regreso de Cooler\".",
        image = "https://dragonball-api.com/characters/Androide13normal.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 30,
        name = "Android 14",
        ki = "192.500.000",
        maxKi = "192.500.000",
        race = "Android",
        gender = "Male",
        description = "Android 14 es otro androide que aparece en la misma película que Android 13.",
        image = "https://dragonball-api.com/characters/14Dokkan.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 31,
        name = "Android 15",
        ki = "175.000.000",
        maxKi = "175.000.000",
        race = "Android",
        gender = "Male",
        description = "Android 15 es otro androide que aparece en la misma película que Android 13.",
        image = "https://dragonball-api.com/characters/15Dokkan.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 32,
        name = "Android 16",
        ki = "440.000.000",
        maxKi = "440.000.000",
        race = "Android",
        gender = "Male",
        description = "Android 16 es un androide gigante conocido por su amor a la naturaleza y la vida.",
        image = "https://dragonball-api.com/characters/Androide_16.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 33,
        name = "Android 17",
        ki = "320.000.000",
        maxKi = "40 Quintillion",
        race = "Android",
        gender = "Male",
        description = "Antes de ser secuestrado, es el hermano mellizo de la Androide Número 18, quien al igual que ella antes de ser Androide era un humano normal hasta que fueron secuestrados por el Dr. Gero, y es por eso que lo odian. Tras su cambio de humano a Androide, le insertaron un chip con el objetivo de destruir a Son Goku, quien en su juventud extermino al Ejército del Listón Rojo. Al considerarse defectuoso porque no quería ser 'esclavo de nadie', el Dr. Gero les había colocado a ambos hermanos, un dispositivo de apagado para detenerlos en cualquier momento de desobediencia, pero cuando el científico los despierta, el rencor y rebeldía de 17 eran tal que se encargó de destruir el control que lo volvería a encerrar y acto seguido mató sin piedad a su propio creador. Su situación se le iría en contra, ya que Cell tenía como misión absorber a 17 y 18 para completar su desarrollo y convertirse en Cell Perfecto.",
        image = "https://dragonball-api.com/characters/17_Artwork.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 34,
        name = "Android 18",
        ki = "280.000.000",
        maxKi = "300.000.000",
        race = "Android",
        gender = "Female",
        description = "Es la hermana melliza del Androide Número 17 y una \"androide\" creada a partir de una base humana por el Dr. Gero con el único fin de destruir a Goku aunque sus deseos cambiaron y ahora es esposa de Krilin con quien tuvo una hija llamada Marron",
        image = "https://dragonball-api.com/characters/Androide_18_Artwork.webp",
        affiliation = "Z Figther",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 35,
        name = "Android 19",
        ki = "122.000.000",
        maxKi = "160.000.000",
        race = "Android",
        gender = "Male",
        description = "Android 19 es uno de los androides creados por el Dr. Gero.",
        image = "https://dragonball-api.com/characters/Android19.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 36,
        name = "Android 20 (Dr. Gero)",
        ki = "128.000.000",
        maxKi = "128.100.000",
        race = "Android",
        gender = "Male",
        description = "Dr. Gero es el científico loco que creó a los androides 17, 18 y 19.",
        image = "Dr. Gero es el científico loco que creó a los androides 17, 18 y 19.",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 37,
        name = "Android 21",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Female",
        description = "La Androide Número 21, es un androide creado a base humana que aparece por primera vez en el videojuego Dragon Ball FighterZ. Es una científica del Ejército Red Ribbon. Ella explica que “ni siquiera” tiene diez años y fue construida a imagen de una mujer humana con el coeficiente de inteligencia de un adulto.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 38,
        name = "Arale Norimaki",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Female",
        description = "Arale Norimaki, es la máxima protagonista de la serie creada por Akira Toriyama Dr. Slump, también hace su aparición en Dragon Ball, Dragon Ball Super y cameos menores a lo largo de la serie.",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 39,
        name = "Cell",
        ki = "250.000.000",
        maxKi = "5 Billion",
        race = "Android",
        gender = "Male",
        description = "Android 16 es un androide gigante conocido por su amor a la naturaleza y la vida.",
        image = "https://dragonball-api.com/characters/celula.webp",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Imperfect Form",
                image = "https://dragonball-api.com/transformaciones/cell imperfect.webp",
                ki = "370.000.000",
            ),
            Transformation(
                id = 8,
                name = "Semi Perfect Form",
                image = "https://dragonball-api.com/transformaciones/Semi-Perfect_Cell.webp",
                ki = "897.000.000",
            ),
            Transformation(
                id = 9,
                name = "Super Perfect Form",
                image = "https://dragonball-api.com/transformaciones/cell perfect.webp",
                ki = "10.970.000.000",
            ),
        ]
    ),
    Character(
        id = 40,
        name = "Cell Jr",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Male",
        description = "",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 41,
        name = "Bio-Broly",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Male",
        description = "Bio-Broly, es un clon mutante del Supersaiyano Legendario Broly. Hace su primera y única aparición cómo antagonista en la película Dragon Ball Z: ¡Los superguerreros vencen! La victoria solamente será mía.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 42,
        name = "Super Android 17",
        ki = "",
        maxKi = "",
        race = "Android",
        gender = "Male",
        description = "Super Número 17, es el superandroide definitivo, formado por la unión entre el Androide Número 17 y su nueva versión, el Androide Número 17 del Infierno, creado por el Dr. Mu y el Dr. Gero en el Infierno. Aparece por primera vez como el antagonista principal del Arco del Androide Definitivo en Dragon Ball GT.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 43,
        name = "Bubbles",
        ki = "0",
        maxKi = "0",
        race = "Mono",
        gender = "Male",
        description = "Bubbles es la mascota y amigo del Kaio del Norte. Él vive junto al Kaio del Norte y Gregory, ayudando al Kaio del Norte en las pruebas de sus alumnos, donde por lo general los discípulos del Kaio del Norte lo deben de atrapar, tarea difícil ya que la gravedad del Planeta Kaio es muy alta y Bubbles está acostumbrado a ella.",
        image = "",
        affiliation = "Other",
        originPlanet = Planet(
            id = 2,
            name = "Kaiō del Norte",
            isDestroyed = False,
            description = "El Planeta Kaio se encuentra al final del largo Camino de la Serpiente. Es donde viven el Kaio del Norte, su mascota Bubbles, al que utiliza como parte de su entrenamiento, y Gregory.",
            image = "https://dragonball-api.com/planetas/Planeta_del_Kaio_del_Norte.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 44,
        name = "Gregory",
        ki = "0",
        maxKi = "0",
        race = "Sprite",
        gender = "Male",
        description = "Android 16 es un androide gigante conocido por su amor a la naturaleza y la vida.",
        image = "",
        affiliation = "Other",
        originPlanet = Planet(
            id = 2,
            name = "Kaiō del Norte",
            isDestroyed = False,
            description = "Gregory es un Sprite macho (confundido con un grillo a veces) con la capacidad de hablar, también es el mayordomo y asistente del Kaio del Norte. Gregory no apareció en el manga original convirtiéndose en un personaje exclusivo del anime, sin embargo tras la llegada de Dragon Ball Z Kai y Dragon Ball Super, Gregory paso a formar parte de la historia principal de la serie.",
            image = "https://dragonball-api.com/planetas/Planeta_del_Kaio_del_Norte.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 45,
        name = "Oolong",
        ki = "",
        maxKi = "",
        race = "Animal",
        gender = "Male",
        description = "Oolong es un personaje del manga y anime de Dragon Ball, el cual forma parte del grupo que acompaña a Bulma en la primera búsqueda de las Esferas del Dragón. Representa al personaje Zhu Bajie de la historia china Viaje al Oeste.",
        image = "",
        affiliation = "Z Figther",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 46,
        name = "Piano",
        ki = "",
        maxKi = "",
        race = "Demon warrior",
        gender = "Asexuado",
        description = "Piano fue el primer 'hijo' del Gran Rey Demonio Piccolo después de su liberación de la técnica Mafuba a manos de Pilaf. Es un ser bastante inteligente, posee forma de pterodáctilo, y a pesar de ser el retoño más longevo del Rey Demonio, este lo trata como una especie de sirviente.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),

    Character(
        id = 47,
        name = "Puar",
        ki = "",
        maxKi = "",
        race = "Animal",
        gender = "Male",
        description = "Pu'er es el compañero inseparable de Yamcha. Aunque al principio era un enemigo, pasa a formar parte del grupo que acompaña a Son Goku, Bulma y Woolong en la primera búsqueda de las Esferas del Dragón en la serie de manga y anime de Dragon Ball.",
        image = "",
        affiliation = "Z Figther",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 48,
        name = "Shu",
        ki = "",
        maxKi = "",
        race = "Humanoide",
        gender = "Male",
        description = "Shu, inicialmente conocido en el manga como Soba, es un perro humanoide. Forma parte del grupo de Pilaf y desde el principio de Dragon Ball hasta Dragon Ball GT estuvo intentando junto a su amo Pilaf conquistar el mundo.",
        image = "",
        affiliation = "Pilaf's Helper",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 49,
        name = "Tortuga Marina",
        ki = "",
        maxKi = "",
        race = "Animal",
        gender = "Male",
        description = "Tortuga Marina, conocido como Urigame en Hispanoamérica, es la tortuga que ha acompañado al Maestro Roshi durante un largo tiempo; tiene más de mil años de edad y hace cientos de años que aprendió a hablar.",
        image = "",
        affiliation = "Master Roshi's Companion",
        originPlanet = Planet(
            id = 2,
            name = "Tierra",
            isDestroyed = False,
            description = "La Tierra también llamado Mundo del Dragón (Dragon World), es el planeta principal donde se desarrolla la serie de Dragon Ball. Se encuentra en el Sistema Solar de la Vía Láctea de las Galaxias del Norte del Universo 7, lugar que supervisa el Kaio del Norte, y tiene su equivalente en el Universo 6. El hogar de los terrícolas y los Guerreros Z. Ha sido atacado en varias ocasiones por enemigos poderosos.",
            image = "https://dragonball-api.com/planetas/Tierra_Dragon_Ball_Z.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 50,
        name = "Awamo",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Awamo es el ángel guía encargado del Universo 1, sirviente y maestro de artes marciales del Dios de la Destrucción Iwen. Es un personaje del Arco de Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Iwen",
        originPlanet = Planet(
            id = 2,
            name = "Universo 1",
            isDestroyed = False,
            description = "",
            image = "",
        ),
        transformations = [

        ]
    ),
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