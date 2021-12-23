from behave import given, when, then
from state_bot import get_resp


@given ("user answers {a}, {b}, {c}")
def parse_answrs(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c

@when ("bot recieves the messages")
def get_msgs(context):
    context.key = ""
    if context.a == "да":
        context.key += "1"
    else: 
        context.key += "0"
    if context.b == "да":
        context.key += "1"
    else: 
        context.key += "0"
    if context.c == "да":
        context.key += "1"
    else: 
        context.key += "0"

@then("I expect the result to bе {result}")
def expect_result(context, result):
    context.result = get_resp(context.key)
    context.result == result

    
