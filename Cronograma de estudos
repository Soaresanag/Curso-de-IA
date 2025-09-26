def preencherCronograma (horasPorDia):
    vetor = []
    for i in range (horasPorDia):
        if horasPorArea[0] > 0:
            vetor.append("Exatas")
            horasPorArea[0] = horasPorArea[0]-1

        elif horasPorArea[1] > 0:
            vetor.append("Linguagem")
            horasPorArea[1] = horasPorArea[1]-1

        elif horasPorArea[2] > 0:
            vetor.append("Natureza")
            horasPorArea[2] = horasPorArea[2]-1

        elif horasPorArea[3] > 0:
            vetor.append("Humanas")
            horasPorArea[3] = horasPorArea[3]-1
    
        elif horasPorArea[4] > 0:
            vetor.append("Redação")
            horasPorArea[4] = horasPorArea[4]-1
    return vetor

#Curso|Exatas|Linguaguens|Natureza|Humanas|Redação
cursos = [["IA","10","6","5","4","6"],
          ["ENG DE PESCA","10","3","9","4","5"],
          ["MEDICINA","6","7","10","5","8"],
          ["LETRAS PORT","5","10","5","7","10"],
          ["DIREITO","4","8","5","10","10"],
          ["ARQUITETURA","7","6","4","9","7"]]

horasPorDia = []
diasDaSemana = ["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado","Domingo"]

for i in range (7):
    print("Quantas horas você tem disponivel para estudar",diasDaSemana[i],":")
    valor = int(input())
    horasPorDia.append(valor)

curso = input("\nDigite o curso desejado: ")
posicao = -1
for i in range(6):
    if cursos[i][0] == curso:
        posicao = i

areasDeEstudos = ["Exatas","Linguagens","Natureza","Humanas","Redação"]
dificuldades = []
for i in range (5):
    print("\nSelecione uma dificuldade de 0 a 10 na prova de", areasDeEstudos[i])
    valor = int(input())
    dificuldades.append(valor)

calcularPrioridade = []
for i in range(5):
    calculo = (int(cursos[posicao][i+1])+dificuldades[i])/2
    calcularPrioridade.append(calculo)

horasPorArea = []
for i in range(5):
    somaHoras = sum(horasPorDia)
    somaPrioridade = sum(calcularPrioridade)
    tempoEstudo= (somaHoras/somaPrioridade)*calcularPrioridade[i]
    horasPorArea.append(round(tempoEstudo)) 
   
horasSegunda = []
horasTerca = []
horasQuarta = []
horasQuinta = []
horasSexta = []
horasSabado = []
horasDomingo = []

horasSegunda = preencherCronograma(horasPorDia[0])
horasTerca = preencherCronograma(horasPorDia[1])
horasQuarta = preencherCronograma(horasPorDia[2])
horasQuinta = preencherCronograma(horasPorDia[3])
horasSexta = preencherCronograma(horasPorDia[4])
horasSabado = preencherCronograma(horasPorDia[5])
horasDomingo = preencherCronograma(horasPorDia[6])

print("------- Cronograma de Estudos -------")
print("\nHorário de Segunda: ",horasSegunda)
print("\nHorário de Terça: ",horasTerca)
print("\nHorário de Quarta: ",horasQuarta)
print("\nHorário de Quinta: ",horasQuinta)
print("\nHorário de Sexta: ",horasSexta)
print("\nHorário de Sábado: ",horasSabado)
print("\nHorário de Domingo: ",horasDomingo)
