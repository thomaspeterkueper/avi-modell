# AVI — Branch Decision Gate O1/O3 v0.1

**Stand:** 25. September 2026  
**Status:** Richtungsentscheidung nach X-global Qualification Gate  
**Ausgangspunkt:** O2 bleibt als QFT+GR-Referenz erhalten, liefert derzeit aber keinen zusätzlichen AVI-Mechanismus.

## 1. Entscheidungsfrage

Nach dem negativen X-global-Gate bleiben zwei prinzipielle Wege für eine physikalisch eigenständige Historien-/Zustandsinformation:

- **O1:** ein echter zusätzlicher dynamischer Freiheitsgrad;
- **O3:** eine physikalisch nicht-Markovsche Dynamik.

Dieses Gate entscheidet nicht, welche Variante wahr ist. Es prüft, welcher Zweig als nächstes wissenschaftlich sinnvoll weiterentwickelt werden kann, ohne durch Umdefinition des Zustandsraums oder freie Parametrisierung künstlich gerettet zu werden.

## 2. Gemeinsamer Mindeststandard

Beide Zweige müssen:

1. einen vollständigen Standardzustand klar vom zusätzlichen Inhalt trennen;
2. einen exakten Nullfall besitzen;
3. eine Dynamik mit Anfangs-/Randdaten angeben;
4. mindestens eine dimensionslose differentielle Observable liefern;
5. QFT+GR und Channel-State-Effekte vollständig als Nullmodell behandeln;
6. vor Datenfits eine Kopplungsstruktur festlegen;
7. einen Test zulassen, der den Zweig verwerfen kann.

## 3. O1 — zusätzlicher dynamischer Freiheitsgrad

Minimal:

    Z = (Y_std, ξ)

    dY_std/dN = F_std(Y_std)
    dξ/dN = G(ξ,Y_std; θξ)

mit einer unabhängigen Anfangsbedingung ξ_i.

Dann können bei gleichem Y_std verschiedene ξ-Werte physikalisch zulässig sein.

### Stärke

O1 löst das Determinismusproblem direkt. ξ ist keine Rekonstruktion einer Standardhistorie, sondern Bestandteil des erweiterten fundamentalen Zustands.

Der passende Test bleibt:

    Test B-F:
    Y_std,A = Y_std,B
    ξ_A != ξ_B
    => O_A != O_B.

### Kosten

O1 ist echte neue Physik. Er benötigt mindestens:

- Ontologie von ξ;
- Dynamik und Stabilität;
- Energie-/Impuls- beziehungsweise Gravitationskonsistenz, sofern relevant;
- Symmetrien und Kausalstruktur;
- Erklärung, warum Präzisionstests ξ bisher nicht ausschließen;
- eine nicht beliebige Kopplung an die Systemsignaturen S_i.

Ein gewöhnliches neues Skalarfeld wäre zwar formal möglich, würde aber den bisherigen engen AVI-Scope deutlich verändern und müsste gegen etablierte Feldmodelle abgegrenzt werden.

### Gate-Status

**Formal offen, aber ontologisch teuer.**

## 4. O3 — nicht-Markovsche Dynamik

Schematisch:

    dY/dN = F[Y(N), history]

oder

    R(N) = ∫ K(N,N') J(N') dN'.

Eine Gedächtnisvariable ξ kann die relevante Vergangenheit komprimieren.

### Stärke

O3 liegt semantisch nahe an der ursprünglichen AVI-Frage: Nicht nur der momentane reduzierte Zustand, sondern die realisierte Historie beeinflusst die aktuelle Response.

### Hauptproblem: Markov-Einbettung

Viele nicht-Markovsche Gleichungen entstehen, weil Freiheitsgrade ausgelassen wurden. Durch Erweiterung

    Y_reduced -> (Y_reduced, E_hidden)

kann die Gesamtdynamik wieder Markovsch werden.

Dann ist ξ kein fundamentaler Historienträger, sondern nur eine effektive Buchhaltung für E_hidden.

Dies ist physikalisch zulässig, aber keine eigenständige fundamentale AVI-Ontologie.

## 5. O3 wird deshalb in zwei Klassen geteilt

### O3-E — effektiv nicht-Markovsch

Die Memory-Struktur entsteht durch coarse graining, offene Systeme, integrierte Umweltfreiheitsgrade oder ähnliche Reduktion.

    full state Markov
      -> reduced state non-Markov.

**Status:** etablierte physikalische Architektur, aber zunächst Standard-/Effektivphysik.

O3-E ist als Referenz- und Modellierungsrahmen wertvoll, kann jedoch Test B-F nicht als fundamentalen AVI-Test erfüllen.

### O3-F — fundamental nicht-Markovsch

Die vollständige fundamentale Dynamik selbst benötigt irreduzible Historieninformation, die durch keinen endlichen oder physikalisch wohldefinierten erweiterten momentanen Zustand ersetzt werden kann.

Das wäre eine wesentlich stärkere Behauptung.

**Status:** konzeptionell möglich, derzeit ohne AVI-spezifische physikalische Grundlage.

## 6. Markov-Embedding Gate

Für jeden O3-Kandidaten muss vor einer AVI-Interpretation versucht werden:

    history kernel
      -> auxiliary states ξ_1 ... ξ_n
      -> local first-order evolution.

Wenn eine physikalisch sinnvolle Einbettung existiert, gilt:

    O3 candidate -> O3-E.

Dann muss entschieden werden, ob die Hilfszustände lediglich bekannte ausgelassene Freiheitsgrade darstellen oder ob daraus ein echter O1-artiger neuer Zustand folgt.

