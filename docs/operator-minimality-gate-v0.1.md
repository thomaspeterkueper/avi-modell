# AVI — Operator Minimality Gate v0.1

**Stand:** 27. September 2026  
**Status:** Struktur-Gate nach Minimal ξ Degree-of-Freedom Gate  
**Pfad:** O1-minimal / Class B

## 1. Gate-Frage

Kann AVI den generischen Raum zusätzlicher EFT-Kopplungen durch eine unabhängige, sparsame Regel so weit einschränken, dass ein eigenständiger falsifizierbarer Kern entsteht?

Dieses Gate führt keinen Datenfit durch und postuliert kein neues Teilchen.

## 2. Vorbedingung: Inferenzraum

Jede spätere Operatorprüfung setzt die Kontrollkette voraus:

    D
      -> P(Y,C | D,M_std)
      -> posterior predictive O_std
      -> residual r
      -> erst danach ξ/operator hypothesis.

Damit dürfen weder Kanalzustände C noch Unsicherheit über den Standardzustand Y als Kopplung eines neuen Freiheitsgrades absorbiert werden.

## 3. Generische Low-Energy-Struktur

Schematisch:

    L = L_std + L_ξ + Σ_a c_a O_ξ O_a / Λ^(d_a-4).

Für lokale dimensionslose Ratenverhältnisse kann dies im schwachen Grenzfall auf

    δ ln Γ_i = Σ_a c_a ξ S_ia

führen.

Damit ist die bisherige Systemsignatur S_i keine fundamentale Größe, sondern muss aus einer kleinen Operatorbasis beziehungsweise deren Sensitivitätskoeffizienten ableitbar sein.

## 4. Minimale Operatorfamilien

### O-A: Kopplung an elektromagnetische/gauge-sector Größen

Kann effektive Kopplungen und damit atomare/molekulare Übergänge differentiell verändern.

**Kontrolle:** varying-constant-, clock- und astrophysikalische Präzisionstests.

### O-B: Kopplung an Fermion-Massen-/Yukawa-Sektoren

Kann Massenverhältnisse, Bindungsenergien und Übergangsraten verändern.

**Kontrolle:** Uhren, Spektroskopie, Äquivalenzprinzip, fünfte Kräfte, kosmologische/astrophysikalische Grenzen.

### O-C: gluonischer/QCD-Sektor

Kann hadronische Skalen und damit materieabhängige Responses beeinflussen.

**Kontrolle:** starke Äquivalenz-/Kompositionssensitivität und Präzisionsgrenzen.

### O-D: neutrino-/schwach-sektorale Kopplung

Kann Zerfalls-/Oszillationsobservablen beeinflussen.

**Kontrolle:** modellabhängige Labor-, Astro- und Kosmologiegrenzen.

### O-E: rein gravitative/curvature coupling

Kopplungen an Krümmungsinvarianten oder gravitative Operatoren können lokale Response und Hintergrunddynamik beeinflussen.

**Problem für Class B:** Backreaction und Änderung der Gravitationsdynamik machen einen Übergang zu Class C wahrscheinlich.

## 5. Was keine AVI-Selektion ist

Folgende Regeln reichen nicht:

- „ξ koppelt schwach“;
- „nur dimensionslose Observablen“;
- „nur differentielle Effekte“;
- „nur kosmologisch langsame Evolution“;
- Auswahl der Operatoren nach denjenigen Daten, die ein Residuum zeigen.

Das sind technische Einschränkungen oder nachträgliche Selektion, keine AVI-spezifische Dynamik.

## 6. Minimalitätsanforderung

Eine eigenständige AVI-Regel müsste vor Datenanalyse mindestens eine Relation der Form

    c_a = λ n_a

erzwingen, wobei der Richtungsvektor n_a durch Theorie festgelegt oder stark eingeschränkt ist.

Dann folgt

    δ ln Γ_i = λ ξ Σ_a n_a S_ia.

Damit besitzt AVI nur einen gemeinsamen Amplitudenparameter λ statt unabhängiger c_a pro Sektor.

