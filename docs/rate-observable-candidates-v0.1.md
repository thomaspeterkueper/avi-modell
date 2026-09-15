# AVI — Kandidatenanalyse für Raten und Observablen v0.1

Stand: 15. September 2026  
Status: Arbeitsdokument / Grundlagenphase

## 1. Zweck

Dieses Dokument sucht noch **keine bestätigende Beobachtung** für AVI. Es prüft, welche physikalische Größe überhaupt als erste beobachtbare Ausgabe `O` einer AVI-Kopplung geeignet wäre.

Ausgangspunkt bleibt:

`X → ℱ → Z_AVI=(Y, ξ) → Q → Φ → C → AVI-Wirkung`

Für Test B reicht ein interner Unterschied `ξ_A != ξ_B` oder `C_A != C_B` nicht. Benötigt wird mindestens eine messbare Größe `O` mit

`Y_A(a*) = Y_B(a*)`, aber `O_A(a*) != O_B(a*)`.

Die ursprüngliche AVI-Motivation betrifft die Kopplung lokaler Zyklen beziehungsweise Raten an globale kosmologische oder informationelle Referenzparameter. Deshalb wird **nicht vorausgesetzt**, dass AVI die kosmologische Expansion `H(a)` selbst verändert.

## 2. Allgemeine Ratenform

Für einen Prozess `i` sei die Standardrate

`Γ_i,std = Γ_i(Y_local, constants, environment)`.

Eine minimale phänomenologische AVI-Schreibweise wäre

`Γ_i,AVI(a) = Γ_i,std(a) · C_i[Φ(a), ξ(a), Y(a)]`.

Im Nullfall gilt

`C_i = 1`.

Entscheidend ist, ob `C_i` universell oder prozessabhängig ist. Eine universelle Multiplikation aller denkbaren Uhren und Prozesse wäre operational schwer oder unmöglich von einer bloßen Änderung der Zeiteinheit zu unterscheiden. Ein physikalisch testbares AVI benötigt daher entweder

1. **differentielle Kopplung** zwischen mindestens zwei Prozessklassen, oder
2. eine Kopplung an eine unabhängig definierte geometrische/kosmologische Observable.

Damit wird die von AVI ausdrücklich vermiedene Formulierung „Zeit läuft schneller oder langsamer“ mathematisch ersetzt durch **vergleichbare dimensionslose Ratenverhältnisse**.

## 3. Kandidat A — Atomare und molekulare Übergangsfrequenzen

### Observable

`O_AB = ν_A / ν_B`

für zwei unterschiedliche atomare, molekulare oder später nukleare Referenzübergänge.

### Stärke

Frequenzverhältnisse sind dimensionslos und extrem präzise messbar. Verschiedene Übergänge besitzen unterschiedliche Sensitivitäten gegenüber dimensionslosen fundamentalen Parametern wie der Feinstrukturkonstante `α` oder dem Elektron-Proton-Massenverhältnis `μ`.

### Bestehende Schranke

Präzisionsuhren gehören bereits zu den stärksten Tests zeitlicher, oszillatorischer und transienter Änderungen fundamentaler Konstanten. Eine AVI-Kopplung, die einfach wie eine Variation von `α`, `μ` oder ähnlichen Parametern wirkt, muss diese Grenzen respektieren.

### AVI-Bewertung

**Sehr guter Messkanal, aber gefährlicher Mechanismuskandidat.**

AVI sollte in der Grundlagenphase nicht postulieren, dass `α` oder andere fundamentale Konstanten variieren. Stattdessen können Frequenzverhältnisse als Nulltest dienen: Jede spätere AVI-Dynamik muss zeigen, ob sie solche Verhältnisse unverändert lässt oder eine wohldefinierte differentielle Abweichung erzeugt.

Priorität: **hoch als Constraint / mittel als mögliche Observable**.

## 4. Kandidat B — Radioaktive und nukleare Zerfallsraten

### Observable

Beispielsweise ein dimensionsloses Verhältnis

`O_decay = Γ_decay / ν_ref`

oder der Vergleich verschiedener Zerfallskanäle.

### Stärke

Nukleare Prozesse bieten einen qualitativ anderen physikalischen Ratenkanal als atomare Übergänge. Geologische und astrophysikalische Archive integrieren zudem sehr lange Zeiträume.

