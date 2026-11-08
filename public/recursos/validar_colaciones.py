"""Audita persona + fecha operativa. Uso: python validar_colaciones.py colaciones.csv"""
import csv
import sys
from collections import Counter
from datetime import date
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print('Uso: python validar_colaciones.py colaciones.csv', file=sys.stderr)
        return 2
    with Path(sys.argv[1]).open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        required = {'persona_id', 'fecha_operativa', 'lote_id', 'turno'}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError('Faltan columnas requeridas')
        rows = list(reader)
    keys = []
    for n, row in enumerate(rows, 2):
        if not all((row.get(k) or '').strip() for k in required):
            raise ValueError(f'Fila {n}: campo obligatorio vacío')
        date.fromisoformat(row['fecha_operativa'].strip())
        if row['turno'].strip() not in {'A', 'B'}:
            raise ValueError(f'Fila {n}: turno inválido')
        keys.append((row['persona_id'].strip(), row['fecha_operativa'].strip()))
    duplicates = {k: count for k, count in Counter(keys).items() if count > 1}
    for (person, day), count in duplicates.items():
        print(f'DUPLICADO: {person}, {day}, {count} retiros')
    print(f'{len(rows)} registros; {len(duplicates)} claves duplicadas.')
    return 1 if duplicates else 0

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, csv.Error) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(2)
