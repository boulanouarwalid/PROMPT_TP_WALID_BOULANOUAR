

# 

**Nom :** Walid Boulanaour 

**Module :**  Ingénierie des Prompts pour la Génération de Code

# **TP : Ingénierie de prompt appliquée à la génération de code avec l'IA**

## Solution choisie : Augment Code (basé sur Claude 3.7 Sonnet)

### Définition
Augment Code est un assistant IA de programmation qui utilise le modèle Claude 3.7 Sonnet d'Anthropic pour aider les développeurs à générer, comprendre et déboguer du code dans divers langages de programmation via une interface conversationnelle.

### Avantages
- Capacité à comprendre le contexte du projet et à générer du code adapté aux besoins spécifiques
- Excellente compréhension des bonnes pratiques de programmation et des conventions de codage
- Peut expliquer le raisonnement derrière les solutions proposées, facilitant l'apprentissage

### Inconvénients
- Peut parfois générer du code qui semble correct mais contient des erreurs subtiles
- Connaissance limitée aux données d'entraînement (coupure des connaissances)
- Dépendance à la qualité du prompt - des instructions vagues produisent des résultats imprécis

### Cas d'utilisation typiques
- Génération rapide de fonctions utilitaires et d'algorithmes courants
- Débogage et refactoring de code existant
- Apprentissage de nouveaux langages ou frameworks en obtenant des exemples pratiques et des explications

## Exercices

### Exercice 2.1

#### Prompt Vague
"Écris une fonction pour faire des opérations entre deux nombres en Python."



![image-20250614123546503](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614123546503.png)





Analyse:
- **La fonction est-elle nommée ?** Oui, la fonction est nommée `calculate_numbers`, ce qui est descriptif mais ne correspond pas exactement au nom `calculate` demandé dans les spécifications.
- **Quelles opérations sont prises en charge ?** La fonction prend en charge quatre opérations de base : addition ("add"), soustraction ("subtract"), multiplication ("multiply") et division ("divide"). Cependant, elle utilise des chaînes complètes comme "add" au lieu des symboles '+', '-', '*', '/' mentionnés dans les spécifications.
- **Y a-t-il une gestion des erreurs ?** Il y a une gestion basique des erreurs : la division par zéro est détectée et renvoie un message d'erreur, et les opérations non reconnues renvoient également un message d'erreur. Cependant, il n'y a pas de validation du type des entrées.
- **Des commentaires ?** Non, le code ne contient aucun commentaire ni docstring expliquant l'utilisation de la fonction, ses paramètres ou ses valeurs de retour.

#### Prompt Spécifique
"Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de l'opération, gérer les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux décimales. Ajoute un docstring détaillé et des commentaires."

![image-20250614123646605](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614123646605.png)



Comparaison:
- **Robustesse**: La seconde version est nettement plus robuste. Elle vérifie les types d'entrée, utilise des exceptions Python appropriées plutôt que des messages d'erreur simples, et implémente correctement l'arrondi à deux décimales pour la division.
- **Lisibilité**: La seconde version est beaucoup plus lisible grâce à son docstring détaillé qui explique clairement les paramètres, les valeurs de retour et les exceptions possibles. Les commentaires ajoutent également à la clarté du code.
- **Couverture des cas**: La seconde version couvre davantage de cas d'erreur, notamment la validation des types d'entrée. Elle utilise également les symboles mathématiques standards comme demandé dans les spécifications, plutôt que des chaînes de caractères.

#### Prompt avec Persona
"En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '*', '/'). La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des commentaires clairs."

## Analyse Critique

1) **Différences observées entre les codes générés par chaque prompt**

   Le premier code (prompt vague) est basique, sans validation de types ni documentation. Le deuxième (prompt spécifique) ajoute une validation des types, des exceptions appropriées et un docstring complet. Le troisième (prompt avec persona) utilise des structures plus avancées (dictionnaire d'opérations), une documentation au format NumPy et des messages d'erreur plus détaillés.

2) **Principe de Prompt Engineering ayant eu le plus grand impact**

   La spécificité a eu l'impact le plus important. Le passage d'un prompt vague à un prompt spécifique a transformé un code basique en code robuste et bien documenté. La persona a principalement amélioré le style et la structure, mais les gains étaient moins importants que ceux apportés par la spécificité.

