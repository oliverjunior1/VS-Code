<?php

function verificarIdade($idade) {
    if ($idade >= 18) {
        return "Maior de idade";
    }
    return "Menor de idade";
    
}

$nome = "Joaquim";
$idade = 30;

echo "Nome: $nome<br>";
echo "Idade: $idade<br>";
echo "Situação: ".verificarIdade($idade);


?>