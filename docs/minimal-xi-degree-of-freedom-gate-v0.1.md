# AVI — Minimal ξ Degree-of-Freedom Gate v0.1

**Stand:** 25. September 2026  
**Status:** kritisches Struktur-Gate nach Branch Decision O1/O3  
**Pfad:** O1-minimal / Class B

## 1. Gate-Frage

Welche minimale physikalische Struktur müsste ein echter zusätzlicher Zustand ξ besitzen, damit er

- nicht aus dem vollständigen Standardzustand rekonstruierbar ist,
- Test B-F prinzipiell bestehen kann,
- eine lokale differentielle dimensionslose Response erzeugen kann,
- und nicht bereits durch seine Definition bloß ein gewöhnliches bekanntes Feldmodell unter neuem Namen ist?

Dieses Gate postuliert **keine neue Entität**. Es bestimmt notwendige Eigenschaften und Ausschlussbedingungen.

## 2. Minimaler Zustandsvertrag

Für O1 gilt zunächst

    Z_fund = (Y_std, ξ)

mit

    dY_std/dN = F_std(Y_std, ξ?)
    dξ/dN = G(ξ,Y_std; θξ).

Für den engen Class-B-Pfad soll im führenden Grenzfall gelten:

    H = H_std

während mindestens ein lokales dimensionsloses Ratenverhältnis

    O_ij = Γ_i / Γ_j

eine ξ-Abhängigkeit besitzt.

Der Nullfall muss exakt sein:

    ξ-coupling -> 0
    => O_ij -> O_ij,QFT+GR.

## 3. Muss ξ ein Skalar sein?

Nein. Aus dem bisherigen AVI-Formalismus folgt keine Lorentz-/Raumzeittransformationseigenschaft von ξ.

Mögliche Strukturen wären:

- skalar/pseudoskalar;
- Vektor/Tensor;
- interner Zustandsparameter ohne klassische Raumzeitfeldinterpretation;
- globaler dynamischer Freiheitsgrad;
- diskreter/sektoraler Zustand.

Die bisherige Schreibweise ξ(a) darf deshalb nicht als Beweis für ein Skalarfeld gelesen werden.

### Minimalitätsentscheidung

Für das erste Screening wird **keine Spin-/Tensorstruktur festgelegt**. Zulässig bleibt nur die schwächere Aussage:

> ξ muss eine operational unterscheidbare Zustandskomponente des erweiterten Modells sein.

## 4. Lokal oder global?

### Lokales propagierendes ξ(x)

Ein lokales Feld benötigt typischerweise:

- lokale Bewegungsgleichung;
- Anfangsdaten auf einer Cauchy-Fläche;
- Propagation/Kausalstruktur;
- Energie-Impuls-Beitrag oder begründete Entkopplung davon;
- Kopplungen an Standardfelder.

Dies führt unmittelbar in bekannte EFT-/Beyond-Standard-Model-Strukturen.

### Globales ξ(t) oder ξ(a)

Ein ausschließlich homogener Freiheitsgrad vermeidet räumliche Propagation nicht automatisch. Eine homogene Feldlösung ist noch immer die Lösung eines Feldmodells und muss Störungen sowie Stabilität erklären.

Ein wirklich globaler, nichtlokaler Freiheitsgrad benötigt dagegen eine eigene konsistente Dynamik und Kausalinterpretation.

### Entscheidung

**Globalität darf nicht als Abkürzung benutzt werden, um Feldtheoriebedingungen zu umgehen.**

## 5. Dynamisch oder constraint-bestimmt?

Ein unabhängiger O1-Zustand benötigt eigene Anfangs-/Randinformation.

Wenn

    ξ = f(Y_std)

zu jedem Zeitpunkt eindeutig gilt, ist ξ kein zusätzlicher Freiheitsgrad.

Auch eine algebraische Constraint-Gleichung kann nur dann einen zusätzlichen Sektor tragen, wenn mehrere physikalisch unterscheidbare Lösungen/Branches mit eigener Zustandsinformation existieren.

Für den Minimalpfad gilt daher:

    independent state information is required.

## 6. Dimension und Normierung

Für die bisherige differentielle Kopplung ist eine dimensionslose ξ-Variable praktisch, aber nicht fundamental erforderlich.

