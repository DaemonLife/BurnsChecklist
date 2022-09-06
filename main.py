import os
from time import sleep
li = [

    'У вас плохое настроение?',
    'Вы чувствуете себя несчастным?',
    'Вы чувствуете желание расплакаться или кричать?',
    'Вы ощущаете разочарованность своей жизнью?',
    'Вы испытываете чувство безнадежности?',
    'Вы ощущаете низкую самооценку?',
    'Вы чувствуете себя бесполезным',
    'Вы испытываете чувство вины или стыда?',
    'Вы обвиняете в бедах самого себя или, наоборот, обвиняете других?',
    'Вы испытываете трудности с принятием решений?',
    'Вы чувствуете потерю интереса к членам семьи, друзьям, коллегам?',
    'Вы испытываете одиночество?',
    'Вы проводите меньше времени с семьей или с друзьями?',
    'Вы чувствуете потерю мотивации?',
    'Вы чувствуете потерю интереса к работе или другим занятиям?',
    'Вы избегаете работы и другой деятельности?',
    'Вы ощущаете потерю удовольствия и нехватку удовлетворения от жизни?',
    'Вы чувствуете усталость?',
    'Вы испытываете затруднения со сном или, наоборот, спите слишком много?',
    'Вы имеете сниженный или, наоборот, повышенный аппетит?',
    'Вы замечаете потерю интереса к сексу?',
    'Вы беспокоитесь по поводу своего здоровья?',
    'Имеются ли у вас суицидальные мысли?',
    'Хотели бы вы окончить свою жизнь?',
    'Планируете ли вы навредить себе?',

]

i = 0
sum = 0
temp = 0
while i < len(li):
    line = li[i]
    os.system('clear')
    print ('Опросник депрессии Бернса.\n')
    print('Варианты ответов:')
    print("0 - совсем нет\n1 - немного\n2 - умеренно\n3 - сильно\n4 - крайне")
    print('\n\"p\" - вернуться назад')
    print('\"q\" - выйти\n')

    print(' - - - - - - - - - - - - - -\n')

    if i < 11:
        print('Блок "Мысли и чувства".')
    elif i < 18:
        print('Блок "Деятельность и личные отношения".')
    elif i < 23:
        print('Блок "Физические симптомы".')
    else:
        print('Блок "Суицидальные побуждения".')


    try:
        print(f"\n{i+1}/{len(li)}: {line}")
        temp = input("Ваш ответ: ")
        if temp == 'q':
            break
        if (temp == 'p') and (i > 0):
            i-=1
            continue
        temp = int(temp)
    except:
        print('Введите число!')
        sleep(1)
        continue
    
    if (temp < 0) or (temp > 4):
        print('Введите число в нужном диапазоне!')
        sleep(1)
        continue
    sum += temp

    i+=1

print(f'\nСумма: {sum}.')
print()
