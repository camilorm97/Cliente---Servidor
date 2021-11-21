import threading
import sys
import socket
import pickle
import os

class Cliente():

	def __init__(self, host=socket.gethostname(), port=59989):
		self.sock = socket.socket()
		#############################################################################
		############################### 1ER EJERCICIO ###############################
		#############################################################################
		# DESKTOP-JPACEKO
		try:
			client_host = input("Introduce el host: ")
			client_port = input("Introduce el puerto: ")
		except:
			client_host = host
			client_port = port
		nickname = str(input("Introduce un Nickname: "))
		self.sock.connect((str(client_host), int(client_port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()
		print('Hilo con PID',os.getpid())
		print('Hilos activos', threading.active_count())
		#############################################################################
		############################## 2NDO EJERCICIO ###############################
		#############################################################################
		while True:
			print("\nHola " + nickname)
			msg = input('Escriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n').upper()
			if msg != 'Q':
				self.enviar([nickname, msg])
			else:
				print(" **** TALOGOOO  ****")
				self.sock.close()
				sys.exit()

	def recibir(self):
		while True:
			try:
				data = self.sock.recv(32)
				if data:
					print(pickle.loads(data) + "\n")
			except:
				pass

	def enviar(self, msg):
		a = self.sock.send(pickle.dumps(msg))

c = Cliente()
