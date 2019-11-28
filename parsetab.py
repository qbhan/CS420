
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVrightUMINUSCOLON COMMA DIV DOUBLEQUOTE ELSE ELSE_IF EQ EQUAL FLOAT FNUM FOR GT ID IF INCREMENT INT INUM LBRACE LBRACKET LPAREN LT MAIN MINUS NEQ PERIOD PLUS POINTER PRINT QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES VOIDprogram : func_declaration_listfunc_declaration_list : func_declaration_list func_declarationfunc_declaration_list : emptyfunc_declaration : type ID LPAREN param_list RPAREN stmt_blockfunc_declaration : type TIMES ID LPAREN param_list RPAREN stmt_blockparam_list : emptyparam_list : param_list COMMA paramparam : type IDparam : type TIMES IDstmt : expr SEMICOLON\n            | local_declaration\n            | stmt_block\n            | stmt_return\n            | SEMICOLONlocal_declaration : type ID SEMICOLONlocal_declaration : type TIMES ID SEMICOLONlocal_declaration : type LBRACKET INUM RBRACKET ID SEMICOLONtype : INT\n            | FLOAT\n            | VOIDstmt_block : LBRACE stmt_list RBRACEstmt_list : stmt_list stmtstmt_list : emptystmt_return : RETURN expr SEMICOLONstmt_return : RETURN SEMICOLONexpr : ID EQUAL exprexpr : incr_exprexpr : basic_exprbasic_expr : basic_expr compare arith_exprbasic_expr : arith_exprcompare : EQ\n               | NEQ\n               | GT\n               | LTincr_expr : ID INCREMENTincr_expr : INCREMENT IDarith_expr : MINUS arith_expr %prec UMINUSarith_expr : LPAREN arith_expr RPARENarith_expr : arith_expr PLUS arith_exprarith_expr : arith_expr MINUS arith_exprarith_expr : arith_expr TIMES arith_exprarith_expr : arith_expr DIV arith_exprarith_expr : IDarith_expr : FNUMarith_expr : INUMempty :'
    
