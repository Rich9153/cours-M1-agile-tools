# Guide de l'animateur - Système de Scoring - FlowMaster Agile Game

## 🎲 Principe général

Chaque **User Story** est décomposée en **critères d'acceptation**. Chaque critère a une **valeur de dé (1 à 6)**.

Pour valider un critère, l'équipe doit **lancer un dé** et obtenir **exactement la valeur** indiquée sur le critère.

---

## ⏱️ Contrainte de temps

- Chaque sprint dispose d'un **temps limité** pour jouer les dés (ex: 2-3 minutes par sprint)
- Ce temps est **volontairement court** pour simuler la pression d'un vrai sprint
- Résultat : **certaines User Stories resteront incomplètes** à la fin du sprint

---

## ✅ Complétion d'une User Story

Une User Story est considérée comme **TERMINÉE** uniquement si :
- ✅ **Tous ses critères d'acceptation** sont validés (dés correspondants obtenus)
- ✅ La **Definition of Done (DoD)** est respectée

Si un seul critère manque, la story reste **EN COURS** et doit être rejouée au sprint suivant (sauf critères permanents, voir bonus).

---

## 🎯 Types de User Stories

### 📦 User Stories Fonctionnelles
- Apportent de la **valeur métier** directe (features utilisateur)
- Exemples : créer un compte, ajouter au panier, passer commande
- **Ne débloquent pas de bonus**, mais font avancer le produit

### ⚙️ User Stories Techniques
- Améliorent l'**infrastructure, la qualité et la vélocité**
- Exemples : CI/CD, tests unitaires, monitoring
- **Débloquent des bonus permanents** qui facilitent les sprints suivants

---

## 🎁 Système de Bonus (US Techniques)

Les **User Stories techniques** débloquent des **bonus permanents** pour tous les sprints suivants.

### Liste des bonus disponibles

| Catégorie | Bonus débloqué | Description | US exemples |
|-----------|----------------|-------------|-------------|
| `[INFRA_TEST]` | 🎲 **+1 dé** | Lancer **2 dés** au lieu d'1 | Infrastructure de test, BDD de test |
| `[CI/CD]` | 🔒 **Critères permanents** | Les critères `[CI/CD]` validés **ne se rejouent plus** | Pipeline CI/CD, déploiement auto |
| `[TESTS]` | 🔒 **Critères permanents** | Les critères `[TESTS]` validés **ne se rejouent plus** | Tests < 3min, couverture > 80% |
| `[ARCHI]` | 🔒 **Critères permanents** | Les critères `[ARCHI]` validés **ne se rejouent plus** | Doc architecture, code review |
| `[SECU]` | 🔒 **Critères permanents** | Les critères `[SECU]` validés **ne se rejouent plus** | Scan vulnérabilités, auth robuste |
| `[DEVOPS]` | 🔄 **Relance** | Relancer **1 dé** par sprint | Monitoring, logs centralisés, IaC |
| `[PERF]` | ⏱️ **+30 secondes** | Temps de jeu **augmenté** de 30s | Optimisation API, cache, profiling |

### Cumul des bonus

- ✅ **Les bonus se cumulent** entre différentes catégories
- ✅ **Les bonus restent actifs** pour tous les sprints suivants
- ✅ Activation : dès qu'une US technique est **100% complétée**

---

## 🍀  Changements et imprévus

**À chaque début de sprint, l'animateur annonce :**
- Nouveaux bugs découverts
- Changements de priorité
- Contraintes supplémentaires
- Opportunités business

**Réaction attendue :**
- **Scrum** : Absorber dans le prochain sprint (sauf bug critique)
- **Kanban** : Ajuster le backlog immédiatement

---

## 🧭 Stratégie recommandée

### Phase 1 : Débloquer le 2ème dé (Sprint 1-2)
**Objectif** : Terminer une US `[INFRA_TEST]` le plus tôt possible
- 🎯 Prioriser TECH-001 "Infrastructure de test"
- Impact : **Double les chances** de valider les critères

