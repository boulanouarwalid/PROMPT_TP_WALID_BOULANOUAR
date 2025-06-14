def bubble_sort(numbers):
    """
    Trie une liste de nombres en utilisant l'algorithme de tri à bulles.
    
    L'algorithme compare chaque élément avec les éléments suivants
    et les échange si nécessaire pour les mettre dans l'ordre croissant.
    
    Parameters
    ----------
    numbers : list
        La liste de nombres à trier
        
    Returns
    -------
    list
        Une nouvelle liste contenant les éléments triés
    
    Examples
    --------
    >>> bubble_sort([5, 3, 8, 6, 7, 2])
    [2, 3, 5, 6, 7, 8]
    """
    # Créer une copie de la liste pour ne pas modifier l'originale
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    
    # Parcourir tous les éléments de la liste
    for i in range(n):
        # Les derniers i éléments sont déjà triés
        for j in range(0, n - i - 1):
            # Comparer l'élément actuel avec le suivant
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                # Échanger les éléments si nécessaire
                sorted_numbers[j], sorted_numbers[j + 1] = sorted_numbers[j + 1], sorted_numbers[j]
                
    return sorted_numbers


def print_sorted_list(numbers):
    """
    Affiche une liste avant et après le tri.
    
    Parameters
    ----------
    numbers : list
        La liste de nombres à trier et afficher
    """
    print(f"Liste originale: {numbers}")
    sorted_numbers = bubble_sort(numbers)
    print(f"Liste triée: {sorted_numbers}")


if __name__ == "__main__":
    # Exemple d'utilisation avec la liste originale
    original_list = [5, 3, 8, 6, 7, 2]
    print_sorted_list(original_list)
    
    # Tests supplémentaires
    test_cases = [
        [1, 2, 3, 4, 5],  # Liste déjà triée
        [5, 4, 3, 2, 1],  # Liste triée en ordre inverse
        [],               # Liste vide
        [42]              # Liste avec un seul élément
    ]
    
    for test_case in test_cases:
        print("\nTest avec:", test_case)
        print_sorted_list(test_case)