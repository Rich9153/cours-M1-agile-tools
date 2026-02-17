# FEAT-042 : Export CSV des commandes (Nouvelle demande client VIP)

## Type
- [x] Fonctionnelle
- [ ] Technique
- [x] **Nouvelle demande urgente** 🎯

## Contexte du changement
📞 **Appel du Sales (Sprint 4)** : Un gros artisan (représente potentiellement 30% du CA de la plateforme) refuse de signer le contrat tant qu'il n'a pas une fonctionnalité d'export CSV de ses commandes pour sa comptabilité.

**Enjeu** : Client stratégique qui pourrait amener 20 autres artisans de sa coopérative. Sans cette feature, il va chez le concurrent.

**Deadline** : Fin du Sprint 4 pour la démo commerciale.

## Description
En tant qu'**artisan**,
Je veux **exporter mes commandes en CSV**,
Afin de **gérer ma comptabilité facilement**.

## Complexité estimée
**Story Points** : 8 pts (intégration + format spécifique comptabilité)

## Critères d'acceptation

### ☑️ Critère 1 : Bouton d'export accessible
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **3**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Sur la page "Mes commandes", un bouton "Exporter en CSV" est visible et cliquable par l'artisan.

---

### ☑️ Critère 2 : API de génération du CSV
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **5**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Une API génère un fichier CSV contenant : date commande, N° commande, client (nom), produits (détail), quantités, montant HT, montant TTC, statut.

---

### ☑️ Critère 3 : Format comptabilité conforme
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **4**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Le CSV respecte un format importable dans les logiciels comptables (séparateur point-virgule, décimales avec virgule, encodage UTF-8 BOM).

---

### ☑️ Critère 4 : Filtrage des commandes à exporter
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **2**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : L'artisan peut choisir une période (date début - date fin) pour exporter uniquement les commandes de cette période (utile pour la compta mensuelle).

---

### ☑️ Critère 5 : Performance pour gros volumes
- **Catégorie** : `[PERF]`
- **Valeur du dé** : 🎲 **6**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : L'export fonctionne même avec 10 000+ commandes. Génération en arrière-plan (async) si > 1000 commandes, avec notification quand le fichier est prêt.

---

### ☑️ Critère 6 : Tests avec données réelles du client
- **Catégorie** : `[TESTS]`
- **Valeur du dé** : 🎲 **1**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non (✅ Oui si bonus `[TESTS]` actif)

**Description** : Le client VIP teste l'export avec ses données (données anonymisées fournies) et valide que c'est importable dans son logiciel (Sage, Ciel, Excel).

---

### ☑️ Critère 7 : Documentation utilisateur
- **Catégorie** : `[DOC]`
- **Valeur du dé** : 🎲 **3**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Un guide "Comment exporter mes commandes pour ma comptabilité" est disponible dans l'aide en ligne avec captures d'écran.

---

## Notes

### Dépendances
- [x] EPIC-5-FM-33 : Voir mes commandes reçues (artisan)

### Priorité
🟠 **Haute - Client stratégique**

⚠️ **Impact business** :
- Perte potentielle d'un gros client (30% CA)
- Perte de 20 autres artisans de la coopérative
- Argument de vente pour les prochains artisans

💡 **Négociation possible** : Proposer un MVP (export simple sans filtrage ni async) pour gagner du temps ?

### Bonus débloqué
_Aucun (US fonctionnelle)_

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
- [ ] Tous les critères d'acceptation sont validés (7/7)
- [ ] Validation par le client VIP (ou simulation)
- [ ] Déployé en production
- [ ] Documentation en ligne publiée

---

## Conseil stratégique pour l'équipe

💡 **Dilemme agile réaliste #2** :

Vous êtes au Sprint 4. Vous aviez planifié d'autres fonctionnalités pour le MVP. Le Sales arrive avec cette demande.

**Questions à se poser en équipe** :
1. Acceptez-vous de prioriser cette feature maintenant ?
2. Proposez-vous un MVP réduit (export basique) ?
3. Négociez-vous un délai (Sprint 5) avec le client ?
4. Cette feature fait-elle partie du MVP ou est-ce du "custom" pour un client ?

**Astuce** : Cette US fait **8 points** et a **7 critères**. C'est faisable mais ça va consommer une bonne partie du sprint.

**Débat intéressant** : Faut-il toujours dire "oui" aux demandes urgentes des clients ? Quel est l'impact sur la roadmap produit ? 🤔