3) **Erreurs ou comportements inattendus introduits**

   Dans la première version, l'IA a utilisé des chaînes comme "add" au lieu de symboles '+', retourné des messages d'erreur au lieu d'exceptions, et omis l'arrondi pour les divisions. Dans la troisième version, il y a une redondance dans la gestion de la division par zéro (vérifiée deux fois).

4) **Coût en temps et en effort pour obtenir un code de haute qualité**

   Avec un prompt vague, il faut plusieurs itérations pour obtenir un code de qualité, ce qui multiplie le temps nécessaire par 3 à 5. Un prompt spécifique bien conçu permet d'obtenir un bon résultat dès la première génération, réduisant considérablement le temps et l'effort cognitif requis.

### Exercice 2.2

#### Prompt basé sur la Règle (zéro-Shot Prompting) :  
"Crée  une  fonction  Python  format_product_code(product_id).  Le  product_id  doit  être  une 
chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le 
7ème  caractère.  Si  la  chaîne  n'a  pas  10  caractères  ou  contient  des  caractères  non 
alphanumériques, elle doit lever une ValueError. Inclue un docstring." 



![image-20250614123812840](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614123812840.png)

#### Questions :
Le code est donc à la fois correct et robuste, répondant parfaitement aux exigences spécifiées dans le prompt.

#### Prompt basé sur l'Exemple (One-Shot Prompting) :
"Crée  une  fonction  Python  format_product_code(product_id).  Le  product_id  doit  être  une chaîne  de  10  caractères  alphanumériques.  Voici  un  exemple  d'entrée-sortie: format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit lever une ValueError si l'entrée est invalide. Inclue un docstring." 



![image-20250614124109978](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614124109978.png)

Question : Comparer avec le résultat précédent. L'exemple a-t-il simplifié la tâche de l'IA ? A-t-il aidé à éviter des erreurs ? 

#### Questions :
Différence principale : Le placement du second tiret a changé. Dans cette version, les tirets sont placés après les 3ème et 6ème caractères (format XXX-XXX-XXXX), alors que dans la version précédente, ils étaient placés après les 3ème et 7ème caractères (format XXX-XXXX-XX).
L'exemple a-t-il simplifié la tâche de l'IA ? Oui, l'exemple a clairement simplifié la tâche en fournissant un modèle concret de l'entrée et de la sortie attendues. Cela a permis à l'IA de comprendre exactement où placer les tirets, ce qui n'était pas explicitement mentionné dans le prompt précédent.
A-t-il aidé à éviter des erreurs ? Oui, l'exemple a aidé à éviter une erreur d'interprétation. Dans le prompt précédent, j'avais interprété "insérer un tiret après le 3ème et le 7ème caractère" comme signifiant que les tirets devraient être placés après les positions 3 et 7. Avec l'exemple, il est clair que le format attendu est "ABC-123-DEF4", ce qui correspond à des tirets après les positions 3 et 6.
    

### Prompt basé sur l'Exemple (Few-Shot Prompting) :
"Reprenez  le  prompt  précédent  et  ajoutez  un  deuxième  exemple  d'entrée-sortie: format_product_code("XYZ987GHIJ")  devrait  retourner "XYZ-987-GHIJ", incluant un cas d'erreur : format_product_code("SHORT") devrait lever une ValueError. "
Question  :  L'IA  gère-t-elle  mieux  les  cas  d'erreur  maintenant  ?  La  robustesse  a-t-elle  été 
améliorée ?

![image-20250614124154387](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614124154387.png)





