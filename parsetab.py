
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVrightUMINUSCOLON COMMA DIV DOUBLEQUOTE ELSE ELSE_IF EQ EQUAL FLOAT FNUM FOR GT ID IF INCREMENT INT INUM LBRACE LBRACKET LPAREN LT MAIN MINUS NEQ PERIOD PLUS POINTER PRINT QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES VOIDprogram : func_declaration_listfunc_declaration_list : func_declaration_list func_declarationfunc_declaration_list : emptyfunc_declaration : type ID LPAREN arg_list RPAREN stmt_blockarg_list : emptyarg_list : arg_list COMMA argarg : type IDstmt : expr SEMICOLON\n            | local_declaration\n            | stmt_block\n            | stmt_return\n            | SEMICOLONlocal_declaration : type ID SEMICOLON\n                   | type TIMES ID SEMICOLON\n                   | type TIMES LBRACKET RBRACKET SEMICOLONtype : INT\n            | FLOAT\n            | VOIDstmt_block : LBRACE stmt_list RBRACEstmt_list : stmt_list stmt\n                 | emptyexpr : ID EQUAL exprexpr : basic_exprstmt_return : RETURN expr SEMICOLONstmt_return : RETURN SEMICOLONbasic_expr : basic_expr compare arith_exprbasic_expr : arith_exprcompare : EQ\n               | NEQ\n               | GT\n               | LTarith_expr : MINUS arith_expr %prec UMINUSarith_expr : LPAREN arith_expr RPARENarith_expr : arith_expr PLUS arith_exprarith_expr : arith_expr MINUS arith_exprarith_expr : arith_expr TIMES arith_exprarith_expr : arith_expr DIV arith_exprarith_expr : IDarith_expr : FNUMarith_expr : INUMempty :'
    
