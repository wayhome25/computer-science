from stack import Stack

class Calculator:
    def __init__(self, org_exp):
        self.org_exp = org_exp.replace(' ', '')
        self.postfix_exp = None

    def get_weight(self, oprt):
        if oprt == '*' or oprt == '/':
            return 9
        elif oprt == '+' or oprt == '-':
            return 7
        elif oprt == '(':
            return 5
        else:
            return -1

    def convert_to_postfix(self):
        exp_list = []
        oprt_stack = Stack()

        for ch in self.org_exp:
            if ch.isdigit():
                exp_list.append(ch)
            #연산자라면
            else:
                #'(' or 연산자 스택이 비었다면
                if ch == '(' or oprt_stack.is_empty():
                    oprt_stack.push(ch)
                #')'
                elif ch == ')':
                    op = oprt_stack.pop()
                    while op != '(':
                        exp_list.append(op)
                        op = oprt_stack.pop()
                #'+', '-', '*', '/' : 가중치가 높을 때
                elif self.get_weight(ch) > \
                    self.get_weight(oprt_stack.peek()):
                    oprt_stack.push(ch)
                #'+', '-', '*', '/' : 가중치가 낮거나 같을 때
                else:
                    while oprt_stack and self.get_weight(ch) <=\
                          self.get_weight(oprt_stack.peek()):
                        exp_list.append(oprt_stack.pop())
                    oprt_stack.push(ch)
        while oprt_stack:
            exp_list.append(oprt_stack.pop())
        self.postfix_exp = ''.join(exp_list)

    def get_postfix_exp(self):
        if not self.postfix_exp:
            self.convert_to_postfix()

        return self.postfix_exp

    def calc_two_oprd(self, oprd1, oprd2, oprt):
        if oprt == '+':
            return oprd1 + oprd2
        elif oprt == '-':
            return oprd1 - oprd2
        elif oprt == '*':
            return oprd1 * oprd2
        elif oprt == '/':
            return oprd1 // oprd2

    def calculate(self):
        oprd_stack = Stack()

        for ch in self.postfix_exp:
            if ch.isdigit():
                oprd_stack.push(int(ch))
            #연산자라면
            else:
                oprd2 = oprd_stack.pop()
                oprd1 = oprd_stack.pop()
                oprd_stack.push(self.calc_two_oprd(
                    oprd1, oprd2, ch))
        return oprd_stack.pop()

if __name__ == "__main__":
    a = input("수식을 입력하세요 : ")
    calc = Calculator(a)
    print(calc.get_postfix_exp())
    print("{exp} = {result}".format(
        exp = calc.org_exp, result = calc.calculate()))
