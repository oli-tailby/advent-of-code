class Monkey:
    # define monkey class with its behaviours and 'inspections' as a items handled tracker
    def __init__(self, number, items, operation, test, iftrue, iffalse, inspections):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspections = inspections

    # define function to represent taking a term
    def take_turn(self, worry_div, mod_lcm):
        throws = []
        for worry in self.items:
            self.inspections += len(self.items)
            worry = run_operation(worry, self.operation)
            if worry_div: # if handling worries, divide by three
                worry = int(worry/3)
            # use product of divisors to maintain divisibility but avoid big worry ints
            worry = worry%mod_lcm
            # test to find which monkey the item is thrown to
            if worry%self.test == 0:
                throws.append((self.iftrue, worry))
            else: throws.append((self.iffalse, worry))
            self.items = []
        return throws

def run_operation(data, directions):
    (op, amount) = directions
    # if based on old worry value update amount to reflect this
    if amount=='old': amount = data
    # update worry value from directions
    if op=='*': data *= int(amount)
    else: data += int(amount)
    return data

def list_product(ls, init=1):
    for i in ls: init *= i
    return init

def read_input(filename):
    monkeys = []
    with open(filename) as f:
        data = f.read().splitlines()
    # read items from raw text format
    def read_items(raw):
        return list(map(int, raw.split(': ')[-1].split(', ')))
    # function to get basic operation info from raw text format
    def get_operation(raw):
        op = raw.split()[-2]
        amount = raw.split()[-1]
        return (op, amount)
    # read in each monkey attribute from raw text data (disgusting, sorry)
    for i in range(int((len(data)+1)/7)):
        monkey_n = Monkey(int(data[7*i].split()[-1][:-1]),
                         read_items(data[7*i+1]),
                         get_operation(data[7*i+2]),
                         int(data[7*i+3].split()[-1]),
                         int(data[7*i+4].split()[-1]),
                         int(data[7*i+5].split()[-1]),
                          0)
        monkeys.append(monkey_n)
    return monkeys

def run_round(monkeys, worry_div, mod_lcm):
    # each monkey has their turn, then throws to other monkeys based on their results
    for monkey in monkeys:
        throws = monkey.take_turn(worry_div=worry_div, mod_lcm=mod_lcm)
        for throw in throws:
            monkeys[throw[0]].items.append(throw[1])

    return monkeys

def monkey_business(filename, n_rounds, top_n=2, worry_div=True):
    monkeys = read_input(filename)
    mod_lcm = list_product([m.test for m in monkeys]) # using product as all primes - can be improved!

    for _ in range(n_rounds):
        monkeys = run_round(monkeys, worry_div, mod_lcm)

    # return the product of specified top n inspections
    insp = sorted([m.inspections for m in monkeys], reverse=True)
    return list_product(insp[:2])

monkey_business('input.txt', 20)
monkey_business('input.txt', 10000, worry_div=False)
