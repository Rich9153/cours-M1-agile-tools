# US-XL : Tâche de taille XL (Très grande)

## Type
- [x] Fonctionnelle
- [ ] Technique

## Description
En tant que développeur,
Je veux réaliser une **tâche complexe et ambitieuse**,
Afin de livrer une fonctionnalité majeure avec une très forte valeur métier.

## Complexité estimée
**Story Points** : **8-13 pts**

⚠️ **ATTENTION** : Les tâches XL sont **très risquées** et difficiles à compléter !

## Critères d'acceptation

### ☑️ Critère 1 : Architecture et conception
- **Catégorie** : `[ARCHI]` _(si bonus actif)_
- **Valeur du dé** : 🎲 Tirer **5**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non / ✅ Oui _(si bonus [ARCHI] actif)_

### ☑️ Critère 2 : Design Base de données
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 Tirer **4 ou +**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non

### ☑️ Critère 3 : Implémentation Back-End
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 Tirer **5 ou +**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non

### ☑️ Critère 4 : Implémentation Front-End
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 Tirer **5 ou +**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non

### ☑️ Critère 5 : Tests exhaustifs
- **Catégorie** : `[TESTS]` _(si bonus actif)_
- **Valeur du dé** : 🎲 Tirer **5 ou +**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non / ✅ Oui _(si bonus [TESTS] actif)_

### ☑️ Critère 6 : Performance et optimisation
- **Catégorie** : `[PERF]` _(si bonus actif)_
- **Valeur du dé** : 🎲 Tirer **3**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non / ✅ Oui _(si bonus [PERF] actif)_

### ☑️ Critère 7 : Sécurité et robustesse
- **Catégorie** : `[SECU]` _(si bonus actif)_
- **Valeur du dé** : 🎲 Tirer **1**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non / ✅ Oui _(si bonus [SECU] actif)_

### ☑️ Critère 8 : Intégration et validation
- **Catégorie** : `[CI/CD]` _(si bonus actif)_
- **Valeur du dé** : 🎲 Tirer **6**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non / ✅ Oui _(si bonus [CI/CD] actif)_

### ☑️ Critère 9 : Déploiement et monitoring
- **Catégorie** : `[DEVOPS]` _(si bonus actif)_
- **Valeur du dé** : 🎲 Tirer **pair**
- **Statut** : ⬜ Non validé / ✅ Validé
- **Permanent** : ❌ Non / ✅ Oui _(si bonus [DEVOPS] actif)_

---

## Notes

### Caractéristiques des tâches XL
- 🔥 **Très complexe** (> 8h de développement, souvent plusieurs jours)
- 🎯 **Scope large** : fonctionnalité majeure, refonte complète, feature stratégique
- 🎲 **Très difficile à valider** : seuils de dé élevés (5-6+)
- ⚠️ **Risque élevé** : peut monopoliser tout le sprint sans garantie de complétion
- 📦 **Exemples** :
  - Système d'authentification OAuth complet
  - Migration d'architecture (monolithe → microservices)
  - Moteur de recommandation ML
  - Marketplace complète avec paiement

### ⚡ Règles spéciales XL

#### ⚠️ Dépréciation de la valeur (même en cas de succès !)
Les tâches XL sont **floues et difficiles à estimer**. Leur valeur métier est **incertaine**.
- **Valeur dépréciée** : Même si complétée, les XL comptent seulement **50% de leurs story points** au scoring final
- **Exemple** : Une XL de 10 pts terminée = seulement **5 points** au score
- **Seul avantage en cas de succès** : Momentum (+1 sur tous les dés au prochain sprint)

#### 🚫 Pénalités en cas d'échec
Si la tâche XL **n'est pas terminée** à la fin du sprint :
- **-50% des points** : L'équipe perd la moitié des story points estimés
- **Dette technique** : Le prochain sprint commence avec un malus de -1 sur tous les dés
- **Pénalité découpage** : 0 points sur le critère "Éviter les XL" du scoring

#### 🔧 Recommandation : DÉCOUPER !
Il est **FORTEMENT recommandé** de découper une tâche XL en plusieurs tâches M/S pour :
- **Réduire le risque** d'échec complet
- **Livrer de la valeur incrémentale** (100% de la valeur au lieu de 50%)
- **Améliorer la prévisibilité** et le taux de complétion
- **Obtenir de meilleurs points** au scoring final

### Stratégie recommandée
- ❌ **À éviter** : Ne **jamais** prendre plusieurs XL dans un sprint
- ⚠️ **Risqué** : Ne prendre une XL que si l'équipe a les **bonus techniques** nécessaires
- ✅ **Idéal** : Découper en tâches plus petites et livrer progressivement

---

## Définition of Done (DoD)
- [ ] **TOUS** les critères d'acceptation sont validés (dés)
- [ ] Code reviewé par au moins 2 personnes
- [ ] Couverture de tests > 90%
- [ ] Documentation architecture complète (ADR, C4)
- [ ] Tests de charge et de sécurité réalisés
- [ ] Déploiement en staging validé
- [ ] Démo complète en revue de sprint
- [ ] Plan de rollback documenté
