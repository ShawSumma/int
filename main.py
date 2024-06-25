
from lark import Lark, Transformer

class Interp(Transformer):
    def start(self, tree):
        return tree[0]

    def single(self, tree):
        return tree[0]
    
    def NUMBER(self, tree):
        return float(tree)

    def op(self, tree):
        if len(tree) == 3:
            match tree[1]:
                case '+':
                    return tree[0] + tree[2]
                case '-':
                    return tree[0] - tree[2]
                case '*':
                    return tree[0] * tree[2]
                case '/':
                    return tree[0] / tree[2]
        else:
            return tree[0]

def main():
    p = Lark.open('in.lark')
    with open('in.lang') as f:
        ast = p.parse(f.read())
    x = Interp().transform(ast)
    print(x)
    
if __name__ == '__main__':
    main()
