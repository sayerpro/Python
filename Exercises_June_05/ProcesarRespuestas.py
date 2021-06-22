# PROCESAR RESPUESTAS POSTULANTES
# ENTRADAS
print("========================================================================")
correctAnswer = int(input("Digite el total de respuestas correctas: "))
incorrectAnswer = int(input("Digite el total de respuestas incorrectas: "))
emptyAnswer = int(input("Digite el total de respuestas en blanco: "))
print("========================================================================")

# PROCESOS
finalScore = correctAnswer * 4 - incorrectAnswer

# SALIDAS
print("========================================================================")
print("RESULTADO PROCESAR RESPUESTAS POSTULANTES")
print("La puntuación por ", correctAnswer,
      " respuestas correctas es de: ", correctAnswer * 4, " puntos")
print("La puntuación por ", incorrectAnswer,
      " respuestas incorrectas es de: -", incorrectAnswer, " puntos")
print("La puntuación por ", emptyAnswer,
      " respuestas en blanco es de: 0 puntos")
print("La puntuación final para un total de ", correctAnswer +
      incorrectAnswer + emptyAnswer, " respuestas es de: ", finalScore, " puntos")
print("========================================================================")
