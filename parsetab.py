
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVrightUMINUSADDRESS COLON COMMA DIV DOUBLEQUOTE ELSE ELSE_IF EQ EQUAL FLOAT FNUM FOR GT ID IF INCREMENT INT INUM LBRACE LBRACKET LITERAL LPAREN LT MAIN MINUS NEQ PERIOD PLUS POINTER PRINT QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON TIMES VOIDprogram : declaration_listdeclaration_list : declaration_list func_declarationdeclaration_list : declaration_list declarationdeclaration_list : emptyfunc_declaration : type ID LPAREN params RPAREN stmt_blockfunc_declaration : type TIMES ID LPAREN params RPAREN stmt_blockfunc_declaration : type MAIN LPAREN params RPAREN stmt_blockparams : VOIDparams : param_listparam_list : paramparam_list : param_list COMMA paramparam : type IDparam : type TIMES IDgenstmt : mstmt\n                | umstmtmstmt : IF LPAREN expr RPAREN mstmt ELSE mstmt\n                | stmtumstmt : IF LPAREN expr RPAREN genstmt\n                | IF LPAREN expr RPAREN mstmt ELSE umstmtstmt : expr SEMICOLON\n            | declaration SEMICOLON\n            | stmt_block\n            | stmt_forloop\n            | stmt_return\n            | SEMICOLONstmt : expr errorstmt : PRINT LPAREN argument_list RPARENdeclaration : type id_listid_list : idbracketid_list : id_list COMMA idbracketidbracket : IDidbracket : ID LBRACKET INUM RBRACKETidbracket : TIMES IDtype : INT\n            | FLOAT\n            | VOIDstmt_block : LBRACE stmt_list RBRACEstmt_list : stmt_list genstmtstmt_list : emptystmt_forloop : FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN stmtstmt_return : RETURN expr SEMICOLONstmt_return : RETURN SEMICOLONexpr : ID EQUAL exprexpr : ID LBRACKET arith_expr RBRACKET EQUAL exprexpr : TIMES ID EQUAL exprexpr : incr_exprexpr : basic_exprbasic_expr : basic_expr compare arith_exprbasic_expr : arith_exprcompare : EQ\n               | NEQ\n               | GT\n               | LTincr_expr : ID INCREMENTincr_expr : INCREMENT IDarith_expr : MINUS arith_expr %prec UMINUSarith_expr : LPAREN arith_expr RPARENarith_expr : arith_expr PLUS arith_exprarith_expr : arith_expr MINUS arith_exprarith_expr : arith_expr TIMES arith_exprarith_expr : arith_expr DIV arith_exprarith_expr : IDarith_expr : FNUMarith_expr : INUMarith_expr : TIMES IDarith_expr : ADDRESS IDarith_expr : ID LBRACKET arith_expr RBRACKETarith_expr : ID LPAREN argument_list RPARENargument_list : argumentargument_list : argument_list COMMA argumentargument : emptyargument : arith_exprargument : LITERALargument : errorempty :'
    
