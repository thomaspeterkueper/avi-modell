# AVI — Beobachtungs-Testmatrix v0.1

Stand: 14. September 2026  
Status: Arbeitsdokument / Grundlagenphase

## Zweck

Diese Matrix trennt drei Ebenen, die in der AVI-Arbeit nicht vermischt werden dürfen:

1. **externe Beobachtungsdaten**, die ein AVI-Modell quantitativ reproduzieren oder erklären müsste;
2. **modellinterne Observablen**, die aus AVI mathematisch ableitbar sein müssen;
3. **eigentliche AVI-spezifische Tests**, insbesondere Test B: Historienseparation bei gleichem Gegenwartszustand.

Ein Datensatz kann für AVI hochrelevant sein, ohne eine AVI-spezifische Vorhersage zu bestätigen.

## 1. Minimale Beobachtungs-Schnittstelle

Bevor AVI mit realen Daten verglichen werden kann, muss das Modell mindestens konsistent liefern:

- `H(a)` beziehungsweise `H(z)`;
- luminosity distance `d_L(z)`;
- distance modulus `mu(z)`;
- gegebenenfalls angular-diameter distance `d_A(z)`;
- gegebenenfalls eine wohldefinierte Abbildung auf `w_eff(a)` als Vergleichsgröße, ohne `w_eff` an die Stelle der AVI-Dynamik zu setzen.

Die Referenzrechnung muss zunächst das jeweilige Standardmodell reproduzieren, bevor zusätzliche AVI-Freiheitsgrade zugelassen werden.

## 2. Testmatrix

| ID | Beobachtung / Referenz | Primäre Größe | Rolle für AVI | Bezug zu Test B | Status |
| --- | --- | --- | --- | --- | --- |
| OBS-01 | Supernovae Unite / `OTA-SCI-0091-2026-DE` | `mu(z)`, `d_L(z)` | externer Distanz-Rotverschiebungs-Likelihood-Test; schränkt zulässige Expansionshistorien ein | **indirekt / nein als positiver Test** | aufgenommen |
| OBS-02 | BAO / DESI-Familie | Distanzskalen, `H(z)`-abhängige Größen | unabhängiger geometrischer Expansionskanal; wichtig zur Kreuzprüfung von SNe-basierten Fits | nein | vorgesehen |
| OBS-03 | CMB / Planck- und Nachfolge-Constraints | frühe Randbedingungen, Geometrie, Materieinhalt | definiert Referenzraum für kosmologische Parameter und frühe Entwicklung | nein | vorgesehen |
| OBS-04 | lokale `H0`-Bestimmungen | gegenwärtige Expansionsrate | Gegenwartsanker; besonders wichtig für die Definition von `Y(a*)` | nein | vorgesehen |
| OBS-05 | kosmische Topologie / globale Struktur | globale Randbedingung / Identifikation | Kontrollfall dafür, dass lokale Gegenwartsgrößen globale Information nicht notwendig vollständig bestimmen | **methodisch relevant** | Referenzfall |
| AVI-B | Historienseparation bei gleichem Gegenwartszustand | `Y_A(a*) = Y_B(a*)`, aber `xi_A != xi_B` und ggf. `C_A != C_B` | eigentlicher AVI-spezifischer Kernversuch | **ja** | Grundlagenarbeit |

## 3. Unite: verbindliche Einordnung

`OBS-01` wird als erster konkreter externer Datensatz geführt.

Für einen späteren echten Vergleich gelten mindestens diese Regeln:

1. Zuerst den publizierten Referenzfit für Flat-LambdaCDM reproduzieren.
2. Datenvektor, Kovarianz und systematische Fehler soweit verfügbar unverändert übernehmen.
3. AVI gegen Flat-LambdaCDM und gegen ein geeignetes `w0-wa`-Vergleichsmodell testen.
4. Zusätzliche AVI-Freiheitsgrade in der Modellbewertung berücksichtigen.
5. Frequentistische Signifikanz und Bayes-Evidenz getrennt berichten.
6. Ein besserer Fit allein gilt nicht als Nachweis eines AVI-Zustandsparameters.

Unite misst eine integrierte Expansionsgeschichte. Daraus folgt keine direkte Evidenz für `xi`, `Phi(a)` oder physikalisches Gedächtnis.

## 4. Definition von Test B

Arbeitsdefinition:

> Zwei kosmologisch zulässige Historien A und B werden so konstruiert, dass sie am Vergleichszeitpunkt `a*` denselben vollständig definierten Standard-Gegenwartszustand besitzen, aber unterschiedliche AVI-Zusatzinformation tragen.

Minimal zu prüfen:

`Y_A(a*) = Y_B(a*)`

und zugleich

`xi_A(a*) != xi_B(a*)`

sowie, falls AVI eine beobachtbare Wirkung beansprucht,

`C_A(a*) != C_B(a*)`.

Die entscheidende Schwierigkeit liegt in der Definition von `Y`. Globale Topologie, Randbedingungen oder andere Standardinformation dürfen nicht versehentlich aus `Y` herausgelassen und anschließend als AVI-Gedächtnis fehlinterpretiert werden.

## 5. Kontrollregel für den Zustandsbegriff

Vor jedem Test-B-Kandidaten muss explizit festgelegt werden:

- welche Größen zu `Y` gehören;
- welche globalen Randbedingungen fixiert sind;
- welche Freiheitsgrade Standardkosmologie bereits enthält;
- welche Information ausschließlich `xi` zugeschrieben wird;
- ob die beiden Historien empirisch und mathematisch zulässig sind.

Der kosmische Topologie-Fall dient hier als methodischer Kontrolltyp: identische lokale Geometrie erzwingt nicht automatisch identische globale Struktur. Er ist kein AVI-Mechanismus.

## 6. Nächste Ausbaustufe v0.2

Für v0.2 sollen die vorgesehenen Beobachtungskanäle jeweils eine eigene Zeile mit folgenden Feldern erhalten:

- Datensatz / Release;
- beobachtete Größe;
- Rotverschiebungsbereich;
- benötigte AVI-Observable;
- Standard-Referenzmodell;
- Likelihood-/Kovarianz-Verfügbarkeit;
- systematische Hauptunsicherheiten;
- AVI-spezifische Vorhersage ja/nein;
- Bezug zu Test B;
- Reifegrad des Vergleichs.

Erst wenn mindestens `H(z)`, `d_L(z)` und `mu(z)` aus einer expliziten AVI-Dynamik berechnet werden können, beginnt die eigentliche quantitative Datenphase.

## 7. Leitplanke

Die Testmatrix dient nicht dazu, aktuelle kosmologische Spannungen nachträglich als AVI-Evidenz zu etikettieren. Sie definiert vielmehr, unter welchen Bedingungen AVI überhaupt mit Beobachtungen vergleichbar und falsifizierbar werden kann.
