# FEAT-041 : Paiement Stripe URGENT (Changement de priorité)

## Type
- [x] Fonctionnelle
- [ ] Technique
- [x] **Changement de priorité** 🚨

## Contexte du changement
📞 **Alerte du CEO (Sprint 3)** : Un investisseur souhaite voir le paiement Stripe fonctionnel **absolument avant la fin du Sprint 3** pour valider un financement de 500K€.

**Conséquence** : Cette US devient **prioritaire sur tout le reste** et doit être terminée dans le sprint en cours, même si cela nécessite de dépiler d'autres stories.

## Description
En tant que **client**,
Je veux **payer par carte bancaire via Stripe**,
Afin de **régler ma commande de manière sécurisée**.

## Complexité estimée
**Story Points** : 13 pts (très complexe - intégration externe)

## Critères d'acceptation

### ☑️ Critère 1 : Compte Stripe configuré
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **2**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Un compte Stripe est créé (test + production). Les clés API (public & secret) sont configurées en variables d'environnement.

---

### ☑️ Critère 2 : Intégration Stripe Checkout
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **5**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : L'API Stripe est intégrée. Le client est redirigé vers Stripe Checkout lors de la validation du panier. Session de paiement créée avec montant correct.

---

### ☑️ Critère 3 : Gestion des webhooks Stripe
- **Catégorie** : `[DEVOPS]`
- **Valeur du dé** : 🎲 **6**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Un webhook reçoit les événements Stripe (payment_intent.succeeded, payment_intent.failed). La commande est mise à jour en base selon le statut du paiement.

---

### ☑️ Critère 4 : Gestion des erreurs de paiement
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **3**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Si le paiement échoue, l'utilisateur est redirigé avec un message clair ("Paiement refusé") et peut réessayer. La commande reste "en attente de paiement".

---

### ☑️ Critère 5 : Sécurité PCI-DSS
- **Catégorie** : `[SECU]`
- **Valeur du dé** : 🎲 **4**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non (✅ Oui si bonus `[SECU]` actif)

**Description** : Aucune donnée de carte bancaire ne transite par notre serveur (Stripe hosted). Les clés API sont stockées de manière sécurisée (secrets manager, .env non commité).

---

### ☑️ Critère 6 : Tests avec cartes de test Stripe
- **Catégorie** : `[TESTS]`
- **Valeur du dé** : 🎲 **1**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non (✅ Oui si bonus `[TESTS]` actif)

**Description** : Tests automatisés avec les cartes de test Stripe vérifient : paiement réussi (4242...), paiement échoué (4000 0000 0000 0002), 3D Secure.

---

### ☑️ Critère 7 : Démonstration fonctionnelle pour l'investisseur
- **Catégorie** : _Aucune_
- **Valeur du dé** : 🎲 **5**
- **Statut** : ⬜ Non validé
- **Permanent** : ❌ Non

**Description** : Parcours complet démontrable : ajouter produit → panier → paiement Stripe → confirmation commande. Déployé en staging accessible publiquement.

---

## Notes

### Dépendances
- [x] EPIC-4-FM-28 : Passer commande (valider le panier)
- [x] EPIC-4-FM-25 : Voir mon panier

### Priorité
🔴🔴🔴 **URGENT - DEADLINE INVESTISSEUR**

⚠️ **Impact sur le sprint** :
- Cette US doit être terminée **avant la fin du Sprint 3**
- Peut nécessiter de **dé-prioriser** d'autres US planifiées
- Toute l'équipe doit se concentrer dessus si nécessaire

### Bonus débloqué
_Aucun (US fonctionnelle, mais débloque le financement !)_

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
- [ ] Démonstration réussie devant le CEO
- [ ] Déployé en staging
- [ ] Documentation de l'intégration Stripe disponible

---

## Conseil stratégique pour l'équipe

💡 **Dilemme agile réaliste** :

Vous êtes au Sprint 3. Vous aviez planifié d'autres US. Le CEO arrive avec cette demande urgente.

**Questions à se poser en équipe** :
1. Acceptez-vous de tout arrêter pour cette US ?
2. Négociez-vous avec le CEO pour repousser d'un sprint ?
3. Demandez-vous des ressources supplémentaires ?
4. Réduisez-vous le scope (MVP du paiement Stripe) ?

**Rappel** : Cette US fait **13 points** et a **7 critères**. Très difficile à terminer en un sprint, surtout en urgence.

C'est un excellent exercice de gestion de priorités et de négociation avec le métier ! 🎯