#### Questions :
L'IA gère-t-elle mieux les cas d'erreur maintenant ? Oui, l'IA gère maintenant correctement les cas d'erreur. Elle lève une ValueError lorsque la longueur de la chaîne n'est pas de 10 caractères, ce qui correspond à la troisième entrée "SHORT" dans les exemples fournis.
La robustesse a-t-elle été améliorée ? Oui, la robustesse a été améliorée. La fonction vérifie maintenant si la chaîne est bien une chaîne de caractères, si elle contient des caractères non alphanumériques, et si elle a la longueur correcte.

## Analyse Critique :
1) Influence des exemples sur la capacité de l'IA
L'ajout d'exemples a considérablement amélioré la précision du code généré. Sans exemple (zéro-shot), l'IA a placé les tirets aux positions 3 et 7. Avec un exemple (one-shot), elle a correctement placé les tirets aux positions 3 et 6. Les exemples ont clarifié les ambiguïtés et montré concrètement le comportement attendu.

2) Utilité du "Few-Shot Prompting" en développement
Le Few-Shot Prompting est particulièrement utile pour:

- Clarifier des spécifications ambiguës
- Illustrer des comportements complexes
- Démontrer la gestion d'erreurs spécifique
- Préciser des formats de sortie exacts
- Enseigner des patterns spécifiques à un domaine

3) Limites aux exemples
Les principales limites sont:

- Nombre: trop peu ou trop d'exemples peuvent être problématiques

- Qualité: des exemples mal choisis induisent en erreur
- Diversité: sans variété, l'IA ne généralise pas bien
- Cohérence: des exemples contradictoires créent de la confusion
- Biais: l'IA peut trop se focaliser sur les exemples au détriment d'autres instructions

## Exercice 2.3 : Génération d'une mini-application Web

### Prompt Vague
"Crée une calculatrice web simple en HTML, CSS et JavaScript."

![image-20250614124251540](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614124251540.png)

#### Résultat
Le prompt vague a généré une calculatrice fonctionnelle mais basique, avec un design minimaliste et des fonctionnalités limitées. Le code manquait de gestion d'erreurs robuste et de styles élaborés. Les opérations mathématiques de base étaient présentes, mais sans validation d'entrée ni traitement des cas particuliers comme la division par zéro.

### Prompt Détaillé
"Crée une calculatrice web en HTML, CSS et JavaScript avec les caractéristiques suivantes :
- Interface responsive avec une grille de boutons (chiffres 0-9, opérations +, -, *, /, =, et effacer)

- Affichage en haut montrant l'entrée actuelle et le résultat

- Styles modernes avec animations pour les clics de boutons (ombres, transitions)

- Gestion complète des erreurs (division par zéro, dépassement de capacité)

- Possibilité d'utiliser le clavier pour entrer des valeurs

- Historique des calculs récents

- Mode sombre/clair"

  ![image-20250614124324346](C:\Users\THE NAZZY\Pictures\Saved Pictures\image-20250614124324346.png)

  
  
  

#### Résultat
Le prompt détaillé a généré une application beaucoup plus sophistiquée avec :
- Une interface utilisateur soignée et responsive
- Des animations et transitions fluides
- Une gestion d'erreurs complète avec messages explicatifs
- Support des entrées clavier
- Fonctionnalité d'historique des calculs
- Thème sombre/clair avec bouton de basculement
- Code bien structuré et commenté

### Évaluation des différences

1. **Qualité du code** : Le code généré par le prompt détaillé était mieux organisé, modulaire et commenté, facilitant la maintenance et l'extension.

2. **Fonctionnalités** : Le prompt détaillé a produit une application avec des fonctionnalités supplémentaires significatives (historique, thèmes, support clavier) absentes de la version basique.

3. **Expérience utilisateur** : L'interface générée par le prompt détaillé offrait une meilleure expérience avec des animations, une meilleure accessibilité et des retours visuels.

4. **Robustesse** : La version détaillée incluait une gestion d'erreurs complète, rendant l'application plus fiable dans des scénarios variés.

5. **Adaptabilité** : La calculatrice issue du prompt détaillé était responsive et s'adaptait à différentes tailles d'écran, contrairement à la version basique.

## Partie 3 – Débogage et Amélioration du Code

