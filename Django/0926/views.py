from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def base(request):
    return render(request, "base.html")


def holjjack(request, id):

    if id == 0:
        result = "0"

    if id % 2 == 0:
        result = "짝수"

    else:
        result = "홀수"

    context = {"result": result, "id": id}

    return render(request, "holjjack", context)


def calculate(request, var1, var2):

    result_sum = var1 + var2
    result_sub = var1 - var2
    result_mul = var1 * var2
    result_div = var1 // var2

    context = {
        "sum": result_sum,
        "sub": result_sub,
        "mul": result_mul,
        "div": result_div,
        "var1": var1,
        "var2": var2,
    }

    return render(request, "calculate.html", context)
