import sys
import os

# Configuração de caminhos absolutos do ecossistema do projeto
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))

sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab03'))
sys.path.insert(1, CURRENT_DIR)

# Importações dos laboratórios anteriores e do módulo atual
from models import ProfessionalAthlete, AmateurAthlete
from container import TypedCollection, Displayable, Scorable, D, S

def patch_classes_for_protocols() -> None:
    """
    Adiciona os métodos exigidos pelos Protocolos de forma dinâmica.
    Garante o Duck Typing Estático (Subtipagem Estrutural) do Nível 5.
    """
    ProfessionalAthlete.display = lambda self: self.__str__()
    ProfessionalAthlete.score = lambda self: float(self.rating)

    AmateurAthlete.display = lambda self: self.__str__()
    AmateurAthlete.score = lambda self: float(self.rating)


def main() -> None:
    # Ativa a compatibilidade estrutural com os Protocolos
    patch_classes_for_protocols()

    print("=" * 75)
    print("      LABORATÓRIO 06 - EXECUÇÃO DOS 3 CENÁRIOS OBRIGATÓRIOS")
    print("=" * 75)

    # Setup de dados comuns extraídos da hierarquia do Lab 03
    p1 = ProfessionalAthlete("Cristiano", 39, "Futebol", 85, 187, 50000, "Nike")
    p2 = ProfessionalAthlete("Rebeca", 25, "Ginástica", 48, 155, 15000, "Adidas")
    a1 = AmateurAthlete("Carlos", 20, "Corrida", 70, 175, "Lisboa Runners", "Estudante")

    # -------------------------------------------------------------------------
    # CENÁRIO 1: VALIDAÇÃO DE TIPOS E OPERAÇÕES GENÉRICAS BASE (NÍVEL 3)
    # -------------------------------------------------------------------------
    print("\n🔹 CENÁRIO 1: Coleção Genérica e Validação de Tipos")
    
    # Instanciação com restrição estática fictícia para Profissionais
    equipa_pro: TypedCollection[ProfessionalAthlete] = TypedCollection()
    equipa_pro.add(p1)
    equipa_pro.add(p2)
    
    print(f" -> Sucesso: Adicionados {len(equipa_pro)} atletas à coleção tipada.")
    for atleta in equipa_pro.get_all():
        print(f"    [Recuperado] Nome: {atleta.name:<10} | Classe Originária: {type(atleta).__name__}")


    # -------------------------------------------------------------------------
    # CENÁRIO 2: PROCESSAMENTO FUNCIONAL E MUTAÇÃO DE TIPOS COM MAP (NÍVEL 4)
    # -------------------------------------------------------------------------
    print("\n🔹 CENÁRIO 2: Filtros Avançados e Mutação de Tipos (TypeVar R)")
    
    # Inicializa uma coleção genérica contendo múltiplos tipos da hierarquia
    base_funcional: TypedCollection[any] = TypedCollection()
    base_funcional.add(p1).add(a1).add(p2)

    # 1. Demonstração do método find()
    busca_sucesso = base_funcional.find(lambda x: getattr(x, 'name', '') == "Cristiano")
    busca_falha = base_funcional.find(lambda x: getattr(x, 'name', '') == "Inexistente")
    print(f" -> find() (Alvo existente): {busca_sucesso.name if busca_sucesso else 'Não encontrado'}")
    print(f" -> find() (Alvo inexistente): {busca_falha}")

    # 2. Demonstração do método filter()
    filtrados = base_funcional.filter(lambda x: getattr(x, 'sport', '') == "Futebol")
    print(f" -> filter() por 'Futebol': {[ath.name for ath in filtrados]}")

    # 3. Demonstração do método map() alterando o tipo de retorno (TypeVar R)
    lista_nomes: list[str] = base_funcional.map(lambda x: x.name)
    lista_pesos: list[float] = base_funcional.map(lambda x: float(x.weight))
    
    print(f" -> map() Resultado 1 (Convertido para list[str]): {lista_nomes}")
    print(f" -> map() Resultado 2 (Convertido para list[float]): {lista_pesos}")


    # -------------------------------------------------------------------------
    # CENÁRIO 3: SUBTIPAGEM ESTRUTURAL VIA MULTI-PROTOCOLOS (NÍVEL 5)
    # -------------------------------------------------------------------------
    print("\n🔹 CENÁRIO 3: Validação de Contratos Estáticos (Displayable & Scorable)")

    # Parte A: Teste do Protocolo Displayable (D)
    # Reúne objetos de classes distintas que partilham apenas o método display()
    colecao_visual: TypedCollection[D] = TypedCollection()
    colecao_visual.add(p1)  # ProfessionalAthlete
    colecao_visual.add(a1)  # AmateurAthlete

    print(" -> Executando contrato Displayable (Sem herança formal):")
    for elemento in colecao_visual:
        print(f"    [Displayable] {elemento.display()}")

    # Parte B: Teste do Protocolo Scorable (S)
    # A mesma classe de container opera com uma restrição de assinatura matemática distinta
    colecao_metrica: TypedCollection[S] = TypedCollection()
    colecao_metrica.add(p2)
    colecao_metrica.add(a1)

    print(" -> Executando contrato Scorable (Extraindo dados numéricos):")
    for elemento in colecao_metrica:
        nome_atleta = getattr(elemento, 'name', 'Desconhecido')
        print(f"    [Scorable] Atleta: {nome_atleta:<10} | Score Pontuado: {elemento.score()}")

    print("\n" + "=" * 75)
    print("✅ EXECUÇÃO CONCLUÍDA: TODOS OS 3 CENÁRIOS FORAM VALIDADOS COM SUCESSO!")
    print("=" * 75)


if __name__ == "__main__":
    main()