### Bestehende Schranke

Meteoriten-Datierungen und insbesondere der natürliche Oklo-Reaktor liefern starke Langzeitgrenzen auf Änderungen nuklear relevanter Parameter. Die Interpretation ist modellabhängiger als bei modernen Laboruhren, weil Kernphysik und Umweltmodellierung eingehen.

### AVI-Bewertung

**Interessanter Langzeitkanal**, besonders wenn AVI eine epochale statt kurzfristige Kopplung vorhersagt. Er ist jedoch ungeeignet als erster fundamentaler AVI-Mechanismus, solange nicht definiert ist, woran die Kernrate koppeln soll.

Priorität: **mittel**.

## 5. Kandidat C — Chemische und biologische Raten

### Observable

Reaktions-, Stoffwechsel-, Entwicklungs- oder Alterungsraten relativ zu einer externen physikalischen Referenz.

### Stärke

Solche Systeme besitzen viele gekoppelte Zeitskalen und könnten langfristig für Anwendungen oder emergente Konsequenzen einer Ratenkopplung interessant sein.

### Problem

Temperatur, Druck, chemische Umgebung, Genetik, Regulation und Nichtgleichgewichtsdynamik dominieren. Ohne vorher etablierten mikrophysikalischen AVI-Kanal wäre eine Abweichung nicht eindeutig AVI zuordenbar.

### AVI-Bewertung

**Keine primäre Fundamentalmessung.** Biologische oder chemische Systeme dürfen erst downstream betrachtet werden, wenn eine mikrophysikalische Kopplung definiert und unabhängig getestet ist.

Priorität: **niedrig für Grundlagenprüfung, später potenziell hoch für Konsequenzen**.

## 6. Kandidat D — Gravitative Dynamik

### Observable

Mögliche dimensionslose Vergleiche wären Orbit-/Pulsations-/Taktfrequenzen relativ zu atomaren Referenzen oder präzise Tests der lokalen Positionsinvarianz und des Äquivalenzprinzips.

### Stärke

Gravitation stellt eine unabhängig definierte geometrische Referenz bereit. Modelle mit raumzeitlich variierenden Kopplungen erzeugen häufig zusätzliche Felder oder Verletzungen der Universalität des freien Falls und sind deshalb bereits stark eingeschränkt.

### AVI-Bewertung

**Sehr wichtiger Ausschluss- und Konsistenzkanal.** Eine AVI-Ratenkopplung darf nicht stillschweigend eine Verletzung des Äquivalenzprinzips oder eine Variation von `G` einführen. Falls AVI später atomare gegenüber gravitativen Raten differentiell koppelt, wird dieser Kanal unmittelbar testbar.

Priorität: **hoch als Constraint und möglicher differentieller Referenzkanal**.

## 7. Kandidat E — Kosmologische Expansion

### Observable

`H(z)`, `d_L(z)`, `d_A(z)` und daraus abgeleitete dimensionslose Kombinationen.

### Stärke

Diese Größen sind bereits durch SNe, BAO, CMB und weitere Beobachtungskanäle zugänglich und bilden die globale kosmologische Entwicklung ab.

### Entscheidende Trennung

AVI entstand aus der Hypothese, dass **lokale Raten** an globale kosmologische/informationelle Referenzparameter gekoppelt sein könnten. Daraus folgt nicht automatisch

`H_AVI(a) != H_std(a)`.

Es sind mindestens zwei saubere Modellklassen möglich:

- **Ratenkopplungs-AVI:** `H(a)` bleibt Standardhintergrund und liefert zusammen mit anderen Größen einen globalen Referenzzustand; `C` verändert bestimmte lokale Ratenverhältnisse.
- **Expansionskopplungs-AVI:** `C` wirkt zusätzlich auf die Hintergrunddynamik, sodass AVI selbst `H(a)` verändert.

Die zweite Variante ist eine zusätzliche Hypothese und darf nicht allein deshalb gewählt werden, weil aktuelle SNe-/BAO-Daten Abweichungen von ΛCDM interessant erscheinen lassen.

Priorität: **hoch als globaler Referenzkanal; offen als AVI-Wirkungskanal**.

## 8. Vergleich

