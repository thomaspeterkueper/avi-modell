# AVI — X-global Qualification Gate v0.1

**Stand:** 24. September 2026  
**Status:** kritisches Qualifikationsgate nach Residual-Space Gate  
**Pfad:** O2 / Class B — globale Kontextseparation

## 1. Gate-Frage

Gibt es einen globalen Prädiktor `X_global`, der

1. unabhängig von den zu erklärenden lokalen Residuen definiert ist,
2. nicht bloß bereits vollständig in QFT+GR enthaltene Zustands-, Geometrie- oder Randinformation umbenennt,
3. einen kausal und mathematisch spezifizierbaren Weg zu einer lokalen differentiellen Response besitzt,
4. mindestens zwei physikalisch verschiedene Messkanäle mit einer sparsamen gemeinsamen Struktur beeinflussen könnte?

Nur ein Kandidat, der diese Bedingungen erfüllt, darf in RS2 weiterverwendet werden.

## 2. Qualifikationskriterien

Für jeden Kandidaten werden acht Fragen gestellt:

- **Q1 Definition:** Ist X_global physikalisch eindeutig definiert?
- **Q2 Unabhängigkeit:** Ist die Größe ohne die Zielresiduen bestimmbar?
- **Q3 Neuheitsabgrenzung:** Ist sie mehr als Standard-QFT+GR-Zustandsinformation?
- **Q4 Mechanismus:** Existiert ein definierter Pfad zur lokalen Response?
- **Q5 Normierung:** Sind Dimension und Referenzwert eindeutig?
- **Q6 Evolution:** Ist ihre zeitliche/kosmologische Entwicklung definiert?
- **Q7 Differentialität:** Kann sie mindestens zwei verschiedene Kanäle nichttrivial vergleichen?
- **Q8 Falsifizierbarkeit:** Gibt es einen Nullfall und Daten, die die Relation verwerfen könnten?

Ein Scheitern an Q3 ist für O2 besonders schwerwiegend: Dann ist der Kandidat als Referenzgröße nützlich, aber keine eigenständige AVI-Physik.

## 3. Kandidat X1 — globale räumliche Topologie

Definition:

    X1 := spezifizierte globale Topologie / Identifikationsklasse
          einer räumlichen Sektion oder Raumzeit.

### Prüfung

**Q1 PASS.** Topologie ist mathematisch eindeutig spezifizierbar.

**Q2 PASS.** Sie kann prinzipiell unabhängig von lokalen Response-Residuen durch globale Beobachtungen beziehungsweise Modellwahl eingeschränkt werden.

**Q3 FAIL für AVI-Neuheit.** Topologie ist Teil der globalen Spezifikation des Standard-Feld-/Gravitationsproblems. Ihre Auswirkungen auf Modenspektren und QFT-Korrelationen gehören in das QFT+GR-Nullmodell.

**Q4 PASS als Standardmechanismus.**

    topology -> allowed modes/state -> Wightman structure -> response.

**Q5 PASS**, sofern eine konkrete Topologie und gegebenenfalls dimensionslose Skalenverhältnisse spezifiziert sind.

**Q6 CONDITIONAL.** Die topologische Klasse kann konstant sein, während physikalische Kompaktifizierungsskalen mit der Geometrie evolvieren.

**Q7 PASS als QFT-Referenz.**

**Q8 PASS als QFT-Referenz.**

### Urteil

**Sehr guter Kontrollprädiktor, kein qualifiziertes AVI-X_global.**

## 4. Kandidat X2 — globale Randbedingungen / Modendaten

Definition:

    X2 := boundary-condition class + global mode spectrum.

### Prüfung

Q1, Q2, Q4, Q5 und Q8 können für ein konkretes Feldproblem erfüllt werden.

**Q3 FAIL.** Randbedingungen und daraus folgende Modenspektren sind bereits Teil der vollständigen QFT-Spezifikation.

Q6 und Q7 sind modellabhängig, aber prinzipiell behandelbar.

### Urteil

**Standard-QFT-Input; nicht als AVI-Zusatzprädiktor zulässig.**

## 5. Kandidat X3 — globaler Quantenzustand / Zustandsklasse

Definition:

    X3 := unabhängig spezifizierter globaler QFT-Zustand ω
          beziehungsweise eine physikalisch definierte Zustandsklasse.

### Prüfung

**Q1 CONDITIONAL.** Ein Zustand kann mathematisch definiert werden, besitzt aber in allgemeiner gekrümmter Raumzeit nicht automatisch eine einzigartige physikalische Auswahlregel.

**Q2 PASS**, wenn die Zustandspräparation oder Auswahlregel unabhängig spezifiziert ist.

**Q3 FAIL.** Der QFT-Zustand ist gerade Bestandteil des vollständigen Standard-QFT-Nullmodells.

**Q4 PASS.** Lokale Korrelationsfunktionen und Responses folgen direkt aus ω.