_lr_action_items = {'INT':([0,2,3,4,17,19,20,24,25,28,29,30,32,33,34,35,48,60,71,74,80,83,],[-46,6,-3,-2,6,-4,-46,6,-23,-5,-21,-22,-14,-11,-12,-13,-10,-25,-15,-24,-16,-17,]),'FLOAT':([0,2,3,4,17,19,20,24,25,28,29,30,32,33,34,35,48,60,71,74,80,83,],[-46,7,-3,-2,7,-4,-46,7,-23,-5,-21,-22,-14,-11,-12,-13,-10,-25,-15,-24,-16,-17,]),'VOID':([0,2,3,4,17,19,20,24,25,28,29,30,32,33,34,35,48,60,71,74,80,83,],[-46,8,-3,-2,8,-4,-46,8,-23,-5,-21,-22,-14,-11,-12,-13,-10,-25,-15,-24,-16,-17,]),'$end':([0,1,2,3,4,19,28,29,],[-46,0,-1,-3,-2,-4,-5,-21,]),'ID':([5,6,7,8,10,20,22,24,25,27,29,30,32,33,34,35,39,41,42,44,45,48,49,51,52,53,54,55,57,60,62,63,64,65,71,74,80,81,83,],[9,-18,-19,-20,12,-46,26,36,-23,47,-21,-22,-14,-11,-12,-13,56,36,61,67,67,-10,36,67,-31,-32,-33,-34,72,-25,67,67,67,67,-15,-24,-16,82,-17,]),'TIMES':([5,6,7,8,22,36,39,40,43,46,66,67,68,70,75,76,77,78,79,],[10,-18,-19,-20,27,-43,57,-45,64,-44,-37,-43,64,64,64,64,-41,-42,-38,]),'LBRACKET':([6,7,8,39,],[-18,-19,-20,58,]),'LPAREN':([9,12,20,24,25,29,30,32,33,34,35,41,44,45,48,49,51,52,53,54,55,60,62,63,64,65,71,74,80,83,],[11,15,-46,45,-23,-21,-22,-14,-11,-12,-13,45,45,45,-10,45,45,-31,-32,-33,-34,-25,45,45,45,45,-15,-24,-16,-17,]),'RPAREN':([11,13,14,15,18,21,26,40,46,47,66,67,68,75,76,77,78,79,],[-46,16,-6,-46,23,-7,-8,-45,-44,-9,-37,-43,79,-39,-40,-41,-42,-38,]),'COMMA':([11,13,14,15,18,21,26,47,],[-46,17,-6,-46,17,-7,-8,-9,]),'LBRACE':([16,20,23,24,25,29,30,32,33,34,35,48,60,71,74,80,83,],[20,-46,20,20,-23,-21,-22,-14,-11,-12,-13,-10,-25,-15,-24,-16,-17,]),'RBRACE':([20,24,25,29,30,32,33,34,35,48,60,71,74,80,83,],[-46,29,-23,-21,-22,-14,-11,-12,-13,-10,-25,-15,-24,-16,-17,]),'SEMICOLON':([20,24,25,29,30,31,32,33,34,35,36,37,38,40,41,43,46,48,50,56,59,60,61,66,67,69,70,71,72,74,75,76,77,78,79,80,82,83,],[-46,32,-23,-21,-22,48,-14,-11,-12,-13,-43,-27,-28,-45,60,-30,-44,-10,-35,71,74,-25,-36,-37,-43,-26,-29,-15,80,-24,-39,-40,-41,-42,-38,-16,83,-17,]),'RETURN':([20,24,25,29,30,32,33,34,35,48,60,71,74,80,83,],[-46,41,-23,-21,-22,-14,-11,-12,-13,-10,-25,-15,-24,-16,-17,]),'INCREMENT':([20,24,25,29,30,32,33,34,35,36,41,48,49,60,71,74,80,83,],[-46,42,-23,-21,-22,-14,-11,-12,-13,50,42,-10,42,-25,-15,-24,-16,-17,]),'MINUS':([20,24,25,29,30,32,33,34,35,36,40,41,43,44,45,46,48,49,51,52,53,54,55,60,62,63,64,65,66,67,68,70,71,74,75,76,77,78,79,80,83,],[-46,44,-23,-21,-22,-14,-11,-12,-13,-43,-45,44,63,44,44,-44,-10,44,44,-31,-32,-33,-34,-25,44,44,44,44,-37,-43,63,63,-15,-24,-39,-40,-41,-42,-38,-16,-17,]),'FNUM':([20,24,25,29,30,32,33,34,35,41,44,45,48,49,51,52,53,54,55,60,62,63,64,65,71,74,80,83,],[-46,46,-23,-21,-22,-14,-11,-12,-13,46,46,46,-10,46,46,-31,-32,-33,-34,-25,46,46,46,46,-15,-24,-16,-17,]),'INUM':([20,24,25,29,30,32,33,34,35,41,44,45,48,49,51,52,53,54,55,58,60,62,63,64,65,71,74,80,83,],[-46,40,-23,-21,-22,-14,-11,-12,-13,40,40,40,-10,40,40,-31,-32,-33,-34,73,-25,40,40,40,40,-15,-24,-16,-17,]),'EQUAL':([36,],[49,]),'PLUS':([36,40,43,46,66,67,68,70,75,76,77,78,79,],[-43,-45,62,-44,-37,-43,62,62,-39,-40,-41,-42,-38,]),'DIV':([36,40,43,46,66,67,68,70,75,76,77,78,79,],[-43,-45,65,-44,-37,-43,65,65,65,65,-41,-42,-38,]),'EQ':([36,38,40,43,46,66,67,70,75,76,77,78,79,],[-43,52,-45,-30,-44,-37,-43,-29,-39,-40,-41,-42,-38,]),'NEQ':([36,38,40,43,46,66,67,70,75,76,77,78,79,],[-43,53,-45,-30,-44,-37,-43,-29,-39,-40,-41,-42,-38,]),'GT':([36,38,40,43,46,66,67,70,75,76,77,78,79,],[-43,54,-45,-30,-44,-37,-43,-29,-39,-40,-41,-42,-38,]),'LT':([36,38,40,43,46,66,67,70,75,76,77,78,79,],[-43,55,-45,-30,-44,-37,-43,-29,-39,-40,-41,-42,-38,]),'RBRACKET':([73,],[81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'func_declaration_list':([0,],[2,]),'empty':([0,11,15,20,],[3,14,14,25,]),'func_declaration':([2,],[4,]),'type':([2,17,24,],[5,22,39,]),'param_list':([11,15,],[13,18,]),'stmt_block':([16,23,24,],[19,28,34,]),'param':([17,],[21,]),'stmt_list':([20,],[24,]),'stmt':([24,],[30,]),'expr':([24,41,49,],[31,59,69,]),'local_declaration':([24,],[33,]),'stmt_return':([24,],[35,]),'incr_expr':([24,41,49,],[37,37,37,]),'basic_expr':([24,41,49,],[38,38,38,]),'arith_expr':([24,41,44,45,49,51,62,63,64,65,],[43,43,66,68,43,70,75,76,77,78,]),'compare':([38,],[51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> func_declaration_list','program',1,'p_program','pycparser.py',16),
  ('func_declaration_list -> func_declaration_list func_declaration','func_declaration_list',2,'p_func_declaration_list_1','pycparser.py',23),
  ('func_declaration_list -> empty','func_declaration_list',1,'p_func_declaration_list_2','pycparser.py',29),
  ('func_declaration -> type ID LPAREN param_list RPAREN stmt_block','func_declaration',6,'p_func_declaration_1','pycparser.py',34),
  ('func_declaration -> type TIMES ID LPAREN param_list RPAREN stmt_block','func_declaration',7,'p_func_declaration_2','pycparser.py',40),
  ('param_list -> empty','param_list',1,'p_param_list_1','pycparser.py',46),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list_2','pycparser.py',52),
  ('param -> type ID','param',2,'p_param_1','pycparser.py',59),
  ('param -> type TIMES ID','param',3,'p_param_2','pycparser.py',65),
  ('stmt -> expr SEMICOLON','stmt',2,'p_statement','pycparser.py',72),
  ('stmt -> local_declaration','stmt',1,'p_statement','pycparser.py',73),
  ('stmt -> stmt_block','stmt',1,'p_statement','pycparser.py',74),
  ('stmt -> stmt_return','stmt',1,'p_statement','pycparser.py',75),
  ('stmt -> SEMICOLON','stmt',1,'p_statement','pycparser.py',76),
  ('local_declaration -> type ID SEMICOLON','local_declaration',3,'p_local_declaration_1','pycparser.py',86),
  ('local_declaration -> type TIMES ID SEMICOLON','local_declaration',4,'p_local_declaration_2','pycparser.py',92),
  ('local_declaration -> type LBRACKET INUM RBRACKET ID SEMICOLON','local_declaration',6,'p_local_declaration_3','pycparser.py',98),
  ('type -> INT','type',1,'p_type','pycparser.py',104),
  ('type -> FLOAT','type',1,'p_type','pycparser.py',105),
  ('type -> VOID','type',1,'p_type','pycparser.py',106),
  ('stmt_block -> LBRACE stmt_list RBRACE','stmt_block',3,'p_stmt_block','pycparser.py',112),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list_1','pycparser.py',119),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list_2','pycparser.py',126),
  ('stmt_return -> RETURN expr SEMICOLON','stmt_return',3,'p_return_stmt_1','pycparser.py',132),
  ('stmt_return -> RETURN SEMICOLON','stmt_return',2,'p_return_stmt_2','pycparser.py',138),
  ('expr -> ID EQUAL expr','expr',3,'p_expr_assign','pycparser.py',145),
  ('expr -> incr_expr','expr',1,'p_expr_incr','pycparser.py',153),
  ('expr -> basic_expr','expr',1,'p_expr_basic','pycparser.py',159),
  ('basic_expr -> basic_expr compare arith_expr','basic_expr',3,'p_basic_expr_compare','pycparser.py',165),
  ('basic_expr -> arith_expr','basic_expr',1,'p_basic_expr_arith_expr','pycparser.py',180),
  ('compare -> EQ','compare',1,'p_compare','pycparser.py',186),
  ('compare -> NEQ','compare',1,'p_compare','pycparser.py',187),
  ('compare -> GT','compare',1,'p_compare','pycparser.py',188),
  ('compare -> LT','compare',1,'p_compare','pycparser.py',189),
  ('incr_expr -> ID INCREMENT','incr_expr',2,'p_incr_expr_1','pycparser.py',195),
  ('incr_expr -> INCREMENT ID','incr_expr',2,'p_incr_expr_2','pycparser.py',204),
  ('arith_expr -> MINUS arith_expr','arith_expr',2,'p_arith_uminus','pycparser.py',214),
  ('arith_expr -> LPAREN arith_expr RPAREN','arith_expr',3,'p_arith_parens','pycparser.py',221),
  ('arith_expr -> arith_expr PLUS arith_expr','arith_expr',3,'p_arith_add','pycparser.py',227),
  ('arith_expr -> arith_expr MINUS arith_expr','arith_expr',3,'p_arith_sub','pycparser.py',237),
  ('arith_expr -> arith_expr TIMES arith_expr','arith_expr',3,'p_arith_mult','pycparser.py',246),
  ('arith_expr -> arith_expr DIV arith_expr','arith_expr',3,'p_arith_div','pycparser.py',255),
  ('arith_expr -> ID','arith_expr',1,'p_arith_id','pycparser.py',268),
  ('arith_expr -> FNUM','arith_expr',1,'p_arith_fnum','pycparser.py',277),
  ('arith_expr -> INUM','arith_expr',1,'p_arith_inum','pycparser.py',285),
  ('empty -> <empty>','empty',0,'p_empty','pycparser.py',293),
]
