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
        description ="El protagonista de la serie, conocido por su gran poder y personalidad amigable. Originalmente enviado a la Tierra como un infante volador con la misión de conquistarla. Sin embargo, el caer por un barranco le proporcionó un brutal golpe que si bien casi lo mata, este alteró su memoria y anuló todos los instintos violentos de su especie, lo que lo hizo crecer con un corazón puro y bondadoso, pero conservando todos los poderes de su raza. No obstante, en la nueva continuidad de Dragon Ball se establece que él fue enviado por sus padres a la Tierra con el objetivo de sobrevivir a toda costa a la destrucción de su planeta por parte de Freeza. Más tarde, Kakarot, ahora conocido como Son Goku, se convertiría en el príncipe consorte del monte Fry-pan y líder de los Guerreros Z, así como el mayor defensor de la Tierra y del Universo 7, logrando mantenerlos a salvo de la destrucción en innumerables ocasiones, a pesar de no considerarse a sí mismo como un héroe o salvador.",
        image = "https://dragonball-api.com/characters/goku_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 1,
                name = "Goku Ozaru",
                image = "",
                ki = "180.000",
            ),
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
                name = "Goku SSJ Fase Dios",
                image = "",
                ki = "2.880.000.000.000",
            ),
            Transformation(
                id = 5,
                name = "Goku SSJ4",
                image = "https://dragonball-api.com/transformaciones/goku_ssj4.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 6,
                name = "Goku SSJB",
                image = "https://dragonball-api.com/transformaciones/goku_ssjb.webp",
                ki = "24 Billion",
            ),
            Transformation(
                id = 1,
                name = "Goku SSJB Kaioken X20",
                image = "",
                ki = "5 Cuatrillones",
            ),
            Transformation(
                id = 7,
                name = "Goku Ultra Instinc",
                image = "https://dragonball-api.com/transformaciones/goku_ultra.webp",
                ki = "100 Cuatrillones",
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
        description =  "Príncipe de los Saiyans, inicialmente un villano, pero luego se une a los Z Fighters. A pesar de que a inicios de Dragon Ball Z, Vegeta cumple un papel antagónico, poco después decide rebelarse ante el Imperio de Freeza, volviéndose un aliado clave para los Guerreros Z. Con el paso del tiempo llegaría a cambiar su manera de ser, optando por permanecer y vivir en la Tierra para luchar a su lado contra las inminentes adversidades que superar. Junto con Piccolo, él es de los antiguos enemigos de Goku que ha evolucionando al pasar de ser un villano y antihéroe, a finalmente un héroe a lo largo del transcurso de la historia, convirtiéndose así en el deuteragonista de la serie.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 1,
                name = "Vegeta Ozaru",
                image = "",
                ki = "180.000",
            ),
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
                id = 1,
                name = "Majin vegeta SSJ2",
                image = "",
                ki = "20.000.000.000",
            ),
            Transformation(
                id = 9,
                name = "Vegeta SSJ4",
                image = "https://dragonball-api.com/transformaciones/vegeta ssj4.webp",
                ki = "1.8 Trillion",
            ),
            Transformation(
                id = 1,
                name = "Vegeta SSJ Fase Dios",
                image = "",
                ki = "600.000.000.000",
            ),
            Transformation(
                id = 10,
                name = "Vegeta SSJB",
                image = "https://dragonball-api.com/transformaciones/vegeta SSJB.webp",
                ki = "100 Quintillion",
            ),
            Transformation(
                id = 1,
                name = "Vegeta SSJB Evolution",
                image = "",
                ki = "10.000.000.000.000",
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
                id = 1,
                name = "Gohan Ozaru",
                image = "",
                ki = "10.000",
            ),
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
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
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
        description = "Hijo de Vegeta y Bulma. Es un mestizo entre humano terrícola y Saiyano nacido en la Tierra, e hijo de Bulma y Vegeta, el cual es introducido en el Arco de los Androides y Cell. Más tarde en su vida como joven, se termina convirtiendo en un luchador de artes marciales, el mejor amigo de Son Goten y en el hermano mayor de su hermana Bra.",
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
                name = "Trunks future Rage",
                image = "https://dragonball-api.com/transformaciones/trunks ssj iracundo.webp",
                ki = "37.4 Septillion",
            )
        ]
    ),
    Character(
        id = 6,
        name = "Goten",
        ki = "19.000.000",
        maxKi = "18.000.000.000",
        race = "Saiyan",
        gender = "Male",
        description = "Hijo de Goku y Milk. Es un mestizo entre humano terrícola y Saiyano nacido en la Tierra, el cual es introducido en el Arco de los Androides y Cell. Más tarde en su vida como joven, se termina convirtiendo en un luchador de artes marciales, el mejor amigo de Trunks y en el hermano menor de su hermano Gohan.",
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
                name = "Goten SSJ",
                image = "",
                ki = "910.000.000",
            ),
            Transformation(
                id = 8,
                name = "Goten SSJ2",
                image = "",
                ki = "18.000.000.000",
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
        description = "Es un saiyano de clase baja proveniente del Planeta Vegeta del Universo 7. Pertenece al Ejército Saiyano, que está bajo el liderazgo del Rey Vegeta, y es jefe de su escuadrón durante la anexión del planeta por parte de las fuerzas coloniales del Imperio de Freeza. Él es el esposo de Gine y padre biológico de Kakarotto y Raditz.",
        image = "https://dragonball-api.com/characters/vegeta_normal.webp",
        affiliation = "Z Fighter",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
            Transformation(
                id = 7,
                name = "Bardock Ozaru",
                image = "",
                ki = "100.000",
            ),
            Transformation(
                id = 8,
                name = "Bardock SSJ",
                image = "",
                ki = "180.000.000",
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
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 9,
        name = "Nappa",
        ki = "4.000",
        maxKi = "7.000",
        race = "Saiyan",
        gender = "Male",
        description = "Nappa es un antagonista en el manga de Dragon Ball y su adaptación al anime, Dragon Ball Z, quien también hace apariciones breves en Dragon Ball GT y Dragon Ball Super.",
        image = "",
        affiliation = "",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [
           
        ]
    ),
    Character(
        id = 10,
        name = "Turles",
        ki = "9.000",
        maxKi = "250.000",
        race = "Saiyan",
        gender = "Male",
        description = "Tullece, también conocido como Tulece o Turles, es un saiyano desertor del Ejército de Freeza que más tarde se convertiría en pirata espacial. Un siniestro personaje con gran parecido físico a Son Goku que, junto con la ayuda de su pelotón, plantaba en los planetas una diabólica semilla que daba un fruto capaz de dotar de un tremendo poder a quien lo deguste, y los destruía al pasar cierto tiempo, luego de absorber toda la energía de estos.",
        image = "",
        affiliation = "Villain",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 11,
        name = "Gine",
        ki = "1.000",
        maxKi = "1.000",
        race = "Saiyan",
        gender = "Female",
        description = "Gine fue una mujer saiyana del Universo 7 de clase baja, esposa de Bardock y madre biológica de Kakarotto y Raditz. Trabajaba en el Centro de distribución de carne del Planeta Vegeta tras haberse retirado del Escuadrón de Bardock debido a su naturaleza dócil.",
        image = "",
        affiliation = "Z Figther",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 12,
        name = "Paragus",
        ki = "4.200",
        maxKi = "4.200",
        race = "Saiyan",
        gender = "Male",
        description = "Paragus era un saiyano nacido en el planeta Vegeta y es el padre de Broly. En un intento de vengarse de Vegeta, acabó muerto por su hijo Broly cuando iba a abandonarle debido a que el Nuevo Planeta Vegeta iba a ser destruido por un meteorito.",
        image = "",
        affiliation = "Other",
        originPlanet = Planet(
            id = 3,
            name = "Vegeta",
            isDestroyed = True,
            description = "El planeta Vegeta, conocido como planeta Plant antes del fin de la Guerra Saiyan-tsufruiana en el año 730, es un planeta rocoso ficticio de la serie de manga y anime Dragon Ball y localizado en la Vía Láctea de las Galaxias del Norte del Universo 7 hasta su destrucción a manos de Freezer en los años 737-739. Planeta natal de los Saiyans, destruido por Freezer. Anteriormente conocido como Planeta Plant.",
            image = "https://dragonball-api.com/planetas/Planeta_Vegeta_en_Dragon_Ball_Super_Broly.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 13,
        name = "Rey Vegeta",
        ki = "11.500",
        maxKi = "11.500",
        race = "Saiyan",
        gender = "Male",
        description = "Vegeta III, reconocido oficialmente como Rey Vegeta III o mejor conocido simplemente como el Rey Vegeta, es el padre del Príncipe Vegeta IV y Tarble, también fue el último y más reciente rey y líder de los saiyanos y el comandante del Ejército Saiyano que emigró del extinto Planeta Sadala al Planeta Vegeta, el cual fue rebautizado con su nombre tras llevar a su gente a la victoria en la Guerra saiyano-tsufruiana.",
        image = "",
        affiliation = "leader of the SSJ army",
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
        ki = "6.000",
        maxKi = "3.000.000",
        race = "Human/Saiyan",
        gender = "Female",
        description = "Pan es la hija de Videl y Gohan, siendo sus abuelos paternos Goku y Chi-Chi y sus abuelos maternos Mr. Satán y la fallecida cantante Miguel.",
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
        ki = "unknown",
        maxKi = "unknown",
        race = "Saiyan",
        gender = "Female",
        description = "Bra, conocida anteriormente como Bura en Hispanoamérica, es la segunda hija de Bulma y Vegeta, hermana de Trunks, por lo tanto es mestiza entre Saiyan y humana terrícola.",
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
        ki = "250.000",
        maxKi = "300.000.000",
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
        ki = "65",
        maxKi = "65",
        race = "Human",
        gender = "Male",
        description = "El Rey Gyuma más conocido como Ox-Satán es el rey del Monte Fry-pan. Fue esposo de la fallecida reina de esta montaña con quien tuvo a su hija, Chi-Chi. Años después, se convertiría en el suegro de Son Goku y el abuelo de Son Gohan y Son Goten.",
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
        ki = "169",
        maxKi = "169",
        race = "Animal",
        gender = "Male",
        description = "El maestro Karin es uno de los primeros maestros que llevó a Goku a un siguiente nivel de su poder, más allá de las artes marciales. Es el encargado de dotar de nubes voladoras a quien lo merezca. Para llegar a él, sin saber volar, el pequeño saiyajin tuvo que escalar una extensa torre, la que conocemos como Torre de Karin.",
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
        ki = "300",
        maxKi = "800.000.000",
        race = "Human",
        gender = "Male",
        description = "Oob, también conocido como Ub o Uub, es la reencarnación del Majin-Boo Puro y el terrícola más fuerte de toda la franquicia. Tras pelear en la 28° edición del Torneo Mundial de las Artes Marciales, él se convirtió en el discípulo de Son Goku.",
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
        ki = "970",
        maxKi = "2.100",
        race = "Human",
        gender = "Male",
        description = "Yajirobei es un personaje secundario en Dragon Ball y Dragon Ball Z, y también toma un aspecto de menor importancia en Dragon Ball Super[2] y Dragon Ball GT.",
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
        ki = "134",
        maxKi = "134",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "28.000.000",
        maxKi = "28.000.000",
        race = "Android",
        gender = "Male",
        description = "Loas Cell Jr son pequeños engendros de Cell, que aparecieron luego de que Cell en su forma perfectalos expulsara de su cuerpo. Cada uno de ellos tienen las mismas técnicas y son casi tan fuertes como su padre.",
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
        ki = "6.500.000.000",
        maxKi = "6.500.000.000",
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
        ki = "800.000.000.000",
        maxKi = "800.000.000.000.000",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "10",
        maxKi = "10",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "Unknown",
        maxKi = "Inknown",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
        ki = "Unknown",
        maxKi = "Unknown",
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
            description = "El Universo 1, el Universo Supremo, como su nombre lo indica, el primero de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 12.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 51,
        name = "Sour",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Sour es el ángel guía del Universo 2, sirviente y maestro de artes marciales personal de la Diosa de la Destrucción Jerez. Es un personaje del Arco de Supervivencia Universal del anime y manga de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Jerez",
        originPlanet = Planet(
            id = 2,
            name = "Universo 2",
            isDestroyed = False,
            description = "El Universo 2, el Universo Amable, como su nombre lo indica, el segundo de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 11.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 52,
        name = "Camparli",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Camparri es el ángel guía encargado del Universo 3, sirviente y maestro de artes marciales del Dios de la Destrucción Mosco. Es un personaje del Arco de Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Mosco",
        originPlanet = Planet(
            id = 2,
            name = "Universo 3",
            isDestroyed = False,
            description = "El Universo 3, el Universo Espiritual, como su nombre lo indica, el tercero de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 10.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 53,
        name = "Cognic",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Cognic es el ángel guía encargado del universo 4, sirviente y maestro del Diosd e la destrucción Quitela. Es un personaje del Arco de la supervivencia universal de Dragon ball Super.",
        image = "",
        affiliation = "Assistant of Quitela",
        originPlanet = Planet(
            id = 2,
            name = "Universo 4",
            isDestroyed = False,
            description = "El Universo 4, el Universo Conspirativo, como su nombre lo indica, el cuarto de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 9.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 54,
        name = "Cucatail",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Female",
        description = "Cucatail es el ángel guía encargado del Universo 5, tratándose de la sirvienta y maestra de artes marciales del Dios de la Destrucción Arak. Es un personaje del Arco de Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Arak",
        originPlanet = Planet(
            id = 2,
            name = "Universo 5",
            isDestroyed = False,
            description = "El Universo 5, el Universo Equilibrado, como su nombre lo indica, el quinto de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 8.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 55,
        name = "Vados",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Female",
        description = "Vados en un ángel guía, una de las hijas del Gran Sacerdote, hermana mayor de Whis y menos de Kus. Es la asistente, sirvienten y maestra del Dios de la destrucción Champa del universo 6 que hace su debut en el primer anime y manga de Dragon ball Super como un personaje secundario.",
        image = "",
        affiliation = "Assistant of Champa",
        originPlanet = Planet(
            id = 2,
            name = "Universo 6",
            isDestroyed = False,
            description = "El Universo 6, el Universo Desafiante, como su nombre lo indica, el sexto de los doce universos existentes actualmente en el omniverso de Dragon Ball, que incluye los planetas, las estrellas y una innumerable cantidad de galaxias. El sexto universo está vinculado con el séptimo, creándose lo que parece ser un universo espejo. Es donde residen el Dios de la Destrucción, Champa y su ángel guía, Vados.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 56,
        name = "Whis",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Whis es uno de los hijos del Gran Sacerdote, hermano menor de Vados, Korn y Kus. Es el ángel guía encargado de asistir y servir como maestro al Dios de la Destrucción del univberso 7. Tuvo su primera aparición en la película Dragon Ball Z: La batalla de los dioses y es un personaje recurrente en el anime y manga de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Beerus",
        originPlanet = Planet(
            id = 2,
            name = "Universo 7",
            isDestroyed = False,
            description = "El Universo 7, el séptimo de los doce universos existentes actualmente en el omniverso de Dragon Ball y el principal de todos ellos. El Kaio-shin de este universo es Shin, mientras que el Dios de la Destrucción es Beerus. Este universo es en donde casi toda la serie Dragon Ball se lleva a cabo.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 57,
        name = "Korn ",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Korn es uno de los doce hijos del Gran Sacerdote y hermano mayor de Whis. Es el ángel guía encargado del Universo 8, laborando como sirviente, asistente y maestro de artes marciales del Dios de la Destrucción Liquir. Es un personaje del Arco de Supervivencia Universal del anime y manga de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Liquir",
        originPlanet = Planet(
            id = 2,
            name = "Universo 8",
            isDestroyed = False,
            description = "El Universo 8, el octavo de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 5.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 58,
        name = "Mojito",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Mojito es el ángel guía del Universo 9, que fue el sirviente y maestro de artes marciales del Dios de la Destrucción Sidra hasta la destrucción de su Universo. Es un personaje del Arco de Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Sidra",
        originPlanet = Planet(
            id = 2,
            name = "Universo 9",
            isDestroyed = False,
            description = "El Universo 9, conocido como el Universo Improvisado, como su nombre lo indica, es el noveno de los doce universos existentes actualmente en el mundo de Dragon Ball.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 59,
        name = "Kus",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Female",
        description = "Kus des el ángel guía del Universo 10, sirviente y maestra de artes marciales del Dios de la Destrucción Rumoosh. Como hermana de todos los ángeles guía, es la hija de mayor edad del Gran Sacerdote.",
        image = "",
        affiliation = "Assistant of Rumoosh",
        originPlanet = Planet(
            id = 2,
            name = "Universo 10",
            isDestroyed = False,
            description = "El Universo 10, conocido como el Universo Macho, como su nombre lo indica, el décimo de los doce universos existentes actualmente en el mundo de Dragon Ball.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 60,
        name = "Marcarita",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Female",
        description = "Marcarita es el ángel guía del Universo 11, sirviente y maestra de artes marciales del Dios de la Destrucción Vermoud. Es un personaje de la Arco de la Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Vermond",
        originPlanet = Planet(
            id = 2,
            name = "Universo 11",
            isDestroyed = False,
            description = "El Universo 11, el Universo de la Justicia, como su nombre lo indica, el undécimo de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 2 y el lugar de origen de las Tropas del Orgullo.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 61,
        name = "Martinu",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Martinu es el ángel guía encargado del Universo 12, sirviente y maestro de artes marciales del Dios de la Destrucción Geen. Es un personaje del Arco de Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Assistant of Geen",
        originPlanet = Planet(
            id = 2,
            name = "Universo 12",
            isDestroyed = False,
            description = "El Universo 12, el Universo Definitivo, como su nombre lo indica, el duodécimo de los doce universos existentes actualmente en el mundo de Dragon Ball. Este es gemelo del Universo 1.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 62,
        name = "Merusu",
        ki = "",
        maxKi = "",
        race = "Angel",
        gender = "Male",
        description = "Awamo es el ángel guía encargado del Universo 1, sirviente y maestro de artes marciales del Dios de la Destrucción Iwen. Es un personaje del Arco de Supervivencia Universal de Dragon Ball Super.",
        image = "",
        affiliation = "Apprentic Angel",
        originPlanet = Planet(
            id = 2,
            name = "Universo 7",
            isDestroyed = False,
            description = "El Universo 7, Nuestro Universo, como su nombre lo indica, el séptimo de los doce universos existentes actualmente en el omniverso de Dragon Ball y el principal de todos ellos. El Kaio-shin de este universo es Shin, mientras que el Dios de la Destrucción es Beerus. Este universo es en donde casi toda la serie Dragon Ball se lleva a cabo.",
            image = "",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 63,
        name = "Gran Sacerdote",
        ki = "969 Googolplex",
        maxKi = "969 Googolplex",
        race = "Angel",
        gender = "Male",
        description = "El Sumo Sacerdote es un personaje introducido en Dragon Ball Super; es un ángel guía que recibe a las visitas en el palacete del Rey de Todo y guía a los invitados hasta él. Es el padre de los ángeles guía de todos los universos, siendo que Kus es su hija mayor.",
        image = "",
        affiliation = "Assistant of Zeno",
        originPlanet = Planet(
            id = 2,
            name = "Templo móvil del rey de todo",
            isDestroyed = False,
            description = "El templo móvil del Rey de Todo (sala del trono), es como su nombre lo indica, un templo móvil en el cual reside los tronos de los dos Reyes de Todo en el Lugar de Supervivencia en Dragon Ball Super.",
            image = "https://dragonball-api.com/planetas/Trono_del_Rey_de_Todo.webp",
        ),
        transformations = [

        ]
    ),
    Character(
        id = 64,
        name = "Zeno-Sama",
        ki = "500 Septillion",
        maxKi = "500 Septillion",
        race = "Unknown",
        gender = "Male",
        description = "Zeno es el ser supremo del multiverso y tiene un poder abrumador .El Rey de Todo, también conocido como Zen Oo (Zeno Sama en España y Zen Oo Sama en Hispanoamerica) y apodado por Son Goku como Pequeño Zen, es el gobernante y dios absoluto de todos los universos y el máximo soberano de todo lo existente en Dragon Ball.",
        image = "https://dragonball-api.com/characters/Zeno_Artwork.webp",
        affiliation = "Other",
        originPlanet = Planet(
            id = 2,
            name = "Templo móvil del rey de todo",
            isDestroyed = False,
            description = "El templo móvil del Rey de Todo (sala del trono), es como su nombre lo indica, un templo móvil en el cual reside los tronos de los dos Reyes de Todo en el Lugar de Supervivencia en Dragon Ball Super.",
            image = "https://dragonball-api.com/planetas/Trono_del_Rey_de_Todo.webp",
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
    
    # Ordenar la lista de personajes por id
    sorted_characters = sorted(SAMPLE_CHARACTERS, key=lambda x: x.id)
    
    total_items = len(sorted_characters)
    total_pages = ceil(total_items / limit)
    start_idx = (page - 1) * limit
    end_idx = start_idx + limit
    
    # Get paginated items
    paginated_items = sorted_characters[start_idx:end_idx]
    
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