# EXERCÍCIO 1 - SISTEMA DESFAZER DE UM EDITOR DE TEXTO UTILIZANDO LIFO

class Editor:
    def __init__(self):
        self.texto = ""       # o texto atual do editor
        self.historico = []   # pilha (lista) que guarda os estados anteriores

    def escrever(self, novo_texto):
        self.historico.append(self.texto)   # guarda como estava ANTES de mudar
        self.texto += novo_texto             # agora sim, atualiza o texto

    def apagar(self, quantidade):
        self.historico.append(self.texto)    # guarda o estado antes de apagar
        self.texto = self.texto[:-quantidade]  # remove os últimos N caracteres

    def desfazer(self):
        if self.historico:                    # só desfaz se tiver algo salvo
            self.texto = self.historico.pop()  # volta pro último estado salvo
        else:
            print("Nada para desfazer.")

    def mostrar(self):
        print(f"Texto atual: '{self.texto}'")


# --- testando ---
ed = Editor()
ed.escrever("Ola")
ed.mostrar()          # Texto atual: 'Ola'

ed.escrever(" mundo")
ed.mostrar()          # Texto atual: 'Ola mundo'

ed.apagar(6)
ed.mostrar()          # Texto atual: 'Ola'

ed.desfazer()
ed.mostrar()          # Texto atual: 'Ola mundo'

ed.desfazer()
ed.mostrar()          # Texto atual: 'Ola'