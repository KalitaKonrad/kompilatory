
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programnonassocJUST_IFnonassocELSEnonassocASSIGNMINUS_ASSIGNPLUS_ASSIGNTIMES_ASSIGNDIVIDE_ASSIGNleftEQNEGTGELTLEleftPLUSMINUSleftTIMESDIVIDEleftNEGATIONleftPLUS_MATMINUS_MATleftTIMES_MATDIVIDE_MATleftTRANSPOSEASSIGN BREAK CONTINUE DIVIDE DIVIDE_ASSIGN DIVIDE_MAT ELSE EQ EYE FLOAT FOR GE GT ID IF INT LE LT MINUS MINUS_ASSIGN MINUS_MAT NE ONES PLUS PLUS_ASSIGN PLUS_MAT PRINT RETURN STRING TIMES TIMES_ASSIGN TIMES_MAT TRANSPOSE WHILE ZEROSprogram : statements_list\n               | emptyempty :number : INT\n              | FLOATexpression : slice_or_id\n                  | number\n                  | STRINGinner_vector : inner_vector ',' expression\n                    | expressionexpression : '[' inner_vector ']' expression : ZEROS '(' expression ')'\n                  | EYE '(' expression ')'\n                  | ONES '(' expression ')' range : expression ':' expressionexpression : MINUS expression %prec NEGATIONexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : expression PLUS_MAT expression\n                  | expression MINUS_MAT expression\n                  | expression TIMES_MAT expression\n                  | expression DIVIDE_MAT expressionexpression : expression TRANSPOSEexpression : expression EQ expression\n                  | expression NE expression\n                  | expression GT expression\n                  | expression GE expression\n                  | expression LT expression\n                  | expression LE expressionslice_argument : expression\n                      | rangeslice : ID '[' slice_argument ']'\n             | ID '[' slice_argument ',' slice_argument ']' slice_or_id : ID\n                   | slicestatement : slice_or_id ASSIGN expression ';'\n                 | slice_or_id MINUS_ASSIGN expression ';'\n                 | slice_or_id PLUS_ASSIGN expression ';'\n                 | slice_or_id TIMES_ASSIGN expression ';'\n                 | slice_or_id DIVIDE_ASSIGN expression ';' statements_list : statements_list statement\n                       | statementstatement : RETURN ';'\n                 | RETURN expression ';' statement : '{' statements_list '}' statement : BREAK ';'\n                 | CONTINUE ';' statement : FOR ID ASSIGN range statementstatement : WHILE '(' expression ')' statementstatement : IF '(' expression ')' statement %prec JUST_IF\n                 | IF '(' expression ')' statement ELSE statementstatement : PRINT inner_vector ';' "
    