| Kandidat | Präzision | Unabhängige Referenz | Hauptproblem | Rolle v0.1 |
| --- | --- | --- | --- | --- |
| atomare/molekulare Frequenzverhältnisse | sehr hoch | ja, differentielle Übergänge | starke bestehende Nullgrenzen | primärer Constraint |
| nukleare Zerfallsraten | hoch / lange Baseline | ja | Kern-/Umweltmodellierung | Langzeit-Constraint |
| chemische/biologische Raten | systemabhängig | schwierig | viele Störgrößen | downstream |
| gravitative Dynamik | sehr hoch in ausgewählten Tests | ja | Äquivalenzprinzip / Modellabhängigkeit | primärer Constraint + Referenz |
| kosmologische Expansion | hoch, komplementäre Datensätze | global | Wirkung vs Referenz nicht entschieden | globaler Referenzkanal |

## 9. Arbeitsentscheidung v0.1

AVI legt **noch keinen einzelnen Prozess als Wirkungsträger fest**.

Der erste testbare Observable-Typ wird stattdessen als dimensionsloses differentielles Ratenverhältnis definiert:

`O_ij(a) = Γ_i(a) / Γ_j(a)`.

Mit

`Γ_i,AVI = Γ_i,std · C_i`

folgt

`O_ij,AVI / O_ij,std = C_i / C_j`.

Damit entsteht nur dann ein beobachtbarer AVI-Effekt, wenn

`C_i / C_j != 1`.

Diese Form ist für die Grundlagenphase stärker als die Behauptung einer absoluten Ratenänderung: Sie ist operational definiert, dimensionslos und direkt an Präzisionsexperimente anschließbar.

## 10. Konsequenz für Test B

Die nächste präzise Test-B-Form lautet:

`Y_A(a*) = Y_B(a*)`

`ξ_A(a*) != ξ_B(a*)`

und für mindestens ein wohldefiniertes Prozesspaar `(i,j)`:

`[C_i/C_j]_A != [C_i/C_j]_B`.

Dann wäre die beobachtbare Größe

`O_ij = Γ_i/Γ_j`.

Das ist wesentlich strenger als ein interner Unterschied in `Φ` oder `C`: Zwei Historien müssen bei gleichem kontrolliertem Standard-Gegenwartszustand ein **unterschiedliches dimensionsloses Ratenverhältnis** vorhersagen.

## 11. Nächster mathematischer Schritt

Als nächstes ist nicht die Auswahl eines konkreten Atoms oder Zerfallsisotops nötig, sondern die Definition der Kopplungsstruktur:

`C_i = C(S_i, Φ, ξ; θ)`

mit einem Prozess-Sensitivitätsparameter oder -vektor `S_i`.

Zu klären sind:

1. Welche physikalische Eigenschaft eines Prozesses bestimmt `S_i`?
2. Gibt es einen universellen Anteil von `C`, der unbeobachtbar herausfällt?
3. Welche differentielle Komponente bleibt in `C_i/C_j` messbar?
4. Wie wird der Nullfall exakt erreicht?
5. Kann dieselbe Kopplungsregel Atomuhren-, Äquivalenzprinzip-, Oklo- und kosmologische Grenzen gleichzeitig erfüllen?

Erst danach ist eine konkrete numerische AVI-Vorhersage sinnvoll.

## 12. Evidenzgrenze

Die existierenden Präzisionstests sind **Constraints für AVI, keine Evidenz für AVI**. Die Kandidatenanalyse nutzt etablierte Messkanäle, um den zulässigen Raum einer späteren AVI-Kopplung frühzeitig einzuengen.

### Wissenschaftliche Referenzbasis

- Jean-Philippe Uzan, *Fundamental constants: from measurement to the universe, a window on gravitation and cosmology*, Living Reviews in Relativity (2025).
- Marianna S. Safronova et al., Arbeiten und Reviews zur Suche nach Variationen fundamentaler Konstanten mit Präzisionsuhren.
- C. R. Gould, E. I. Sharapov, A. A. Sonzogni, *Nuclear Data and the Oklo Natural Nuclear Reactors*, Nuclear Data Sheets 118 (2014).
- Thomas Dent, Steffen Stern, Christof Wetterich, *Competing bounds on the present-day time variation of fundamental constants*, Physical Review D 79, 083533 (2009).

Diese Literatur wird hier als Constraint-Landschaft verwendet. AVI postuliert in v0.1 keine Variation fundamentaler Konstanten.