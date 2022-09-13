#............................
def new_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
    print("--------")
    print(key)
    for i in options[question_num-1]:
      print(i)
    guess = input("Seleccione (A, B, C o D): ")
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key),guess)
    question_num += 1

  display_score(correct_guesses, guesses)
   
#..............................
def check_answer(answer, guess):
  if answer == guess:
    print("Exelente")
    return 1
  else:
    print("Incorrecto")
    return 0
#..............................
def display_score(correct_guesses, guesses):
  print("-----------------------")
  print("resultados")
  print("------------------------")
  print("answers: ", end="")
  print()

  print("guesses: ", end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()

  score =int((correct_guesses/len(questions))*100)
  print("tú puntaje es: "+str(score)+"%")
  
#..............................
def play_again():
  response = input("¿Quieres jugar otra vez? (SI O NO): ")
  response = response.upper()
  if response == "SI":
    return True
  else:
    return False


# diccionario de preguntas
questions = {
    "¿Qué es un casuario?: ": "C",
    "¿Qué estudia la limnología?: ": "D",
    "¿Quién es el creador de python?: ": "C",
    "¿Cómo se llamaba el sistema de escritura de los antiguos egipcios?: ": "A",
    "¿Cuántos ojos tienen los cíclopes?: ": "A",
    "¿Cuántos viajes hizo Colón a América?: ": "C",
    "¿Quién escribió el poema épico de la Odisea?: ": "B",
    "¿Cuánto tardó en hundirse el Titanic?: ": "D",
    "¿Qué planeta es más cercano al sol?: ": "B",
    "¿A los cuántos años murió la Reina ISABEL II?: ": "A"
} 
options = [
  ["A. Monumento", "B. Coche", "C. Ave", "D. Metal"],
  ["A. Peces", "B. Plagas", "C. Frutas", "D. Ecosistemas"],
  ["A. Brendan Eich", "B. Tim Berners-Lee", "C. Guido van Rossum", "D. Rasmus Lerdorf"],
  ["A. Jeroglíficos", "B. Braille", "C. Arameo", "D. Zapoteco"],
  ["A. 1", "B. 10", "C. 3", "D. 100"],
  ["A. 2", "B. 3", "C. 4", "D. 10"],
  ["A. Sócrates", "B. Homero", "C. Hesíodo", "D. Plutarco"],
  ["A. Media hora", "B. Una hora y veinte minutos", "C. Cinco horas y media", "D. Dos horas y cuarenta minutos"],
  ["A. Tierra", "B. Mercurio", "C. Venus", "D. Saturno"],
  ["A. 96", "B. 86", "C. 79", "D. 98"] 
]
  
new_game()
while play_again():
  new_game()
  print("ADIOS")