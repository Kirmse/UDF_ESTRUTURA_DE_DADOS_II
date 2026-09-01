# EXERCÍCIO 2 - FILA DE IMPRESSÃO UTILIZANDO FIFO

from collections import deque

class Impressora:
    def __init__(self):
        self.fila = deque()   # fila que guarda os documentos aguardando

    def enfileirar(self, documento):
        self.fila.append(documento)   # adiciona no FINAL da fila
        print(f"'{documento}' adicionado à fila de impressão.")

    def imprimir(self):
        if self.fila:
            documento = self.fila.popleft()   # remove do INÍCIO da fila
            print(f"Imprimindo: '{documento}'")
        else:
            print("Nenhum documento na fila.")

    def mostrar_fila(self):
        print(f"Fila atual: {list(self.fila)}")


# --- testando ---
imp = Impressora()
imp.enfileirar("Documento_1")
imp.enfileirar("Documento_2")
imp.enfileirar("Documento_3")
imp.mostrar_fila()      # Fila atual: ['Documento_1', 'Documento_2', 'Documento_3']

imp.imprimir()          # Imprimindo: 'Documento_1'
imp.mostrar_fila()      # Fila atual: ['Documento_2', 'Documento_3']

imp.imprimir()          # Imprimindo: 'Documento_2'
imp.mostrar_fila()