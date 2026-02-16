# US-DORA-1 : Mettre en place les métriques DORA

## Type
- [ ] Fonctionnelle
- [x] Technique

## Particularité

*Cette US est à remettre en jeu à chaque sprint. 
Elle ne se conserve pas d'un sprint à l'autre.*

Et si la valeur du dé est incompatible avec le critère, cette US est perdue pour le sprint.

## Description
En tant qu'**équipe de développement**,
Je veux **mettre en place les métriques DORA** (Deployment Frequency, Lead Time, MTTR, Change Failure Rate),
Afin d'**améliorer notre performance de livraison** et **bénéficier d'un multiplicateur de valeur métier ×2**.

## Complexité estimée
**Story Points** : 13 pts

## Critères d'acceptation

### ☑️ Critère 1 : Deployment Frequency (Fréquence de déploiement)
- **Catégorie** : `[CI/CD]`
- **Valeur du dé** : 🎲 **3 +**
- **Statut** : ⬜ Non validé
- **Permanent** : ✅  Oui si  `[CI/CD]` en place

**Description** : Un système automatique mesure et affiche la fréquence de déploiement en production (nombre de déploiements par jour/semaine). Métrique visible dans un dashboard.

---

### ☑️ Critère 2 : Lead Time for Changes (Délai de livraison)
- **Catégorie** : `[DEVOPS]`
- **Valeur du dé** : 🎲 **4 +**
- **Statut** : ⬜ Non validé
- **Permanent** : ✅  Oui si `[DEVOPS]` en place

**Description** : Le temps écoulé entre le commit du code et son déploiement en production est mesuré automatiquement (via Git + CI/CD). Moyenne calculée et affichée.

---

### ☑️ Critère 3 : Mean Time to Recovery (MTTR - Temps moyen de récupération)
- **Catégorie** : `[DEVOPS]`
- **Valeur du dé** : 🎲 **pair**
- **Statut** : ⬜ Non validé
- **Permanent** : ✅  Oui si `[SECU]` ou `[PERF]` en place

**Description** : Le temps moyen pour restaurer le service après un incident est mesuré (depuis détection de l'incident jusqu'à résolution). Historique des incidents tracé.

---

### ☑️ Critère 4 : Change Failure Rate (Taux d'échec des changements)
- **Catégorie** : `[DEVOPS]`
- **Valeur du dé** : 🎲 **impair**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Le pourcentage de déploiements causant des incidents en production est calculé automatiquement (déploiements échoués ou rollbackés / total déploiements).


---

## ⚠️ RÈGLE SPÉCIALE 

Cette US fonctionne différemment des autres :

📌 **Réévaluation à chaque sprint** :
- Cette US peut être tentée sur plusieurs sprints consécutifs
- À chaque sprint où l'équipe travaille dessus, on lance **1 dé par critère non validé**
- A chaque nouveau sprint, on rejoue tous les critères, sauf si on a acquis les bonus permanent 

📌 **Stratégie** :
- Commencer tôt (Sprint 2-3) pour avoir plusieurs chances de validation
- Chaque sprint apporte des progrès incrémentaux
- Possibilité d'activer le bonus ×2 même si l'US n'est pas 100% complète (voir Notes)

---

## Notes

### Dépendances
- [x] TECH-002 : Pipeline CI/CD (recommandé pour automatiser les métriques)
- [x] TECH-004 : Monitoring et alerting (recommandé pour MTTR)

### Bonus débloqué (US technique spéciale)
🎁 **🚀 MULTIPLICATEUR DORA ×2** : Une fois cette US complétée, **toutes les valeurs métier** des US terminées **après son achèvement** sont **multipliées par 2** jusqu'à la fin du jeu !

Ce bonus représente l'impact massif des métriques DORA sur la performance et la valeur délivrée par l'équipe. 
Les équipes qui maîtrisent DORA livrent 2× plus vite.

### Historique des tentatives

| Sprint | Dés lancés | Critères validés | Statut |
|--------|------------|------------------|--------|
| - | - | - | ⏳ Pas encore jouée |

---

## Définition of Done (DoD)
- [ ] Tous les critères d'acceptation sont validés (4/4)
- [ ] Dashboard DORA accessible à toute l'équipe
- [ ] Les 4 métriques affichent des données réelles
- [ ] Démo technique préparée pour la revue de sprint

---



## Conseil stratégique

🏆 **US STRATÉGIQUE GAME-CHANGER** : Cette US est la plus puissante du jeu ! Avec 4 critères et une difficulté élevée (13 pts), elle est risquée mais offre un retour sur investissement massif.

**Quand la jouer ?**
- ✅ **Commencer en Sprint 2-3** pour avoir plusieurs sprints de progression et maximiser le bonus ×2
- ✅ **Utiliser les bonus de catégorie** pour rendre certains critères permanents (`[CI/CD]`, `[DEVOPS]`, `[SECU]`, `[PERF]`)
- ❌ **PAS en Sprint 1** : trop tôt, pas assez de bonus techniques disponibles
- ❌ **PAS après Sprint 4** : pas assez de sprints restants pour profiter du multiplicateur

**ROI calculé** : Si complétée en Sprint 3, et que l'équipe livre ~30 pts de valeur métier dans les 3 sprints suivants → 30 pts supplémentaires gagnés grâce au multiplicateur ×2 !

⚠️ **Important** : Avec 4 critères et 1 seul lancement par critère, planifier de travailler sur cette US pendant 2-3 sprints consécutifs pour maximiser les chances de complétion.
