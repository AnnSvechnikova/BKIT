from behave import given, when, then
from lab4 import get_roots

@given ("I have the coefs {a:g} and {b:g} and {c:g}")
def have_coefs(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c

@when("I solve equation")
def solve_eq(context):
    context.result = get_roots(context.a, context.b, context.c)

@then("I expect the result to be {result}")
def expect_result(context, result):
    context.result == result


