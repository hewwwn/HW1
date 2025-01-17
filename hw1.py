def calculator():
    while True:
        operation = input("연산 선택 (+ 또는 -): ")
        if operation not in ['+', '-']:
            print("error 잘못된 연산임. + 또는 -을 선택 요망.")
            continue
        try:
            num1 = int(input("첫 번째 숫자를 입력: "))
            num2 = int(input("두 번째 숫자를 입력: "))
        except ValueError:
            print("error 잘못된 입력. 숫자 입력 요망.")
            continue

        if operation == '+':
            result = num1 + num2
        else:
            result = num1 - num2

        print(f"결과: {result}")
        cont = input("다시 계산하기 (y/n): ")
        if cont.lower() != 'y':
            break

calculator()
