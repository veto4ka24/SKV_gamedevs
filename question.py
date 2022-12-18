class Replica():
    def __init__(self,rep):
          self.replica=rep
    def __str__(self):
        return str(self.replica)

class Question(Replica):
    def __init__(self, rep, yes, no=False):
          self.replica=rep
          self.yes=yes
          self.no=no


    def next_yes(self):
            return self.yes
    def next_no(self):
            return self.no
    def __str__(self):
        return str(self.replica)

regions = []

import csv
with open("regions.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file)
    for row in file_reader:
        region = Replica(row[0])
        regions.append(region)


herocity = Question('Этот регион является городом-героем?', regions[-1], regions[79])
whitenights = ('Можно ли наблюдать белые ночи в этом регионе?', regions[78], regions[77])
million = Question('Население региона больше 1 млн человек?', whitenights, herocity)

yamal = Question('Полуостров, входящий в состав субъекта так и говорит о себе, что он маленького размера?', regions[83], regions[80])
fish = Question('Ловят ли в округе рыбу в промышленных масштабах?', regions[82], regions[81])
nentsy = Question('Кореное население - ненцы?', yamal, fish)

okrug = Question('Тогда, может, это автономный округ?', nentsy ,million)

enisey = Question('По территории этого края течёт Енисей?', regions[26], regions[27])
border1 = Question('Граничит ли этот регион с другими государствами?', regions[22], regions[29])
olympics = Question('Проводилась ли в этом регионе Олимпийские игры?', regions[25], border1)
ecology = Question('В регионе плохая экология?', enisey, olympics)

vulcanos = Question('Есть ли вулканы на территории субъекта?', regions[24], regions[23])
twothouthand = Question('... 2000?', regions[28], regions[30])
car = Question('В этом регионе много праворульных машин?', twothouthand, vulcanos)

threedays = Question('До этого региона из Москвы на поезде ехать меньше трёх суток?', ecology, car)

cry = Question('Этот субъект имеет статус края?', threedays, okrug) 

salavat = Question('Есть ли в республике памятник Салавату Юлаеву?', regions[1], regions[13])
polarlight = Question('Можно ли в этом регионе вживую любоваться северным сиянием?', regions[11], regions[19])
differenthours = Question('Часовой пояс региона отличен от Москвы?', salavat, polarlight)

buddism = Question('Преимущественно, в ресублике исповедуют буддизм?', regions[7], regions[10])
lakes = Question('Республика славится своими озёрами?', regions[9], buddism)

nearsea1 = Question('Есть ли выход к морю?', lakes, differenthours)

tubiteyka = Question('Национальным убором там является тюбитейка?', regions[16], regions[12])
kremlin1 = Question('В столице республики есть Кремль?', tubiteyka , regions[21])

volga1 = Question('Столица республики расположена на Волге?', kremlin1, nearsea1)

polus = Question('Там расположен полюс холода?', regions[14], regions[2])
altai = Question('Субъект назван по горному хребту?', regions[3], regions[17])
mongolia = Question('У республики есть сухопутная граница с Монголией?', altai, regions[19])

fourhour = Question('Там празднуют новый год на 4 часа раньше москвичей?', mongolia, polus)
siberia = Question('Тогда, наверное, это Сибирь?', fourhour, volga1) 

respect = Question('Уважают ли особо жителей республики все россияне?', regions[20], regions[15])
abhazia = Question('Республика граничит с Абхазией?', regions[8], regions[6])
elbrus = Question('Эльбрус является достопримечательностью этой республики?', abhazia, respect)

nearsea2 = Question('У республики есть выход к Каспийскому морю?', regions[4], regions[5])
nearborder2 = Question('У республики есть сухопутная граница с другими государствами?', nearsea2, regions[0])

capitalM = Question('Название столицы республики начинается на М?', nearborder2, elbrus)

kavkaz = Question('Это Кавказ?', capitalM, siberia)

respublica = Question('Регион имеет статус республики?', kavkaz, cry)

submarine = Question('В честь этого региона названа изветсная подводная лодка?', regions[48], regions[34])
anomaly = Question('Курская магнитная аномалия расположена, в том числе, на территории субъекта?', submarine, regions[35])
qazak = Question('В этих местах находятся представители донского казачества?', regions[62], regions[39])
million = Question('Административный центр - город-милионник?', qazak, anomaly)

tvardovsky = Question('Из этих краёв Твардовский?', regions[68], regions[31])
capital = Question('Город из этой области был столицей Руси давным-давно?', regions[55], tvardovsky)

lenin = Question('У берегов области пришвартован атомный ледокол "Ленин"?', regions[53], regions[49])

kremlin2 = Question('В административном центре есть Кремль?', capital, lenin)

ukraine = Question('Не с Украиной ли граничит?', million, kremlin2)

dver = Question('В Москву дверь?', regions[70], regions[76])
sunset = Question('Там есть город-герой?', regions[38], regions[54])
name = Question('В советский период административный центр носил иное название?', sunset, regions[46])
history = Question('Центр области старше Москвы?', dver, name)

lace = Question('Есть одноимённый вид русского кружева?', regions[37], regions[50])
nevesty = Question('Именно там находится столица невест?', regions[40], regions[43])
metall = Question('В регионе расположено крупный металлургический завод?', lace, nevesty)

solovky = Question('Соловецкие острова входят в состав именно этого субъекта?', regions[32], regions[60])
kvas =  Question('Эх, а известный вятский квас производят тут?', regions[45], solovky)

road = Question('Тем не менее, обычно туда добираются на поезде не дольше 10 часов?', metall, kvas)

macbet = Question('Леди Макбет связана с этой областью, если вы понимаете, о чём я?', regions[59], regions[52])
samovar = Question('За вкусными настоящими пряниками сюда?', regions[72], macbet)

nerli = Question('Область славится памятниками белокаменного зодчества?', regions[36], regions[63])
boy = Question('Мальчик хочет именно сюда?', regions[69], nerli)

train = Question('По пути в Белгород из Москвы на ласточке Вы будете проезжать этот регион?', samovar, boy)

aero = Question('В адмистративном центре есть аэропорт?', road, train)

volga2 = Question('Административный центр загаданной области стоит на Волге-матушке?', history, aero)

nearborder3 = Question('Загаданная область граничит с другими странами?', ukraine, volga2)

jvcr = Question('JVCR?', regions[57], regions[41])
population = Question('Здесь находится третий по численности населения город России?', regions[56], regions[44])
gerb = Question('На гербе изображён зверёк?', jvcr, population)

dalniy = Question('Это на Дальнем Востоке?', regions[31], regions[73])
tagil = Question('Тагиил?', regions[67], dalniy)

railway = Question('Железнодородный вокзал в региональном центре бирюзово-зелёный?', gerb, tagil)

earthquake = Question('Там относительно часто происходят землетрясения?', regions[66], regions[51])
briges = Question('Именно в этом регионе родилась задача о семи мостах?', regions[42], earthquake)


toliati = Question('В этом регионе находится крупнейший город, не являющийся административным центром?', regions[64], regions[74])
az = Question('В загаданной области есть крупный автомобильный завод?', toliati, regions[71])
sea = Question('У области есть выход к морю?', briges, az)

watermelon = Question('Купите арбузы из этого региона?', regions[33], regions[58])
verblud = Question('На гербе изображён верблюд?', regions[75], regions[65])
polution = Question('Регион очень загрязнён?', verblud, watermelon)
sad = Question('Область считается бедной и бесперспективной?', regions[47], polution)

kazah = Question('Регион соседствует с Казахстаном?', sad, sea)

transsib = Question('Современная Транссибирская магистраль проходит по территории этой области?', railway, kazah)

MSK = Question('Этот регион в московском часовом поясе?', nearborder3, transsib)

oblast = Question('Вы загадали область?', MSK, respublica)






















