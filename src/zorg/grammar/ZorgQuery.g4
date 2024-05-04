grammar ZorgQuery;

import CommonLexerRules;

//// parser rules
prog : query NL? ;

query : where_query | select_query ;
where_query : (select SPACE)? where (SPACE order_by)? (SPACE group_by)? ;
select_query : select ;

select : 'S' SPACE select_body ;
where : 'W' SPACE where_body ;
order_by : 'O' ;
group_by : 'G' group_by_body ;

select_body : 'file' | 'note' | AT_SIGN | HASH | PLUS | PERCENT ;

where_body : note_status ;
note_status : note_status_char+ ;
note_status_char : DASH | LOWER_O | LOWER_X | TILDE | LANGLE | RANGLE ;

group_by_body : 'file' ;
