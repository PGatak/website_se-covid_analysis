sw_string = 'a aby ach acz aczkolwiek aj albo ale alez ależ ani az aż bardziej bardzo beda bedzie bez' \
      ' beda będą bede będę będzie bo bowiem by byc być byl byla byli bylo byly był była było były' \
      ' bynajmniej cala cali caly cała cały ci cie ciebie cię co cokolwiek cos coś czasami czasem' \
      ' czemu czy czyli daleko dla dlaczego dlatego do dobrze dokad dokąd dosc dość duzo dużo dwa' \
      ' dwaj dwie dwoje dzis dzisiaj dziś gdy gdyby gdyz gdyż gdzie gdziekolwiek gdzies gdzieś go i' \
      ' ich ile im inna inne inny innych iz iż ja jak jakas jakaś jakby jaki jakichs jakichś jakie' \
      ' jakis jakiś jakiz jakiż jakkolwiek jako jakos jakoś ją je jeden jedna jednak jednakze' \
      ' jednakże jedno jego jej jemu jesli jest jestem jeszcze jeśli jezeli jeżeli juz już kazdy' \
      ' każdy kimś kto ktokolwiek ktora ktore ktorego ktorej ktory ktorych ktorym ktorzy ktos ktoś' \
      ' która które którego której który których którym którzy ku lat lecz lub ma mają mało mam mi' \
      ' miał mial miedzy między mimo mna mną mnie moga mogą moi moim moj moja moje moze mozliwe mozna może' \
      ' możliwe można mój mu musi my na nad nam  nami nas nasi nasz nasza nasze naszego naszych' \
      ' natomiast natychmiast nawet nia nią nic nich nie niech niego niej niemu nigdy nim nimi niz' \
      ' niż no o obok od około on ona one oni ono oraz oto owszem pan pana pani po pod podczas' \
      ' pomimo ponad poniewaz ponieważ powinien powinna powinni powinno poza prawie przeciez' \
      ' przecież przed przede przedtem przez przy roku rowniez również sam sama są sie się skad' \
      ' skąd soba sobą sobie sposob sposób swoje ta tak taka taki takie takze także tam te tego tej' \
      ' ten teraz też to toba tobą tobie totez toteż trzeba tu tutaj twoi twoim twoj twoja twoje' \
      ' twój twym ty tych tylko tym u w wam wami was wasz wasza wasze we według wiele wielu więc' \
      ' więcej wlasnie właśnie wszyscy wszystkich wszystkie wszystkim wszystko wtedy wy z za zaden' \
      ' zadna zadne zadnych zapewne zawsze ze zeby zeznowu zł znow znowu znów zostal został żaden' \
      ' żadna żadne żadnych że żeby polecany artykuł zobacz supports please video web html browser' \
      ' this enable javascript consider nn and upgrading thatn latek latka marca to view this mówi' \
      ' super express pw kiedy proc html videon stycznia lutego min kwietnia maja czerwca lipca' \
      ' sierpnia woj pw dodaje lublinie na lubelszczyźnie mężczyzna osób pw św parafii pw czytaj' \
      ' super lublina woj lubelskim kobieta dzieci woj lubelskie polsce należy ma terenie polski' \
      ' przy ul na terenie później'


def Convert(string):
    li = list(string.split(" "))
    return li

sw_list = Convert(sw_string)


stop_words = frozenset(sorted(sw_list))

