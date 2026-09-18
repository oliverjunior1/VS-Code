<?php

function verificarNome($nome) {
    $clientes = [
    "João",
    "Maria",
    "Pedro",
    "Ana",
    "Carlos"
];
    foreach($clientes as $cliente) {
        if ($nome == $cliente) {
            echo "Cliente: $cliente <br>, cliente encontrado! <br>";
        }else {
            echo "Cliente: $cliente <br>";
        }
    }
}

verificarNome("Maria");




?>