from KnowledgeBase import Rulebase
from Fuzzyfication import FuzzyInterface

import time
from random import randint
#simulazione di temperatura
room=FuzzyInterface()
rules=Rulebase()

#IN CELSIUS DEGREE
room.addlv('temperature','VERY HOT', [25,30,35])
room.addlv('temperature', 'HOT', [20,25,30])
room.addlv('temperature', 'MILD', [15,20,25])
room.addlv('temperature', 'COLD', [10,15,20])
room.addlv('temperature', 'VERY COLD', [5,10,15])

rules.addlv('conditioner-temperature', 'HIGH-TEMP', [20,25,30])
rules.addlv('conditioner-temperature', 'STABLE', [15,20,25])
rules.addlv('conditioner-temperature', 'LOW-TEMP', [5,10,15])

#IN RPM
rules.addlv('conditioner-speed', 'FAST', [250,450,650])
rules.addlv('conditioner-speed', 'MODERATE', [150,250,350])
rules.addlv('conditioner-speed', 'LOW', [50,150,250])

rules.setcondition(lambda dictb: dictb['VERY HOT'] if 'VERY HOT' in dictb else False,'LOW-TEMP','conditioner-temperature')
rules.setcondition(lambda dictb: dictb['HOT'] if 'HOT' in dictb else False,'LOW-TEMP','conditioner-temperature')
rules.setcondition(lambda dictb: dictb['MILD'] if 'MILD' in dictb else False,'STABLE','conditioner-temperature')
rules.setcondition(lambda dictb: dictb['COLD'] if 'COLD' in dictb else False,'HIGH-TEMP','conditioner-temperature')
rules.setcondition(lambda dictb: dictb['VERY COLD'] if 'VERY COLD' in dictb else False,'HIGH-TEMP','conditioner-temperature')

rules.setcondition(lambda dictb: dictb['VERY HOT'] if 'VERY HOT' in dictb else False,'FAST','conditioner-speed')
rules.setcondition(lambda dictb: dictb['HOT'] if 'HOT' in dictb else False,'MODERATE','conditioner-speed')
rules.setcondition(lambda dictb: dictb['MILD'] if 'MILD' in dictb else False,'LOW','conditioner-speed')
rules.setcondition(lambda dictb: dictb['COLD'] if 'COLD' in dictb else False,'MODERATE','conditioner-speed')
rules.setcondition(lambda dictb: dictb['VERY COLD'] if 'VERY COLD' in dictb else False,'FAST','conditioner-speed')

num=21
room.fuzzify(num, 'temperature', 'triangular', True)
print(room.inst_var)

#print(room.inst_var)

rules.translate(room.inst_var, 'conditioner-temperature', 'triangular', 'temperature')
rules.translate(room.inst_var,'conditioner-speed', 'triangular', 'temperature')

''' simulazione di cambio di temperatura
for x in range (150):

    room.fuzzify(num, 'temperature', 'triangular')
    print('\nroom %1.2fC %s ' % (num, room.inst_var))
    print('TEMPERATURE:')
    temp, label =rules.translate(room.inst_var, 'conditioner-temperature', 'triangular')
    print('FAN SPEED:')
    speed, label2=rules.translate(room.inst_var,'conditioner-speed', 'triangular')
    if label == 'HIGH-TEMP':

        num=num+ ((temp/10)*((650-speed)/650))
    elif label == 'STABLE':
        num= num + randint(15,30)/10
    else:
        num = num - ((temp / 10) * ((650 - speed) / 650))

    time.sleep(2)
'''
