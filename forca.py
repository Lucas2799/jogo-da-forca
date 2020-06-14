# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
# Board (tabuleiro)
board = ['''

>>>>>>>>>>>>>>FORCA<<<<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.missed_letters = []
		self.guessed_letters = []
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word and letter not in self.guessed_letters:
			self.guessed_letters.append(letter)
		elif letter not in self.word and letter not in self.missed_letters:
			self.missed_letters.append(letter)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.missed_letters) == 6)
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if '*' not in self.hide_word():
			return True
		return False
		
	# Método para não mostrar a letra no board
	def hide_word(self):
		rtn = ''
		for letter in self.word:
			if letter not in self.guessed_letters:
				rtn += '*'
			else:
				rtn += letter
		return rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print (board[len(self.missed_letters)])
		print ('\nPalavra: ' + self.hide_word())
		print("\ndica nome de pessoas")
		print ('\nLetras erradas: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Letras corretas: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

	def print_jogo_status(self):
		print (board[len(self.missed_letters)])
		print ('\nPalavra: ' + self.hide_word())
		print("\ndica : objetos")
		print ('\nLetras erradas: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Letras corretas: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

	def print_joginho_status(self):
		print (board[len(self.missed_letters)])
		print ('\nPalavra: ' + self.hide_word())
		print("\ndica: nome de paises ")
		print ('\nLetras erradas: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Letras corretas: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()

	def print_job_status(self):
		print (board[len(self.missed_letters)])
		print ('\nPalavra: ' + self.hide_word())
		print("\ndica: nome de paises ")
		print ('\nLetras erradas: ',) 
		for letter in self.missed_letters:
			print (letter,) 
		print ()
		print ('Letras corretas: ',)
		for letter in self.guessed_letters:
			print (letter,)
		print ()


# Método para ler uma palavra de forma aleatória do banco de palavras
def banconome():
        with open("nome.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

def bancoobjeto():
		with open("objeto.txt", "rt") as f:
        		bank = f.readlines()
		return bank[random.randint(0,len(bank))].strip()

def bancopais():
		with open("paises.txt", "rt") as f:
        		bank = f.readlines()
		return bank[random.randint(0,len(bank))].strip()

def bancofrutas():
		with open("frutas.txt", "rt") as f:
        		bank = f.readlines()
		return bank[random.randint(0,len(bank))].strip()


# Método Main - Execução do Programa
def main():

	# Objeto
	game =  Hangman(banconome()) 

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		print("a dica é: nome de pessoas\n")
		game.guess(user_input)
		# define uma dica 


	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)


		# Objeto
	jogo =  Hangman(bancoobjeto()) 

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not jogo.hangman_over():
		jogo.print_jogo_status()
		user_input = input('\nDigite uma letra: ')
		print("a dica é : nome de objetos \n")
		jogo.guess(user_input)
		# define uma dica 


	# Verifica o status do jogo
	jogo.print_jogo_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if jogo.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + jogo.word)

		# Objeto
	joginho =  Hangman(bancopais()) 

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not joginho.hangman_over():
		joginho.print_joginho_status()
		user_input = input('\nDigite uma letra: ')
		print("a dica é : nome de paises \n")
		joginho.guess(user_input)
		# define uma dica 


	# Verifica o status do jogo
	joginho.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if joginho.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + joginho.word)

		# Objeto
	job =  Hangman(bancofrutas()) 

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not job.hangman_over():
		job.print_job_status()
		user_input = input('\nDigite uma letra: ')
		print("a dica é : nome de frutas \n")
		job.guess(user_input)
		


	# Verifica o status do jogo
	jogo.print_jogo_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if jogo.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + job.word)

		
	
	

# Executa o programa		
if __name__ == "__main__":
	main()
