# AVI — Global Carrier Screening v0.1

**Stand:** 21. September 2026
**Status:** kritisches Screening nach Global-Context Gate
**Pfad:** O2 — globale Kontextseparation

## 1. Ausgangspunkt

Das Global-Context Gate hat nur die Architektur bestätigt:

    G_global -> Q -> lokale Observable

Nun muss Q physikalisch identifiziert werden. Ein Kandidat ist nur brauchbar, wenn er globale Information tragen kann, lokal operational wirksam ist und nicht bloß bekannte QFT/GR unter neuem Namen darstellt.

## 2. Prüfkriterien

Für jeden Carrier Q prüfen wir:

1. physikalische Definition;
2. Abhängigkeit von globalem Kontext;
3. lokale Operationalisierbarkeit;
4. mögliche Verbindung zu dimensionslosen Ratenverhältnissen;
5. Abgrenzung von Standard-QFT/GR;
6. zusätzliche freie Parameter;
7. Falsifizierbarkeit.

## 3. Q1 — Quantenzustand eines etablierten Feldes

In QFT auf gekrümmter Raumzeit sind lokale Feldobservablen lokal und kovariant definiert, während der physikalische Quantenzustand zusätzliche Information enthält. Es existiert im Allgemeinen kein universell bevorzugter Vakuumzustand.

Schematisch:

    (M,g,G_global,boundary data)
      -> admissible state ω
      -> <O_local>_ω.

### Stärke

Dies ist der sauberste reale Carrier-Referenzfall. Globale/boundary Daten können die Menge bzw. Auswahl zulässiger Zustände und Moden beeinflussen, während lokale Erwartungswerte zustandsabhängig bleiben.

### Grenze

Wenn AVI lediglich

    ξ = "QFT state"

setzt, entsteht keine neue Theorie. Dann muss jede beobachtbare Wirkung vollständig aus Standard-QFT berechnet werden.

### Urteil

**Referenzcarrier: JA. AVI-spezifischer Carrier: noch NEIN.**

## 4. Q2 — globales Modenspektrum / diskrete Modendaten

Nichttriviale räumliche Topologie oder endliche/boundary Geometrie kann das Spektrum zulässiger Feldmoden verändern.

    G_global -> spectrum {k_n} -> state observables.

### Stärke

Direkte und berechenbare Verbindung zwischen globaler Struktur und Feldphysik. Casimir-Phänomene sind der experimentell etablierte Grenzfall der boundary-sensitiven Architektur.

### Grenze

Das Modenspektrum ist keine eigenständige lokale dynamische Variable. Es ist Teil der Spezifikation des Feldproblems. Eine zusätzliche AVI-Kopplung wäre nur gerechtfertigt, wenn eine neue Observable vorhergesagt wird, die Standard-QFT nicht bereits liefert.

### Urteil

**Sehr guter Architekturtest; kein eigenständiges ξ.**

## 5. Q3 — renormierter lokaler Stress-Energie-Erwartungswert

Ein operational näherer Carrier ist

    Q_mu_nu(x) = <T_mu_nu(x)>_ren.

Dieser kann vom globalen Zustand, von Randbedingungen und Topologie abhängen und koppelt in semiklassischer Gravitation direkt an die Geometrie:

    G_mu_nu + ... = 8πG <T_mu_nu>_ren.

### Stärke

Q ist lokal auswertbar und besitzt einen etablierten physikalischen Kopplungsweg. Die 2026 untersuchte topologische Casimir-Rückwirkung ist ein konkreter Referenzfall dafür.

### Grenze

Für AVI-Class B ist genau diese Stärke zugleich ein Problem: Wenn Q nur über Einstein-Gleichungen die Geometrie verändert, liegt der Effekt näher an einer Expansions-/Gravitationskopplung (Class A/C) als an einer separaten lokalen Ratenkopplung bei festem H_std.

### Urteil

**Physikalisch stärkster Carrier, aber nicht automatisch kompatibel mit Class B.**

## 6. Q4 — lokale Zweipunkt-/Korrelationsstruktur

Statt einer einzelnen Energiedichte kann der lokale Zustand über Korrelationsfunktionen charakterisiert werden:

    Q(x,x') = <φ(x)φ(x')>_ω

bzw. über daraus konstruierte Hadamard-/Response-Größen.

Atom- oder Detektorantworten hängen in QFT von Feldkorrelationen entlang ihrer Weltlinie ab. Damit existiert prinzipiell ein Weg

    global state
      -> local correlation function
      -> detector/transition response.

### Stärke

Dies ist konzeptionell besonders interessant für Class B: Der Carrier kann lokale Übergangsraten beeinflussen, ohne dass man zuerst eine universelle Änderung der Hintergrundexpansion postulieren muss.

### Grenze

Auch dieser Mechanismus ist zunächst vollständig Standard-QFT. Eine AVI-spezifische Aussage entsteht erst, wenn AVI eine zusätzliche, universell definierte Relation zwischen kosmologischem globalem Kontext und der lokalen Korrelationsstruktur vorhersagt.