Eine dimensionsbehaftete fundamentale Variable kann über eine unabhängig definierte Referenzskala M_* normiert werden:

    ξ = X / M_*^d.

Unzulässig ist eine Normierung, deren Skala erst aus dem zu erklärenden Residuum bestimmt wird.

Damit bleibt die frühere dimensionslose ξ-Schreibweise als **normalisierte Arbeitsvariable** erhalten.

## 7. Minimale lokale Kopplung

Die bestehende phänomenologische Form

    ln(C_i/C_j) = λ ξ ΔS_ij · n

kann nur als Low-Energy-/Response-Parametrisierung gelten.

Ein echter O1-Mechanismus muss darunter eine Wechselwirkung oder effektive Operatorstruktur besitzen, schematisch

    L = L_std + L_ξ + L_int

mit

    L_int = Σ_a g_a O_ξ O_a / Λ^(d_a-4)

oder einer äquivalenten wohldefinierten Kopplung.

Damit entsteht sofort eine wichtige Konsequenz:

> Sobald ξ lokal an Standardprozesse koppelt, liegt AVI im Territorium effektiver Feldtheorie und muss deren Symmetrie-, Renormierungs-, Stabilitäts- und Präzisionstestbedingungen erfüllen.

## 8. Differentialität versus Universalität

Ein rein universeller common-mode Faktor

    Γ_i -> A(ξ) Γ_i

fällt aus

    Γ_i / Γ_j

heraus.

Für eine messbare Class-B-Signatur braucht AVI deshalb sektor- oder operatorabhängige Sensitivität:

    δ ln Γ_i = λ ξ S_i

mit

    S_i != S_j.

Genau diese Differentialität macht das Modell jedoch empfindlich für:

- Tests der Konstanz fundamentaler Konstanten;
- Atomuhrenvergleiche;
- Lorentz-/CPT-Tests, abhängig von der Operatorstruktur;
- Äquivalenzprinzip- und fünfte-Kraft-Tests bei materieabhängiger Kopplung;
- astrophysikalische und kosmologische Grenzen.

Die bereits definierte S_i-Matrix bleibt daher zentral.

## 9. Kann Class B die Expansion unverändert lassen?

Nur als kontrollierter Näherungsbereich.

Ein neuer dynamischer Freiheitsgrad besitzt im Allgemeinen Energie, Impuls oder einen effektiven Stress-Energie-Beitrag. Damit kann er die Hintergrundgeometrie beeinflussen.

Für striktes Class B muss mindestens eine der folgenden Bedingungen quantitativ gelten:

1. ξ-Energiedichte ist gegenüber dem kosmologischen Budget vernachlässigbar;
2. ξ ist ein effektiver interner Zustand ohne relevante gravitative Rückwirkung;
3. eine Symmetrie/Constraint-Struktur unterdrückt den führenden Beitrag;
4. die Analyse ist auf einen Bereich beschränkt, in dem Backreaction unter der geforderten Genauigkeit liegt.

Ohne eine solche Begründung wandert O1 von Class B nach Class C.

## 10. Mapping auf bekannte Theorieklassen

### M1 — leichtes Skalar-/Pseudoskalarfeld

Kann unabhängige Anfangsdaten und lokale Kopplungen besitzen.

**Problem:** keine AVI-spezifische Struktur allein durch Umbenennung in ξ. Fifth-force-, clock-, equivalence- und cosmological constraints werden relevant.

### M2 — Vektor-/Tensorfeld

Erzeugt zusätzliche Richtungs-/Polarisationsstruktur.

**Problem:** höhere strukturelle Kosten; Lorentz-/Isotropiegrenzen werden unmittelbar relevant. Keine Minimalmotivation aus AVI.

### M3 — Modulus / varying-coupling field

Ein Zustand verändert effektive Kopplungen oder Massen.

**Passung:** sehr direkte differentielle Ratenwirkung.

**Problem:** fällt in etablierte Klassen variierender Konstanten beziehungsweise skalarer Kopplungsmodelle. AVI benötigt eine zusätzliche spezifische Vorhersage.

### M4 — ultraleichter/coherent background degree of freedom

Kann zeitabhängige oder oszillatorische Signaturen in Präzisionsmessungen erzeugen.

**Problem:** ebenfalls bekannte BSM/EFT-Klasse; Frequenz-, Kohärenz- und Kopplungsstruktur wären zusätzliche Modellannahmen.

