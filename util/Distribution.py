import random
from math import log

class Distribution():
    def __init__(self, seq_num, seed_num):
        if seq_num < 1 or seq_num > 4 or seed_num < 1 or seed_num > 25:
            exit()
        self.seeds = [0,
                      149054804787264,
                      62292142997632,
                      152357846892736,
                      123555636150528,
                      150798460748096,
                      158603751047552,
                      14882342191552,
                      76571119387136,
                      116784547103296,
                      11184802710144,
                      213245677585088,
                      48085408711424,
                      17317928403776,
                      233623184262016,
                      51586110145472,
                      20704155010048,
                      249588858684480,
                      247911055377536,
                      246089704916160,
                      52074677765376,
                      230298097911104,
                      254769686103424,
                      110240567805376,
                      274885965055488,
                      84506772244032,
                      107749550016128,
                      88095635982016,
                      52443743422208,
                      82686420617024,
                      157655254353792,
                      65434817611712,
                      230470291556352,
                      77769041315904,
                      126645633173632,
                      214185921988800,
                      40879696480512,
                      68097045399872,
                      234133654194560,
                      147999729404352,
                      198002597366272,
                      197423256701504,
                      70886511954560,
                      48149897988800,
                      83836418427648,
                      191960958405440,
                      6400511363968,
                      100583010290624,
                      281320159316992,
                      204808823180352,
                      63001160862848,
                      214443596565696,
                      41059604729088,
                      253000959757632,
                      197318149131648,
                      22074134777280,
                      96077091507712,
                      17506912931392,
                      18810368380544,
                      4914957438656,
                      128536718249728,
                      124706640269120,
                      197140797902720,
                      86129368059840,
                      177119228858368,
                      146390512111680,
                      210376690389120,
                      193553594568896,
                      4072059121920,
                      36809358152000,
                      33839432192384,
                      259696789311936,
                      8159290135040,
                      258574374277696,
                      140104543326848,
                      221741029053120,
                      243186671588096,
                      12332285596480,
                      91626793915264,
                      21541314974656,
                      273576691635200,
                      51515113542720,
                      229590064452736,
                      168575526098112,
                      231743460447488,
                      149065385481536,
                      266532462253440,
                      51094559020480,
                      43667780081152,
                      223336041551424,
                      130771251582592,
                      187922141599424,
                      273322074609408,
                      56615457953600,
                      247877830367104,
                      258129995978688,
                      152345553147904,
                      139552377083968,
                      133302846642304,
                      226937745430720]
        multiplier = 0x5DEECE66D
        self.seed = self.seeds[(seq_num - 1) * 25 + (seed_num - 1)]
        self.seed = self.seed ^ multiplier
        random.seed(self.seed)

    def nextExponential(self, b):
        randx = random.random()
        return (-1 * b * log(randx))

    def nextInt(self, num):
        return random.randint(0, num - 1)
