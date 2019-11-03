
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVDIV LPAREN MINUS NUMBER PLUS RPAREN TIMESexpr : expr PLUS exprexpr : expr MINUS exprexpr : expr TIMES expr\n            | expr DIV exprexpr : NUMBERexpr : LPAREN expr RPAREN'
    
_lr_action_items = {'NUMBER':([0,3,4,5,6,7,],[2,2,2,2,2,2,]),'LPAREN':([0,3,4,5,6,7,],[3,3,3,3,3,3,]),'$end':([1,2,9,10,11,12,13,],[0,-5,-1,-2,-3,-4,-6,]),'PLUS':([1,2,8,9,10,11,12,13,],[4,-5,4,-1,-2,-3,-4,-6,]),'MINUS':([1,2,8,9,10,11,12,13,],[5,-5,5,-1,-2,-3,-4,-6,]),'TIMES':([1,2,8,9,10,11,12,13,],[6,-5,6,6,6,-3,-4,-6,]),'DIV':([1,2,8,9,10,11,12,13,],[7,-5,7,7,7,-3,-4,-6,]),'RPAREN':([2,8,9,10,11,12,13,],[-5,13,-1,-2,-3,-4,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr':([0,3,4,5,6,7,],[1,8,9,10,11,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr","S'",1,None,None,None),
  ('expr -> expr PLUS expr','expr',3,'p_add','example_parser.py',50),
  ('expr -> expr MINUS expr','expr',3,'p_sub','example_parser.py',54),
  ('expr -> expr TIMES expr','expr',3,'p_mult_div','example_parser.py',62),
  ('expr -> expr DIV expr','expr',3,'p_mult_div','example_parser.py',63),
  ('expr -> NUMBER','expr',1,'p_expr2NUM','example_parser.py',74),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_parens','example_parser.py',78),
]
