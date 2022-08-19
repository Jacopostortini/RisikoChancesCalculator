import random
import numpy
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("ggplot")

def roll(atk, defense):
    lancio_atk = [random.randrange(1, 6) for _ in range(atk-1 if atk<4 else 3)]
    lancio_def= [random.randrange(1, 6) for _ in range(defense if defense<3 else 3)]
    lancio_atk = list(reversed(sorted(lancio_atk)))
    lancio_def = list(reversed(sorted(lancio_def)))
    for i in range(min(len(lancio_atk), len(lancio_def))):
        if lancio_atk[i]>lancio_def[i]:
            defense -= 1
        else: 
            atk -= 1
    if atk > 1 and defense > 0:
        return roll(atk, defense)
    if atk==1:
        return False, atk, defense
    elif defense == 0:
        return True, atk, defense
    
def predict(atk, defense, repetitions):
    fav = 0
    mean_a = 0
    mean_d = 0
    for i in range(repetitions):
        att = roll(atk, defense)
        if att[0]:
            fav += 1
            mean_a += att[1]
        else:
            mean_d += att[2]
    probability = fav/repetitions
    try:
        return probability, int(mean_a/fav), int(mean_d/(repetitions-fav))
    except ZeroDivisionError:
        try:
            return probability, int(mean_a/fav), 0
        except ZeroDivisionError:
            return probability, 1, int(mean_d/(repetitions-fav))

def generate_dataset(max_attack=50, max_defense=50, repetitions=100, filename=False):    
    results = []

    for a in range(2, max_attack+1):
        for d in range(1, max_defense+1):
            results.append([a, d, predict(a, d, repetitions)[0]])
                    
    if filename:
        results = numpy.array(results, dtype=numpy.float64)
        numpy.savetxt(filename, results, delimiter=",")
        
    return results

def generate_probabilities_given_fixed_attack(attack, max_defense=50, repetitions=100):
    result = []
    for d in range(1, max_defense+1):
        result.append(predict(attack, d, repetitions)[0])
    return result

def generate_probabilities_given_fixed_defense(defense, max_attack=50, repetitions=100):
    result = []
    for a in range(2, max_attack+1):
        result.append(predict(a, defense, repetitions)[0])
    return result
            
max_attack = 50
max_defense = 50
repetitions = 50
filename = "risk_dataset.csv"
attack = 10
defense = 10


"""Creazione e salvataggio del dataset"""
#dataset = generate_dataset(max_attack, max_defense, repetitions, filename)


"""Etichetta y per grafici con valori fissati"""
#plt.ylabel("Probabilità di vittoria")


"""Grafico Probabilità-Difesa con attacco fissato ripetuto per diversi valori di attacco"""
#plt.title("Attacco fissato a " + str(attack))
#plt.xlabel("Difesa")
#for i in range(2, 10):
#    fixed_attack = generate_probabilities_given_fixed_attack(i, max_defense, repetitions)
#    plt.plot(range(2, len(fixed_attack)+2), fixed_attack)
#    plt.scatter(range(2, len(fixed_attack)+2), fixed_attack, s=10)


"""Grafico Probabilità-Attacco con difesa fissata ripetuto per diversi valori di difesa"""
#plt.title("Difesa fissata a " + str(defense))
#plt.xlabel("Attacco")
#for i in range(1, 10):
#    fixed_defense = generate_probabilities_given_fixed_defense(i, max_attack, repetitions)
#    plt.plot(range(1, len(fixed_defense)+1), fixed_defense)
#    plt.scatter(range(1, len(fixed_defense)+1), fixed_defense, s=10)


"""Crea grafico Attacco-Difesa con punti di grandezza proporzionale alla probabilità di vittoria"""
#df = [i for i in range(1, max_defense+1)]
#atk = [i for i in range(2, max_attack+1)]
#plt.xlabel("Difesa")
#plt.ylabel("Attacco")
#plt.axis((0, max_defense*11/10, 0, max_attack*11/10))
#
#for d in df:
#    for a in atk:
#        p = predict(a, d, repetitions)
#        plt.scatter([d], [a], s=10*p[0])
#plt.plot([0, max_attack/2], [0, max_attack])
#plt.plot([0, max_attack*3], [0, max_attack])
#plt.plot([0, max_attack/10], [0, max_attack])
#plt.show()


"""Predizione di un risultato"""
print("LANCIANDO QUESTO PROGRAMMA PUOI FARE SOLO UNA PREDIZIONE DELLA PROBABILITÀ DI VITTORIA CON NUMERO DI ATTACCANTI E DIFENSORI DATI, PER GENERARE DEI DATASET MODIFICA IL FILE")
print("Inserisci il numero di attaccanti")
attaccanti = int(input())
print("Inserisci il numero di difensori")
difensori = int(input())
print("Inserisci il numero di ripetizioni da eseguire")
ripetizioni = int(input())
prob, attrimasti, difrimasti = predict(attaccanti, difensori, ripetizioni)
print("La probabilità di vittoria è circa del "+str(prob*100)+"%")
print("In caso di vittoria rimarranno mediamente "+str(attrimasti)+" attaccanti")
print("In caso di sconfitta rimarranno mediamente "+str(difrimasti)+" difensori")



                
    

    
    
    
