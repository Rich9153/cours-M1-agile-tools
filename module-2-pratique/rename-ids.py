#!/usr/bin/env python3
"""
Renomme les IDs des User Stories selon le format EPIC-x-FM-y
x = numéro de l'epic, y = numéro continu global de la story
"""

import os
import re
import glob

# Mapping: ancien numéro FM (int) → (epic, nouveau numéro continu)
MAPPING = {
    # EPIC 1 - Authentification & Comptes
    1: (1, 1),   # FM-1  → EPIC-1-FM-1
    2: (1, 2),   # FM-2  → EPIC-1-FM-2
    3: (1, 3),   # FM-3  → EPIC-1-FM-3
    4: (1, 4),   # FM-4  → EPIC-1-FM-4
    5: (1, 5),   # FM-5  → EPIC-1-FM-5
    6: (1, 6),   # FM-6  → EPIC-1-FM-6
    91: (1, 7),  # FM-91 → EPIC-1-FM-7
    92: (1, 8),  # FM-92 → EPIC-1-FM-8

    # EPIC 2 - Gestion des Produits (Artisan)
    7: (2, 9),   # FM-7  → EPIC-2-FM-9
    8: (2, 10),  # FM-8  → EPIC-2-FM-10
    11: (2, 11), # FM-11 → EPIC-2-FM-11
    12: (2, 12), # FM-12 → EPIC-2-FM-12
    13: (2, 13), # FM-13 → EPIC-2-FM-13
    81: (2, 14), # FM-81 → EPIC-2-FM-14
    82: (2, 15), # FM-82 → EPIC-2-FM-15

    # EPIC 3 - Catalogue & Recherche (Client)
    14: (3, 16), # FM-14 → EPIC-3-FM-16
    15: (3, 17), # FM-15 → EPIC-3-FM-17
    16: (3, 18), # FM-16 → EPIC-3-FM-18
    17: (3, 19), # FM-17 → EPIC-3-FM-19
    18: (3, 20), # FM-18 → EPIC-3-FM-20
    19: (3, 21), # FM-19 → EPIC-3-FM-21
    71: (3, 22), # FM-71 → EPIC-3-FM-22
    72: (3, 23), # FM-72 → EPIC-3-FM-23

    # EPIC 4 - Panier & Commande
    20: (4, 24), # FM-20 → EPIC-4-FM-24
    21: (4, 25), # FM-21 → EPIC-4-FM-25
    22: (4, 26), # FM-22 → EPIC-4-FM-26
    23: (4, 27), # FM-23 → EPIC-4-FM-27
    24: (4, 28), # FM-24 → EPIC-4-FM-28
    25: (4, 29), # FM-25 → EPIC-4-FM-29
    26: (4, 30), # FM-26 → EPIC-4-FM-30
    61: (4, 31), # FM-61 → EPIC-4-FM-31
    62: (4, 32), # FM-62 → EPIC-4-FM-32

    # EPIC 5 - Gestion des Commandes
    27: (5, 33), # FM-27 → EPIC-5-FM-33
    28: (5, 34), # FM-28 → EPIC-5-FM-34
    29: (5, 35), # FM-29 → EPIC-5-FM-35
    30: (5, 36), # FM-30 → EPIC-5-FM-36
    31: (5, 37), # FM-31 → EPIC-5-FM-37
    51: (5, 38), # FM-51 → EPIC-5-FM-38
    52: (5, 39), # FM-52 → EPIC-5-FM-39

    # EPIC 6 - Fonctionnalités Bonus
    32: (6, 40), # FM-32 → EPIC-6-FM-40
    33: (6, 41), # FM-33 → EPIC-6-FM-41
    34: (6, 42), # FM-34 → EPIC-6-FM-42
    35: (6, 43), # FM-35 → EPIC-6-FM-43
    36: (6, 44), # FM-36 → EPIC-6-FM-44
    37: (6, 45), # FM-37 → EPIC-6-FM-45
    38: (6, 46), # FM-38 → EPIC-6-FM-46
    39: (6, 47), # FM-39 → EPIC-6-FM-47
    40: (6, 48), # FM-40 → EPIC-6-FM-48
    41: (6, 49), # FM-41 → EPIC-6-FM-49
    42: (6, 50), # FM-42 → EPIC-6-FM-50
}


def new_id_plain(old_num: int) -> str:
    """Retourne le nouvel ID sans zéro-padding, ex: EPIC-1-FM-1"""
    epic, new_num = MAPPING[old_num]
    return f"EPIC-{epic}-FM-{new_num}"


def new_id_padded(old_num: int, width: int = 3) -> str:
    """Retourne le nouvel ID avec zéro-padding, ex: EPIC-1-FM-001"""
    epic, new_num = MAPPING[old_num]
    return f"EPIC-{epic}-FM-{str(new_num).zfill(width)}"


def replace_in_content(content: str) -> str:
    """Remplace tous les FM-N (avec ou sans padding) dans un texte."""

    def replace_match(m):
        num = int(m.group(1))
        if num not in MAPPING:
            return m.group(0)  # pas dans le mapping, on laisse
        # Détermine si l'original était paddé (ex: FM-001 ou US-FM-001)
        raw = m.group(1)
        if len(raw) > len(str(num)):  # zéro-padding détecté
            width = len(raw)
            return m.group(0).replace(f"FM-{raw}", new_id_padded(num, width))
        else:
            return m.group(0).replace(f"FM-{raw}", new_id_plain(num))

    # Remplace FM-N et US-FM-N (avec ou sans padding)
    # On utilise un look-behind pour éviter de toucher aux préfixes EPIC déjà convertis
    pattern = re.compile(r'(?<!EPIC-\d-)(?<!EPIC-\d\d-)FM-(\d+)', re.IGNORECASE)
    return pattern.sub(replace_match, content)


def rename_file(filepath: str) -> str | None:
    """Renomme un fichier si son nom contient un FM-N mappé.
    Retourne le nouveau chemin ou None si pas de renommage."""
    dirpath = os.path.dirname(filepath)
    filename = os.path.basename(filepath)

    # Cherche FM-NNN dans le nom de fichier (avec padding), seulement si pas déjà préfixé EPIC-
    if re.search(r'EPIC-\d+-FM-', filename):
        return None
    m = re.search(r'FM-(\d+)', filename)
    if not m:
        return None

    num = int(m.group(1))
    if num not in MAPPING:
        return None

    raw = m.group(1)
    width = len(raw)
    old_part = f"FM-{raw}"
    new_part = new_id_padded(num, width)

    new_filename = filename.replace(old_part, new_part, 1)
    new_filepath = os.path.join(dirpath, new_filename)
    return new_filepath


# ── Main ──────────────────────────────────────────────────────────────────────

base_dir = os.path.dirname(os.path.abspath(__file__))
md_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

print(f"Fichiers .md trouvés : {len(md_files)}\n")

# 1. Remplacement du contenu
for filepath in sorted(md_files):
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    updated = replace_in_content(original)

    if updated != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated)
        rel = os.path.relpath(filepath, base_dir)
        print(f"[CONTENT] {rel}")

print()

# 2. Renommage des fichiers (après avoir mis à jour le contenu)
for filepath in sorted(md_files):
    new_filepath = rename_file(filepath)
    if new_filepath and new_filepath != filepath:
        os.rename(filepath, new_filepath)
        rel_old = os.path.relpath(filepath, base_dir)
        rel_new = os.path.relpath(new_filepath, base_dir)
        print(f"[RENAME] {rel_old}\n      → {rel_new}")

print("\nTerminé.")