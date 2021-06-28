#!/usr/bin/env python                                                                                               

def energyoftrans(wave):
    import numpy as np
    # wave : wavelength of photon in A
    #returns energy of transiton in ergs
    light = 2.99792e+18   #(* A s^-1 *)
    hplanckerg = 6.626068e-27  #(* erg s *)
    return (light/wave)*hplanckerg

def emist(ne, Tgas_exponent, Ycal, Eion, gground, n_ion):
    import numpy as np
    # ne : number density of electrons
    # Tgas_exponent : power of temperature of gas in Kelvin
    # Ycal : effective collision strength
    # Eion : Energy of the photon coming from the transition (erg)
    # gground : ground degeneracy, can be found with Chianti or Stout
    # n_ion : Number density of the ion 
    Tgas=10**Tgas_exponent
    kboltz= 1.38065e-16 #(*cgs*)
    numberemis=n_ion*ne*((8.629e-6)/np.sqrt(Tgas))*(Ycal/gground)*np.exp(-Eion/(kboltz*Tgas))
    #returns emisstivity of line
    return numberemis * Eion