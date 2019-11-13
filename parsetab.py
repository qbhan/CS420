
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVCOLON COMMA DIV DOUBLEQUOTE ELSE ELSE_IF EQ EQUAL FLOAT FOR GT ID IF INCREMENT INT LBRACE LBRACKET LPAREN LT MAIN MINUS NEQ NUMBER PERIOD PLUS POINTER PRINT QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES VOIDexpr : ID EQUAL arith_exprexpr : bool_exprbool_expr : arith_exprbool_expr : bool_expr EQ arith_exprbool_expr : bool_expr NEQ arith_exprbool_expr : bool_expr GT arith_exprbool_expr : bool_expr LT arith_exprarith_expr : arith_expr PLUS termarith_expr : arith_expr MINUS termarith_expr : termterm : term TIMES factorterm : term DIV factorterm : factorfactor : LPAREN expr RPARENfactor : MINUS factorfactor : IDfactor : NUMBER'
    
_lr_action_items = {'ID':([0,6,8,10,11,12,13,14,15,16,17,18,],[2,20,2,20,20,20,20,20,20,20,20,20,]),'LPAREN':([0,6,8,10,11,12,13,14,15,16,17,18,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'MINUS':([0,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,],[6,-16,12,-10,6,-13,6,-17,6,6,6,6,6,6,6,6,6,-15,-16,12,-8,-9,12,12,12,12,-11,-12,-14,]),'NUMBER':([0,6,8,10,11,12,13,14,15,16,17,18,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,3,4,5,7,9,19,20,22,23,24,25,26,27,28,29,30,31,],[0,-16,-3,-2,-10,-13,-17,-15,-16,-1,-8,-9,-4,-5,-6,-7,-11,-12,-14,]),'EQUAL':([2,],[10,]),'TIMES':([2,5,7,9,19,20,23,24,29,30,31,],[-16,17,-13,-17,-15,-16,17,17,-11,-12,-14,]),'DIV':([2,5,7,9,19,20,23,24,29,30,31,],[-16,18,-13,-17,-15,-16,18,18,-11,-12,-14,]),'PLUS':([2,3,5,7,9,19,20,22,23,24,25,26,27,28,29,30,31,],[-16,11,-10,-13,-17,-15,-16,11,-8,-9,11,11,11,11,-11,-12,-14,]),'EQ':([2,3,4,5,7,9,19,20,23,24,25,26,27,28,29,30,31,],[-16,-3,13,-10,-13,-17,-15,-16,-8,-9,-4,-5,-6,-7,-11,-12,-14,]),'NEQ':([2,3,4,5,7,9,19,20,23,24,25,26,27,28,29,30,31,],[-16,-3,14,-10,-13,-17,-15,-16,-8,-9,-4,-5,-6,-7,-11,-12,-14,]),'GT':([2,3,4,5,7,9,19,20,23,24,25,26,27,28,29,30,31,],[-16,-3,15,-10,-13,-17,-15,-16,-8,-9,-4,-5,-6,-7,-11,-12,-14,]),'LT':([2,3,4,5,7,9,19,20,23,24,25,26,27,28,29,30,31,],[-16,-3,16,-10,-13,-17,-15,-16,-8,-9,-4,-5,-6,-7,-11,-12,-14,]),'RPAREN':([2,3,4,5,7,9,19,20,21,22,23,24,25,26,27,28,29,30,31,],[-16,-3,-2,-10,-13,-17,-15,-16,31,-1,-8,-9,-4,-5,-6,-7,-11,-12,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,8,],[1,21,]),'arith_expr':([0,8,10,13,14,15,16,],[3,3,22,25,26,27,28,]),'bool_expr':([0,8,],[4,4,]),'term':([0,8,10,11,12,13,14,15,16,],[5,5,5,23,24,5,5,5,5,]),'factor':([0,6,8,10,11,12,13,14,15,16,17,18,],[7,19,7,7,7,7,7,7,7,7,29,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> ID EQUAL arith_expr','expr',3,'p_expr_assign','pycparser.py',17),
  ('expr -> bool_expr','expr',1,'p_expr_bool','pycparser.py',21),
  ('bool_expr -> arith_expr','bool_expr',1,'p_compare_expr_arith','pycparser.py',25),
  ('bool_expr -> bool_expr EQ arith_expr','bool_expr',3,'p_compare_expr_eq','pycparser.py',29),
  ('bool_expr -> bool_expr NEQ arith_expr','bool_expr',3,'p_compare_expr_neq','pycparser.py',33),
  ('bool_expr -> bool_expr GT arith_expr','bool_expr',3,'p_compare_expr_gt','pycparser.py',37),
  ('bool_expr -> bool_expr LT arith_expr','bool_expr',3,'p_compare_expr_lt','pycparser.py',41),
  ('arith_expr -> arith_expr PLUS term','arith_expr',3,'p_arith_add','pycparser.py',77),
  ('arith_expr -> arith_expr MINUS term','arith_expr',3,'p_arith_sub','pycparser.py',81),
  ('arith_expr -> term','arith_expr',1,'p_arith_term','pycparser.py',85),
  ('term -> term TIMES factor','term',3,'p_term_mult','pycparser.py',89),
  ('term -> term DIV factor','term',3,'p_term_div','pycparser.py',93),
  ('term -> factor','term',1,'p_term_factor','pycparser.py',99),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_parens','pycparser.py',103),
  ('factor -> MINUS factor','factor',2,'p_factor_neg','pycparser.py',107),
  ('factor -> ID','factor',1,'p_factor_id','pycparser.py',111),
  ('factor -> NUMBER','factor',1,'p_factor_number','pycparser.py',115),
]
