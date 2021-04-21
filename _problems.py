# redo as objects
from random import randint, random, choice
from math import log10
import sympy

def randData(frm, to, exp):
  x = randint(frm, to) * 10**exp
  if exp < 0 and x.is_integer():
    x = int(x)
  return round(x, abs(exp)+5)

def roundn(x, n):
  if x < 1:
    return abs(round(x, abs(int(log10(abs(x)))) + n))
  else:
    y = abs(int(log10(abs(x))))
    z = round(x / 10 ** (y-n), 0) * 10 ** (y-n)
    if float.is_integer(float(z)):
      return abs(int(z))
    else:
      return abs(z)

class Question:
  def __init__(self, data_dict, formulae):
    self.question = data_dict['question']
    self.constants = {i: constants[i] for i in data_dict['constants']}
    self.parameters = data_dict['parameters']
    self.unknown = data_dict['unknown']
    self.formulae = formulae + data_dict['formulae']
    self.knowns = data_dict['knowns']
    self.data = {}
    self.equations = [sympy.Eq(*map(sympy.S, formula.split("="))) for formula in self.formulae]
    self.symbols = {b.name: b for a in [eq.free_symbols for eq in self.equations] for b in a}
    self.generateData()
    self.solve()
  
  def generateData(self):
    for key, value in self.knowns.items():
      self.data[self.symbols[key]] = randData(*eval(value))
    if self.parameters:
      self.data.update({self.symbols[i]: self.parameters[i] for i in self.parameters})
    if self.constants:
      self.data.update({self.symbols[i]: self.constants[i] for i in self.constants})
    return
  
  def solve(self):
    while self.equations:
      for eq in self.equations:
        unknown = eq.free_symbols - set(self.data.keys())
        if len(unknown) == 1:
          solved_exp = sympy.solve(eq, list(unknown)[0])
          solved_data = [i.subs(self.data) for i in solved_exp]
          solved_data.sort(reverse = True)
          self.data[list(unknown)[0]] = solved_data[0]
          self.equations.remove(eq)
    res = self.data[self.symbols[self.unknown]]
    self.solution_exact = res
    self.solution_decimal = roundn(self.solution_exact, 3)
    return
 
  def __str__(self):
    return self.question.format(**{i:self.data[self.symbols[i]] for i in self.symbols})

with open('constants.txt', 'r') as consts:
  constants = {c.split("=")[0]: eval(c.split("=")[1]) for c in consts.readlines()}