Erst eine solche Reduktion erzeugt kanalübergreifende Falsifizierbarkeit.

## 7. Test auf vorhandene AVI-Selektionsregel

Die bisherige AVI-Struktur enthält:

- Historien-/Zustandsfrage;
- ξ als möglichen zusätzlichen Zustand;
- Systemsignaturen S_i;
- Forderung nach differentiellen dimensionslosen Observablen;
- Class-B-Präferenz.

Sie enthält bislang **keine hergeleitete Regel**, die n_a im EFT-Operatorraum eindeutig oder ausreichend eng festlegt.

Die vorhandene S_i-Notation parametrisiert Sensitivität; sie leitet deren fundamentale Richtung nicht her.

## 8. Konsequenz

Damit kann gegenwärtig für praktisch jede gewünschte differentielle Signatur ein passender Satz c_a gewählt werden. Ein solcher Fit wäre generische EFT und hätte keine eigenständige AVI-Erklärungskraft.

Die korrekte Nullposition lautet daher:

    no AVI operator selection rule
      -> no AVI-specific local-rate prediction.

## 9. Class-B-Filter

Zusätzlich muss jeder Operatorfamilien-Kandidat zeigen:

    |δH/H| < ε_H

im betrachteten Regime, während eine messbare differentielle lokale Response verbleibt.

ε_H muss später experiment-/analysebezogen definiert werden.

Kann diese Trennung nicht erreicht werden, gehört der Kandidat zu Class C und nicht zum engen Class-B-Pfad.

## 10. State-Completeness-Filter

Vor jedem Operatorfit müssen mindestens drei Unsicherheitsklassen getrennt werden:

    C = channel/apparatus/environment state
    Y = standard physical state with posterior P(Y|D,M)
    ξ = hypothesized extra physical state.

Ein c_a darf nicht deshalb von null verschieden erscheinen, weil C unvollständig modelliert oder P(Y|D,M) auf eine einzelne Rekonstruktion kollabiert wurde.

OTA-SCI-0093 und OTA-SCI-0094 sind dafür die verbindlichen Kontrollfälle.

## 11. Gate-Ergebnis

**Operator Minimality Gate: FAIL AS DISTINCT AVI PREDICTION.**

Die generische EFT-Struktur erlaubt die gesuchte differentielle Class-B-Response prinzipiell. AVI besitzt derzeit jedoch keine unabhängige Selektionsregel, die den Operatorraum auf eine spezifische Richtung n_a reduziert.

Damit ist O1-minimal physikalisch formulierbar, aber noch nicht AVI-spezifisch.

Das Ergebnis blockiert Datenfits, nicht die Grundlagenarbeit.

## 12. Nächster sinnvoller Schritt

Kein weiterer freier Operator sollte eingeführt werden.

Stattdessen folgt ein **Selection-Principle Gate** mit genau einer Frage:

> Lässt sich aus den ursprünglichen AVI-Prinzipien — ohne Rückgriff auf beobachtete Anomalien — eine Symmetrie, Invarianz, Erhaltungsstruktur oder andere mathematische Bedingung ableiten, die den zulässigen Operatorvektor n_a einschränkt?

Falls nein, ist O1 als eigenständige AVI-Physik redundant und sollte als generische EFT-Exploration gekennzeichnet werden.

Falls ja, muss die Regel zuerst formalisiert und erst danach mit Daten konfrontiert werden.

## 13. Epistemischer Status

- **[R]** Zusätzliche Freiheitsgrade können über EFT-Operatoren differentielle lokale Observablen beeinflussen.
- **[D]** Die bisherige AVI-Systemsignatur ist noch keine Herleitung einer fundamentalen Operatorrichtung.
- **[D]** Ohne unabhängige Selektionsregel besitzt AVI im O1-Zweig derzeit keine spezifische lokale Ratenvorhersage.
- **[OFFEN]** Ob aus AVI-internen Prinzipien eine solche Selektionsregel ableitbar ist.