### Objectif
Utiliser l'IA pour corriger des bugs, refactoriser et documenter du code existant.

### Exercice 3.1 : Débogage assisté

Vous recevez un code d'un collègue qui présente des erreurs et n'est pas optimal.

#### 1) Exécution du code et observation de l'erreur

Lors de l'exécution du code, l'erreur suivante apparaît :

```
Traceback (most recent call last):
  File "buggy_code.py", line 10, in <module>
    avg = calculate_average(my_nums)
  File "buggy_code.py", line 6, in calculate_average
    total += num
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
```

#### 2) Identification de la cause et correction proposée

La cause de l'erreur est que la liste `my_nums` contient une chaîne de caractères ('three') alors que la fonction `calculate_average` s'attend à recevoir uniquement des nombres. Lorsque la boucle essaie d'ajouter 'three' à la variable `total` (qui est un entier), Python génère une erreur de type car on ne peut pas additionner un entier et une chaîne de caractères.

De plus, la fonction ne gère pas le cas où la liste est vide, ce qui provoquerait une division par zéro.

#### 3) Tests unitaires avec pytest

Ces tests unitaires vérifient le comportement de la fonction corrigée dans différents scénarios, y compris les cas limites et les cas d'erreur.

## Exercice 3.2 : Refactoring avec l'IA

Le code ci-dessous trie une liste d'entiers, mais il est :
• non structuré,
• difficile à lire (noms non explicites),
• sans fonction ni commentaires.

### Analyse du code fourni

1) **Fonction du code** : Ce code implémente l'algorithme de tri à bulles (bubble sort) pour trier une liste d'entiers en ordre croissant. Il compare chaque élément avec tous les éléments suivants et les échange si nécessaire.

2) **Défauts de lisibilité** :
   - Variables non explicites (`a`, `i`, `j`, `tmp`)
   - Absence de fonction dédiée au tri
   - Aucun commentaire expliquant la logique ou l'algorithme
   - Pas de séparation entre la logique de tri et l'exécution
   - Code "en dur" sans possibilité de réutilisation

### Prompt de refactoring

"Refactorise ce code de tri à bulles en suivant les bonnes pratiques Python :
```python
a = [5, 3, 8, 6, 7, 2]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a)
```

Contraintes :
- Suivre la convention PEP8
- Ajouter des docstrings au format Google ou NumPy
- Séparer en fonctions modulaires (au moins une fonction de tri)
- Utiliser des noms explicites pour les variables et les fonctions
- Ajouter un bloc if __name__ == \"__main__\"
- Inclure des commentaires expliquant les parties complexes
- Ajouter des tests basiques pour vérifier le fonctionnement"

### Améliorations apportées

1. **Structure** : Le code est maintenant organisé en fonctions réutilisables.
2. **Lisibilité** : Les variables ont des noms explicites (`numbers`, `sorted_numbers`).
3. **Documentation** : Des docstrings détaillés expliquent le fonctionnement des fonctions.
4. **Modularité** : Séparation entre la logique de tri et l'affichage.
5. **Bonnes pratiques** : Utilisation du bloc `if __name__ == "__main__"` pour l'exécution.
6. **Tests** : Ajout de cas de test variés pour vérifier le bon fonctionnement.
7. **Commentaires** : Explications des étapes clés de l'algorithme.
8. **Immutabilité** : La fonction de tri retourne une nouvelle liste sans modifier l'originale.

Cette version est beaucoup plus maintenable, réutilisable et conforme aux standards Python.

## Exercice 3.3 : Génération de Documentation

### 1) Docstring généré pour la fonction get_user_permissions

