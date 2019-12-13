from datastructure import *
from pycvisitor import *
from ply import yacc as yacc
from pycparser import *
from pyclexer import *

# # ###
# # class test:
# #     def k(self, v):
# #         return v+1
# # x = test()
# # kay = getattr(test, 'k', None)
# # print(kay(x, 1))
# # ###
visitor1 = SymtabVisitor()
visitor2 = InterpVisitor()

# ast1 = DeclStmt('int', 'x')
# ast2 = Assignment(Identifier('x', 40), Constant(1))
# ast3 = DeclStmt('int', 'a')
# ast4 = Assignment(Identifier('a', 42), Binop(Negation(Identifier('x', 40)), '+', Constant(1)))
#
# visitor.visit(ast1)
# print(table.entry)
# visitor.visit(ast2)
# print(table.entry)
# visitor.visit(ast3)
# print(table.entry)
# visitor.visit(ast4)
# print(table.entry['x'].value, table.entry['a'].value)
# # The result of the last line is...
# # <datastructure.Constant object at 0x014F76B0> <datastructure.Binop object at 0x014F77B0>

# # Mac book 16inch
# body = StmtBlock ... Assignment(Identifier('res', 44), Binop(Identifier('res', 41), '+', Identifier('i', 43)))
# ast1 = DeclStmt('int', 'res')
# ast2 = Assignment(Identifier('res', 41), Constant(0))
# ast3 = DeclStmt('int', 'i')
# ast4 = For(Assignment(Identifier('i', 43), Constant(0)),
#            Binop(Identifier('i', 43), '<', Constant(5)), Increment(Identifier('i', 43)), body)
# visitor.visit(ast1)
# print(table.entry)
# visitor.visit(ast2)
# print(table.entry)
# visitor.visit(ast3)
# print(table.entry)
# visitor.visit(ast4)
# print(table.entry)


# # e.g.1
# # Translation Unit
# ast0 = GlobalList()
#
# # global vars
# ast1 = DeclStmt('int', 'g')
#
# # function f1
# ast5 = StmtList()
# f1stmtnodes = [ReturnStmt(Binop(Identifier('x', 33), '+', Constant(1)))]
# ast5.nodes = f1stmtnodes
# Pl = ParameterList()
# Pl.nodes = [DeclStmt('int', 'y')]
# ast4 = Function('int', 'f1', Pl, ast5)
#
# # function main
# ast3 = StmtList()
# argl = ArgumentList()
# argl.nodes = [Identifier('x', 38)]
# assign = Assignment(Identifier('x', 38), FunctionCall(ast4, argl))
# mainstmtnodes = [DeclStmt('int', 'x'), Assignment(Identifier('x', 37), Constant(1)), assign, ReturnStmt(Identifier('x', 39))]
# ast3.nodes = mainstmtnodes
# ast2 = Function('int', 'main', ParameterList(), ast3)
#
# globallist = [ast1, ast4, ast2]
# ast0.nodes = globallist
#
# visitor1.visit_symtab(ast0)
# visitor2.visit_interp(ast0)
#
# print(visitor2.currSymtab.history)
# print(ast2.symtab.history)
# print(ast4.symtab.history)

# # e.g.2
# ast0 = GlobalList()
#
# ast1 = DeclStmt('int', 'a')
# ast4 = Assignment(Identifier('a', 32), Constant(1))
# ast2 = DeclStmt('int', 'b')
# ast3 = Assignment(Identifier('b', 34), Binop(Identifier('a', 34), '+', Negation(Constant(3))))
#
# ast0.nodes = [ast1, ast4, ast2, ast3]
#
# visitor1.visit_symtab(ast0)
# visitor2.visit_interp(ast0)
#
# print(visitor2.currSymtab.history)

# parsing with yacc
parser = yacc.yacc()
input = ''
f = open('test.txt', 'r')
while True:
    line = f.readline()
    input += line
    if not line:
        break
print(input)
f.close()
print(input)
ast = parser.parse(input)
print(ast)
# visitor1.visit_symtab(ast)
visitor2.visit_interp(ast)
print(ast.nodes[2].symtab.history)

# # (Return Statement in IF, FOR)
# ast0 = GlobalList()
#
# body1 = StmtList()
# ifstmt = StmtList()
# ifstmt.nodes = [Assignment(Identifier('x', 33), Constant(10)), ReturnStmt(Identifier('x', 33))]
# body1.nodes = [If(Binop(Identifier('x', 33), '>', Constant(1)), ifstmt, StmtList(ReturnStmt(Identifier('x', 33))))]
# ast1 = Function('int', 'f', ParameterList(DeclStmt('int', 'x')), body1)
#
# body2 = StmtList()
# body2.nodes = [DeclStmt('int', 'a'), DeclStmt('int', 'b'), Assignment(Identifier('a', 77), FunctionCall(ast1, ArgumentList(Constant(1))))
#     , Assignment(Identifier('b', 78), FunctionCall(ast1, ArgumentList(Constant(2))))
#     , ReturnStmt(Constant(0))]
# ast2 = Function('int', 'main', ParameterList(), body2)
#
# ast0.nodes = [ast1, ast2]
# visitor1.visit_symtab(ast0)
# visitor2.visit_interp(ast0)
# print(ast1.symtab.history)
