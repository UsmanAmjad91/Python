param(
  [string]$DbName="portfolio_db"
)
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$out = "backup_$timestamp.sql"
Write-Host "Dumping $DbName to $out"
& pg_dump.exe -U postgres -d $DbName -F p > $out
Write-Host "Done: $out"