### Urteil

**Bester Class-B-Referenzcarrier.**

## 7. Q5 — neuer AVI-spezifischer Feld-/Vakuumzustand

Man könnte einen neuen Zustand Q_AVI postulieren, der globale Information trägt und differentiell an Systeme koppelt.

### Stärke

Er könnte die gewünschte Kette direkt schließen.

### Grenze

Ohne unabhängige Motivation wäre dies genau der unerlaubte Schritt, den die bisherigen Gates verhindern sollen: ein neuer Freiheitsgrad wird eingeführt, weil das Modell ihn benötigt.

### Urteil

**Nicht zulässig als nächster Minimalpfad.**

## 8. Zentrale Erkenntnis

Für Class-B-AVI ist der interessante Standard-Referenzmechanismus nicht primär

    G_global -> <T_mu_nu> -> H,

sondern

    G_global
      -> quantum state / correlation structure
      -> local transition or detector response
      -> dimensionless rate ratio.

Damit rückt die lokale Korrelations-/Response-Struktur vor den Stress-Energie-Tensor.

## 9. Neue Arbeitsrolle von ξ

Für den O2/Class-B-Pfad sollte ξ vorläufig nicht als fundamentaler neuer Stoff verstanden werden.

Arbeitsdefinition:

    ξ := minimaler dimensionsloser Parameter oder Parametersatz,
         der eine global mitbestimmte lokale Response-Struktur
         relativ zu einer festgelegten Standard-QFT-Referenz beschreibt.

Diese Definition ist absichtlich **operational**. Sie behauptet nicht, dass ξ unabhängig von QFT existiert.

Falls Standard-QFT ξ vollständig vorhersagt, ist ξ nur eine abgeleitete Referenzgröße und kein neuer AVI-Freiheitsgrad.

## 10. Harte AVI-Abgrenzung

Eine echte AVI-Erweiterung müsste mindestens eine der folgenden Leistungen erbringen:

A. eine neue universelle Relation

    G_global -> ξ

die nicht bereits aus Standard-QFT/GR folgt;

B. eine neue, präregistrierte differentielle Kopplung

    ξ -> C_i/C_j

mit weniger Freiheit als ein beliebiger Satz sektorabhängiger Koeffizienten;

C. eine Beobachtung, bei der Standard-QFT/GR und AVI unterschiedliche quantitative Vorhersagen liefern.

Ohne A, B oder C bleibt der Carrier-Screen ein Referenzrahmen, keine AVI-Theorie.

## 11. Class-B-Konsistenzgate

Ein Carrier wird für AVI-B nur zugelassen, wenn sein führender beobachtbarer Effekt als lokales dimensionsloses Raten-/Response-Verhältnis formulierbar ist, ohne gleichzeitig eine nicht vernachlässigbare Änderung von H oder der lokalen Metrik vorauszusetzen.

Andernfalls muss die Variante ehrlich nach Class A oder C verschoben werden.

## 12. Ergebnis

Priorisierung für den nächsten Test:

1. **Q4 lokale Korrelations-/Response-Struktur** — stärkster Class-B-Referenzcarrier;
2. **Q1 Quantenzustand etablierter Felder** — notwendige übergeordnete Zustandsbeschreibung;
3. **Q3 <T_mu_nu>_ren** — stärkster etablierter lokaler Carrier, aber eher A/C;
4. **Q2 Modenspektrum** — globaler Input, nicht eigenständiger lokaler Zustand;
5. **Q5 neuer AVI-Zustand** — vorerst nicht zulässig.

## 13. Nächster Gate-Test

Für Q4 wird ein Response Gate benötigt:

> Können zwei global verschiedene, lokal geometrisch gleiche QFT-Konfigurationen eine unterschiedliche lokale dimensionslose Übergangs-/Detektorantwort besitzen, und lässt sich dieser Unterschied vollständig standardtheoretisch berechnen?

Wenn ja, besitzt AVI einen sehr guten Null-/Referenzkanal. Danach muss geprüft werden, ob überhaupt ein wohldefinierter Residualraum für eine zusätzliche AVI-Relation verbleibt.

## 14. Epistemischer Status

- **[R]** Lokale QFT-Observablen hängen vom Quantenzustand ab; gekrümmte Raumzeiten besitzen im Allgemeinen keinen kanonischen universellen Vakuumzustand.
- **[R]** Randbedingungen und Topologie können Modenspektren und Casimir-/Vakuumerwartungswerte verändern.
- **[R/H]** Topologieabhängige kosmologische Casimir-Rückwirkung ist ein aktueller theoretischer Referenzfall, dessen kosmologische Relevanz modellabhängig ist.
- **[D]** Für einen Class-B-Referenzpfad sind lokale Korrelations-/Response-Größen konzeptionell geeigneter als eine reine Stress-Energie-Rückwirkung.
- **[H]** Eine zusätzliche AVI-Relation könnte über einen solchen Carrier wirken; dafür existiert bislang kein Nachweis.
