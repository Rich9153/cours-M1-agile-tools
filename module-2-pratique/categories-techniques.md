# User Stories techniques

Ce document définit les US techniques et leurs critères , ainsi les bonus qu'elles débloquent dans le jeu.

---

## `[INFRA_TEST]` - Infrastructure de test

### Critères d'Acceptation
- mise en place de la librairie de tests dans le code → ⚂ Tirer **1 ou 2**
- Environnement de test isolé → ⚂ Tirer **3 ou +**
- Données de test automatisées (migration) → ⚃ Tirer **4 ou +**
- librairie d'assertions moderne   → ⚂ Tirer **impair**
- Containers de test (Docker) → ⚄ Tirer **pair**

### 🎁 Bonus débloqué
**🎲 +1 dé** : L'équipe peut lancer **2 dés** au lieu d'1 pour valider les critères d'acceptation (et garder le meilleur résultat)

---

## `[CI/CD]` - Intégration Continue / Déploiement Continu

### Critères d'Acceptation
- Pipeline CI/CD fonctionnel → ⚃ Tirer **4 ou +**
- Déploiement automatisé en staging → ⚂ Tirer **3 ou +**
- Déploiement automatisé en production → ⚄ Tirer **impair**
- Rollback automatique en cas d'erreur → ⚄ Tirer **5 ou +**
- Build automatique sur commit → ⚂ Tirer **3 ou +**

### 🎁 Bonus débloqué
**🔒 Critères permanents** : Les critères marqués `[CI/CD]` une fois validés ne doivent **plus être rejoués** dans les sprints suivants

---

## `[DEVOPS]` - DevOps & Automatisation

### Critères d'Acceptation
- Infrastructure as Code (Terraform, Ansible) → ⚄ Tirer **5 ou +**
- Monitoring et alerting (Prometheus, Grafana) → ⚃ Tirer **4 ou +**
- Logs centralisés (ELK, Loki) → ⚃ Tirer **impair**
- Gestion des secrets (Vault) → ⚄ Tirer **5 ou +**
- Auto-scaling → ⚅ Tirer **6**

### 🎁 Bonus débloqué
**🔄 Relance** : L'équipe peut **relancer 1 dé** par sprint (choisir quel dé relancer)

---

## `[TESTS]` - Qualité des tests
  
**ne peut se jouer que si [INFRA_TEST] est en place**

### Critères d'Acceptation
- Tests unitaires exécutés en < 3 minutes → ⚂ Tirer **3 ou +**
- Couverture de tests > 80% → ⚃ Tirer **4 ou +**
- Tests d'intégration automatisés → ⚃ Tirer **impair**

### 🎁 Bonus débloqué
**🔒 Critères permanents** : Les critères marqués `[TESTS]` une fois validés ne doivent **plus être rejoués** dans les sprints suivants

---

## `[ARCHI]` - Architecture & Design

### Critères d'Acceptation
*(tirer le dé, si la valeur correspond aux critères ci dessous, alors ils sont validés, sinon continuer à tirer)*
- Documentation architecture à jour (C4, ADR) → ⚃ Tirer **4 ou +**
- Code review systématique (obligatoire) → ⚂ Tirer **3 ou +**
- Refactoring de la dette technique → ⚃ Tirer **4 ou +**
- Design patterns documentés → ⚄ Tirer **5 ou +**
- Diagrammes UML/Architecture → ⚃ Tirer **4 ou +**

### 🎁 Bonus débloqué
**🔒 Critères permanents** : Les critères marqués `[ARCHI]` une fois validés ne doivent **plus être rejoués** dans les sprints suivants

---

## `[PERF]` - Performance

### Critères d'Acceptation
- Temps de réponse API < 200ms → ⚃ Tirer **4 ou +**
- Optimisation des requêtes BDD → ⚂ Tirer **3 ou +**
- Cache distribué (Redis) → ⚄ Tirer **5 ou +**
- Profiling de performance → ⚃ Tirer **pair**
- Load testing automatisé → ⚄ Tirer **impair**

### 🎁 Bonus débloqué
**⏱️ Temps supplémentaire** : L'équipe gagne **+30 secondes** de temps de jeu par sprint

---

## `[SECU]` - Sécurité

### Critères d'Acceptation
- Scan de vulnérabilités automatisé → ⚃ Tirer **4 ou +**
- Authentification/Autorisation robuste → ⚄ Tirer **5 ou +**
- Chiffrement des données sensibles → ⚄ Tirer **pair**
- HTTPS obligatoire → ⚂ Tirer **3 ou +**
- Protection CSRF/XSS → ⚃ Tirer **impair**

### 🎁 Bonus débloqué
**🔒 Critères permanents** : Les critères marqués `[SECU]` une fois validés ne doivent **plus être rejoués** dans les sprints suivants

---

## Règles d'application des bonus

1. **Cumul des bonus** : Les bonus de différentes catégories se cumulent
2. **Activation** : Un bonus s'active dès qu'une US technique de la catégorie est **complètement terminée** (tous ses critères validés au dé)
3. **Permanence** : Les bonus restent actifs pour tous les sprints suivants

---

## 💡 Idées pour pimenter le jeu

### 🎯 Événements aléatoires (optionnel)
À chaque début de sprint, l'équipe peut tirer **1d6** pour un événement :
- **1** : 🐛 Bug critique ! un bug est tiré au sort
- **2** : 📉 Dette technique : Tous les critères à 4+ deviennent 5+ ce sprint, et 3+ deviennent 4+
- **3-4** : ✅ Rien de spécial
- **5** : 🎁 Coup de pouce : Un critère au choix réussit automatiquement
- **6** : ⚡ Productivité maximale : +1 minute de temps de jeu ce sprint

### 🏆 Défis d'équipe
- **Sprint parfait** : Si tous les critères sont validés du premier coup, +2 points de vélocité bonus
- **Combo technique** : Valider 3 US techniques dans le même sprint = débloquer **tous** les bonus immédiatement
- **Mode hardcore** : Augmenter tous les seuils de dé de +1 pour plus de difficulté

---
