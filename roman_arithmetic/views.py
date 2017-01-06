from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


numeral_map = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))


def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = i // integer
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)


def roman_to_int(n):
    n = n.upper()
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result


@csrf_exempt
def roman_operation(request):
    if request.method == "POST":
        operand1 = request.POST['operand1']
        operand2 = request.POST['operand2']
        operation = request.POST['operation']
        operand1 = roman_to_int(operand1)
        operand2 = roman_to_int(operand2)
        if operation == 'addition':
            result = operand1 + operand2
        if operation == 'subtraction':
            result = operand1 - operand2
        if operation == 'multiplication':
            result = operand1 * operand2
        if operation == 'devide':
            result = operand1 / operand2
        result = int_to_roman(result)
        status = "success"
    else:
        status = "fail"
        result = ''
    return JsonResponse({"status": status, 'operation': operation, 'result': result})
