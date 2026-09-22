/* document.getElementById("id02") = document.getElementById('id01').innerHTML; */ 

/* document.getElementById("id02").innerHTML = document.getElementById("id01").firstChild.nodeValue; */

document.getElementById("id02").innerHTML = document.getElementById("id01").childNodes[0].nodeValue;