### M5 — globaler constrained mode

Könnte näher an der ursprünglichen AVI-Intuition liegen.

**Problem:** Ohne konkrete Wirkung/Dynamik ist dies nur eine Bezeichnung. Mit konkreter Wirkung muss gezeigt werden, wodurch er sich mathematisch von bekannten globalen/zero-mode Strukturen unterscheidet.

### M6 — diskreter/branch state

Ein zusätzlicher Sektor könnte diskrete Zustandsinformation tragen.

**Problem:** Übergänge, Auswahlregel, Kopplung und kosmologische Population müssten erklärt werden. Keine bestehende AVI-Motivation legt dies nahe.

## 11. Screening-Ergebnis

Es gibt **keine minimale ξ-Struktur, die allein aufgrund der bisherigen AVI-Prinzipien bereits eine neue Theorieklasse definiert**.

Der physikalisch geradlinigste O1-Zustand mappt auf bekannte zusätzliche Freiheitsgrade bzw. EFT-Strukturen.

Das ist kein logischer Widerspruch. Es bedeutet aber:

> O1 wird erst dann AVI-spezifisch, wenn eine zusätzliche, sparsame und unabhängig motivierte Struktur existiert, die über „neuer Zustand koppelt an lokale Prozesse“ hinausgeht.

## 12. Harte Abgrenzung

Die folgenden Aussagen sind ab jetzt unzulässig:

- „ξ ist ein neues Feld“, ohne L_ξ und Symmetriestruktur;
- „ξ ist global“, um lokale Konsistenzbedingungen zu umgehen;
- „ξ speichert Geschichte“, wenn seine unabhängige Zustandsinformation nicht gezeigt ist;
- „Class B verändert H nicht“, ohne Backreaction-Bound;
- „AVI erklärt Uhren-/H0-/S8-Anomalien“, bevor eine präregistrierte Operator- und Signaturstruktur existiert.

## 13. Gate-Ergebnis

**Minimal ξ Degree-of-Freedom Gate: PASS AS STRUCTURAL POSSIBILITY, FAIL AS DISTINCT THEORY.**

Ein echter zusätzlicher ξ-Zustand kann Test B-F formal ermöglichen. Die bisher minimal zulässigen Realisierungen sind jedoch nicht AVI-spezifisch; sie fallen in bekannte zusätzliche-Freiheitsgrad-/EFT-Klassen oder benötigen noch undefinierte globale Strukturen.

Damit ist die zentrale Frage nicht länger „Kann ξ existieren?“, sondern:

> Welche AVI-spezifische Restriktion würde den zulässigen Operator-/Kopplungsraum enger machen als eine generische EFT?

## 14. Nächster Gate-Test — Operator Minimality Gate

Das nächste Gate soll **keinen Datenfit** durchführen.

Es prüft stattdessen:

1. welche niedrigstdimensionalen Operatorfamilien überhaupt eine Class-B-differentielle Ratenwirkung erzeugen;
2. welche davon sofort mit Symmetrien oder Präzisionstests kollidieren;
3. ob die vorhandene Systemsignatur S_i aus einer kleinen Operatorbasis ableitbar ist;
4. ob AVI eine zusätzliche Selektionsregel für diese Basis besitzt;
5. ob nach diesen Bedingungen ein nichttrivialer, falsifizierbarer Rest gegenüber generischer EFT verbleibt.

Wenn kein solcher Rest verbleibt, ist O1 als eigenständige AVI-Theorie redundant.

## 15. Epistemischer Status

- **[R]** Zusätzliche lokale Freiheitsgrade und ihre Kopplungen werden konsistent im Rahmen von Feldtheorie/EFT beschrieben.
- **[R]** Differentielle Kopplungen sind durch Präzisionsmessungen stark testbar und modellabhängig beschränkt.
- **[D]** Die bisherige ξ-Notation definiert weder Spin noch Feldcharakter noch eine neue Theorieklasse.
- **[D]** Ein unabhängiger ξ-Zustand kann Test B-F formal ermöglichen, ist aber ohne zusätzliche Restriktion generische neue Physik.
- **[OFFEN]** Ob AVI eine physikalisch motivierte Operator-Selektionsregel besitzt, die einen eigenständigen falsifizierbaren Rest erzeugt.
