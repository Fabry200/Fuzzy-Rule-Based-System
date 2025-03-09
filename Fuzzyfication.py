
from KnowledgeBase import Rulebase

class FuzzyInterface:
    def __init__(self):
        self.lv={}
        self.inst_var={}
    def addlv(self, quality,label,membership_params):

        if quality not in self.lv.keys():
            self.lv[quality]={}
            self.lv[quality][label]=membership_params
        else:
            self.lv[quality][label]=membership_params



    def fuzzify(self,x,quality, type_fun, switch=True):
        massimo=0
        variabile_linguistica=None
        for attribute, lv in self.lv.items():
            if attribute == quality:
                for label, cordinate in lv.items():
                    match type_fun:
                        case 'triangular':
                            if quality not in self.inst_var.keys():
                                self.inst_var[quality]={}

                            a,b,c= cordinate
                            if x <= a:
                               calc=0
                               self.inst_var[quality][label] = calc
                            elif x<=b and x >= a:
                                calc=round((x-a)/(b-a),2)
                                self.inst_var[quality][label]=calc
                            elif x >= b and x <=c:
                                calc=round((c-x)/(c-b),2)
                                self.inst_var[quality][label]=calc
                            if x >= c:
                                calc=0
                                self.inst_var[quality][label] = calc

                        case 'trapezoidal':

                            a,b,c,d= cordinate

                            if x <= a:
                                calc=0
                                self.inst_var[quality][label] = calc
                            elif a <= x and x <= b:
                                calc=round((x-a)/(b-a),2)
                                self.inst_var[quality][label]=calc
                            elif b <= x and x<=c:
                                self.inst_var[quality][label] =1
                            elif c <= x and x<= d:
                                calc=round((d-x)/(d-c),2)
                                self.inst_var[quality][label]=calc
                            elif d <= x:
                                calc=0
                                self.inst_var[quality][label] = calc
        if switch == False:
            pass
        else:
            self.clean(quality)

    def clean(self, qual):
        counter=0
        for quality, inputs in self.inst_var.items():
            if qual == quality:
                for label, value in sorted(inputs.items(), key=lambda x: x[1], reverse=True):
                    if counter >= 1:
                        self.inst_var[quality][label]=0
                    counter+=1




def main():
    car=FuzzyInterface()
    car.addlv( 'speed', 'VERY FAST',[70,110,130])
    car.addlv('speed', 'FAST', [50,70,90])
    car.addlv('speed', 'LOW', [30,50,60])


    #visualizzation
    '''
    x=np.arange(0,140, 1)
    mfx=sk.trimf(x,[70,110,130])
    mfy=sk.trimf(x, [50,70,90])
    mfz=sk.trimf(x, [30,50,60])
    plt.plot(x, mfx)
    plt.plot(x,mfy)
    plt.plot(x, mfz)
    plt.show()
    '''

    car.addlv('fuel', 'HIGH CONSUME',[0.71, 1.15, 1.25, 1.58])
    car.addlv('fuel', 'MEDIUM CONSUME', [0.38, 0.49, 0.68, 0.79])
    car.addlv('fuel', 'LOW CONSUME', [0.10, 0.22, 0.34, 0.46])
    car.addlv('fuel', 'NO CONSUME', [0.0, 0.02, 0.08, 0.12])


    a=Rulebase()
    a.addlv('cost', 'VERY LOW COST', [50,100,125])
    a.addlv('cost', 'MEDIUM COST', [75, 150, 225])
    a.addlv('cost', 'HIGH COST', [175,250,350])
    '''
    a.setcondition(lambda dictb: min(dictb['LOW'], dictb['LOW CONSUME']) if 'LOW' in dictb and 'LOW CONSUME' in dictb else False, 'VERY LOW COST')
    a.setcondition(lambda dictb: min(dictb['VERY FAST'], dictb['HIGH CONSUME']) if 'VERY FAST' in dictb and 'HIGH CONSUME' in dictb else False, 'HIGH COST')
    a.setcondition(lambda dictb: min(dictb['FAST'], dictb['MEDIUM CONSUME']) if 'FAST' in dictb and 'MEDIUM CONSUME' in dictb else False, 'HIGH COST')
    a.setcondition(lambda dictb: min(dictb['LOW'], dictb['HIGH CONSUME']) if 'LOW' in dictb and 'HIGH CONSUME' in dictb else False, 'MEDIUM COST')
    a.setcondition(lambda dictb: min(dictb['FAST'], dictb['LOW CONSUME']) if 'FAST' in dictb and 'LOW CONSUME' in dictb else False, 'MEDIUM COST')
    a.setcondition(lambda dictb: min(dictb['VERY FAST'], dictb['NO CONSUME']) if 'VERY FAST' in dictb and 'NO CONSUME' in dictb else False, 'VERY LOW COST')
    a.setcondition(lambda dictb: min(dictb['FAST'], dictb['NO CONSUME']) if 'FAST' in dictb and 'NO CONSUME' in dictb else False, 'VERY LOW COST')
    a.setcondition(lambda dictb: min(dictb['LOW'], dictb['NO CONSUME']) if 'LOW' in dictb and 'NO CONSUME' in dictb else False, 'VERY LOW COST')

    #a.setcondition(lambda x: x > 0.4 and x < 0.7, 'MEDIUM', [0.4,0.7])
    #a.setcondition(lambda x: x > 0.0 and x < 0.4, 'LOW', [0.0, 0.4])


    car.fuzzify(129,'speed','triangular')
    car.fuzzify(1.44, 'fuel', 'trapezoidal')
    a.translate(car.inst_var, 'cost', 'triangular')
    '''
if __name__ == '__main__':
    main()
#a.get_lv()