### Phase 2 : Sécuriser avec des critères permanents (Sprint 2-3)
**Objectif** : Valider des US `[CI/CD]`, `[TESTS]`, `[SECU]`
- 🎯 Prioriser TECH-002 "Pipeline CI/CD" ou TECH-003 "Tests rapides"
- Impact : **Réduire la dette** en rendant certains critères définitifs

### Phase 3 : Maximiser la vélocité (Sprint 4-6)
**Objectif** : Débloquer relances et temps supplémentaire
- 🎯 Compléter TECH-004 "Monitoring" `[DEVOPS]`
- Impact : **Flexibilité maximale** pour terminer les stories difficiles

### Phase 4 : Sprints fonctionnels (Sprint 4-6)
**Objectif** : Délivrer un maximum de valeur métier
- 🎯 Profiter des bonus pour enchaîner les US fonctionnelles
- Impact : **MVP riche et stable**

---

## 📋 Structure d'une carte User Story

Chaque US est documentée dans un fichier `.md` distinct :

```markdown
# US-XXX : Titre

## Type
- [x] Fonctionnelle / Technique

## Description
En tant que [rôle], je veux [action], afin de [bénéfice].

## Critères d'acceptation

### ☑️ Critère 1 : Description
- Catégorie : `[CATEGORIE]`
- Valeur du dé : 🎲 **X**
- Statut : ⬜ Non validé / ✅ Validé
- Permanent : ❌ Non / ✅ Oui

[... autres critères ...]

## Bonus débloqué (pour US techniques)
🎁 Description du bonus

## Historique des tentatives
| Sprint | Dés lancés | Critères validés | Statut |
|--------|------------|------------------|--------|
```

---

## 🎲 Déroulement d'un sprint (mécanique de jeu)

### 1. Planning (1-2 min)
- Sélectionner les US à traiter dans le sprint
- Vérifier les dépendances

### 2. Phase de jeu (2-3 minutes - CHRONOMÈTRE)
- ⏱️ **Lancer le chronomètre**
- 🎲 Lancer les dés pour valider les critères
- ✅ Cocher les critères validés dans les fichiers `.md`
- 🔄 Utiliser les bonus (relances, dés supplémentaires)

### 3. Fin du sprint
- ⏹️ **STOP** quand le temps est écoulé
- 📊 Compter les US terminées (tous critères validés)
- 📝 Mettre à jour le board

### 4. Rétrospective (5 min)
- Analyser la vélocité
- Ajuster la stratégie pour le prochain sprint

---

## 📁 Organisation des fichiers

```
module-2-pratique/
├── categories-techniques.md          # Référence des catégories et bonus
├── systeme-de-scoring.md             # Ce fichier
├── user-stories/
│   ├── TEMPLATE.md                   # Template vierge
│   ├── EPIC-1-FM-001-creer-compte-artisan.md
│   ├── EPIC-4-FM-024-ajouter-produit-panier.md
│   ├── TECH-001-infrastructure-test.md
│   ├── TECH-002-pipeline-ci-cd.md
│   ├── TECH-003-tests-unitaires-rapides.md
│   └── TECH-004-monitoring-devops.md
└── regles-du-jeu.md
```

---

## 🎯 Objectif pédagogique

Ce système simule **les réalités d'un projet agile** :

1. ⏱️ **Contrainte de temps** : On ne peut pas tout faire dans un sprint
2. 🎲 **Incertitude** : Les estimations ne garantissent pas la réussite
3. ⚙️ **Dette technique vs features** : Investir dans la technique rapporte à long terme
4. 🚀 **Vélocité croissante** : Les bonnes pratiques accélèrent le développement
5. 🎯 **Priorisation critique** : Il faut faire des choix stratégiques

---

## 📖 Voir aussi

- [Categories techniques](./categories-techniques.md) - Détail de chaque catégorie
- [Règles du jeu](./regles-du-jeu.md) - Règles complètes
- [Backlog initial](./backlog-initial.md) - Liste des 40 US fonctionnelles
- [Template US](./user-stories/TEMPLATE.md) - Modèle vierge pour créer de nouvelles US
