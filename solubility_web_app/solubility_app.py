# Importing libraries
import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
from rdkit import Chem
from rdkit.Chem import Descriptors

# Custom Function
# Calculate Molecular Descriptors


def AromaticProportion(m):
    aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic()
                      for i in range(m.GetNumAtoms())]
    aa_count = []
    for i in aromatic_atoms:
        if i == True:
            aa_count.append(1)
    AromaticAtom = sum(aa_count)
    Heavyatom = Descriptors.HeavyAtomCount(m)
    AR = AromaticAtom/Heavyatom
    return AR


def generate(smiles, verbosa=False):

    moldata = []
    for elem in smiles:
        mol = Chem.MolFromSmiles(elem)
        moldata.append(mol)

    baseData = np.arange(1, 1)
    i = 0
    for mol in moldata:
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotatableBonds = Descriptors.NumRotatableBonds(mol)
        desc_AromaticProportion = AromaticProportion(mol)

        row = np.array([desc_MolLogP,
                        desc_MolWt,
                        desc_NumRotatableBonds,
                        desc_AromaticProportion])

        if(i == 0):
            baseData = row
        else:
            baseData = np.vstack([baseData, row])
        i = i + 1

    columnNames = ["MolLogP", "MolWt",
                   "NumRotatableBonds", "AromaticProportion"]
    descriptors = pd.DataFrame(data=baseData, columns=columnNames)

    return descriptors
