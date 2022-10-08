myname = "김시우"


def calculator():

    result = 0
    input_data = 0
    while True:
        input_data = input("궁금한 계산 물어봐")
        if "+" in input_data:
            result = int(input_data.split("+")[0]) + int(input_data.split("+")[1])
        elif "-" in input_data:
            result = int(input_data.split("-")[0]) - int(input_data.split("-")[1])
        elif "*" in input_data:
            result = int(input_data.split("*")[0]) * int(input_data.split("*")[1])
        elif "/" in input_data:
            result = int(input_data.split("/")[0]) / int(input_data.split("/")[1])
    
        elif "ㄲㅈ" in input_data:
            print("ㅇㅋ")
            break
        else:
            print("계산식")
            continue
        print(f"{input_data} = {result}")