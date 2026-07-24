%{
#include "parser.tab.h"
%}

%option noyywrap
%option nounput
%option noinput

%%

"networks"                                  { return NETWORKS_KEY; }
"driver"                                     { return DRIVER_KEY; }
"ipam"                                       { return IPAM_KEY; }
"config"                                     { return CONFIG_KEY; }
"subnet"                                     { return SUBNET_KEY; }
":"                                          { return COLON; }
"-"                                          { return DASH; }
[a-zA-Z_][a-zA-Z0-9_-]*                      { return ID; }
[a-zA-Z0-9_]+                                { return STRING; }
[0-9]+"."[0-9]+"."[0-9]+"."[0-9]+"/"[0-9]+   { return IP_CIDR; }
[ \t\r\n]+                                   { /* skip whitespace, mirrors WS -> skip */ }
.                                            { /* unrecognized char, ignore for error tolerance */ }

%%