**Q5–Q8** sind in konkreten Modellen prinzipiell erfüllbar.

### Urteil

**Unverzichtbarer Nullmodellbestandteil; kein AVI-X_global.**

## 6. Kandidat X4 — kosmologische Expansionsgrößen

Mögliche Größen:

    H/H0,
    q = -a ä / ȧ²,
    Ω_m(a),
    Ω_r(a),
    Ω_DE(a),
    d ln H/dN.

### Prüfung

**Q1 PASS.**
**Q2 PASS.**
**Q5 PASS.**
**Q6 PASS.**
**Q8 PASS** für eine konkret postulierte Kopplung.

Das Problem liegt bei Q3/Q4.

Diese Größen gehören zum lokalen beziehungsweise kosmologischen Standardzustand Y und bestimmen bereits Standard-QFT/GR-Responses über Geometrie und Dynamik.

Eine zusätzliche direkte Relation

    H or q -> local rate residual

wäre nicht aus O2 abgeleitet, sondern ein **neues Kopplungspostulat**.

### Urteil

**Als unabhängige Regressoren messbar, aber keine zusätzliche globale Information.** Eine direkte AVI-Kopplung wäre neue Physik und müsste als solche deklariert werden.

## 7. Kandidat X5 — integrierte Expansionshistorie Φ_hist

