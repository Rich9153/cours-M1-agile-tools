# 🏆 Système de Scoring - Jeu Agile

Ce document définit comment calculer le score final des équipes à la fin du jeu.

---

## 📊 Composantes du Score

Le score final est calculé selon **4 piliers** :

### 1️⃣ Valeur métier livrée (35 points max)

**Calcul** : Points de vélocité accumulés sur tous les sprints

#### Scoring
- **1 point de vélocité = 1 point de score** (pour tailles S et M uniquement)
- **⚠️ Pénalité XL réussie** : Les tâches XL comptent seulement **50% de leur valeur** (floues, difficiles à estimer, valeur métier incertaine)
- **❌ Malus XL échouée** : **-50% des story points** de la tâche XL non terminée
- **📉 Malus US ouvertes** : **-2 points par US non terminée** en fin de sprint (work-in-progress excessif)

#### Formule de calcul
```
Score = Σ(story points S/M livrés)
      + Σ(story points XL livrés × 0.5)
      - Σ(story points XL échouées × 0.75)
      - (Nombre total d'US ouvertes en fin de sprint × 2)
```

#### Exemple
```
Sprint 1 : 8 pts livrés (2 M de 4 pts) + 1 US S ouverte
Sprint 2 : 10 pts livrés (1 S + 2 M) + 0 US ouverte
Sprint 3 : 12 pts livrés (dont 1 XL de 10 pts → 5 pts) + 2 US M ouvertes
Sprint 4 : 1 XL échouée (10 pts)

Score = 8 + 10 + (2 + 5) - 0 - (1×2) - (2×2) - (10×0.5)
      = 8 + 10 + 7 - 2 - 4 - 5 = 14 points
```


---

### 2️⃣ Qualité du découpage (25 points max)

**Calcul** : Mesure objective de la stratégie de découpage

#### Critères évalués

| Critère | Points | Calcul objectif |
|---------|--------|-----------------|
| **Taille moyenne optimale** | 0-10 pts | Moyenne des story points des US prises |
| **Éviter les XL** | 0-8 pts | Nombre de XL prises |
| **Taux de complétion** | 0-7 pts | % d'US terminées / US commencées |

#### Formule de calcul détaillée

**1. Points taille moyenne (0-10 pts)**
```
Taille moyenne = Σ(story points de toutes les US prises) / Nombre total d'US prises

Points attribués :
- Si 3,0 ≤ moyenne ≤ 5,0 : 10 points (optimal, taille M)
- Si 2,5 ≤ moyenne < 3,0 : 7 points
- Si 5,0 < moyenne ≤ 6,0 : 5 points
- Si 2,0 ≤ moyenne < 2,5 : 4 points
- Si 6,0 < moyenne ≤ 7,0 : 3 points
- Si moyenne < 2,0 ou > 7,0 : 0 points
```

**2. Points éviter les XL (0-8 pts)**
```
Nombre de XL prises = Comptage des US XL dans tout le projet

Points attribués :
- 0 XL : 8 points (aucune XL, découpage parfait)
- 1 XL : 3 points (acceptable si bien justifiée)
- 2 XL : 0 points (mauvaise stratégie)
- 3+ XL : -2 points (très mauvaise stratégie)
```

**3. Points taux de complétion (0-7 pts)**
```
Taux = (Nombre d'US terminées / Nombre d'US commencées) × 100

Points attribués :
- Si taux ≥ 90% : 7 points (excellent)
- Si 80% ≤ taux < 90% : 6 points (très bon)
- Si 70% ≤ taux < 80% : 4 points (bon)
- Si 60% ≤ taux < 70% : 2 points (moyen)
- Si taux < 60% : 0 points (mauvais)
```


---

### 3️⃣ Gestion de la dette technique (25 points max)

**Calcul** : Investissement dans les US techniques et leur utilisation

#### Critères évalués

| Critère | Points | Description |
|---------|--------|-------------|
| **US techniques complétées** | 0-15 pts | 1 US technique terminée = 3 pts<br>Maximum 5 US (15 pts) |
| **Utilisation des bonus** | 0-5 pts | Bonus activés et **utilisés efficacement** |
| **Pas de dette accumulée** | 0-5 pts | Aucune dette technique non résolue en fin de jeu |

#### Formule de calcul

```
Points US techniques :
- Nombre d'US techniques terminées × 3 points
- Maximum 15 points (5 US techniques)

Points utilisation bonus :
- 0 bonus utilisé : 0 pts
- 1-2 bonus utilisés : 2 pts
- 3-4 bonus utilisés : 4 pts
- 5+ bonus utilisés : 5 pts

Points dette :
- Aucune dette en fin de jeu : 5 pts
- 1 dette : 3 pts
- 2 dettes : 1 pt
- 3+ dettes : 0 pts
```

**💡 Conseil** : Ce pilier récompense l'**investissement technique** et la **vision long terme**.

