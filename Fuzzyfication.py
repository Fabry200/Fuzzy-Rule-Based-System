
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





