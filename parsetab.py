
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVrightUMINUSADDRESS COLON COMMA DIV DOUBLEQUOTE ELSE ELSE_IF EQ EQUAL FLOAT FNUM FOR GT ID IF INCREMENT INT INUM LBRACE LBRACKET LITERAL LPAREN LT MAIN MINUS NEQ PERIOD PLUS POINTER PRINT QUOTE RBRACE RBRACKET RETURN RPAREN SEMICOLON TIMES VOIDprogram : declaration_listdeclaration_list : declaration_list func_declarationdeclaration_list : declaration_list declaration SEMICOLONdeclaration_list : emptyfunc_declaration : type ID LPAREN params RPAREN stmt_blockfunc_declaration : type TIMES ID LPAREN params RPAREN stmt_blockfunc_declaration : type MAIN LPAREN params RPAREN stmt_blockparams : VOIDparams : param_listparam_list : paramparam_list : param_list COMMA paramparam : type IDparam : type TIMES IDgenstmt : mstmt\n                | umstmtmstmt : IF LPAREN expr RPAREN mstmt ELSE mstmt\n                | stmtumstmt : IF LPAREN expr RPAREN genstmt\n                | IF LPAREN expr RPAREN mstmt ELSE umstmtstmt : expr SEMICOLON\n            | declaration SEMICOLON\n            | stmt_block\n            | stmt_forloop\n            | stmt_return\n            | SEMICOLONstmt : expr errorstmt : PRINT LPAREN argument_list RPARENdeclaration : declaration COMMA idbracketdeclaration : declaration COMMA TIMES idbracketdeclaration : type idbracketdeclaration : type TIMES idbracketidbracket : IDidbracket : ID LBRACKET INUM RBRACKETtype : INT\n            | FLOAT\n            | VOIDstmt_block : LBRACE stmt_list RBRACEstmt_list : stmt_list genstmtstmt_list : emptystmt_forloop : FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN stmtstmt_return : RETURN expr SEMICOLONstmt_return : RETURN SEMICOLONexpr : ID EQUAL exprexpr : ID LBRACKET arith_expr RBRACKET EQUAL exprexpr : TIMES ID EQUAL exprexpr : incr_exprexpr : basic_exprbasic_expr : basic_expr compare arith_exprbasic_expr : arith_exprcompare : EQ\n               | NEQ\n               | GT\n               | LTincr_expr : ID INCREMENTincr_expr : INCREMENT IDarith_expr : MINUS arith_expr %prec UMINUSarith_expr : LPAREN arith_expr RPARENarith_expr : arith_expr PLUS arith_exprarith_expr : arith_expr MINUS arith_exprarith_expr : arith_expr TIMES arith_exprarith_expr : arith_expr DIV arith_exprarith_expr : IDarith_expr : FNUMarith_expr : INUMarith_expr : TIMES IDarith_expr : ADDRESS IDarith_expr : ID LBRACKET arith_expr RBRACKETarith_expr : TIMES ID LBRACKET arith_expr RBRACKETarith_expr : ID LPAREN argument_list RPARENargument_list : argumentargument_list : argument_list COMMA argumentargument : emptyargument : arith_exprargument : LITERALargument : errorempty :'
    
