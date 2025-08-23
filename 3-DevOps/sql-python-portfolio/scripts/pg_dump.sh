#!/usr/bin/env bash
set -euo pipefail
DB_NAME=${1:-portfolio_db}
OUT=backup_$(date +%Y%m%d_%H%M%S).sql
echo "Dumping $DB_NAME to $OUT"
pg_dump -U postgres -d "$DB_NAME" -F p > "$OUT"
echo "Done: $OUT"
