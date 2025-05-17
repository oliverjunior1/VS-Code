/*
 1) Faça um algoritmo que dado as 3 notas tiradas por um aluno em um semestre da faculdadee calcule e imprima a
 sua média e a sua classificação conforme a tabela conforme a tabela abaixo.

 Média = (nota 1 + nota2 + nota3)/3;

 Classificação:
 - Média menor que 5, reprovação;
 - Média entre 5 e 7, recuperação;
 - Média acima de 7, passou de semestre;
*/

let nota1 = Number(prompt("Coloque a nota 1"))
let nota2 = Number(prompt("Coloque a nota 2"))
let nota3 = Number(prompt("Coloque a nota 3"))


let media = (nota1 + nota2 + nota3)/3
90
if (media < 50) {
    alert("reprovado")
}
else if(media >=50 & media <70) {
    alert("recuperação")
}
else {
    alert("passou de semestre")
}
alert("A média foi:"+media)