---

### 4️⃣ Excellence opérationnelle (15 points max)

**Calcul** : Respect des bonnes pratiques Agile

#### Critères évalués

| Critère | Points | Description |
|---------|--------|-------------|
| **Régularité de livraison** | 0-5 pts | Livraison à chaque sprint |
| **Respect du temps** | 0-5 pts | Sprints terminés dans le temps imparti |
| **Collaboration équipe** | 0-5 pts | Qualité du travail d'équipe (subjectif, évalué par l'animateur) |

#### Formule de calcul

```
Points régularité :
- Livraison dans 100% des sprints : 5 pts
- Livraison dans 66-99% des sprints : 3 pts
- Livraison dans 33-65% des sprints : 1 pt
- Livraison dans <33% des sprints : 0 pts

Points respect du temps :
- Aucun dépassement : 5 pts
- 1 dépassement : 3 pts
- 2+ dépassements : 0 pts

Points collaboration (évaluation animateur) :
- Excellente : 5 pts
- Bonne : 3 pts
- Moyenne : 1 pt
- Faible : 0 pts
```

**💡 Conseil** : Ce pilier récompense la **discipline** et l'**esprit d'équipe**.

---

## 🎯 Score Final

### Calcul

```
Score Total = Valeur métier (40)
            + Qualité découpage (20)
            + Dette technique (25)
            + Excellence opérationnelle (15)

Maximum possible : 100 points
```

### Grille d'évaluation

| Score | Niveau | Commentaire |
|-------|--------|-------------|
| 90-100 | 🏆 **Elite** | Équipe Agile exemplaire ! |
| 75-89 | 🥇 **Expert** | Très bonne maîtrise des pratiques Agile |
| 60-74 | 🥈 **Compétent** | Bonne compréhension, quelques axes d'amélioration |
| 45-59 | 🥉 **Débutant** | Bases acquises, beaucoup à apprendre |
| 0-44 | 📚 **Apprenti** | Revoir les fondamentaux de l'Agile |

---

## 📋 Feuille de Score (Template)

### Équipe : ___________________

#### 1️⃣ Valeur métier livrée (/40)

| Sprint | Story Points livrés (S/M) | XL livrés (50%) | Cumul |
|--------|---------------------------|-----------------|-------|
| Sprint 1 | ___ | ___ | ___ |
| Sprint 2 | ___ | ___ | ___ |
| Sprint 3 | ___ | ___ | ___ |
| Sprint 4 | ___ | ___ | ___ |

**Pénalité XL réussies** : ___ pts × 50% = - ___ points
**Malus XL échouées** : - ___ points
**Total Valeur métier** : ___/40 points

---

#### 2️⃣ Qualité du découpage (/20)

- **Taille moyenne des US** : ___ → ___/8 points
- **Éviter les XL** : ___ XL prises → ___/5 points
- **Taux de complétion** : ___% → ___/7 points

**Total Découpage** : ___/20 points

---

#### 3️⃣ Gestion de la dette technique (/25)

- **US techniques terminées** : ___ × 3 = ___/15 points
- **Bonus utilisés** : ___ → ___/5 points
- **Dette non résolue** : ___ → ___/5 points

**Total Dette technique** : ___/25 points

---

#### 4️⃣ Excellence opérationnelle (/15)

- **Régularité de livraison** : ___% → ___/5 points
- **Respect du temps** : ___ → ___/5 points
- **Collaboration équipe** : ___ → ___/5 points

**Total Excellence** : ___/15 points

---

### 🏆 SCORE FINAL

```
Valeur métier :         ___/40
Qualité découpage :     ___/20
Dette technique :       ___/25
Excellence opérat. :    ___/15
─────────────────────────────
TOTAL :                 ___/100

Niveau : _______________
```

---

## 🎓 Débriefing - Questions de réflexion

À la fin du jeu, l'animateur pose ces questions aux équipes :

### Sur la valeur métier
- Qu'avez-vous priorisé et pourquoi ?
- Auriez-vous pu livrer plus de valeur ? Comment ?

### Sur le découpage
- Avez-vous bien estimé la complexité des tâches ?
- Quelles tâches auraient dû être découpées différemment ?

### Sur la dette technique
- Quand avez-vous investi dans les US techniques ?
- Les bonus ont-ils eu un impact sur votre vélocité ?

### Sur l'excellence opérationnelle
- Comment s'est passée la collaboration dans l'équipe ?
- Qu'auriez-vous fait différemment ?

---



## 🎯 Objectifs pédagogiques

Ce système de scoring vise à faire comprendre :

 - ✅ L'importance de **livrer régulièrement de la valeur**
 - ✅ L'art du **bon découpage** (ni trop gros, ni trop petit)
 - ✅ L'**investissement technique** paie sur le long terme
 - ✅ La **discipline** et la **collaboration** sont essentielles

**Bonne chance ! 🚀**
