import math
import time
from itertools import batched

with open("./day17/ex2.txt", "r") as file:
    registers, instructions = file.read().split("\n\n")
    reg_a, reg_b, reg_c = registers.split("\n")
    reg_a = int(reg_a.split(":")[1])
    reg_b = int(reg_b.split(":")[1])
    reg_c = int(reg_c.split(":")[1])
    instructions = instructions.split(":")[1]
    instructions = [int(i) for i in instructions.split(",")]


class CPU:
    def __init__(self, reg_a, reg_b, reg_c, instructions):
        self.pointer = 0
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.reg_c = reg_c
        self.instructions = instructions
        self.results = []
        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def run_op(self):
        if self.pointer >= len(self.instructions):
            return self.results
        current_instruction = self.instructions[self.pointer]
        operand = self.instructions[self.pointer + 1]
        fn = self.opcodes[current_instruction]
        fn(operand)
        self.pointer += 2
        return self.run_op()

    def combo(self, x):
        combo_value = {
            0: x,
            1: x,
            2: x,
            3: x,
            4: self.reg_a,
            5: self.reg_b,
            6: self.reg_c,
        }[x]
        return combo_value

    # 0
    def adv(self, x):
        num = self.reg_a
        den = 2 ** self.combo(x)
        self.reg_a = math.floor(num / den)

    # 1
    def bxl(self, x):
        result = self.reg_b ^ x
        self.reg_b = result

    # 2
    def bst(self, x):
        result = self.combo(x) % 8
        self.reg_b = result

    # 3
    def jnz(self, x):
        if self.reg_a == 0:
            return
        self.pointer = x - 2

    # 4
    def bxc(self, x):
        self.reg_b = self.reg_b ^ self.reg_c

    # 5
    def out(self, x):
        self.results.append(self.combo(x) % 8)

    # 6
    def bdv(self, x):
        num = self.reg_a
        den = 2 ** self.combo(x)
        self.reg_b = math.floor(num / den)

    # 7
    def cdv(self, x):
        num = self.reg_a
        den = 2 ** self.combo(x)
        self.reg_c = math.floor(num / den)


expected_result = instructions
expected_length = len(instructions)
min_reg_a = 8 ** (expected_length - 1)
max_reg_a = 8 ** (expected_length)
diff = max_reg_a - min_reg_a

start = time.time()

first_values = []


def get_period(values):
    for i in range(2, len(values) // 2):
        batches = list(batched(values, i))
        first = batches[0]
        is_period = False
        for j in range(1, len(batches)):
            cur = batches[j]
            if len(cur) != len(first):
                is_period = True
                break
            elif batches[0] != batches[j]:
                is_period = False
                break
            is_period = True
        if is_period:
            return first


for i in range(min_reg_a, max_reg_a):
    cpu = CPU(i, reg_b, reg_c, instructions)
    result = cpu.run_op()
    first_values.append(result[0])


period = get_period(first_values)
iteration = 0

for idx, value in enumerate(instructions):
    index = period.index(value)
    iteration += index * (8**idx)

print(iteration)
