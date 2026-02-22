def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in "values" gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args:
        values: 1D array of values (list).
        num_iterations: Integer to set the number of iterations.
        share: Fraction of the highest value to share with neighbors.
        
    Returns:
        A new list with the updated values.
    """
    # Wir arbeiten mit einer Kopie, um die Ursprungsliste nicht ungewollt zu verändern
    values_new = values.copy()
    
    for _ in range(num_iterations):
        # 1. Höchsten Wert und dessen Index finden
        max_value = max(values_new)
        max_index = values_new.index(max_value)
        
        # 2. Anteil berechnen (als Integer, um halbe Werte zu vermeiden, falls gewünscht. 
        # In Python erzeugt Multiplikation mit Float aber ohnehin Floats, wir runden hier auf Integer für die Test-Kompatibilität)
        share_value = int(max_value * share)
        
        # 3. Den Wert beim Maximum reduzieren (2 * share_value, da an zwei Nachbarn abgegeben wird)
        values_new[max_index] -= (share_value * 2)
        
        # 4. Nachbarn berechnen (mit Modulo % für den Rand-Überlauf)
        left_index = (max_index - 1) % len(values_new)
        right_index = (max_index + 1) % len(values_new)
        
        # 5. Werte an Nachbarn verteilen
        values_new[left_index] += share_value
        values_new[right_index] += share_value
        
    return values_new