_lr_action_items = {'$end':([0,1,2,3,4,16,22,35,36,48,69,76,78,79,80,81,82,112,115,116,119,],[-3,0,-1,-2,-44,-43,-45,-48,-49,-46,-47,-54,-38,-39,-40,-41,-42,-50,-51,-52,-53,]),'RETURN':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[6,6,-44,6,-36,-37,-43,-45,-6,-7,-8,-4,-5,6,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,6,-34,6,6,-12,-13,-14,-50,-15,-51,-52,-35,6,-53,]),'{':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[7,7,-44,7,-36,-37,-43,-45,-6,-7,-8,-4,-5,7,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,7,-34,7,7,-12,-13,-14,-50,-15,-51,-52,-35,7,-53,]),'BREAK':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[8,8,-44,8,-36,-37,-43,-45,-6,-7,-8,-4,-5,8,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,8,-34,8,8,-12,-13,-14,-50,-15,-51,-52,-35,8,-53,]),'CONTINUE':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[9,9,-44,9,-36,-37,-43,-45,-6,-7,-8,-4,-5,9,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,9,-34,9,9,-12,-13,-14,-50,-15,-51,-52,-35,9,-53,]),'FOR':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[10,10,-44,10,-36,-37,-43,-45,-6,-7,-8,-4,-5,10,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,10,-34,10,10,-12,-13,-14,-50,-15,-51,-52,-35,10,-53,]),'WHILE':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[12,12,-44,12,-36,-37,-43,-45,-6,-7,-8,-4,-5,12,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,12,-34,12,12,-12,-13,-14,-50,-15,-51,-52,-35,12,-53,]),'IF':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[13,13,-44,13,-36,-37,-43,-45,-6,-7,-8,-4,-5,13,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,13,-34,13,13,-12,-13,-14,-50,-15,-51,-52,-35,13,-53,]),'PRINT':([0,2,4,7,11,15,16,22,24,25,26,32,33,34,35,36,48,57,68,69,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,106,107,109,110,111,112,114,115,116,117,118,119,],[14,14,-44,14,-36,-37,-43,-45,-6,-7,-8,-4,-5,14,-48,-49,-46,-25,-16,-47,-54,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,14,-34,14,14,-12,-13,-14,-50,-15,-51,-52,-35,14,-53,]),'ID':([0,2,4,6,7,10,11,14,15,16,17,18,19,20,21,22,24,25,26,27,31,32,33,34,35,36,38,39,40,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,69,70,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,103,104,105,106,107,109,110,111,112,114,115,116,117,118,119,],[11,11,-44,11,11,37,-36,11,-37,-43,11,11,11,11,11,-45,-6,-7,-8,11,11,-4,-5,11,-48,-49,11,11,11,-46,11,11,11,11,11,11,11,11,-25,11,11,11,11,11,11,11,11,11,-16,-47,11,-54,11,-38,-39,-40,-41,-42,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,11,-34,11,11,11,11,-12,-13,-14,-50,-15,-51,-52,-35,11,-53,]),'}':([4,16,22,34,35,36,48,69,76,78,79,80,81,82,112,115,116,119,],[-44,-43,-45,69,-48,-49,-46,-47,-54,-38,-39,-40,-41,-42,-50,-51,-52,-53,]),'ASSIGN':([5,11,15,37,103,117,],[17,-36,-37,70,-34,-35,]),'MINUS_ASSIGN':([5,11,15,103,117,],[18,-36,-37,-34,-35,]),'PLUS_ASSIGN':([5,11,15,103,117,],[19,-36,-37,-34,-35,]),'TIMES_ASSIGN':([5,11,15,103,117,],[20,-36,-37,-34,-35,]),'DIVIDE_ASSIGN':([5,11,15,103,117,],[21,-36,-37,-34,-35,]),';':([6,8,9,11,15,23,24,25,26,32,33,41,42,43,44,45,46,47,57,68,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,108,109,110,111,117,],[22,35,36,-36,-37,48,-6,-7,-8,-4,-5,76,-10,78,79,80,81,82,-25,-16,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,-34,-9,-12,-13,-14,-35,]),'STRING':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'[':([6,11,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[27,38,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'ZEROS':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'EYE':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'ONES':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'MINUS':([6,11,14,15,17,18,19,20,21,23,24,25,26,27,31,32,33,38,39,40,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,70,72,74,75,77,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,104,105,108,109,110,111,114,117,],[31,-36,31,-37,31,31,31,31,31,50,-6,-7,-8,31,31,-4,-5,31,31,31,50,50,50,50,50,50,31,31,31,31,31,31,31,31,-25,31,31,31,31,31,31,31,31,31,-16,31,50,50,50,31,-17,-18,-19,-20,-21,-22,-23,-24,50,50,50,50,50,50,-11,50,50,50,50,-34,31,31,50,-12,-13,-14,50,-35,]),'INT':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'FLOAT':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'PLUS':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,49,-6,-7,-8,-4,-5,49,49,49,49,49,49,-25,-16,49,49,49,-17,-18,-19,-20,-21,-22,-23,-24,49,49,49,49,49,49,-11,49,49,49,49,-34,49,-12,-13,-14,49,-35,]),'TIMES':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,51,-6,-7,-8,-4,-5,51,51,51,51,51,51,-25,-16,51,51,51,51,51,-19,-20,-21,-22,-23,-24,51,51,51,51,51,51,-11,51,51,51,51,-34,51,-12,-13,-14,51,-35,]),'DIVIDE':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,52,-6,-7,-8,-4,-5,52,52,52,52,52,52,-25,-16,52,52,52,52,52,-19,-20,-21,-22,-23,-24,52,52,52,52,52,52,-11,52,52,52,52,-34,52,-12,-13,-14,52,-35,]),'PLUS_MAT':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,53,-6,-7,-8,-4,-5,53,53,53,53,53,53,-25,53,53,53,53,53,53,53,53,-21,-22,-23,-24,53,53,53,53,53,53,-11,53,53,53,53,-34,53,-12,-13,-14,53,-35,]),'MINUS_MAT':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,54,-6,-7,-8,-4,-5,54,54,54,54,54,54,-25,54,54,54,54,54,54,54,54,-21,-22,-23,-24,54,54,54,54,54,54,-11,54,54,54,54,-34,54,-12,-13,-14,54,-35,]),'TIMES_MAT':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,55,-6,-7,-8,-4,-5,55,55,55,55,55,55,-25,55,55,55,55,55,55,55,55,55,55,-23,-24,55,55,55,55,55,55,-11,55,55,55,55,-34,55,-12,-13,-14,55,-35,]),'DIVIDE_MAT':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,56,-6,-7,-8,-4,-5,56,56,56,56,56,56,-25,56,56,56,56,56,56,56,56,56,56,-23,-24,56,56,56,56,56,56,-11,56,56,56,56,-34,56,-12,-13,-14,56,-35,]),'TRANSPOSE':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,57,-6,-7,-8,-4,-5,57,57,57,57,57,57,-25,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-11,57,57,57,57,-34,57,-12,-13,-14,57,-35,]),'EQ':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,58,-6,-7,-8,-4,-5,58,58,58,58,58,58,-25,-16,58,58,58,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,58,58,58,58,-34,58,-12,-13,-14,58,-35,]),'NE':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,59,-6,-7,-8,-4,-5,59,59,59,59,59,59,-25,-16,59,59,59,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,59,59,59,59,-34,59,-12,-13,-14,59,-35,]),'GT':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,60,-6,-7,-8,-4,-5,60,60,60,60,60,60,-25,-16,60,60,60,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,60,60,60,60,-34,60,-12,-13,-14,60,-35,]),'GE':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,61,-6,-7,-8,-4,-5,61,61,61,61,61,61,-25,-16,61,61,61,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,61,61,61,61,-34,61,-12,-13,-14,61,-35,]),'LT':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,62,-6,-7,-8,-4,-5,62,62,62,62,62,62,-25,-16,62,62,62,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,62,62,62,62,-34,62,-12,-13,-14,62,-35,]),'LE':([11,15,23,24,25,26,32,33,42,43,44,45,46,47,57,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,108,109,110,111,114,117,],[-36,-37,63,-6,-7,-8,-4,-5,63,63,63,63,63,63,-25,-16,63,63,63,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,63,63,63,63,-34,63,-12,-13,-14,63,-35,]),',':([11,15,24,25,26,32,33,41,42,57,64,68,71,72,73,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,108,109,110,111,114,117,],[-36,-37,-6,-7,-8,-4,-5,77,-10,-25,77,-16,104,-32,-33,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,-34,-9,-12,-13,-14,-15,-35,]),']':([11,15,24,25,26,32,33,42,57,64,68,71,72,73,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,103,108,109,110,111,113,114,117,],[-36,-37,-6,-7,-8,-4,-5,-10,-25,97,-16,103,-32,-33,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,-34,-9,-12,-13,-14,117,-15,-35,]),':':([11,15,24,25,26,32,33,57,68,72,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,102,103,109,110,111,117,],[-36,-37,-6,-7,-8,-4,-5,-25,-16,105,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,105,-34,-12,-13,-14,-35,]),')':([11,15,24,25,26,32,33,57,68,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,109,110,111,117,],[-36,-37,-6,-7,-8,-4,-5,-25,-16,106,107,-17,-18,-19,-20,-21,-22,-23,-24,-26,-27,-28,-29,-30,-31,-11,109,110,111,-34,-12,-13,-14,-35,]),'(':([12,13,28,29,30,],[39,40,65,66,67,]),'ELSE':([22,35,36,48,69,76,78,79,80,81,82,112,115,116,119,],[-45,-48,-49,-46,-47,-54,-38,-39,-40,-41,-42,-50,-51,118,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements_list':([0,7,],[2,34,]),'empty':([0,],[3,]),'statement':([0,2,7,34,101,106,107,118,],[4,16,4,16,112,115,116,119,]),'slice_or_id':([0,2,6,7,14,17,18,19,20,21,27,31,34,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,101,104,105,106,107,118,],[5,5,24,5,24,24,24,24,24,24,24,24,5,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,5,24,24,5,5,5,]),'slice':([0,2,6,7,14,17,18,19,20,21,27,31,34,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,101,104,105,106,107,118,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'expression':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[23,42,43,44,45,46,47,42,68,72,74,75,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,102,108,72,114,]),'number':([6,14,17,18,19,20,21,27,31,38,39,40,49,50,51,52,53,54,55,56,58,59,60,61,62,63,65,66,67,70,77,104,105,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'inner_vector':([14,27,],[41,64,]),'slice_argument':([38,104,],[71,113,]),'range':([38,70,104,],[73,101,73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements_list','program',1,'p_program','parser.py',20),
  ('program -> empty','program',1,'p_program','parser.py',21),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',27),
  ('number -> INT','number',1,'p_number','parser.py',32),
  ('number -> FLOAT','number',1,'p_number','parser.py',33),
  ('expression -> slice_or_id','expression',1,'p_expression','parser.py',39),
  ('expression -> number','expression',1,'p_expression','parser.py',40),
  ('expression -> STRING','expression',1,'p_expression','parser.py',41),
  ('inner_vector -> inner_vector , expression','inner_vector',3,'p_inner_vector','parser.py',47),
  ('inner_vector -> expression','inner_vector',1,'p_inner_vector','parser.py',48),
  ('expression -> [ inner_vector ]','expression',3,'p_vector','parser.py',57),
  ('expression -> ZEROS ( expression )','expression',4,'p_matrix_maker','parser.py',62),
  ('expression -> EYE ( expression )','expression',4,'p_matrix_maker','parser.py',63),
  ('expression -> ONES ( expression )','expression',4,'p_matrix_maker','parser.py',64),
  ('range -> expression : expression','range',3,'p_range','parser.py',70),
  ('expression -> MINUS expression','expression',2,'p_negation','parser.py',75),
  ('expression -> expression PLUS expression','expression',3,'p_binary_operators','parser.py',80),
  ('expression -> expression MINUS expression','expression',3,'p_binary_operators','parser.py',81),
  ('expression -> expression TIMES expression','expression',3,'p_binary_operators','parser.py',82),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary_operators','parser.py',83),
  ('expression -> expression PLUS_MAT expression','expression',3,'p_matrix_binary_operators','parser.py',89),
  ('expression -> expression MINUS_MAT expression','expression',3,'p_matrix_binary_operators','parser.py',90),
  ('expression -> expression TIMES_MAT expression','expression',3,'p_matrix_binary_operators','parser.py',91),
  ('expression -> expression DIVIDE_MAT expression','expression',3,'p_matrix_binary_operators','parser.py',92),
  ('expression -> expression TRANSPOSE','expression',2,'p_transposition','parser.py',98),
  ('expression -> expression EQ expression','expression',3,'p_compare','parser.py',103),
  ('expression -> expression NE expression','expression',3,'p_compare','parser.py',104),
  ('expression -> expression GT expression','expression',3,'p_compare','parser.py',105),
  ('expression -> expression GE expression','expression',3,'p_compare','parser.py',106),
  ('expression -> expression LT expression','expression',3,'p_compare','parser.py',107),
  ('expression -> expression LE expression','expression',3,'p_compare','parser.py',108),
  ('slice_argument -> expression','slice_argument',1,'p_slice_argument','parser.py',114),
  ('slice_argument -> range','slice_argument',1,'p_slice_argument','parser.py',115),
  ('slice -> ID [ slice_argument ]','slice',4,'p_slice','parser.py',121),
  ('slice -> ID [ slice_argument , slice_argument ]','slice',6,'p_slice','parser.py',122),
  ('slice_or_id -> ID','slice_or_id',1,'p_slice_or_id','parser.py',131),
  ('slice_or_id -> slice','slice_or_id',1,'p_slice_or_id','parser.py',132),
  ('statement -> slice_or_id ASSIGN expression ;','statement',4,'p_statement','parser.py',138),
  ('statement -> slice_or_id MINUS_ASSIGN expression ;','statement',4,'p_statement','parser.py',139),
  ('statement -> slice_or_id PLUS_ASSIGN expression ;','statement',4,'p_statement','parser.py',140),
  ('statement -> slice_or_id TIMES_ASSIGN expression ;','statement',4,'p_statement','parser.py',141),
  ('statement -> slice_or_id DIVIDE_ASSIGN expression ;','statement',4,'p_statement','parser.py',142),
  ('statements_list -> statements_list statement','statements_list',2,'p_statements_list','parser.py',148),
  ('statements_list -> statement','statements_list',1,'p_statements_list','parser.py',149),
  ('statement -> RETURN ;','statement',2,'p_return_statement','parser.py',158),
  ('statement -> RETURN expression ;','statement',3,'p_return_statement','parser.py',159),
  ('statement -> { statements_list }','statement',3,'p_code_block','parser.py',168),
  ('statement -> BREAK ;','statement',2,'p_loop_statement','parser.py',173),
  ('statement -> CONTINUE ;','statement',2,'p_loop_statement','parser.py',174),
  ('statement -> FOR ID ASSIGN range statement','statement',5,'p_for_loop','parser.py',180),
  ('statement -> WHILE ( expression ) statement','statement',5,'p_while_loop','parser.py',185),
  ('statement -> IF ( expression ) statement','statement',5,'p_if_statement','parser.py',190),
  ('statement -> IF ( expression ) statement ELSE statement','statement',7,'p_if_statement','parser.py',191),
  ('statement -> PRINT inner_vector ;','statement',3,'p_print','parser.py',200),
]
