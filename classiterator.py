from fibonacci import Fib
import PluralRule


for n in Fib(1000):
    print(n, end =' ')

r1 = PluralRule.LazyRules()
print(r1.pattern_file)