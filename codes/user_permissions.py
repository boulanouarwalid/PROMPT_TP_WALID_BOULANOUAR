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