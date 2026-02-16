# 🏆 Système de Scoring - Jeu Agile

Ce document définit comment calculer le score final des équipes à la fin du jeu.

---

## 📊 Composantes du Score

Le score final est calculé selon **4 piliers** :

### 1️⃣ Valeur métier livrée

**Calcul** : Valeur métier accumulée sur tous les sprints

#### Scoring
- **1 point de valeur métier = 1 point de score** (pour tailles S et M uniquement)
- **⚠️ Pénalité XL réussie** : Les tâches XL comptent seulement **50% de leur valeur métier** (floues, difficiles à estimer, valeur métier incertaine)
- **❌ Malus échouée** : AU DEUXIEME TOUR et suivants: **-50% de la valeur métier** de la tâche non terminée
- **📉 Malus US ouvertes** : retrancher 2 × valeur métier pour chaque US **non commencée** en fin de sprint (work-in-progress excessif)
- **📈 Malus vélocité non alignée** : à la 2e itération vous devez appliquer la vélocité constatée à la 1ère itération (= votre capacité à produire). Si en fin de sprint, votre vélocité n'est pas atteinte, c'est à dire que vous avez moins de points effectués que prévu, **retrancher cette différence de points au score**.  

> US ouvertes veut dire: non commencées

#### Formule de calcul
```
Score = Σ(valeur métier S/M livrées × multiplicateur DORA)
      + Σ(valeur métier XL livrées × 0.5 × multiplicateur DORA)
      - Σ(story points échouées × 0.5)
      - (story points des US ouvertes en fin de sprint × 2)

Valeur Multiplicateur DORA :
 = 1 si DORA-1 non complétée
 = 2 pour toutes les US terminées APRÈS la complétion de DORA-1
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
- 
- **🚀 BONUS DORA** : Si l'US technique **DORA-1** est complétée, **toutes les valeurs métier** des US terminées **après son achèvement** sont **multipliées par 2** !


---

## 🎯 Score Final

### Calcul

```
Score Total = Valeur métier (40)
            + Qualité découpage (20)
            + Dette technique (25)       
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
 - ✅ L'art du **bon découpage** ()
 - ✅ L'**investissement technique** paie sur le long terme
 - ✅ La **discipline** et la **collaboration** sont essentielles

**Bonne chance ! 🚀**
