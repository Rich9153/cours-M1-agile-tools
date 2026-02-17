# Règles du Jeu - FlowMaster Serious Game

## Vue d'ensemble

**Objectif :** Livrer un maximum de valeur en 6 sprints tout en gérant les imprévus.

**Durée :** 3h (dont 2h de jeu effectif)

**Équipes :** 4-5 personnes

---

## Phase 1 : Scrum / Flux Poussé (3 sprints × 20 min)

### Principe du flux poussé

- On **planifie** tout au début de chaque sprint (Sprint Planning)
- On s'engage sur un ensemble de stories
- On **pousse** le travail dans le sprint
- On ne peut **PAS** changer le contenu du sprint en cours

### Déroulement d'un sprint (20 min)

| Étape | Durée | Activité                                                 |
|-------|-------|----------------------------------------------------------|
| **Sprint Planning** | 5 min | Sélectionner les stories (max vélocité), créer le Sprint |
| **Développement** | 5 min | Réaliser les stories (écrire livrables)                  |
| **Daily Standup** | 0 min | À mi-parcours (rapide tour de table)                     |
| **Sprint Review** | 1 min | Démo des stories; tirer 6 au dé pour que ce soit Done    |
| **Retrospective** | 1 min | 1 action d'amélioration                                  |

**Contrainte Scrum :** Pas de nouveau travail en cours de sprint (sauf bugs critiques)

---

## Phase 2 : Kanban / Flux Tiré (3 sprints × 20 min)

### Principe du flux tiré

- Pas de sprint fixe, **flux continu**
- On **tire** le travail quand on a de la capacité
- **WIP limits** (Work In Progress) par colonne
- On peut changer les priorités **à tout moment**

### Déroulement d'une itération (20 min)

| Étape | Durée | Activité |
|-------|-------|----------|
| **Replenishment** | 2 min | Re-prioriser le backlog si nécessaire |
| **Flow** | 16 min | Tirer les stories, respecter WIP limits |
| **Review** | 1 min | Compter les stories livrées |
| **Retrospective** | 1 min | 1 action d'amélioration |

**Contrainte Kanban :** Respecter les WIP limits (ex: max 3 stories "In Progress")

---

## Règles communes aux 2 phases

### 1. Vélocité / Capacité

**Vous avez une capacité limitée par sprint/itération :**

- **Sprint 1-2** : Vélocité = 20 points max
- **Sprint 3-4** : Vélocité = 25 points max (équipe monte en compétence)
- **Sprint 5-6** : Vélocité = 22 points max (un dev part en vacances)

**Important :** Vous NE pouvez PAS prendre plus de points que votre vélocité !

---

### 2. Definition of Done (DoD) - CRUCIALE

**Une story n'est Done QUE si :**

✅ **Tous les critères d'acceptation sont cochés** dans Jira

✅ **Un livrable a été produit** (voir section Livrables ci-dessous)

✅ **Le PO a validé** (vérifié la DoD)

✅ **La story est passée en "Done"** dans Jira

**Attention :** Une story non Done à la fin du sprint/itération **ne compte PAS** pour la vélocité et doit retourner au backlog !

---

### 3. Types de livrables (au choix selon la story)

Comme on ne peut pas coder en 3h, voici ce que vous devez produire pour qu'une story soit Done :



---

####  Système de dés avec critères d'acceptation 🎲 **[RETENUE]**

**Format :** Validation des critères d'acceptation par lancer de dés

**Principe :**
- Chaque User Story possède des **critères d'acceptation** numérotés de 1 à 6
- L'équipe dispose d'un **temps limité par sprint** pour lancer les dés (2-3 minutes)
- Pour valider un critère, il faut **obtenir exactement la valeur du dé** indiquée sur le critère
- Une User Story est **terminée** uniquement si **tous ses critères** sont validés