_lr_action_items = {'INT':([0,2,3,4,10,19,23,31,36,41,42,45,46,47,48,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[-76,7,-4,-2,-3,7,7,7,7,-5,-76,-7,7,-39,-6,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,7,-27,-14,-18,7,-16,-19,7,-40,]),'FLOAT':([0,2,3,4,10,19,23,31,36,41,42,45,46,47,48,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[-76,8,-4,-2,-3,8,8,8,8,-5,-76,-7,8,-39,-6,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,8,-27,-14,-18,8,-16,-19,8,-40,]),'VOID':([0,2,3,4,10,19,23,31,36,41,42,45,46,47,48,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[-76,9,-4,-2,-3,27,27,27,9,-5,-76,-7,9,-39,-6,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,9,-27,-14,-18,9,-16,-19,9,-40,]),'$end':([0,1,2,3,4,10,41,45,48,49,],[-76,0,-1,-4,-2,-3,-5,-7,-6,-37,]),'SEMICOLON':([5,12,15,16,18,21,22,24,37,42,46,47,49,50,51,52,55,56,57,58,59,60,61,63,64,66,67,70,73,74,79,80,81,82,86,92,100,101,102,103,104,106,107,115,118,119,120,121,124,125,126,127,129,131,132,133,136,137,138,141,142,143,144,146,147,149,150,],[10,-32,-30,-28,-32,-32,-31,-29,-33,-76,57,-39,-37,-38,-14,-15,80,-17,-25,82,-22,-23,-24,-62,-49,-46,-47,101,-63,-64,-62,-20,-26,-21,-54,-65,126,-42,-55,-56,-66,-57,-65,-43,-58,-59,-60,-61,-48,135,-41,57,-27,-67,-69,-45,-14,-18,-67,-68,145,57,-44,-16,-19,57,-40,]),'COMMA':([5,12,15,16,18,21,22,24,28,29,33,37,40,43,58,73,74,79,83,87,103,104,106,107,109,110,111,112,113,114,117,118,119,120,121,130,132,138,139,141,],[11,-32,-30,-28,-32,-32,-31,-29,36,-10,-12,-33,-13,-11,11,-63,-64,-62,-76,-76,-56,-66,-57,-65,130,-70,-72,-73,-74,-75,130,-58,-59,-60,-61,-76,-69,-67,-71,-68,]),'ID':([6,7,8,9,11,13,17,25,27,34,42,46,47,49,50,51,52,54,56,57,59,60,61,65,68,70,71,72,75,76,78,80,81,82,83,84,85,87,88,89,90,91,93,94,95,96,97,98,99,101,108,122,123,126,127,129,130,135,136,137,140,143,145,146,147,149,150,],[12,-34,-35,-36,18,21,18,33,-36,40,-76,63,-39,-37,-38,-14,-15,79,-17,-25,-22,-23,-24,92,18,63,102,79,104,63,107,-20,-26,-21,79,63,79,79,79,79,79,79,79,-50,-51,-52,-53,18,63,-42,79,63,79,-41,63,-27,79,63,-14,-18,63,63,63,-16,-19,63,-40,]),'TIMES':([6,7,8,9,11,25,27,42,46,47,49,50,51,52,54,56,57,59,60,61,63,64,68,70,72,73,74,76,77,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,106,107,108,112,116,118,119,120,121,122,123,124,126,127,128,129,130,131,132,134,135,136,137,138,140,141,143,145,146,147,149,150,],[13,-34,-35,-36,17,34,-36,-76,65,-39,-37,-38,-14,-15,78,-17,-25,-22,-23,-24,-62,90,98,65,78,-63,-64,65,90,-62,-20,-26,-21,78,65,78,78,78,78,78,78,-65,78,-50,-51,-52,-53,65,-42,-56,-66,-57,-65,78,90,90,90,90,-60,-61,65,78,90,-41,65,90,-27,78,-67,-69,90,65,-14,-18,-67,65,-68,65,65,-16,-19,65,-40,]),'MAIN':([6,7,8,9,],[14,-34,-35,-36,]),'LPAREN':([12,14,21,42,46,47,49,50,51,52,53,54,56,57,59,60,61,62,63,69,70,72,76,79,80,81,82,83,84,85,87,88,89,90,91,93,94,95,96,97,99,101,108,122,123,126,127,129,130,135,136,137,140,143,145,146,147,149,150,],[19,23,31,-76,54,-39,-37,-38,-14,-15,76,54,-17,-25,-22,-23,-24,83,87,99,54,54,54,87,-20,-26,-21,54,54,54,54,54,54,54,54,54,-50,-51,-52,-53,54,-42,54,54,54,-41,54,-27,54,54,-14,-18,54,54,54,-16,-19,54,-40,]),'LBRACKET':([12,18,21,63,79,92,107,],[20,20,20,85,108,123,123,]),'INUM':([20,42,46,47,49,50,51,52,54,56,57,59,60,61,70,72,76,80,81,82,83,84,85,87,88,89,90,91,93,94,95,96,97,99,101,108,122,123,126,127,129,130,135,136,137,140,143,145,146,147,149,150,],[30,-76,74,-39,-37,-38,-14,-15,74,-17,-25,-22,-23,-24,74,74,74,-20,-26,-21,74,74,74,74,74,74,74,74,74,-50,-51,-52,-53,74,-42,74,74,74,-41,74,-27,74,74,-14,-18,74,74,74,-16,-19,74,-40,]),'RPAREN':([26,27,28,29,32,33,38,40,43,63,64,66,67,73,74,77,79,83,86,87,92,102,103,104,105,106,107,109,110,111,112,113,114,115,117,118,119,120,121,124,130,131,132,133,138,139,141,144,148,],[35,-8,-9,-10,39,-12,44,-13,-11,-62,-49,-46,-47,-63,-64,106,-62,-76,-54,-76,-65,-55,-56,-66,127,-57,-65,129,-70,-72,-73,-74,-75,-43,132,-58,-59,-60,-61,-48,-76,-67,-69,-45,-67,-71,-68,-44,149,]),'RBRACKET':([30,73,74,79,103,104,106,107,116,118,119,120,121,128,132,134,138,141,],[37,-63,-64,-62,-56,-66,-57,-65,131,-58,-59,-60,-61,138,-69,141,-67,-68,]),'LBRACE':([35,39,42,44,46,47,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[42,42,-76,42,42,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,42,-27,-14,-18,42,-16,-19,42,-40,]),'RBRACE':([42,46,47,49,50,51,52,56,57,59,60,61,80,81,82,101,126,129,136,137,146,147,150,],[-76,49,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,-27,-14,-18,-16,-19,-40,]),'IF':([42,46,47,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,150,],[-76,53,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,53,-27,-14,-18,53,-16,-19,-40,]),'PRINT':([42,46,47,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[-76,62,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,62,-27,-14,-18,62,-16,-19,62,-40,]),'FOR':([42,46,47,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[-76,69,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,69,-27,-14,-18,69,-16,-19,69,-40,]),'RETURN':([42,46,47,49,50,51,52,56,57,59,60,61,80,81,82,101,126,127,129,136,137,143,146,147,149,150,],[-76,70,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,70,-27,-14,-18,70,-16,-19,70,-40,]),'INCREMENT':([42,46,47,49,50,51,52,56,57,59,60,61,63,70,76,80,81,82,84,99,101,122,126,127,129,135,136,137,140,143,145,146,147,149,150,],[-76,71,-39,-37,-38,-14,-15,-17,-25,-22,-23,-24,86,71,71,-20,-26,-21,71,71,-42,71,-41,71,-27,71,-14,-18,71,71,71,-16,-19,71,-40,]),'MINUS':([42,46,47,49,50,51,52,54,56,57,59,60,61,63,64,70,72,73,74,76,77,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,99,101,103,104,106,107,108,112,116,118,119,120,121,122,123,124,126,127,128,129,130,131,132,134,135,136,137,138,140,141,143,145,146,147,149,150,],[-76,72,-39,-37,-38,-14,-15,72,-17,-25,-22,-23,-24,-62,89,72,72,-63,-64,72,89,-62,-20,-26,-21,72,72,72,72,72,72,72,72,-65,72,-50,-51,-52,-53,72,-42,-56,-66,-57,-65,72,89,89,-58,-59,-60,-61,72,72,89,-41,72,89,-27,72,-67,-69,89,72,-14,-18,-67,72,-68,72,72,-16,-19,72,-40,]),'FNUM':([42,46,47,49,50,51,52,54,56,57,59,60,61,70,72,76,80,81,82,83,84,85,87,88,89,90,91,93,94,95,96,97,99,101,108,122,123,126,127,129,130,135,136,137,140,143,145,146,147,149,150,],[-76,73,-39,-37,-38,-14,-15,73,-17,-25,-22,-23,-24,73,73,73,-20,-26,-21,73,73,73,73,73,73,73,73,73,-50,-51,-52,-53,73,-42,73,73,73,-41,73,-27,73,73,-14,-18,73,73,73,-16,-19,73,-40,]),'ADDRESS':([42,46,47,49,50,51,52,54,56,57,59,60,61,70,72,76,80,81,82,83,84,85,87,88,89,90,91,93,94,95,96,97,99,101,108,122,123,126,127,129,130,135,136,137,140,143,145,146,147,149,150,],[-76,75,-39,-37,-38,-14,-15,75,-17,-25,-22,-23,-24,75,75,75,-20,-26,-21,75,75,75,75,75,75,75,75,75,-50,-51,-52,-53,75,-42,75,75,75,-41,75,-27,75,75,-14,-18,75,75,75,-16,-19,75,-40,]),'ELSE':([49,56,57,59,60,61,80,81,82,101,126,129,136,146,150,],[-37,-17,-25,-22,-23,-24,-20,-26,-21,-42,-41,-27,143,-16,-40,]),'error':([55,63,64,66,67,73,74,79,83,86,87,92,102,103,104,106,107,115,118,119,120,121,124,130,131,132,133,138,141,144,],[81,-62,-49,-46,-47,-63,-64,-62,114,-54,114,-65,-55,-56,-66,-57,-65,-43,-58,-59,-60,-61,-48,114,-67,-69,-45,-67,-68,-44,]),'EQUAL':([63,92,131,],[84,122,140,]),'PLUS':([63,64,73,74,77,79,92,103,104,106,107,112,116,118,119,120,121,124,128,131,132,134,138,141,],[-62,88,-63,-64,88,-62,-65,-56,-66,-57,-65,88,88,-58,-59,-60,-61,88,88,-67,-69,88,-67,-68,]),'DIV':([63,64,73,74,77,79,92,103,104,106,107,112,116,118,119,120,121,124,128,131,132,134,138,141,],[-62,91,-63,-64,91,-62,-65,-56,-66,-57,-65,91,91,91,91,-60,-61,91,91,-67,-69,91,-67,-68,]),'EQ':([63,64,67,73,74,79,92,103,104,106,107,118,119,120,121,124,131,132,138,141,],[-62,-49,94,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-69,-67,-68,]),'NEQ':([63,64,67,73,74,79,92,103,104,106,107,118,119,120,121,124,131,132,138,141,],[-62,-49,95,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-69,-67,-68,]),'GT':([63,64,67,73,74,79,92,103,104,106,107,118,119,120,121,124,131,132,138,141,],[-62,-49,96,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-69,-67,-68,]),'LT':([63,64,67,73,74,79,92,103,104,106,107,118,119,120,121,124,131,132,138,141,],[-62,-49,97,-63,-64,-62,-65,-56,-66,-57,-65,-58,-59,-60,-61,-48,-67,-69,-67,-68,]),'LITERAL':([83,87,130,],[113,113,113,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'empty':([0,42,83,87,130,],[3,47,111,111,111,]),'func_declaration':([2,],[4,]),'declaration':([2,46,127,143,149,],[5,58,58,58,58,]),'type':([2,19,23,31,36,46,127,143,149,],[6,25,25,25,25,68,68,68,68,]),'idbracket':([6,11,13,17,68,98,],[15,16,22,24,15,22,]),'params':([19,23,31,],[26,32,38,]),'param_list':([19,23,31,],[28,28,28,]),'param':([19,23,31,36,],[29,29,29,43,]),'stmt_block':([35,39,44,46,127,143,149,],[41,45,48,59,59,59,59,]),'stmt_list':([42,],[46,]),'genstmt':([46,127,],[50,137,]),'mstmt':([46,127,143,],[51,136,146,]),'umstmt':([46,127,143,],[52,52,147,]),'expr':([46,70,76,84,99,122,127,135,140,143,145,149,],[55,100,105,115,125,133,55,142,144,55,148,55,]),'stmt':([46,127,143,149,],[56,56,56,150,]),'stmt_forloop':([46,127,143,149,],[60,60,60,60,]),'stmt_return':([46,127,143,149,],[61,61,61,61,]),'arith_expr':([46,54,70,72,76,83,84,85,87,88,89,90,91,93,99,108,122,123,127,130,135,140,143,145,149,],[64,77,64,103,64,112,64,116,112,118,119,120,121,124,64,128,64,134,64,112,64,64,64,64,64,]),'incr_expr':([46,70,76,84,99,122,127,135,140,143,145,149,],[66,66,66,66,66,66,66,66,66,66,66,66,]),'basic_expr':([46,70,76,84,99,122,127,135,140,143,145,149,],[67,67,67,67,67,67,67,67,67,67,67,67,]),'compare':([67,],[93,]),'argument_list':([83,87,],[109,117,]),'argument':([83,87,130,],[110,110,139,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','pycparser.py',26),
  ('declaration_list -> declaration_list func_declaration','declaration_list',2,'p_declaration_list_1','pycparser.py',36),
  ('declaration_list -> declaration_list declaration SEMICOLON','declaration_list',3,'p_declaration_list_2','pycparser.py',43),
  ('declaration_list -> empty','declaration_list',1,'p_declaration_list_3','pycparser.py',49),
  ('func_declaration -> type ID LPAREN params RPAREN stmt_block','func_declaration',6,'p_func_declaration_1','pycparser.py',60),
  ('func_declaration -> type TIMES ID LPAREN params RPAREN stmt_block','func_declaration',7,'p_func_declaration_2','pycparser.py',66),
  ('func_declaration -> type MAIN LPAREN params RPAREN stmt_block','func_declaration',6,'p_func_declaration_3','pycparser.py',72),
  ('params -> VOID','params',1,'p_params_1','pycparser.py',83),
  ('params -> param_list','params',1,'p_params_2','pycparser.py',88),
  ('param_list -> param','param_list',1,'p_param_list_1','pycparser.py',93),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list_2','pycparser.py',100),
  ('param -> type ID','param',2,'p_param_1','pycparser.py',113),
  ('param -> type TIMES ID','param',3,'p_param_2','pycparser.py',119),
  ('genstmt -> mstmt','genstmt',1,'p_general_statement','pycparser.py',130),
  ('genstmt -> umstmt','genstmt',1,'p_general_statement','pycparser.py',131),
  ('mstmt -> IF LPAREN expr RPAREN mstmt ELSE mstmt','mstmt',7,'p_matched_statement','pycparser.py',136),
  ('mstmt -> stmt','mstmt',1,'p_matched_statement','pycparser.py',137),
  ('umstmt -> IF LPAREN expr RPAREN genstmt','umstmt',5,'p_unmatched_statement','pycparser.py',145),
  ('umstmt -> IF LPAREN expr RPAREN mstmt ELSE umstmt','umstmt',7,'p_unmatched_statement','pycparser.py',146),
  ('stmt -> expr SEMICOLON','stmt',2,'p_statement','pycparser.py',163),
  ('stmt -> declaration SEMICOLON','stmt',2,'p_statement','pycparser.py',164),
  ('stmt -> stmt_block','stmt',1,'p_statement','pycparser.py',165),
  ('stmt -> stmt_forloop','stmt',1,'p_statement','pycparser.py',166),
  ('stmt -> stmt_return','stmt',1,'p_statement','pycparser.py',167),
  ('stmt -> SEMICOLON','stmt',1,'p_statement','pycparser.py',168),
  ('stmt -> expr error','stmt',2,'p_statement_error_1','pycparser.py',179),
  ('stmt -> PRINT LPAREN argument_list RPAREN','stmt',4,'p_stmt_printf','pycparser.py',192),
  ('declaration -> declaration COMMA idbracket','declaration',3,'p_declaration_1','pycparser.py',227),
  ('declaration -> declaration COMMA TIMES idbracket','declaration',4,'p_declaration_2','pycparser.py',238),
  ('declaration -> type idbracket','declaration',2,'p_declaration_3','pycparser.py',250),
  ('declaration -> type TIMES idbracket','declaration',3,'p_declaration_4','pycparser.py',261),
  ('idbracket -> ID','idbracket',1,'p_id_bracket_1','pycparser.py',278),
  ('idbracket -> ID LBRACKET INUM RBRACKET','idbracket',4,'p_id_bracket_2','pycparser.py',283),
  ('type -> INT','type',1,'p_type','pycparser.py',289),
  ('type -> FLOAT','type',1,'p_type','pycparser.py',290),
  ('type -> VOID','type',1,'p_type','pycparser.py',291),
  ('stmt_block -> LBRACE stmt_list RBRACE','stmt_block',3,'p_stmt_block','pycparser.py',302),
  ('stmt_list -> stmt_list genstmt','stmt_list',2,'p_stmt_list_1','pycparser.py',314),
  ('stmt_list -> empty','stmt_list',1,'p_stmt_list_2','pycparser.py',321),
  ('stmt_forloop -> FOR LPAREN expr SEMICOLON expr SEMICOLON expr RPAREN stmt','stmt_forloop',9,'p_forloop','pycparser.py',330),
  ('stmt_return -> RETURN expr SEMICOLON','stmt_return',3,'p_return_stmt_1','pycparser.py',344),
  ('stmt_return -> RETURN SEMICOLON','stmt_return',2,'p_return_stmt_2','pycparser.py',351),
  ('expr -> ID EQUAL expr','expr',3,'p_expr_assign_1','pycparser.py',366),
  ('expr -> ID LBRACKET arith_expr RBRACKET EQUAL expr','expr',6,'p_expr_assign_2','pycparser.py',374),
  ('expr -> TIMES ID EQUAL expr','expr',4,'p_expr_assign_3','pycparser.py',379),
  ('expr -> incr_expr','expr',1,'p_expr_incr','pycparser.py',384),
  ('expr -> basic_expr','expr',1,'p_expr_basic','pycparser.py',391),
  ('basic_expr -> basic_expr compare arith_expr','basic_expr',3,'p_basic_expr_compare','pycparser.py',397),
  ('basic_expr -> arith_expr','basic_expr',1,'p_basic_expr_arith_expr','pycparser.py',412),
  ('compare -> EQ','compare',1,'p_compare','pycparser.py',418),
  ('compare -> NEQ','compare',1,'p_compare','pycparser.py',419),
  ('compare -> GT','compare',1,'p_compare','pycparser.py',420),
  ('compare -> LT','compare',1,'p_compare','pycparser.py',421),
  ('incr_expr -> ID INCREMENT','incr_expr',2,'p_incr_expr_1','pycparser.py',430),
  ('incr_expr -> INCREMENT ID','incr_expr',2,'p_incr_expr_2','pycparser.py',439),
  ('arith_expr -> MINUS arith_expr','arith_expr',2,'p_arith_uminus','pycparser.py',452),
  ('arith_expr -> LPAREN arith_expr RPAREN','arith_expr',3,'p_arith_parens','pycparser.py',459),
  ('arith_expr -> arith_expr PLUS arith_expr','arith_expr',3,'p_arith_add','pycparser.py',471),
  ('arith_expr -> arith_expr MINUS arith_expr','arith_expr',3,'p_arith_sub','pycparser.py',481),
  ('arith_expr -> arith_expr TIMES arith_expr','arith_expr',3,'p_arith_mult','pycparser.py',490),
  ('arith_expr -> arith_expr DIV arith_expr','arith_expr',3,'p_arith_div','pycparser.py',499),
  ('arith_expr -> ID','arith_expr',1,'p_arith_id','pycparser.py',513),
  ('arith_expr -> FNUM','arith_expr',1,'p_arith_fnum','pycparser.py',522),
  ('arith_expr -> INUM','arith_expr',1,'p_arith_inum','pycparser.py',530),
  ('arith_expr -> TIMES ID','arith_expr',2,'p_arith_pointer','pycparser.py',539),
  ('arith_expr -> ADDRESS ID','arith_expr',2,'p_arith_address','pycparser.py',544),
  ('arith_expr -> ID LBRACKET arith_expr RBRACKET','arith_expr',4,'p_arith_array_index','pycparser.py',549),
  ('arith_expr -> TIMES ID LBRACKET arith_expr RBRACKET','arith_expr',5,'p_arith_pointer_array','pycparser.py',555),
  ('arith_expr -> ID LPAREN argument_list RPAREN','arith_expr',4,'p_arith_functioncall','pycparser.py',560),
  ('argument_list -> argument','argument_list',1,'p_argument_list_1','pycparser.py',578),
  ('argument_list -> argument_list COMMA argument','argument_list',3,'p_argument_list_2','pycparser.py',585),
  ('argument -> empty','argument',1,'p_argument_1','pycparser.py',591),
  ('argument -> arith_expr','argument',1,'p_argument_2','pycparser.py',596),
  ('argument -> LITERAL','argument',1,'p_argument_3','pycparser.py',602),
  ('argument -> error','argument',1,'p_argument_error','pycparser.py',608),
  ('empty -> <empty>','empty',0,'p_empty','pycparser.py',614),
]
