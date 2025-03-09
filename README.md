# Fuzzy Rule-Based System

Questo repository implementa un sistema fuzzy basato su regole per l'analisi e l'inferenza di variabili linguistiche. Il sistema è sviluppato in Python e consente di:

- **Definire variabili linguistiche**: Utilizzando funzioni di appartenenza (triangolari e trapezoidali).
- **Fuzzificare input numerici**: Calcolando il grado di appartenenza di ogni variabile.
- **Applicare regole fuzzy**: Collegando i gradi di appartenenza degli input ad output linguistici.
- **Defuzzificare i risultati**: Convertendo i valori fuzzy in valori crisp utilizzabili.

## Struttura del Codice

- **Rulebase**:  
  Gestisce le regole fuzzy e le variabili linguistiche. Comprende:
  - `translate`: Applica le regole al dizionario di input e defuzzifica il risultato.
  - `setcondition`: Aggiunge nuove regole fuzzy alla base.
  - `addlv`: Definisce le variabili linguistiche con le rispettive funzioni di appartenenza.
  - `defuzzify`: Converte il valore fuzzy in un valore crisp, utilizzando una funzione triangolare o trapezoidale.

- **FuzzyInterface**:  
  Fornisce un'interfaccia per:
  - Aggiungere variabili linguistiche.
  - Fuzzificare i valori in ingresso.
  - **Switch Condition**: Durante la fuzzificazione, il parametro `switch` (impostato di default a `True`) determina se eseguire una "pulizia" dei risultati:
    - Se `switch` è **True**, dopo aver calcolato i gradi di appartenenza viene chiamato il metodo `clean`, che conserva soltanto il valore massimo per ogni variabile, azzerando gli altri. Questa operazione assicura che venga considerata solo la regola con il grado di attivazione più elevato.
    - Se `switch` è **False**, la procedura di cleaning viene saltata e vengono mantenuti tutti i valori fuzzy calcolati.

## Funzionamento

1. **Definizione delle Variabili Linguistiche**:  
   Le variabili come `speed` o `fuel` sono definite con etichette (es. 'VERY FAST', 'LOW CONSUME') e parametri per le funzioni di appartenenza (es. `[70, 110, 130]` per funzioni triangolari).

2. **Fuzzificazione**:  
   Con `FuzzyInterface.fuzzify`, un valore numerico viene convertito nei relativi gradi di appartenenza per ciascuna etichetta della variabile definita. Il parametro `switch` controlla se, dopo la fuzzificazione, deve essere eseguita la pulizia dei risultati, mantenendo soltanto il valore massimo per ogni qualità.

3. **Applicazione delle Regole**:  
   La classe `Rulebase` applica le regole definite tramite `setcondition` per valutare i gradi di appartenenza e associare output linguistici (es. 'HIGH COST', 'MEDIUM COST'). si e' scelto
   di utilizzare funzioni lambda il cui output puo' essere un valore di appartenza come anche il minimo nel caso di operatore AND o il massimo in caso di operatore O

4. **Defuzzificazione**:  
   Attraverso `defuzzify`, il valore fuzzy viene convertito in un valore crisp, calcolato mediamente (ad esempio, come media dei valori ottenuti dai lati sinistro e destro della funzione di appartenenza).

## Esempio d'Uso

Nel `main()` viene mostrato un esempio pratico:
- Vengono definite variabili linguistiche per **velocità** e **consumo di carburante**.
- Vengono impostate regole che collegano la velocità e il consumo a differenti livelli di **costo**.
- Infine, il sistema fuzzifica i valori di input, applica le regole e defuzzifica il risultato per ottenere una stima del costo.

---

Questo approccio modulare permette di estendere facilmente il sistema per includere ulteriori variabili e regole, rendendo il tool versatile per applicazioni basate su logica fuzzy.
