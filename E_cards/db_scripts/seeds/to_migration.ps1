# Pegar o diretorio atual
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition -Parent

# Gerar o arquivo de saída com todos os sql
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

 # Identifica se o arquivo ja existe e remove
if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

# Até aqui o mesmo que o professor fez
# Pega o conteúdo dos arrquivos sql e concatena no arquivo de saída
Get-ChildItem -Path $scriptDirectory -Filter *.sql | ForEach-Object {
    $sqlContent = Get-Content -Path $_.FullName
    Add-Content -Path $outputFile -Value $sqlContent
    Add-Content -Path $outputFile -Value "`n`n"  # Adiciona duas quebras de linha entre os arquivos
}

Write-Host "Arquivo de migração gerado em: $outputFile"