# BUG-001 : Crash lors de l'ajout au panier (produit sans stock) - Template BUGS

## Type
- [ ] Fonctionnelle
- [ ] Technique
- [x] **Bug** - Critique

## Description
**Problème détecté** : L'application crash lors de l'ajout au panier si le produit a un stock = 0 ou NULL.

**Comportement attendu** : Afficher un message d'erreur "Produit en rupture de stock" sans crash.

**Impact** : 🔴 Critique - Bloque le tunnel d'achat, perte de revenus.

## Complexité estimée
**Story Points** : 3 pts (bug urgent mais fix simple normalement)

## Critères d'acceptation (Fix du bug)

### ☑️ Critère 1 : Reproduction du bug
- **Catégorie** : `[TESTS]`
- **Valeur du dé** : 🎲 **1**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non (✅ Oui si bonus `[TESTS]` actif)

**Description** : Le bug est reproduit en environnement de test avec un test automatisé (test de non-régression).

---

### ☑️ Critère 2 : Correction du crash
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **3**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Le code est corrigé pour vérifier le stock AVANT d'ajouter au panier. Gestion d'erreur propre (try/catch ou validation).

---

### ☑️ Critère 3 : Message d'erreur utilisateur
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **2**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Un message d'erreur clair s'affiche : "Ce produit n'est plus disponible" avec bouton "Retour au catalogue".

---

### ☑️ Critère 4 : Test de non-régression validé
- **Catégorie** : `[TESTS]`
- **Valeur du dé** : 🎲 **4**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non (✅ Oui si bonus `[TESTS]` actif)

**Description** : Les tests automatisés passent et couvrent les cas : stock=0, stock=NULL, stock négatif.

---

### ☑️ Critère 5 : Déployé en production (hotfix)
- **Catégorie** : `[CI/CD]`
- **Valeur du dé** : 🎲 **5**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non (✅ Oui si bonus `[CI/CD]` actif)

**Description** : Le fix est déployé en production en urgence (hotfix). Monitoring vérifie qu'il n'y a plus de crash.

---

## Notes

### Dépendances
- Bloque : Toutes les US du panier (EPIC-4-FM-24 à EPIC-4-FM-28)
- Apparaît pendant : Sprint 2

### Priorité
🔴 **Critique** - À traiter EN URGENCE dès le Sprint 2. Peut nécessiter d'interrompre le sprint en cours.

### Bonus débloqué
_Aucun (c'est un bug)_

### Historique des tentatives

| Sprint | Dés lancés | Critères validés | Statut |
|--------|------------|------------------|--------|
|  | - | - | ⏳ Pas encore jouée |
|   |   |   |  - |
|   |   |   |  - |
|   |   |   |  - |
|   |   |   |  - |
|   |   |   |  - |

---

## Définition of Done (DoD)
- [ ] Tous les critères d'acceptation sont validés (5/5)
- [ ] Bug corrigé et testé
- [ ] Déployé en production (hotfix)
- [ ] Post-mortem rédigé (optionnel : qu'est-ce qui a causé ce bug ?)

---

## Note pour l'enseignant

🐛 **Template pour tous les BUGS (BUG-1 à BUG-4)**

Tous les bugs partagent ces mêmes critères d'acceptation. Seuls changent :
- Le titre du bug
- La description du problème
- La sévérité (Critique, Haute, Moyenne)
- Le sprint d'apparition

**Particularité des bugs** :
- 5 critères standards
- Doivent être traités en urgence (peuvent interrompre le sprint planifié)
- Simulent la réalité : imprévus qui perturbent la vélocité
