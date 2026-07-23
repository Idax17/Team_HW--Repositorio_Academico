grammar DockerNetworks;

// --- REGLAS SINTÁCTICAS (PARSER) ---
composeFile : NETWORKS_KEY COLON networkDef+ EOF ;

networkDef  : ID COLON property+ ;

property    : DRIVER_KEY COLON STRING
            | IPAM_KEY COLON ipamDef
            ;

ipamDef     : CONFIG_KEY COLON dashConfig+ ;

dashConfig  : DASH SUBNET_KEY COLON IP_CIDR ;

// --- REGLAS LÉXICAS (LEXER) ---
NETWORKS_KEY : 'networks' ;
DRIVER_KEY   : 'driver' ;
IPAM_KEY     : 'ipam' ;
CONFIG_KEY   : 'config' ;
SUBNET_KEY   : 'subnet' ;
COLON        : ':' ;
DASH         : '-' ;

// Identificadores y cadenas genéricas
ID           : [a-zA-Z_][a-zA-Z0-9_-]* ;
STRING       : [a-zA-Z0-9_]+ ;

// Expresión regular básica para atrapar una subred (Ej: 192.168.1.0/24)
IP_CIDR      : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ '/' [0-9]+ ;

// Ignorar espacios en blanco, tabulaciones y saltos de línea
WS           : [ \t\r\n]+ -> skip ;