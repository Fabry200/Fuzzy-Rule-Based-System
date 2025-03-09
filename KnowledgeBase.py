class Rulebase:
    def __init__(self):
        # Lista per memorizzare le regole fuzzy
        self.rules = []
        # Dizionario per memorizzare le variabili linguistiche
        self.linguistic_variables = {}


    def translate(self, input_dictionary, quality, membership_type, reference):
        """
        Applica le regole fuzzy al dizionario di input e defuzzifica il risultato.
        :param input_dictionary: Dizionario contenente i gradi di appartenenza delle variabili di input.
        :param quality: La qualità (variabile linguistica) da valutare.
        :param membership_type: Tipo di funzione di appartenenza (es. 'triangular').
        """

        for qual,rule_label, rule_condition in self.rules:
            if quality == qual:
                if reference in input_dictionary:
                    if rule_condition(input_dictionary[reference]):  # Se la condizione della regola è soddisfatta
                        print(rule_condition(input_dictionary[reference]), rule_label, end='->')  # Stampa il grado di attivazione e l'etichetta
                        self.defuzzify(rule_condition(input_dictionary[reference]), quality, membership_type, rule_label)
                        #return (self.defuzzify(rule_condition(input_dictionary), quality, membership_type, rule_label), rule_label)  # Defuzzifica

    def setcondition(self, condition_function, output_label, quality):
        """
        Aggiunge una regola fuzzy alla rule base.
        :param quality:
        :param condition_function: Funzione lambda che definisce la condizione della regola.
        :param output_label: Etichetta linguistica associata alla regola.
        """
        self.rules.append([quality,output_label, condition_function])

    def addlv(self, quality, label, membership_params):
        """
        Aggiunge una variabile linguistica alla rule base.
        :param quality: La qualità (variabile linguistica) da definire.
        :param label: Etichetta linguistica (es. 'LOW COST').
        :param membership_params: Parametri della funzione di appartenenza (es. [50, 100, 125]).
        """
        if quality not in self.linguistic_variables.keys():
            self.linguistic_variables[quality] = {}  # Crea una nuova entry per la qualità
        self.linguistic_variables[quality][label] = membership_params  # Aggiunge l'etichetta con i parametri

    def defuzzify(self, fuzzy_value, quality, membership_type, output_label):
        """
        Defuzzifica un valore fuzzy per ottenere un valore crisp.
        :param fuzzy_value: Grado di appartenenza fuzzy (es. 0.75).
        :param quality: La qualità (variabile linguistica) da defuzzificare.
        :param membership_type: Tipo di funzione di appartenenza (es. 'triangular').
        :param output_label: Etichetta linguistica associata al valore fuzzy.
        """
        for attribute, linguistic_variable in self.linguistic_variables.items():
            if attribute == quality:  # Trova la variabile linguistica corretta
                for label, membership_coordinates in linguistic_variable.items():
                    if label == output_label:  # Trova l'etichetta corretta
                        match membership_type:
                            case 'triangular':
                                a, b, c = membership_coordinates  # Estrai i parametri della funzione triangolare
                                # Calcola il valore crisp per il lato sinistro
                                left_value = ((b - a) * fuzzy_value) + a
                                # Calcola il valore crisp per il lato destro
                                right_value = c - ((c - b) * fuzzy_value)

                                # Stampa la media dei due valori (defuzzificazione simmetrica)
                                #print((left_value + right_value) / 2, end='\n')
                                print(right_value, end='\n')
                                #return right_value
                                #print(left_value, end='\n')

                            case 'trapezoidal':
                                a, b, c, d = membership_coordinates
                                if fuzzy_value == 1:
                                    print((b+c)/2)
                                else:
                                    left_value = ((b - a) * fuzzy_value) + a
                                    right_value = c - ((c - b) * fuzzy_value)