```python
def get_user_permissions(user_id, system_context):
    """
    Récupère les permissions d'un utilisateur en fonction de son ID et du contexte système.
    
    Cette fonction détermine les permissions d'accès d'un utilisateur en vérifiant
    son appartenance aux groupes d'administrateurs ou d'éditeurs dans le contexte système.
    Les permissions possibles sont 'read', 'write', 'delete' et 'admin'.
    
    Parameters
    ----------
    user_id : str or int
        L'identifiant unique de l'utilisateur dont on veut connaître les permissions
    system_context : dict
        Un dictionnaire contenant les configurations du système, avec au minimum
        les clés 'admins' (liste d'IDs) et 'editors' (liste d'IDs)
    
    Returns
    -------
    list
        Une liste de chaînes représentant les permissions accordées à l'utilisateur:
        - Les administrateurs reçoivent ['read', 'write', 'delete', 'admin']
        - Les éditeurs reçoivent ['read', 'write']
        - Les autres utilisateurs reçoivent ['read']
    
    Examples
    --------
    >>> context = {'admins': [1, 2], 'editors': [3, 4]}
    >>> get_user_permissions(1, context)
    ['read', 'write', 'delete', 'admin']
    >>> get_user_permissions(3, context)
    ['read', 'write']
    >>> get_user_permissions(5, context)
    ['read']
    """
    if user_id in system_context['admins']:
        return ['read', 'write', 'delete', 'admin']
    elif user_id in system_context['editors']:
        return ['read', 'write']
    else:
        return ['read']
```

### 2) Section README.md pour la fonction get_user_permissions

## Gestion des Permissions Utilisateur

La fonction `get_user_permissions` est un composant essentiel de notre système de contrôle d'accès. Elle permet de déterminer dynamiquement les permissions d'un utilisateur en fonction de son identifiant et du contexte système actuel.

### Prérequis

Pour utiliser cette fonction, vous devez disposer d'un dictionnaire `system_context` correctement formaté contenant au minimum les clés suivantes :

```python
system_context = {
    'admins': [liste_des_ids_administrateurs],
    'editors': [liste_des_ids_editeurs]
}
```

Où :
- `admins` est une liste contenant les identifiants des utilisateurs ayant des droits d'administration
- `editors` est une liste contenant les identifiants des utilisateurs ayant des droits d'édition

### Utilisation

```python
from permissions import get_user_permissions

# Exemple de contexte système
system_context = {
    'admins': [1, 2, 100],
    'editors': [3, 4, 5, 200]
}

# Vérifier les permissions d'un administrateur
admin_permissions = get_user_permissions(1, system_context)
# Résultat: ['read', 'write', 'delete', 'admin']

# Vérifier les permissions d'un éditeur
editor_permissions = get_user_permissions(3, system_context)
# Résultat: ['read', 'write']

# Vérifier les permissions d'un utilisateur standard
user_permissions = get_user_permissions(10, system_context)
# Résultat: ['read']
```

### Niveaux de Permission

La fonction retourne une liste de permissions parmi les suivantes :

| Permission | Description |
|------------|-------------|
| `read`     | Permet de consulter les ressources |
| `write`    | Permet de modifier les ressources existantes |
| `delete`   | Permet de supprimer des ressources |
| `admin`    | Donne accès aux fonctionnalités d'administration |

### Intégration avec d'autres composants

Pour vérifier si un utilisateur possède une permission spécifique, vous pouvez utiliser :

```python
permissions = get_user_permissions(user_id, system_context)
if 'write' in permissions:
    # Autoriser l'opération d'écriture
```

### 3) Analyse de la documentation générée

La documentation générée est :

- **Claire** : Les explications sont précises et utilisent un langage simple pour décrire la fonction et son utilisation.
- **Complète** : Le docstring couvre tous les aspects importants (paramètres, valeurs de retour, exemples) et la section README fournit des informations contextuelles supplémentaires.
- **Facile à comprendre** : Les exemples concrets montrent clairement comment utiliser la fonction dans différents scénarios.
- **Bien structurée** : L'utilisation de tableaux, de sections et de blocs de code améliore la lisibilité.
- **Informative** : Elle fournit non seulement la syntaxe mais aussi le contexte d'utilisation et l'intégration avec d'autres composants.

Un autre développeur pourrait facilement comprendre comment utiliser cette fonction grâce à cette documentation, qui explique à la fois les aspects techniques (signature, paramètres) et conceptuels (rôle dans le système de permissions).