_lr_action_items = {'INT':([0,2,3,4,5,10,13,14,15,17,18,26,28,29,34,35,38,40,41,44,45,46,47,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[-75,7,-4,-2,-3,-31,-28,-29,7,-33,7,7,-30,-31,7,-32,-33,-5,-75,-7,7,-39,-6,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,7,-27,-14,-18,7,-16,-19,7,-40,]),'FLOAT':([0,2,3,4,5,10,13,14,15,17,18,26,28,29,34,35,38,40,41,44,45,46,47,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[-75,8,-4,-2,-3,-31,-28,-29,8,-33,8,8,-30,-31,8,-32,-33,-5,-75,-7,8,-39,-6,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,8,-27,-14,-18,8,-16,-19,8,-40,]),'VOID':([0,2,3,4,5,10,13,14,15,17,18,26,28,29,34,35,38,40,41,44,45,46,47,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[-75,9,-4,-2,-3,-31,-28,-29,22,-33,22,22,-30,-31,9,-32,-33,-5,-75,-7,9,-39,-6,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,9,-27,-14,-18,9,-16,-19,9,-40,]),'$end':([0,1,2,3,4,5,10,13,14,17,28,29,35,38,40,44,47,48,],[-75,0,-1,-4,-2,-3,-31,-28,-29,-33,-30,-31,-32,-33,-5,-7,-6,-37,]),'ID':([6,7,8,9,11,19,20,22,30,32,41,45,46,48,49,50,51,53,55,56,58,59,60,64,67,69,70,71,74,75,77,79,80,81,82,83,84,86,87,88,89,90,92,93,94,95,96,97,99,106,120,123,124,126,127,131,132,133,136,138,140,141,142,144,145,],[10,-34,-35,-36,17,29,31,-36,38,39,-75,62,-39,-37,-38,-14,-15,78,-17,-25,-22,-23,-24,91,29,62,100,78,102,62,105,-20,-26,-21,78,62,78,78,78,78,78,78,78,-50,-51,-52,-53,62,-42,78,62,-41,62,-27,78,62,-14,-18,62,62,62,-16,-19,62,-40,]),'TIMES':([6,7,8,9,19,20,22,41,45,46,48,49,50,51,53,55,56,58,59,60,62,63,67,69,71,72,73,75,76,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,97,99,101,102,104,105,106,110,114,116,117,118,119,120,121,123,124,125,126,127,128,129,131,132,133,134,136,138,140,141,142,144,145,],[11,-34,-35,-36,30,32,-36,-75,64,-39,-37,-38,-14,-15,77,-17,-25,-22,-23,-24,-62,89,30,64,77,-63,-64,64,89,-62,-20,-26,-21,77,64,77,77,77,77,77,77,-65,77,-50,-51,-52,-53,64,-42,-56,-66,-57,-65,77,89,89,89,89,-60,-61,64,89,-41,64,89,-27,77,-67,-68,64,-14,-18,-67,64,64,64,-16,-19,64,-40,]),'MAIN':([6,7,8,9,],[12,-34,-35,-36,]),'LPAREN':([10,12,17,41,45,46,48,49,50,51,52,53,55,56,58,59,60,61,62,68,69,71,75,78,79,80,81,82,83,84,86,87,88,89,90,92,93,94,95,96,97,99,106,120,123,124,126,127,131,132,133,136,138,140,141,142,144,145,],[15,18,26,-75,53,-39,-37,-38,-14,-15,75,53,-17,-25,-22,-23,-24,82,86,97,53,53,53,86,-20,-26,-21,53,53,53,53,53,53,53,53,53,-50,-51,-52,-53,53,-42,53,53,-41,53,-27,53,53,-14,-18,53,53,53,-16,-19,53,-40,]),'COMMA':([10,13,14,17,23,24,28,29,31,35,38,39,42,72,73,78,82,86,101,102,104,105,107,108,109,110,111,112,115,116,117,118,119,127,129,134,135,],[-31,19,-29,-33,34,-10,-30,-31,-12,-32,-33,-13,-11,-63,-64,-62,-75,-75,-56,-66,-57,-65,127,-69,-71,-72,-73,-74,127,-58,-59,-60,-61,-75,-68,-67,-70,]),'LBRACKET':([10,29,62,78,],[16,16,84,106,]),'SEMICOLON':([13,14,28,29,35,38,41,45,46,48,49,50,51,54,55,56,57,58,59,60,62,63,65,66,69,72,73,78,79,80,81,85,91,98,99,100,101,102,104,105,113,116,117,118,119,121,122,123,124,126,128,129,130,132,133,134,137,138,139,141,142,144,145,],[-28,-29,-30,-31,-32,-33,-75,56,-39,-37,-38,-14,-15,79,-17,-25,81,-22,-23,-24,-62,-49,-46,-47,99,-63,-64,-62,-20,-26,-21,-54,-65,123,-42,-55,-56,-66,-57,-65,-43,-58,-59,-60,-61,-48,131,-41,56,-27,-67,-68,-45,-14,-18,-67,140,56,-44,-16,-19,56,-40,]),'INUM':([16,41,45,46,48,49,50,51,53,55,56,58,59,60,69,71,75,79,80,81,82,83,84,86,87,88,89,90,92,93,94,95,96,97,99,106,120,123,124,126,127,131,132,133,136,138,140,141,142,144,145,],[25,-75,73,-39,-37,-38,-14,-15,73,-17,-25,-22,-23,-24,73,73,73,-20,-26,-21,73,73,73,73,73,73,73,73,73,-50,-51,-52,-53,73,-42,73,73,-41,73,-27,73,73,-14,-18,73,73,73,-16,-19,73,-40,]),'RPAREN':([21,22,23,24,27,31,36,39,42,62,63,65,66,72,73,76,78,82,85,86,91,100,101,102,103,104,105,107,108,109,110,111,112,113,115,116,117,118,119,121,127,128,129,130,134,135,139,143,],[33,-8,-9,-10,37,-12,43,-13,-11,-62,-49,-46,-47,-63,-64,104,-62,-75,-54,-75,-65,-55,-56,-66,124,-57,-65,126,-69,-71,-72,-73,-74,-43,129,-58,-59,-60,-61,-48,-75,-67,-68,-45,-67,-70,-44,144,]),'RBRACKET':([25,72,73,78,101,102,104,105,114,116,117,118,119,125,129,134,],[35,-63,-64,-62,-56,-66,-57,-65,128,-58,-59,-60,-61,134,-68,-67,]),'LBRACE':([33,37,41,43,45,46,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[41,41,-75,41,41,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,41,-27,-14,-18,41,-16,-19,41,-40,]),'RBRACE':([41,45,46,48,49,50,51,55,56,58,59,60,79,80,81,99,123,126,132,133,141,142,145,],[-75,48,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,-27,-14,-18,-16,-19,-40,]),'IF':([41,45,46,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,145,],[-75,52,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,52,-27,-14,-18,52,-16,-19,-40,]),'PRINT':([41,45,46,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[-75,61,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,61,-27,-14,-18,61,-16,-19,61,-40,]),'FOR':([41,45,46,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[-75,68,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,68,-27,-14,-18,68,-16,-19,68,-40,]),'RETURN':([41,45,46,48,49,50,51,55,56,58,59,60,79,80,81,99,123,124,126,132,133,138,141,142,144,145,],[-75,69,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,69,-27,-14,-18,69,-16,-19,69,-40,]),'INCREMENT':([41,45,46,48,49,50,51,55,56,58,59,60,62,69,75,79,80,81,83,97,99,120,123,124,126,131,132,133,136,138,140,141,142,144,145,],[-75,70,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,85,70,70,-20,-26,-21,70,70,-42,70,-41,70,-27,70,-14,-18,70,70,70,-16,-19,70,-40,]),'MINUS':([41,45,46,48,49,50,51,53,55,56,58,59,60,62,63,69,71,72,73,75,76,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,95,96,97,99,101,102,104,105,106,110,114,116,117,118,119,120,121,123,124,125,126,127,128,129,131,132,133,134,136,138,140,141,142,144,145,],[-75,71,-39,-37,-38,-14,-15,71,-17,-25,-22,-23,-24,-62,88,71,71,-63,-64,71,88,-62,-20,-26,-21,71,71,71,71,71,71,71,71,-65,71,-50,-51,-52,-53,71,-42,-56,-66,-57,-65,71,88,88,-58,-59,-60,-61,71,88,-41,71,88,-27,71,-67,-68,71,-14,-18,-67,71,71,71,-16,-19,71,-40,]),'FNUM':([41,45,46,48,49,50,51,53,55,56,58,59,60,69,71,75,79,80,81,82,83,84,86,87,88,89,90,92,93,94,95,96,97,99,106,120,123,124,126,127,131,132,133,136,138,140,141,142,144,145,],[-75,72,-39,-37,-38,-14,-15,72,-17,-25,-22,-23,-24,72,72,72,-20,-26,-21,72,72,72,72,72,72,72,72,72,-50,-51,-52,-53,72,-42,72,72,-41,72,-27,72,72,-14,-18,72,72,72,-16,-19,72,-40,]),'ADDRESS':([41,45,46,48,49,50,51,53,55,56,58,59,60,69,71,75,79,80,81,82,83,84,86,87,88,89,90,92,93,94,95,96,97,99,106,120,123,124,126,127,131,132,133,136,138,140,141,142,144,145,],[-75,74,-39,-37,-38,-14,-15,74,-17,-25,-22,-23,-24,74,74,74,-20,-26,-21,74,74,74,74,74,74,74,74,74,-50,-51,-52,-53,74,-42,74,74,-41,74,-27,74,74,-14,-18,74,74,74,-16,-19,74,-40,]),'ELSE':([48,55,56,58,59,60,79,80,81,99,123,126,132,141,145,],[-37,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,-27,138,-16,-40,]),'error':([54,62,63,65,66,72,73,78,82,85,86,91,100,101,102,104,105,113,116,117,118,119,121,127,128,129,130,134,139,],[80,-62,-49,-46,-47,-63,-64,-62,112,-54,112,-65,-55,-56,-66,-57,-65,-43,-58,-59,-60,-61,-48,112,-67,-68,-45,-67,-44,]),'EQUAL':([62,91,128,],[83,120,136,]),'PLUS':([62,63,72,73,76,78,91,101,102,104,105,110,114,116,117,118,119,121,125,128,129,134,],[-62,87,-63,-64,87,-62,-65,-56,-66,-57,-65,87,87,-58,-59,-60,-61,87,87,-67,-68,-67,]),'DIV':([62,63,72,73,76,78,91,101,102,104,105,110,114,116,117,118,119,121,125,128,129,134,],[-62,90,-63,-64,90,-62,-65,-56,-66,-57,-65,90,90,90,90,-60,-61,90,90,-67,-68,-67,]),'EQ':([62,63,66,72,73,78,91,101,102,104,105,116,117,118,119,121,128,129,134,],[-62,-49,93,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-68,-67,]),'NEQ':([62,63,66,72,73,78,91,101,102,104,105,116,117,118,119,121,128,129,134,],[-62,-49,94,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-68,-67,]),'GT':([62,63,66,72,73,78,91,101,102,104,105,116,117,118,119,121,128,129,134,],[-62,-49,95,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-68,-67,]),'LT':([62,63,66,72,73,78,91,101,102,104,105,116,117,118,119,121,128,129,134,],[-62,-49,96,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-68,-67,]),'LITERAL':([82,86,127,],[111,111,111,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'empty':([0,41,82,86,127,],[3,46,109,109,109,]),'func_declaration':([2,],[4,]),'declaration':([2,45,124,138,144,],[5,57,57,57,57,]),'type':([2,15,18,26,34,45,124,138,144,],[6,20,20,20,20,67,67,67,67,]),'id_list':([6,67,],[13,13,]),'idbracket':([6,19,67,],[14,28,14,]),'params':([15,18,26,],[21,27,36,]),'param_list':([15,18,26,],[23,23,23,]),'param':([15,18,26,34,],[24,24,24,42,]),'stmt_block':([33,37,43,45,124,138,144,],[40,44,47,58,58,58,58,]),'stmt_list':([41,],[45,]),'genstmt':([45,124,],[49,133,]),'mstmt':([45,124,138,],[50,132,141,]),'umstmt':([45,124,138,],[51,51,142,]),'expr':([45,69,75,83,97,120,124,131,136,138,140,144,],[54,98,103,113,122,130,54,137,139,54,143,54,]),'stmt':([45,124,138,144,],[55,55,55,145,]),'stmt_forloop':([45,124,138,144,],[59,59,59,59,]),'stmt_return':([45,124,138,144,],[60,60,60,60,]),'arith_expr':([45,53,69,71,75,82,83,84,86,87,88,89,90,92,97,106,120,124,127,131,136,138,140,144,],[63,76,63,101,63,110,63,114,110,116,117,118,119,121,63,125,63,63,110,63,63,63,63,63,]),'incr_expr':([45,69,75,83,97,120,124,131,136,138,140,144,],[65,65,65,65,65,65,65,65,65,65,65,65,]),'basic_expr':([45,69,75,83,97,120,124,131,136,138,140,144,],[66,66,66,66,66,66,66,66,66,66,66,66,]),'compare':([66,],[92,]),'argument_list':([82,86,],[107,115,]),'argument':([82,86,127,],[108,108,135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','pycparser.py',24),
  ('declaration_list -> declaration_list func_declaration','declaration_list',2,'p_declaration_list_1','pycparser.py',34),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list_2','pycparser.py',41),
  ('declaration_list -> empty','declaration_list',1,'p_declaration_list_3','pycparser.py',47),
  ('func_declaration -> type ID LPAREN params RPAREN stmt_block','func_declaration',6,'p_func_declaration_1','pycparser.py',58),
  ('func_declaration -> type TIMES ID LPAREN params RPAREN stmt_block','func_declaration',7,'p_func_declaration_2','pycparser.py',64),
  ('func_declaration -> type MAIN LPAREN params RPAREN stmt_block','func_declaration',6,'p_func_declaration_3','pycparser.py',70),
  ('params -> VOID','params',1,'p_params_1','pycparser.py',81),
  ('params -> param_list','params',1,'p_params_2','pycparser.py',86),
  ('param_list -> param','param_list',1,'p_param_list_1','pycparser.py',91),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list_2','pycparser.py',98),
  ('param -> type ID','param',2,'p_param_1','pycparser.py',111),
  ('param -> type TIMES ID','param',3,'p_param_2','pycparser.py',117),
  ('genstmt -> mstmt','genstmt',1,'p_general_statement','pycparser.py',128),
  ('genstmt -> umstmt','genstmt',1,'p_general_statement','pycparser.py',129),
  ('mstmt -> IF LPAREN expr RPAREN mstmt ELSE mstmt','mstmt',7,'p_matched_statement','pycparser.py',134),
  ('mstmt -> stmt','mstmt',1,'p_matched_statement','pycparser.py',135),
  ('umstmt -> IF LPAREN expr RPAREN genstmt','umstmt',5,'p_unmatched_statement','pycparser.py',141),
  ('umstmt -> IF LPAREN expr RPAREN mstmt ELSE umstmt','umstmt',7,'p_unmatched_statement','pycparser.py',142),
  ('stmt -> expr SEMICOLON','stmt',2,'p_statement','pycparser.py',158),
  ('stmt -> declaration SEMICOLON','stmt',2,'p_statement','pycparser.py',159),
  ('stmt -> stmt_block','stmt',1,'p_statement','pycparser.py',160),
  ('stmt -> stmt_forloop','stmt',1,'p_statement','pycparser.py',161),
  ('stmt -> stmt_return','stmt',1,'p_statement','pycparser.py',162),
  ('stmt -> SEMICOLON','stmt',1,'p_statement','pycparser.py',163),
  ('stmt -> expr error','stmt',2,'p_statement_error_1','pycparser.py',172),
  ('stmt -> PRINT LPAREN argument_list RPAREN','stmt',4,'p_stmt_printf','pycparser.py',185),
  ('declaration -> type id_list','declaration',2,'p_declaration_1','pycparser.py',196),
  ('id_list -> idbracket','id_list',1,'p_id_list_1','pycparser.py',214),
  ('id_list -> id_list COMMA idbracket','id_list',3,'p_id_list_2','pycparser.py',219),
  ('idbracket -> ID','idbracket',1,'p_id_bracket_1','pycparser.py',225),
  ('idbracket -> ID LBRACKET INUM RBRACKET','idbracket',4,'p_id_bracket_2','pycparser.py',230),
  ('idbracket -> TIMES ID','idbracket',2,'p_id_bracket_3','pycparser.py',235),
  ('type -> INT','type',1,'p_type','pycparser.py',242),
  ('type -> FLOAT','type',1,'p_type','pycparser.py',243),
  ('type -> VOID','type',1,'p_type','pycparser.py',244),
  ('stmt_block -> LBRACE stmt_list RBRACE','stmt_block',3,'p_stmt_block','pycparser.py',255),
  ('stmt_list -> stmt_list genstmt','stmt_list',2,'p_stmt_list_1','pycparser.py',266),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list_2','pycparser.py',273),
  ('stmt_forloop -> FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN stmt','stmt_forloop',9,'p_forloop','pycparser.py',282),
  ('stmt_return -> RETURN expr SEMICOLON','stmt_return',3,'p_return_stmt_1','pycparser.py',295),
  ('stmt_return -> RETURN SEMICOLON','stmt_return',2,'p_return_stmt_2','pycparser.py',301),
  ('expr -> ID EQUAL expr','expr',3,'p_expr_assign_1','pycparser.py',315),
  ('expr -> ID LBRACKET arith_expr RBRACKET EQUAL expr','expr',6,'p_expr_assign_2','pycparser.py',323),
  ('expr -> TIMES ID EQUAL expr','expr',4,'p_expr_assign_3','pycparser.py',328),
  ('expr -> incr_expr','expr',1,'p_expr_incr','pycparser.py',333),
  ('expr -> basic_expr','expr',1,'p_expr_basic','pycparser.py',340),
  ('basic_expr -> basic_expr compare arith_expr','basic_expr',3,'p_basic_expr_compare','pycparser.py',346),
  ('basic_expr -> arith_expr','basic_expr',1,'p_basic_expr_arith_expr','pycparser.py',361),
  ('compare -> EQ','compare',1,'p_compare','pycparser.py',367),
  ('compare -> NEQ','compare',1,'p_compare','pycparser.py',368),
  ('compare -> GT','compare',1,'p_compare','pycparser.py',369),
  ('compare -> LT','compare',1,'p_compare','pycparser.py',370),
  ('incr_expr -> ID INCREMENT','incr_expr',2,'p_incr_expr_1','pycparser.py',379),
  ('incr_expr -> INCREMENT ID','incr_expr',2,'p_incr_expr_2','pycparser.py',388),
  ('arith_expr -> MINUS arith_expr','arith_expr',2,'p_arith_uminus','pycparser.py',401),
  ('arith_expr -> LPAREN arith_expr RPAREN','arith_expr',3,'p_arith_parens','pycparser.py',408),
  ('arith_expr -> arith_expr PLUS arith_expr','arith_expr',3,'p_arith_add','pycparser.py',420),
  ('arith_expr -> arith_expr MINUS arith_expr','arith_expr',3,'p_arith_sub','pycparser.py',430),
  ('arith_expr -> arith_expr TIMES arith_expr','arith_expr',3,'p_arith_mult','pycparser.py',439),
  ('arith_expr -> arith_expr DIV arith_expr','arith_expr',3,'p_arith_div','pycparser.py',448),
  ('arith_expr -> ID','arith_expr',1,'p_arith_id','pycparser.py',462),
  ('arith_expr -> FNUM','arith_expr',1,'p_arith_fnum','pycparser.py',471),
  ('arith_expr -> INUM','arith_expr',1,'p_arith_inum','pycparser.py',479),
  ('arith_expr -> TIMES ID','arith_expr',2,'p_arith_pointer','pycparser.py',488),
  ('arith_expr -> ADDRESS ID','arith_expr',2,'p_arith_address','pycparser.py',493),
  ('arith_expr -> ID LBRACKET arith_expr RBRACKET','arith_expr',4,'p_arith_array_index','pycparser.py',498),
  ('arith_expr -> ID LPAREN argument_list RPAREN','arith_expr',4,'p_arith_functioncall','pycparser.py',504),
  ('argument_list -> argument','argument_list',1,'p_argument_list_1','pycparser.py',523),
  ('argument_list -> argument_list COMMA argument','argument_list',3,'p_argument_list_2','pycparser.py',530),
  ('argument -> empty','argument',1,'p_argument_1','pycparser.py',536),
  ('argument -> arith_expr','argument',1,'p_argument_2','pycparser.py',541),
  ('argument -> LITERAL','argument',1,'p_argument_3','pycparser.py',547),
  ('argument -> error','argument',1,'p_argument_error','pycparser.py',553),
  ('empty -> <empty>','empty',0,'p_empty','pycparser.py',559),
]
