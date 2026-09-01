# Exercício feio por IA com objetivo de comrpeender o código (anotação própria).

class Paciente:
    # guarda os dados de um paciente
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade  # "Normal" ou "Prioridade"


class NodePaciente:
    # no da fila: guarda um paciente e a referencia para o proximo no
    def __init__(self, paciente):
        self.paciente = paciente
        self.proximo = None


class FilaAtendimento:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.qtd = 0

    def adicionar(self, paciente):
        novo_no = NodePaciente(paciente)

        if self.esta_vazia():
            # fila vazia: o novo no e o inicio e o fim ao mesmo tempo
            self.inicio = novo_no
            self.fim = novo_no

        elif paciente.prioridade == "Prioridade":
            # paciente prioritario entra depois dos outros prioritarios,
            # mas antes do primeiro paciente normal
            anterior = None
            atual = self.inicio

            while atual is not None and atual.paciente.prioridade == "Prioridade":
                anterior = atual
                atual = atual.proximo

            if anterior is None:
                # nao havia nenhum prioritario antes: o novo no vira o inicio
                novo_no.proximo = self.inicio
                self.inicio = novo_no
            else:
                # insere o novo no entre "anterior" e "atual"
                novo_no.proximo = atual
                anterior.proximo = novo_no

            if atual is None:
                # o novo no acabou entrando no final da fila
                self.fim = novo_no

        else:
            # paciente normal: sempre vai para o final da fila
            self.fim.proximo = novo_no
            self.fim = novo_no

        self.qtd = self.qtd + 1

    def atender(self):
        if self.esta_vazia():
            return None

        atendido = self.inicio.paciente
        self.inicio = self.inicio.proximo  # remove o primeiro paciente da fila

        if self.inicio is None:
            # a fila ficou vazia depois da remocao
            self.fim = None

        self.qtd = self.qtd - 1
        return atendido

    def listar(self):
        atual = self.inicio
        while atual is not None:
            linha = atual.paciente.nome + " - " + str(atual.paciente.idade) + " anos - " + atual.paciente.prioridade
            print(linha)
            atual = atual.proximo

    def esta_vazia(self):
        return self.inicio is None

    def tamanho(self):
        return self.qtd


# ------------------------------------------------------------
# Exemplo de utilizacao
# ------------------------------------------------------------

fila = FilaAtendimento()

fila.adicionar(Paciente("Ana", 32, "Normal"))
fila.adicionar(Paciente("Bruno", 70, "Normal"))
fila.adicionar(Paciente("Carlos", 45, "Prioridade"))

print("Fila de atendimento:")
fila.listar()

print("")
print("Tamanho da fila: " + str(fila.tamanho()))

paciente_atendido = fila.atender()
print("")
print("Atendendo: " + paciente_atendido.nome)

print("")
print("Fila apos o atendimento:")
fila.listar()
