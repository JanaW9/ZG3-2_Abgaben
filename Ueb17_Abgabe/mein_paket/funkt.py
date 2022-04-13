def mad(dB,sysB):
    """Die 'mad'-Funktion berechnet den mittleren arteriellen Blutdruck. 
    Das Ergebnis wird auf Null Nachkommastellen gerundet und als Integer ausgegeben.
    :param:sysB: systolischer Blutdruck
    :param:dB: diastolischer Blutdruck
    
    Beispiel:
    >>> mad(60,130)
    95"""
    erg=dB+ 0.5*(sysB - dB)
    return int(round(erg,0))