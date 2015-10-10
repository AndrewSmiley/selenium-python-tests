__author__ = 'pridemai'


def hello():
    return "Hello, World!"


def my_decorator(some_function):

  def wrapper(num):
      if num % 2 == 0:
          return some_function(True)
      else:
          return some_function(False)




# @my_decorator
# def just_some_function(3):
#     print "testing"


def is_prime(num):
    return num % 2 == 0