Definition beispielsweise:

    Φ_hist(a) = ∫ W[a',H(a'),Ω_i(a'),...] da'.

### Prüfung

**Q1 PASS**, sobald W präregistriert ist.

**Q2 PASS**, wenn Φ_hist ausschließlich aus unabhängigen kosmologischen Daten berechnet wird.

**Q3 FAIL im deterministischen Standardfall.** Wenn die vollständige Standardhistorie aus Anfangsdaten und Dynamik bestimmt ist, ist Φ_hist eine abgeleitete Größe und keine zusätzliche Zustandsinformation.

**Q4 FAIL als eigenständiger Mechanismus.** Eine Wirkung auf lokale Residuen benötigt weiterhin ein neues Kopplungsgesetz.

**Q5/Q6 PASS** bei expliziter Definition.

**Q7/Q8 CONDITIONAL** auf ein neues Kopplungspostulat.

### Urteil

**Als deskriptiver Historienindex zulässig; kein eigenständiges X_global für O2.**

Dies bestätigt das frühere Determinismus-Gate.

## 8. Kandidat X6 — globale Materie-/Strukturinformation

Mögliche Repräsentationen:

    large-scale density field,
    power spectrum / correlation hierarchy,
    global environmental descriptors,
    baryon distribution.

### Prüfung

Diese Größen sind physikalisch und unabhängig beobachtbar. FRB-, Lensing-, Galaxien- und CMB-Kanäle können sie zunehmend einschränken.

Aber:

**Q3 FAIL als AVI-Neuheit.** Materie- und Baryonenverteilung gehören zur Standardzustands-/Astrophysikbeschreibung.

**Q4 PASS** nur über bekannte gravitative, elektromagnetische oder QFT-Wege, sofern kein neuer Mechanismus postuliert wird.

### Urteil

**Wichtige Kontrollinformation für channel/state completeness, kein AVI-X_global.**

## 9. Kandidat X7 — kausale globale Struktur / Horizontdeskriptor

Mögliche Größen:

    horizon scale ratios,
    conformal age,
    causal-patch descriptors,
    global causal invariants.

### Prüfung

**Q1 CONDITIONAL.** Einzelne Größen sind eindeutig definierbar.

**Q2 PASS** für kosmologisch berechenbare Größen.

**Q3 überwiegend FAIL.** Größen wie konformes Alter oder Horizontskalen folgen aus Metrik und Expansionshistorie und sind damit Standard-GR-abgeleitet.

**Q4 FAIL für eine zusätzliche lokale AVI-Response**, solange kein neuer Kopplungsmechanismus angegeben wird.

### Urteil

**Interessante globale Deskriptoren, derzeit keine zusätzliche physikalische Information.**

## 10. Kandidat X8 — unbekannte globale Zustandsinvariante

Schematisch:

    X8 := I_global[M,g,quantum state,...]

mit der Forderung, dass I_global nicht auf die vollständigen Standarddaten reduzierbar ist.

### Prüfung

Q3 wäre definitionsgemäß erfüllbar.

Aber derzeit scheitert der Kandidat bereits an:

- Q1: keine physikalische Definition;
- Q2: keine unabhängige Messvorschrift;
- Q4: kein Mechanismus;
- Q5: keine Normierung;
- Q6: keine Dynamik;
- Q7: keine präregistrierte Differentialsignatur.

### Urteil

**Nicht qualifiziert.** X8 wäre gegenwärtig nur ein Platzhalter für unbekannte Physik.

## 11. Screening-Matrix

| Kandidat | unabhängig definierbar | außerhalb vollständiger QFT+GR-Daten | etablierter Response-Pfad | AVI-qualifiziert |
| --- | --- | --- | --- | --- |
| X1 Topologie | ja | nein | ja | nein |
| X2 Randbedingungen/Moden | ja | nein | ja | nein |
| X3 QFT-Zustand | bedingt | nein | ja | nein |
| X4 H, q, Ω_i | ja | nein | Standardwirkung ja; Zusatzwirkung nein | nein |
| X5 integrierte Historie | ja | nein | Zusatzwirkung nein | nein |
| X6 globale Materiestruktur | ja | nein | bekannte Physik | nein |
| X7 kausale/Horizontgrößen | ja | überwiegend nein | Zusatzwirkung nein | nein |
| X8 unbekannte Invariante | nein | hypothetisch ja | nein | nein |

## 12. Gate-Ergebnis

Das Screening liefert ein klares negatives Ergebnis:

> **Keiner der derzeit konkret definierbaren X_global-Kandidaten qualifiziert sich als eigenständiger zusätzlicher AVI-Prädiktor im minimalistischen O2/RS2-Pfad.**

Die physikalisch besten Kandidaten X1–X3 besitzen gerade deshalb keinen AVI-Neuheitsstatus, weil ihre lokale Wirkung bereits Standard-QFT+GR ist.

X4–X7 sind unabhängig definierbar, aber aus Standardkosmologie beziehungsweise Standardzuständen abgeleitet. Eine zusätzliche lokale Wirkung wäre ein neues Kopplungspostulat und keine Konsequenz globaler Kontextinformation allein.

X8 wäre neue Physik ohne gegenwärtige Definition.

## 13. Konsequenz für O2

Der minimalistische O2-Pfad erreicht damit eine natürliche Grenze:

    global context
      -> local quantum response

ist real, aber Standard-QFT.

Eine zusätzliche Kette

    global context
      -> AVI residual response

ist derzeit weder theoretisch notwendig noch unabhängig spezifiziert.

Daher wird O2 **nicht verworfen**, aber als eigenständiger AVI-Mechanismus auf **HOLD** gesetzt.

Er bleibt:

- Referenzarchitektur;
- Nullmodell für globale Kontextsensitivität;
- Quelle methodischer Tests für lokale/globalen Zustandsbegriffe.

Er ist derzeit **kein geschlossener AVI-Mechanismus**.

## 14. Was jetzt nicht getan werden sollte

Nach diesem Ergebnis wären folgende Schritte methodisch falsch:

- X8 frei parametrisieren;
- Φ_hist allein wegen seiner Historienform zur neuen Physik erklären;
- H0-, S8- oder DE-Spannungen zur Auswahl von X_global verwenden;
- mehrere Residuen durchsuchen, bis eine gemeinsame Korrelation erscheint;
- bekannte topologische/QFT-Effekte als AVI-Vorhersage umetikettieren.

## 15. Verbleibende wissenschaftlich saubere Pfade

Das Gate lässt drei Wege offen.

### P1 — O2 als Referenzrahmen behalten

AVI bleibt zunächst eine Forschungsfrage nach global/lokalem Zustandsbezug; QFT+GR ist der vollständig auszuarbeitende Referenzfall.

### P2 — O1 explizit prüfen

Ein echter zusätzlicher Freiheitsgrad könnte Test B-F ermöglichen. Dann muss AVI jedoch offen als neue Physik mit eigener Dynamik behandelt werden.

### P3 — O3 vertieft prüfen

Eine fundamental oder effektiv nicht-Markovsche Dynamik könnte Historieninformation tragen. Dabei muss erneut geprüft werden, ob der Effekt durch Erweiterung des Standardzustands wieder Markovsch wird.

Keiner dieser Wege erhält durch das negative O2-Ergebnis empirische Unterstützung.

## 16. Entscheidung

**X-global Qualification Gate: FAIL for additional O2/RS2 physics.**

Das ist ein produktives negatives Resultat. Es verhindert, dass AVI durch immer abstraktere globale Variablen unfalsifizierbar wird.

Als nächster Grundlagenvergleich ist deshalb kein weiteres X_global-Screening sinnvoll. Der methodisch saubere nächste Schritt ist ein **Branch Decision Gate O1/O3**, das die Kosten, Testbarkeit und Redundanz beider verbleibenden Ontologien gegeneinander prüft, während O2 als Standard-QFT-Referenz erhalten bleibt.

## 17. Epistemischer Status

- **[R]** Topologie, Randbedingungen, QFT-Zustände, kosmologische Expansion und Materieverteilung können lokale Observablen über etablierte Physik beeinflussen.
- **[D]** Diese Größen werden nicht dadurch zu AVI-Zuständen, dass sie global oder historienabhängig sind.
- **[D]** Für O2/RS2 ist derzeit kein zusätzlicher qualifizierter X_global-Prädiktor identifiziert.
- **[H]** Neue fundamentale oder nicht-Markovsche Physik könnte einen zusätzlichen Zustand ermöglichen; dies ist bislang unbelegt.
