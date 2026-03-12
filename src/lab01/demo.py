from model import Athlete

def main():
    print("="*50)
    print("LAB 1 - NÍVEL 5 (NOTA MÁXIMA)") #ЛАБОРАТОРИЯ 1-УРОВЕНЬ 5 (МАКСИМАЛЬНАЯ ОЦЕНКА)
    print("="*50)
    
    # 1. CRIAÇÃO VÁLIDA // ДЕЙСТВИТЕЛЬНОЕ СОЗДАНИЕ
    print("\n1. Criando atletas:") # Создание спортсменов
    a1 = Athlete("João", 25, "Futebol", 75, 178)
    a2 = Athlete("Maria", 22, "Natação", 62, 165)
    print(f"   {a1}")
    print(f"   {a2}")
    
    # 2. VALIDAÇÕES SEPARADAS // ОТДЕЛЬНЫЕ ПРОВЕРКИ
    print("\n2. Testando validações (erros esperados):") #Тестирование валидаций (ожидаемые ошибки)
    testes = [
        ("A", 25, "Futebol", 75, 180),      # nome curto// короткое имя
        ("João", 10, "Futebol", 75, 180),   # idade baixa//низкий возраст
        ("João", 25, "", 75, 180),           # esporte vazio/ пустой спорт
        ("João", 25, "Futebol", 500, 180),   # peso alto// высокий вес
    ]
    
    for nome, idade, esporte, peso, altura in testes:
        try:
            a = Athlete(nome, idade, esporte, peso, altura)
        except ValueError as e:
            print(f"    {e}")
    
    # 3. ESTADOS E COMPORTAMENTO DEPENDENTE // СОСТОЯНИЯ И ЗАВИСИМОЕ ПОВЕДЕНИЕ 
    print("\n3. Testando estados (comportamento dependente):")
    print(f"   {a1}")
    a1.treinar(60)      # Funciona (ativo) // Работает (активно)
    a1.desativar()
    try:
        a1.treinar(30)  # Deve falhar // Должен потерпеть неудачу
    except Exception as e:
        print(f"    Erro esperado: {e}") #Ожидаемая ошибка
    a1.ativar()
    a1.treinar(30)      # Funciona de novo // Работает снова
    
    # 4. COMPETIÇÕES // КОНКУРС
    print("\n4. Competições:")
    a1.competir(True)   # Vitória // Победа
    a1.competir(False)  # Derrota // Поражение
    a1.competir(True)   # Vitória // Победа
    
    # 5. SETTER COM VALIDAÇÃO // СЕТТЕР С ПРОВЕРКОЙ
    print("\n5. Setter com validação:")
    print(f"   Peso atual: {a1.weight}kg")
    a1.weight = 77
    print(f"   Novo peso: {a1.weight}kg")
    try:
        a1.weight = 500
    except ValueError as e:
        print(f"    Erro: {e}")
    
    # 6. COMPARAÇÃO (__eq__) // Сравнение (__eq__)
    print("\n6. Comparação:")
    a3 = Athlete("João", 30, "Futebol", 80, 180)
    print(f"   a1 == a2: {a1 == a2}")
    print(f"   a1 == a3: {a1 == a3} (mesmo nome/esporte)") #(то же имя/спорт)
    
    # 7. MÉTODOS MÁGICOS // МАГИЧЕСКИЕ МЕТОДЫ
    print("\n7. Métodos mágicos:")
    print(f"   __str__: {a1}")
    print(f"   __repr__: {repr(a1)}")
    
    # 8. ATRIBUTO DE CLASSE // АТРИБУТ КЛАССА
    print("\n8. Atributo de classe:")
    print(f"   Total atletas: {Athlete.total_athletes}")

if __name__ == "__main__":
    main()