Nur wenn keine solche physikalisch adäquate Einbettung existiert, bleibt O3-F als Kandidat bestehen.

## 7. Vergleich

| Kriterium | O1 | O3-E | O3-F |
| --- | --- | --- | --- |
| unabhängiger Zustand möglich | ja | nur im erweiterten Modell | irreduzible Historie postuliert |
| strong Test B-F prinzipiell | ja | nein als fundamentaler Test | möglicherweise |
| etablierte Referenzphysik | zusätzliche Felder/Sektoren | offene Systeme/coarse graining | keine direkte AVI-Grundlage |
| neue Ontologie nötig | ja | nicht zwingend | stark |
| mathematische Schließbarkeit | gut, wenn G definiert | oft gut | offen |
| Redundanzrisiko | Feld unter neuem Namen | sehr hoch | geringer, aber Spekulationsrisiko hoch |
| unmittelbare Datenreife | nein | nein | nein |

## 8. Entscheidendes Ergebnis

O3 ist **nicht automatisch der konservativere Weg**.

- O3-E ist konservativ, liefert aber keine fundamentale Historienseparation.
- O3-F würde die gewünschte Historienabhängigkeit retten, verlangt jedoch eine noch stärkere physikalische Behauptung als ein zusätzlicher O1-Zustand.

Damit darf „Memory“ nicht als Abkürzung verwendet werden, um die Ontologiekosten von O1 zu vermeiden.

## 9. Branch-Entscheidung

Für die nächste aktive Grundlagenarbeit wird gewählt:

### Primärer aktiver Zweig: O1-minimal

Nicht weil ein neuer Freiheitsgrad empirisch angezeigt wäre, sondern weil O1 die klarste falsifizierbare Form des verbleibenden Problems besitzt.

Die nächste Aufgabe lautet ausdrücklich **nicht**, ein Feld zu erfinden. Zuerst wird geprüft, welche minimale mathematische und physikalische Struktur ein ξ-Freiheitsgrad besitzen müsste und welche bekannten Theorieklassen diese Struktur bereits abdecken.

### Kontrollzweig: O3-E

O3-E bleibt als Null-/Redundanzkontrolle erhalten. Jeder Memory-Ansatz muss gegen eine Markov-Einbettung geprüft werden.

### Reserve: O3-F

O3-F wird auf HOLD gesetzt, bis ein unabhängiger physikalischer Grund für irreduzible fundamentale Nicht-Markovianität vorliegt.

### Referenz: O2

O2 bleibt Standard-QFT/GR-Referenz für global-context-sensitive lokale Response.

## 10. O1-minimal: erlaubte nächste Fragen

Das folgende Screening darf nur Strukturfragen beantworten:

- Muss ξ skalar, vektoriell, tensorial oder andersartig sein?
- lokal, global oder effektiv?
- kontinuierlich oder diskret?
- dynamisch oder constraint-bestimmt?
- welche Dimension/Normierung?
- welche Symmetrien muss ξ respektieren?
- kann ξ ohne direkte Änderung von H in Class B wirken?
- welche bekannte Theorieklasse wäre mathematisch äquivalent?
- welche bestehenden Präzisionstests wären unmittelbar relevant?

Noch **nicht** erlaubt:

- Parameterfit an H0/S8/DE;
- Wahl einer Masse oder Kopplung aus Anomalien;
- Behauptung eines AVI-Teilchens oder Feldes;
- Identifikation ξ = Φ ohne Herleitung.

## 11. Falsifikationslogik des O1-Zweigs

O1-minimal soll bereits auf Theorieebene scheitern können.

Der Zweig wird zurückgestellt, wenn jede minimale Realisierung entweder:

1. vollständig einer bekannten Standard-/EFT-Erweiterung entspricht, ohne AVI-spezifische Zusatzvorhersage;
2. Class B nicht einhalten kann, weil die führende Wirkung unvermeidlich die Hintergrundgeometrie verändert;
3. nur durch kanalweise freie Kopplungen mit beliebiger Anpassungsfähigkeit funktioniert;
4. mit bestehenden Präzisionsgrenzen strukturell unvereinbar ist;
5. keinen operationalen Test B-F erzeugt.

## 12. Nächster Gate-Test

**Minimal ξ Degree-of-Freedom Gate**

Ziel:

> Bestimme die minimal zulässigen Eigenschaften eines echten ξ-Zustands, ohne eine konkrete neue Entität zu postulieren, und mappe diese Eigenschaften auf bekannte Theorieklassen.

Das Gate muss insbesondere klären, ob Class-B-AVI überhaupt einen neuen Freiheitsgrad zulässt, der differentiell lokale Raten beeinflusst, ohne bereits als gewöhnliches Skalar-/Vektorfeld oder als Verletzung etablierter Äquivalenz-/Konstanztests aufzugehen.

## 13. Epistemischer Status

- **[R]** Effektive nicht-Markovsche Dynamik kann durch ausgelassene Freiheitsgrade entstehen und durch erweiterten Zustandsraum teilweise/oft lokalisiert werden.
- **[D]** Eine Memory-Schreibweise allein etabliert keine fundamentale Historieninformation.
- **[D]** O1 ist formal der klarste verbleibende Testzweig, aber keine empirisch bevorzugte Theorie.
- **[H]** Ein echter zusätzlicher ξ-Zustand könnte Test B-F ermöglichen.
- **[OFFEN]** Ob eine minimale O1-Realisierung gegenüber bekannten Feld-/EFT-Erweiterungen überhaupt eigenständige AVI-Struktur besitzt.