_lr_action_items = {'INT':([0,2,3,4,14,15,16,19,20,22,23,25,26,27,28,38,48,58,61,67,69,],[-41,6,-3,-2,6,-4,-41,6,-21,-19,-20,-12,-9,-10,-11,-8,-25,-13,-24,-14,-15,]),'FLOAT':([0,2,3,4,14,15,16,19,20,22,23,25,26,27,28,38,48,58,61,67,69,],[-41,7,-3,-2,7,-4,-41,7,-21,-19,-20,-12,-9,-10,-11,-8,-25,-13,-24,-14,-15,]),'VOID':([0,2,3,4,14,15,16,19,20,22,23,25,26,27,28,38,48,58,61,67,69,],[-41,8,-3,-2,8,-4,-41,8,-21,-19,-20,-12,-9,-10,-11,-8,-25,-13,-24,-14,-15,]),'$end':([0,1,2,3,4,15,22,],[-41,0,-1,-3,-2,-4,-19,]),'ID':([5,6,7,8,16,18,19,20,22,23,25,26,27,28,31,32,34,35,38,39,40,41,42,43,44,46,48,49,50,51,52,58,61,67,69,],[9,-16,-17,-18,-41,21,29,-21,-19,-20,-12,-9,-10,-11,45,29,54,54,-8,29,54,-28,-29,-30,-31,59,-25,54,54,54,54,-13,-24,-14,-15,]),'TIMES':([6,7,8,29,31,33,36,37,53,54,55,57,62,63,64,65,66,],[-16,-17,-18,-38,46,51,-39,-40,-32,-38,51,51,51,51,-36,-37,-33,]),'LPAREN':([9,16,19,20,22,23,25,26,27,28,32,34,35,38,39,40,41,42,43,44,48,49,50,51,52,58,61,67,69,],[10,-41,35,-21,-19,-20,-12,-9,-10,-11,35,35,35,-8,35,35,-28,-29,-30,-31,-25,35,35,35,35,-13,-24,-14,-15,]),'RPAREN':([10,11,12,17,21,36,37,53,54,55,62,63,64,65,66,],[-41,13,-5,-6,-7,-39,-40,-32,-38,66,-34,-35,-36,-37,-33,]),'COMMA':([10,11,12,17,21,],[-41,14,-5,-6,-7,]),'LBRACE':([13,16,19,20,22,23,25,26,27,28,38,48,58,61,67,69,],[16,-41,16,-21,-19,-20,-12,-9,-10,-11,-8,-25,-13,-24,-14,-15,]),'RBRACE':([16,19,20,22,23,25,26,27,28,38,48,58,61,67,69,],[-41,22,-21,-19,-20,-12,-9,-10,-11,-8,-25,-13,-24,-14,-15,]),'SEMICOLON':([16,19,20,22,23,24,25,26,27,28,29,30,32,33,36,37,38,45,47,48,53,54,56,57,58,59,61,62,63,64,65,66,67,68,69,],[-41,25,-21,-19,-20,38,-12,-9,-10,-11,-38,-23,48,-27,-39,-40,-8,58,61,-25,-32,-38,-22,-26,-13,67,-24,-34,-35,-36,-37,-33,-14,69,-15,]),'RETURN':([16,19,20,22,23,25,26,27,28,38,48,58,61,67,69,],[-41,32,-21,-19,-20,-12,-9,-10,-11,-8,-25,-13,-24,-14,-15,]),'MINUS':([16,19,20,22,23,25,26,27,28,29,32,33,34,35,36,37,38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,57,58,61,62,63,64,65,66,67,69,],[-41,34,-21,-19,-20,-12,-9,-10,-11,-38,34,50,34,34,-39,-40,-8,34,34,-28,-29,-30,-31,-25,34,34,34,34,-32,-38,50,50,-13,-24,-34,-35,-36,-37,-33,-14,-15,]),'FNUM':([16,19,20,22,23,25,26,27,28,32,34,35,38,39,40,41,42,43,44,48,49,50,51,52,58,61,67,69,],[-41,36,-21,-19,-20,-12,-9,-10,-11,36,36,36,-8,36,36,-28,-29,-30,-31,-25,36,36,36,36,-13,-24,-14,-15,]),'INUM':([16,19,20,22,23,25,26,27,28,32,34,35,38,39,40,41,42,43,44,48,49,50,51,52,58,61,67,69,],[-41,37,-21,-19,-20,-12,-9,-10,-11,37,37,37,-8,37,37,-28,-29,-30,-31,-25,37,37,37,37,-13,-24,-14,-15,]),'EQUAL':([29,],[39,]),'PLUS':([29,33,36,37,53,54,55,57,62,63,64,65,66,],[-38,49,-39,-40,-32,-38,49,49,-34,-35,-36,-37,-33,]),'DIV':([29,33,36,37,53,54,55,57,62,63,64,65,66,],[-38,52,-39,-40,-32,-38,52,52,52,52,-36,-37,-33,]),'EQ':([29,30,33,36,37,53,54,57,62,63,64,65,66,],[-38,41,-27,-39,-40,-32,-38,-26,-34,-35,-36,-37,-33,]),'NEQ':([29,30,33,36,37,53,54,57,62,63,64,65,66,],[-38,42,-27,-39,-40,-32,-38,-26,-34,-35,-36,-37,-33,]),'GT':([29,30,33,36,37,53,54,57,62,63,64,65,66,],[-38,43,-27,-39,-40,-32,-38,-26,-34,-35,-36,-37,-33,]),'LT':([29,30,33,36,37,53,54,57,62,63,64,65,66,],[-38,44,-27,-39,-40,-32,-38,-26,-34,-35,-36,-37,-33,]),'LBRACKET':([46,],[60,]),'RBRACKET':([60,],[68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'func_declaration_list':([0,],[2,]),'empty':([0,10,16,],[3,12,20,]),'func_declaration':([2,],[4,]),'type':([2,14,19,],[5,18,31,]),'arg_list':([10,],[11,]),'stmt_block':([13,19,],[15,27,]),'arg':([14,],[17,]),'stmt_list':([16,],[19,]),'stmt':([19,],[23,]),'expr':([19,32,39,],[24,47,56,]),'local_declaration':([19,],[26,]),'stmt_return':([19,],[28,]),'basic_expr':([19,32,39,],[30,30,30,]),'arith_expr':([19,32,34,35,39,40,49,50,51,52,],[33,33,53,55,33,57,62,63,64,65,]),'compare':([30,],[40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> func_declaration_list','program',1,'p_program','pycparser.py',12),
  ('func_declaration_list -> func_declaration_list func_declaration','func_declaration_list',2,'p_func_declaration_list_1','pycparser.py',16),
  ('func_declaration_list -> empty','func_declaration_list',1,'p_func_declaration_list_2','pycparser.py',19),
  ('func_declaration -> type ID LPAREN arg_list RPAREN stmt_block','func_declaration',6,'p_func_declaration','pycparser.py',23),
  ('arg_list -> empty','arg_list',1,'p_arg_list_1','pycparser.py',27),
  ('arg_list -> arg_list COMMA arg','arg_list',3,'p_arg_list_2','pycparser.py',30),
  ('arg -> type ID','arg',2,'p_arg','pycparser.py',33),
  ('stmt -> expr SEMICOLON','stmt',2,'p_statement','pycparser.py',37),
  ('stmt -> local_declaration','stmt',1,'p_statement','pycparser.py',38),
  ('stmt -> stmt_block','stmt',1,'p_statement','pycparser.py',39),
  ('stmt -> stmt_return','stmt',1,'p_statement','pycparser.py',40),
  ('stmt -> SEMICOLON','stmt',1,'p_statement','pycparser.py',41),
  ('local_declaration -> type ID SEMICOLON','local_declaration',3,'p_local_declaration','pycparser.py',47),
  ('local_declaration -> type TIMES ID SEMICOLON','local_declaration',4,'p_local_declaration','pycparser.py',48),
  ('local_declaration -> type TIMES LBRACKET RBRACKET SEMICOLON','local_declaration',5,'p_local_declaration','pycparser.py',49),
  ('type -> INT','type',1,'p_type','pycparser.py',53),
  ('type -> FLOAT','type',1,'p_type','pycparser.py',54),
  ('type -> VOID','type',1,'p_type','pycparser.py',55),
  ('stmt_block -> LBRACE stmt_list RBRACE','stmt_block',3,'p_stmt_block','pycparser.py',58),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','pycparser.py',62),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list','pycparser.py',63),
  ('expr -> ID EQUAL expr','expr',3,'p_expr_assign','pycparser.py',67),
  ('expr -> basic_expr','expr',1,'p_expr_basic','pycparser.py',71),
  ('stmt_return -> RETURN expr SEMICOLON','stmt_return',3,'p_return_stmt_1','pycparser.py',81),
  ('stmt_return -> RETURN SEMICOLON','stmt_return',2,'p_return_stmt_2','pycparser.py',84),
  ('basic_expr -> basic_expr compare arith_expr','basic_expr',3,'p_basic_expr_compare','pycparser.py',87),
  ('basic_expr -> arith_expr','basic_expr',1,'p_basic_expr_arith_expr','pycparser.py',98),
  ('compare -> EQ','compare',1,'p_compare','pycparser.py',102),
  ('compare -> NEQ','compare',1,'p_compare','pycparser.py',103),
  ('compare -> GT','compare',1,'p_compare','pycparser.py',104),
  ('compare -> LT','compare',1,'p_compare','pycparser.py',105),
  ('arith_expr -> MINUS arith_expr','arith_expr',2,'p_arith_uminus','pycparser.py',109),
  ('arith_expr -> LPAREN arith_expr RPAREN','arith_expr',3,'p_arith_parens','pycparser.py',113),
  ('arith_expr -> arith_expr PLUS arith_expr','arith_expr',3,'p_arith_add','pycparser.py',117),
  ('arith_expr -> arith_expr MINUS arith_expr','arith_expr',3,'p_arith_sub','pycparser.py',122),
  ('arith_expr -> arith_expr TIMES arith_expr','arith_expr',3,'p_arith_mult','pycparser.py',127),
  ('arith_expr -> arith_expr DIV arith_expr','arith_expr',3,'p_arith_div','pycparser.py',132),
  ('arith_expr -> ID','arith_expr',1,'p_arith_id','pycparser.py',140),
  ('arith_expr -> FNUM','arith_expr',1,'p_arith_fnum','pycparser.py',144),
  ('arith_expr -> INUM','arith_expr',1,'p_arith_inum','pycparser.py',148),
  ('empty -> <empty>','empty',0,'p_empty','pycparser.py',152),
]
