class Russianregions:
    q = 'Это область?'
    a = None
    b = None

class oblast(Russianregions):
    q = 'Этот регион в московском часовом поясе?'

class MSK(oblast):
    q = 'Граничит ли регион с другими государствами?'

class nearborder(MSK):
    q = 'Граничит с Украиной?'

class nearUkraine(nearborder):
    q = 'Захватывает ли территория региона Курскую магнитную аномалию?'

class anomalia(nearUkraine):
    q = 'В честь столицы этого региона названа известная подводная лодка?'

class underwater(anomalia):
    a = 'Курская область'
    b = 'Белгородская область'

class nonanomalia(nearUkraine):
    q = 'Столица региона -- город-миллионник?'

class milionnik(nonanomalia):
    b = 'Брянская область'
    q = 'В этом регионе находятся представители донского казачества?'

class qazak(milionnik):
    a = 'Ростовская область'
    b = 'Воронежская область'

class notUkraine(nearborder):
    q = 'Есть ли в столице области кремль?'

class kremlin(notUkraine):
    q = 'Это второй по значимости после Киева центр Киевской Руси?'

class KievRus(kremlin):
    a = 'Великий Новгород'
    q = 'Столица региона стоит на Днепре?'


class neoblast(Russianregions):
    q = 'Это республика?'

class respublica(neoblast):
    q = 'Она располагается на Кавказе?'

class Kavkaz(respublica):
    q = 'Название столицы ресублики начинается на М?'

class capitalM(Kavkaz):
    q = 'Есть ли сухопутная граница с другим государством?'

class nearborder(capitalM):
    q = 'Есть ли выход к морю?'
    b = 'Адыгея'

class nearsea(nearborder):
    a = 'Дагестан'
    b = 'Ингушетия'

class notcapitalM(Kavkaz):
    q = 'Эльбрус является достопримечательностью этой республики?'

class Elbrus(notcapitalM):
    q = 'Граничит ли с Абхазией?'

class Abhazia(Elbrus):
    a = 'Карачаево-Черкесская Ресублика'
    b = 'Кабардино-Балкарская Республика'

class notElbrus(notcapitalM):
    q = 'Уважают ли граждан республики все россияне?'

class respect(notElbrus):
    a = 'Чеченская Республика'
    b = 'Республика Северная Осетия - Алания'

class notKavkaz(respublica):
    q = 'Это Сибирь?'

class Siberia(notKavkaz):
    q = 'Жители празднуют новый год на 4 часа раньше, чем в Долгопрудном?'

class fourhour(Siberia):
    q = 'Есть ли у республики сухопутная граница с Монголией?'

class Mongolia(fourhour):
    q = 'Названа по горному хребту?'
    b = 'Республика Хакасия'

class altai(Mongolia):
    a = 'Республика Алтай'
    b = 'Республика Тыва'

class notfourhour(Siberia):
    q = 'Там расположен полюс холода?'

class polus(notfourhour):
    a = 'Республика Саха - Якутия'
    b = 'Республика Бурятия'

class notSiberia(notKavkaz):
    q = 'Столица республики расположена на Волге?'

class Volga(notSiberia):
    q = 'Есть ли в столице Кремль?'

class kremlin(Volga):
    q = 'Является ли тюбитейка национальным головным убором республики?'

class tubiteyka(kremlin):
    a = 'Республика Татарстан'
    b = 'Республика Марий-Эл'

class notVolga(notSiberia):
    q = 'Есть ли выход к морю?'

class nearsea(notVolga):
    q = 'Эта республика известна своими озерами?'

class lakes(nearsea):
    a = 'Республика Карелия'

class notlakes(nearsea):
    q = 'В этой республике преобладающее число людей исповедует буддизм?'

class buddism(notlakes):
    a = 'Республика Калмыкия'
    b = 'Республика Крым'

class notnearsea(notVolga):
    q = 'Часовой пояс отличен от Москвы?'

class notdifferenthours(notnearsea):
    q = 'Можно ли в этом регионе наблюдать северное сияние?'

class polarlight(notdifferenthours):
    a = 'Республика Коми'
    b = 'Республика Удмуртия'

class differenthours(notnearsea):
    q = 'Есть ли в республике памятник Салавату Юлаеву?'

class SaLaVaT(differenthours):
    a = 'Республика Башкортостан'
    b = 'Республика Мордовия'

class notrespublica(neoblast):
   q = 'Это край?'

class cry(notrespublica):
    q = 'До этого региона из Москвы на поезде ехать меньше трех суток?'

class lessthan3(cry):
    q = 'Хорошая ли экология в этом крае?'

class goodecology(lessthan3):
    q = 'Проводилась ли в этом регионе олимпиада?'

class Olymp(goodecology):
    a = 'Краснодарский край'
    q = 'Граничит ли регион с другими государствами?'

class nearborder(Olymp):
    a = 'Алтайский край'
    b = 'Ставропольский край'

class badecology(lessthan3):
    q = 'Протекает ли по этому региону Енисей?'

class enisey(badecology):
    a = 'Красноярский край'
    b = 'Пермский край'

class morethan3(cry):
    q = "В этом регионе много праворульных машин?"

class rigthcar(morethan3):
    q = '... 2000?'

class twothouthand(rigthcar):
    a = 'Приморский край'
    b = 'Хабаровский край'

class leftcar(morethan3):
    q = 'Есть ли вулканы на территории субъекта?'

class vulcanos(leftcar):
    a = 'Камчатский край'
    b = 'Забайкальский край'

class necry(neoblast):
    q = 'Это автономный округ?'

class avtonomn(necry):
    q = 'Кореное население - ненцы?'

class nentsy(avtonomn):
    q = 'Полуостров, входяций в состав субъекта говорит о себе, что он маленького размера?'

class yamal(nentsy):
    a = 'Ямало-Ненецкий автономный округ'
    b = 'Ненецкий автономный округ'

class notnentsy(avtonomn):
    q = 'Ловят ли в округе рыбу в промышленных масштабах?'

class fish(notnentsy):
    a = 'Чукотский автономный округ'
    b = 'Ханты-Манскийский автономный округ'

class notorug(necry):
    q = 'Население региона больше 1 млн человек?'

class morethanmln(notorug):
    q = 'Можно ли наблюдоть белые ночи в этом регионе?'

class whitenights(morethanmln):
    a = 'Санкт-Петербург'
    b = 'Москва'

class lessthanmln(notorug):
    q = 'Этот регион является городом-героем?'

class herocity(lessthanmln):
    a = 'Севастополь'
    b = 'Еврейская автономная область'