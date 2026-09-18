<?php

$clientes = [
    "João",
    "Maria",
    "Pedro",
    "Ana",
    "Carlos"
];
function verificarNome($nome) {
    if ("$nome" == "João") {
        echo "Hello $nome";
    }elseif ("$nome" == "Maria") {
        echo "Cliente $nome";
    }elseif ("$nome" == "Pedro") {
        echo "Hello $nome";
    }elseif ("$nome" == "Ana") {
        echo "Hello $nome";
    } else {
        echo "Hello $nome";
    } ;
}

foreach($clientes as $cliente) {
    verificarNome($cliente);
}




?>