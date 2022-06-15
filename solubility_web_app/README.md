# Molecular Solubility Prediction App

This app predicts the Solubility **(LogS)** values of molecules!

## Literature Review

[ESOL: Estimating Aqueous Solubility Directly from Molecular Structure](https://pubs.acs.org/doi/10.1021/ci034243x). _J. Chem. Inf. Comput. Sci._ 2004, 44, 3, 1000-1005.

## Description

In the field of drug discovery, the solubility of the target molecule is a crucial parameter. Various factors influence this solubility - logp<sub>octanol</sub>, molecular weight, the proportion of heavy atoms in aromatic systems, number of rotatable bonds, etc.
A wide range of models has been proposed to date to predict molecular solubility, among which **GSE** (**G**eneral **S**olubility **E**quation) is one of the most robust and effective ones, which measures the **LogP** and melting point **(Tm)** to predict the solubility **(LogS)**.

---

## ![GSE Experimental vs Predicted](GSE.png)

As a limitation, GSE cannot predict the solubility of a molecule if the Tm is unknown. For that reason, a new model has been developed - **E**stimated **Sol**ubility or **ESOL**.In this model, four parameters are used to predict the LogS - **cLogP**, Molecular Weight (**MWT**), Rotatable Bonds (**RB**), and Aromatic Proportion (**AP**).

---

## ![ESOL Experimental vs Predicted](ESOL.png)

---

- First of all, dataset is collected from [here](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv), containing **MolLogP**, **MolWt**, **NumRotatableBonds**, **AromaticProportion** and finally **logS** columns.
`	MolLogP	MolWt	NumRotatableBonds	AromaticProportion	logS
0	2.59540	167.850	0.0	0.000000	-2.180
1	2.37650	133.405	0.0	0.000000	-2.000
2	2.59380	167.850	1.0	0.000000	-1.740
3	2.02890	133.405	1.0	0.000000	-1.480
4	2.91890	187.375	1.0	0.000000	-3.040
...	...	...	...	...	...
1139	1.98820	287.343	8.0	0.000000	1.144
1140	3.42130	286.114	2.0	0.333333	-4.925
1141	3.60960	308.333	4.0	0.695652	-3.893
1142	2.56214	354.815	3.0	0.521739	-3.790
1143	2.02164	179.219	1.0	0.461538	-2.581
1144 rows × 5 columns`
- Next, **logS** column is dropped and assigned as the `target`.
  **Linear Regression Model** is used for the prediction, and model performance is checked.
- Next, model equataion is created, containing the five parameters.
- Next, Experimental vs Predicted logS values are plotted.

---

## ![Experimental vs Predicted LogS for Training Data](exp_vs_pred.png)

---

- Finally, model is saved as a `Pickle Object`.

Write briefly about the app building

finally attach the screenshot of the app

also add the outputs