**Bonus techniques :**
- Des **User Stories techniques** débloquent des bonus permanents :
  - `[INFRA_TEST]` → 🎲 **+1 dé** (lancer 2 dés au lieu d'1)
  - `[CI/CD]` → 🔒 **Critères permanents** (ne plus rejouer les critères `[CI/CD]` validés)
  - `[TESTS]` → 🔒 **Critères permanents**
  - `[DEVOPS]` → 🔄 **Relancer 1 dé par sprint**
  - `[PERF]` → ⏱️ **+30 secondes de temps**
  - `[SECU]` → 🔒 **Critères permanents**
  - `[ARCHI]` → 🔒 **Critères permanents**

**Exemple pour EPIC-1-FM-001 (Créer un compte artisan) :**
```
CRITÈRES D'ACCEPTATION

☑️ Critère 1 : Formulaire d'inscription fonctionnel
- Valeur du dé : 🎲 1
- Statut : ⬜ Non validé

☑️ Critère 2 : Validation des données [SECU]
- Valeur du dé : 🎲 4
- Statut : ⬜ Non validé
- Permanent : ✅ Oui (si bonus [SECU] actif)

☑️ Critère 3 : Compte créé en base de données
- Valeur du dé : 🎲 3
- Statut : ⬜ Non validé

☑️ Critère 4 : Email de bienvenue envoyé
- Valeur du dé : 🎲 5
- Statut : ⬜ Non validé
```

**Déroulement :**
1. **Sprint Planning** : Sélectionner les US à traiter
2. **Phase de jeu (2-3 min CHRONO)** :
   - Lancer les dés pour valider les critères
   - Cocher les critères validés dans les fichiers `.md`
   - Utiliser les bonus si débloqués
3. **Fin du sprint** : Compter les US terminées (tous critères validés)



**Fichiers de référence :**
- `systeme-de-scoring.md` - Documentation complète du système
- `categories-techniques.md` - Liste des catégories et bonus
- `user-stories/*.md` - Templates de critères par EPIC

**Temps estimé :** 2-3 min de jeu de dés par sprint + suivi des critères validés

---



### 4. Critères d'acceptation dans JIRA(optionnel)


**Utilisez la checklist de Jira** (ou les sous-tâches) :

Exemples :
```
Story EPIC-1-FM-1 (Créer un compte artisan):
- [ ] Formulaire avec email, mot de passe, nom, prénom
- [ ] Email unique (vérification BDD)
- [ ] Mot de passe min 8 caractères (1 majuscule, 1 chiffre)
- [ ] Email de confirmation envoyé
- [ ] Compte créé en BDD (statut: en attente de validation)
```

---

### 5. Gestion des bugs

**Les bugs apparaissent au début de certains sprints** (voir phases-et-evenements.md)

**Règles bugs :**

- **Bug Critique** : DOIT être traité en priorité (même en cours de sprint Scrum)
- **Bug Haute** : Priorité haute, mais peut attendre le prochain sprint
- **Bug Moyenne** : Backlog normal

**Estimation des bugs :** 1-3 points selon complexité

**DoD Bug :**
- Décrire le problème identifié
- Décrire la solution (modification apportée)
- Cas de test pour éviter la régression

---

### 6. Gestion du temps

**Chronomètre strict :**
- Le Scrum Master/Facilitateur chronomètre chaque phase
- À la fin du temps imparti → STOP, on passe à l'étape suivante
- Stories non terminées → retournent au backlog (même si à 90% !)

**Réalisme :** C'est frustrant, mais c'est la vraie vie ! On apprend à mieux estimer et à découper.

---

### 7. Workflow Jira

**Colonnes du board :**

```
BACKLOG → TO DO → IN PROGRESS → REVIEW → DONE
```

**Phase 1 (Scrum) :**
- Sprint Planning : Déplacer stories du BACKLOG vers le Sprint (TO DO)
- Dev : Déplacer TO DO → IN PROGRESS → REVIEW
- Review : PO valide et déplace REVIEW → DONE

**Phase 2 (Kanban) :**
- WIP Limits :
  - IN PROGRESS : max 3 stories
  - REVIEW : max 2 stories
- Dès qu'une colonne libère de la place → tirer du backlog

---

### 8. Métriques à tracker

**À noter à chaque fin de sprint/itération :**

| Métrique | Description | Comment calculer |
|----------|-------------|------------------|
| **Story Points livrés** | Somme des points des stories Done | Additionner les estimations |
| **Nb stories livrées** | Nombre de stories Done | Compter |
| **Lead Time moyen** | Temps moyen de To Do → Done | (Temps total) / Nb stories |
| **Cycle Time moyen** | Temps moyen de In Progress → Done | (Temps total actif) / Nb stories |
| **WIP moyen** | Nombre moyen de stories en cours | Observer pendant le sprint |
| **Valeur livrée** | Somme de la valeur business | Si valeur estimée |

**Outil :** Utiliser fiche-metriques.md ou Jira Reports

---

---

### 10. Rotation des rôles

**Entre Phase 1 et Phase 2 :**
- Le PO devient Dev
- Un Dev devient PO
- Le Scrum Master/Facilitateur peut rester OU tourner

**Objectif :** Expérimenter différentes perspectives

---

## Critères de réussite

### Réussite minimale (MVP)

✅ **Au moins 1 parcours utilisateur complet fonctionnel :**
- Exemple : Artisan crée compte → ajoute produit → Client voit produit → achète (avec paiement)

✅ **Au moins 80 points de valeur livrés** (sur ~200 au total)

---

### Réussite excellente

✅ Tous les parcours MVP fonctionnels

✅ Au moins 120 points livrés

✅ Bugs critiques tous résolus

✅ Amélioration du flow entre Phase 1 et Phase 2 (Lead Time réduit de 20%+)

---

## Conseils stratégiques

**💡 Stratégies gagnantes observées :**

1. **Focus MVP** : Faire d'abord un parcours bout-en-bout fonctionnel
2. **Découper finement** : Stories > 8 pts → découper en plus petites
3. **Faire simple** : Livrables minimaux mais respectant la DoD
4. **Paralléliser** : Plusieurs devs travaillent sur des stories indépendantes
5. **Communiquer** : Daily/Standup vraiment utiles pour débloquer

**🚨 Pièges à éviter :**

1. **Surestimer la vélocité** : Mieux vaut sous-promettre et sur-livrer
2. **Stories trop grosses** : Difficile à terminer dans le temps
3. **Zapper la DoD** : Stories "presque finies" → frustrantes et non comptées
4. **Ignorer les bugs** : Ils s'accumulent et bloquent tout
5. **Pas de priorisation** : Faire les stories "fun" avant les stories "utiles"

---

## Débriefing final (Phase 1 vs Phase 2)

**Questions à discuter :**

1. **Productivité** : Avez-vous livré plus de points en Scrum ou en Kanban ?
2. **Réactivité** : Dans quelle phase avez-vous mieux géré les imprévus ?
3. **Stress** : Quelle approche était la plus stressante ? Pourquoi ?
4. **Qualité** : Avez-vous mieux respecté la DoD dans une phase ?
5. **Préférence** : Quelle méthode préférez-vous ? Pour quel type de projet ?

---

**Prêts ? Let's go ! 🚀**
