<?php
$dir = "Funcionarios";
$listDiretorio = scandir($dir);

foreach($listDiretorio as $diretorio){
   
    echo '<p>'.$diretorio.'</p>';

}

?>