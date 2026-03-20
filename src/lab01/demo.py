from model import Athlete

def main():
    print("="*50)
    print("LAB 1 - УРОВЕНЬ 5") #ЛАБОРАТОРИЯ 1- NÍVEL 5// level 5
    print("="*50)
    
    # 1. ДЕЙСТВИТЕЛЬНОЕ СОЗДАНИЕ // CRIAÇÃO VÁLIDA
    print("\n1. Создание спортсменов:") # Criando Atletas  
    a1 = Athlete("João", 25, "Футбол", 75, 178)
    a2 = Athlete("Maria", 22, "Плавание", 62, 165)
    print(f"   {a1}")
    print(f"   {a2}")
    
    # 2. VALIDAÇÕES SEPARADAS // ОТДЕЛЬНЫЕ ПРОВЕРКИ
    print("\n2. Тестирование валидаций (ожидаемые ошибки):") # Testando validações  (erros esperados)
    testes = [
        ("A", 25, "Футбол", 75, 50),      # короткое имя// Nome curto 
        ("João", 10, "Футбол", 75, 90),   # низкий возраст//idade baixa
        ("João", 25, "", 75, 180),           # пустой спорт/ Esporte vázio
        ("João", 25, "Футбол", 500, 180),   # высокий вес// Peso alto
    ]
    
    for имя, возраст, спорт, вес, рост in testes:
        try:
            a = Athlete(имя, возраст, спорт, вес, рост)
        except ValueError as e:
            print(f"    {e}")
    
    # 3.   СОСТОЯНИЯ И ЗАВИСИМОЕ ПОВЕДЕНИЕ // ESTADOS E COMPORTAMENTO DEPENDENTE
    print("\n3. Тестирование состояний (зависимое поведение):") #Teste de Estado (comportamento dependente)
    print(f"   {a1}")
    a1.treinar(60)      # Работает (активно) // Funciona (ativo)
    a1.desativar()
    try:
        a1.treinar(30)  #Должен потерпеть неудачу //  Deve falhar
    except Exception as e:
        print(f"    Ожидаемая ошибка: {e}") #Ожидаемая ошибка Erro esperado
    a1.ativar()
    a1.treinar(30)      #  Работает снова // Funciona de novo
    
    # 4. КОНКУРС // Competições
    print("\n4.  КОНКУРС:")
    a1.competir(True)   #Победа // vitória
    a1.competir(False)  #Поражение //Derrota
    a1.competir(True)   #Победа // Vitória
    
    # 5.СЕТТЕР С ПРОВЕРКОЙ//SETTER COM VALIDAÇÃO   
    print("\n5. СЕТТЕР С ПРОВЕРКОЙ:")
    print(f"  Текущий вес: {a1.weight}kg")
    a1.weight = 77
    print(f"   Новый вес: {a1.weight}kg")
    try:
        a1.weight = 500
    except ValueError as e:
        print(f"    Erro: {e}")
    
    # 6.    Сравнение (__eq__)   //  COMPARAÇÃO (__eq__)
    print("\n6. Сравнение:")
    a3 = Athlete("João", 30, "Футбол", 80, 180)
    print(f"   a1 == a2: {a1 == a2}")
    print(f"   a1 == a3: {a1 == a3} (то же имя/спорт)  ") #(mesmo nome/esporte)
    
    # 7.МАГИЧЕСКИЕ МЕТОДЫ // MÉTODOS MÁGICOS
    print("\n7.МАГИЧЕСКИЕ МЕТОДЫ:")
    print(f"   __str__: {a1}")
    print(f"   __repr__: {repr(a1)}")
    
    # 8. АТРИБУТ КЛАССА // ATRIBUTO DE CLASSE   
    print("\n8. q:")
    print(f"   Total atletas: {Athlete.total_athletes}")

if __name__ == "__main__":
    main()