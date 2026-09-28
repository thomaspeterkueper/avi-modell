# AVI — Beobachtungs-Testmatrix v0.2

Stand: 22. September 2026  
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
- für Struktur-/Materiesonden eine explizite Vorhersage der jeweils benötigten Materie- und Baryonenstatistik;
- gegebenenfalls eine wohldefinierte Abbildung auf `w_eff(a)` als Vergleichsgröße, ohne `w_eff` an die Stelle der AVI-Dynamik zu setzen.

Die Referenzrechnung muss zunächst das jeweilige Standardmodell reproduzieren, bevor zusätzliche AVI-Freiheitsgrade zugelassen werden.

## 2. Testmatrix

| ID | Datensatz / Referenz | Beobachtete Größe | Bereich / Domäne | Benötigte AVI-Observable | Standardreferenz | Likelihood / Kovarianz | Hauptsystematiken | AVI-spezifische Vorhersage? | Bezug zu Test B | Reifegrad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBS-01 | Supernovae Unite / `OTA-SCI-0091-2026-DE` | `mu(z)`, `d_L(z)` | kosmologische Distanz-Rotverschiebungs-Beziehung | `H(z) -> d_L(z) -> mu(z)` | Flat-LambdaCDM; `w0-wa`CDM als Erweiterungsvergleich | publizierter Datenvektor; vollständige öffentliche Analyseprodukte weiter prüfen | Kalibration, Selektion, Host-Mass, Klassifikation, intrinsischer Scatter | nein, externer Constraint | indirekt; kein positiver Test | aufgenommen |
| OBS-02 | BAO / DESI-Familie | transversale/radiale Distanzskalen, `H(z)`-abhängige Größen | großräumige Struktur / mehrere Rotverschiebungsbins | `H(z)`, `D_M(z)` bzw. surveykonforme Größen | Flat-LambdaCDM | releaseabhängig | Rekonstruktion, Surveyselektion, Fiducial-Cosmology-Abbildung | nein | nein | vorgesehen |
| OBS-03 | CMB / Planck und Nachfolger | frühe Randbedingungen, Geometrie, Materieinhalt, Leistungsspektren | Rekombination bis heute | konsistente frühe Entwicklung und Transferfunktionen | LambdaCDM | missions-/releaseabhängig | Foregrounds, Kalibration, Modellannahmen | nein | nein | vorgesehen |
| OBS-04 | lokale `H0`-Bestimmungen | gegenwärtige Expansionsrate | `z ~ 0` | `H(a=1)` plus Kalibrationsabbildung | LambdaCDM-unabhängiger bzw. methodenspezifischer Vergleich | methodenabhängig | Distanzleiter, Standardkerzen/-sirenen, Kalibration | nein | nein; wichtiger Gegenwartsanker für `Y(a*)` | vorgesehen |
| OBS-05 | kosmische Topologie / globale Struktur | globale Identifikation / Randbedingung | globale Geometrie und CMB/LSS-Signaturen | keine einzelne AVI-Observable; Kontrollvariable für vollständige Definition von `Y` | FLRW mit expliziter Topologie | methodenabhängig | Beobachterposition, Topologieskala, Masken, kosmische Varianz | nein | **methodisch relevant** | Referenzfall |
| OBS-06 | FRB-Dispersionsmaße / `OTA-SCI-0092-2026-DE` | `DM`, DM-Fluktuationen, baryonische Materieverteilung / Clustering | Sichtlinien über kosmologische Distanzen; publizierte Analyse sensitiv ungefähr auf `k = 0.1–3 h Mpc^-1` und Halos `>= 10^13 M_sun` | Vorhersage für Elektronensäulendichte und deren Statistik aus kosmologischer Materie-/Baryonenentwicklung | Standardkosmologie plus baryonisches Feedbackmodell | publizierte Analyse; öffentliche likelihood-fähige Produkte vor quantitativer AVI-Nutzung prüfen | Host-/lokale DM-Beiträge, IGM-Modellierung, Halo-Gas, Feedback, Selektion/Lokalisierung | nein, unabhängiger Materie-/Baryonenkanal | indirekt; erweitert empirische Bestimmung von `Y`, kein positiver Test | aufgenommen |
| OBS-07 | GW-Standard-Sirenen / `OTA-SCI-0093-2026-DE` | `d_L`, Host-Rotverschiebung, daraus `H0` | Gravitationswellen-Kosmologie | `H(z) -> d_L(z)` plus explizites Kanal-/Populationsmodell | Standard-Sirenen-Kosmologie ohne AVI-Zusatzterm | ereignis- und populationsabhängig | Wellenform, Detektorkalibration, Inklination, Lensing, Pekuliargeschwindigkeit, Selektion, Host-Zuordnung, **Sichtlinienbeschleunigung/Umgebung** | nein, unabhängiger Distanzkanal | **methodische Negativkontrolle**; kein positiver Test B | aufgenommen |
| OBS-09 | Orbitaler WEP-Quantentest / `OTA-SCI-0098-2026-DE` | differentielle Freifallbeschleunigung 85Rb/87Rb | Erdorbit / Mikrogravitation | keine AVI-Core-Observable; Präzisions-Nullkanal | GR/WEP | 280 Tage; publizierte Fehleranalyse | Plattformbewegung, Detektion, Detuning, Atominterferometer-Systematik | nein; Nullconstraint | T2/T3 Negativkontrolle | aufgenommen |\n| OBS-10 | Károlyházy-Dekohärenz / `OTA-SCI-0099-2026-DE` | spontane Strahlung / Modellparameter R_K | Niedriguntergrund-Quantenfundamenttest | keine AVI-Core-Observable; Falsifikationsreferenz | QM plus Untergrundmodell | publizierte Bayes-Spektralanalyse | Material-/Emissionsmodell, Untergrund | nein; konkrete Alternativmodellklasse ausgeschlossen | T3/T4 Negativkontrolle | aufgenommen |\n| AVI-B | Historienseparation bei gleichem Gegenwartszustand | `Y_A(a*) = Y_B(a*)`, aber `xi_A != xi_B`; daraus messbares `O_A != O_B` | modellabhängig | explizite AVI-Dynamik und Observable `O` | passendes Standardmodell ohne `xi` | erst nach konkreter Observable definierbar | Vollständigkeit von `Y`, versteckte Randbedingungen, Parametertuning | **ja** | **ja** | Grundlagenarbeit |

## 3. OBS-01 Unite: verbindliche Einordnung

Für einen späteren echten Vergleich gelten mindestens diese Regeln:

1. Zuerst den publizierten Referenzfit für Flat-LambdaCDM reproduzieren.
2. Datenvektor, Kovarianz und systematische Fehler soweit verfügbar unverändert übernehmen.
3. AVI gegen Flat-LambdaCDM und gegen ein geeignetes `w0-wa`-Vergleichsmodell testen.
4. Zusätzliche AVI-Freiheitsgrade in der Modellbewertung berücksichtigen.
5. Frequentistische Signifikanz und Bayes-Evidenz getrennt berichten.
6. Ein besserer Fit allein gilt nicht als Nachweis eines AVI-Zustandsparameters.

Unite misst eine integrierte Expansionsgeschichte. Daraus folgt keine direkte Evidenz für `xi`, `Phi(a)` oder physikalisches Gedächtnis.

## 4. OBS-06 FRB: verbindliche Einordnung

`OBS-06` basiert auf dem peer-reviewten Befund aus `OTA-SCI-0092-2026-DE`. FRB-Dispersionsmaße liefern einen physikalisch anderen Beobachtungskanal als SNe, BAO und CMB: Sie reagieren auf die integrierte freie Elektronendichte entlang der Sichtlinie und können dadurch die räumliche Verteilung ionisierter baryonischer Materie und astrophysikalisches Feedback einschränken.

Für AVI ist dies zunächst ein **Constraint auf den empirisch zulässigen Standardzustand und seine Entwicklung**. Der Kanal ist besonders wertvoll, weil eine unzureichende Modellierung baryonischer Rückkopplung in Large-Scale-Structure-Analysen nicht als neue kosmologische Dynamik oder AVI-Effekt fehlinterpretiert werden darf.

Verbindliche Grenze:

> Ein historienintegriertes FRB-Signal ist nicht dasselbe wie physikalische Historienabhängigkeit bei identischem Gegenwartszustand.

Daher gilt:

- keine Evidenz für `xi`;
- keine Evidenz für `Phi(a)`;
- kein positiver Test B;
- aber ein zusätzlicher unabhängiger Kanal zur empirischen Einschränkung dessen, was in `Y` und in der Standardentwicklung bereits erklärt werden muss.

Vor einer quantitativen AVI-Nutzung sind insbesondere Datenprodukte, Kovarianzen, Host-/lokale DM-Beiträge, IGM-/Halo-Gas-Modellierung und Feedbackparameter explizit zu behandeln.


## 5. OBS-07 Standard-Sirenen: Channel-State-Completeness

`OBS-07` basiert auf dem Preprint `OTA-SCI-0093-2026-DE`. Die dort simulierte Sichtlinienbeschleunigung zeigt einen wichtigen Inferenzfall: Ein nicht modellierter astrophysikalischer Kanalzustand kann die Leuchtkraftdistanz und damit die H0-Inferenz kohärent verschieben; mehr Ereignisse müssen diesen Bias nicht ausmitteln.

Für AVI gilt deshalb verbindlich:

> **Channel-state completeness before history-state inference.**

Vor einer AVI-Interpretation einer Differenz zwischen rekonstruierten kosmologischen Zuständen müssen relevante Messkanalzustände `C` explizit kontrolliert, modelliert oder marginalisiert werden. Formal ist die Inferenz als `P(O | Y, C, Modell)` zu behandeln und nicht allein als `P(O | Y)`.

Insbesondere gilt: Ein Unterschied zwischen zwei rekonstruierten `H0`-Werten oder Distanzkanälen ist weder Evidenz für `xi` noch ein positiver Test B, solange bekannte oder plausible kanalabhängige Zustände die Differenz erklären können.


## 6. OBS-08 TRGB-H0: State-Reconstruction-Completeness

`OBS-08` basiert auf dem Preprint `OTA-SCI-0094-2026-DE`. Die TRGB-Distanzleiter wird gegen 80 zulässige Rekonstruktionen der lokalen Dichte- und Peculiar-Velocity-Felder ausgewertet; die daraus resultierende Feld-zu-Feld-Streuung von H0 ist gegenwärtig größer als mehrere innerhalb einer festgehaltenen Rekonstruktion getestete Modellvarianten.

Für AVI wird deshalb zusätzlich verbindlich:

> **State-reconstruction completeness before extra-state inference.**

Es muss zwischen dem physikalischen Standardzustand `Y_true`, seiner datenbedingten Rekonstruktion `P(Y | D,M)` und einem hypothetischen zusätzlichen Zustand `xi` unterschieden werden. Unterschiedliche zulässige Rekonstruktionen von `Y`, die unterschiedliche H0-Posterioren erzeugen, sind kein Test B.

Eine AVI-Residualanalyse darf erst nach Marginalisierung über relevante Standardzustands- und Kanalunsicherheiten beginnen:

    P(O | D) = integral dY dC P(O | Y,C,M) P(Y,C | D,M).

Damit ergänzt OBS-08 die OBS-07-Regel: OBS-07 kontrolliert unvollständig modellierte **Kanalzustände C**; OBS-08 kontrolliert Unsicherheit über den **Standardzustand Y selbst**.

## 7. Definition von Test B

Arbeitsdefinition:

> Zwei kosmologisch zulässige Historien A und B werden so konstruiert, dass sie am Vergleichszeitpunkt `a*` denselben vollständig definierten Standard-Gegenwartszustand besitzen, aber unterschiedliche AVI-Zusatzinformation tragen.

Minimal zu prüfen:

`Y_A(a*) = Y_B(a*)`

und zugleich

`xi_A(a*) != xi_B(a*)`.

Ein Unterschied nur in einer internen Hilfsgröße genügt nicht. Für einen physikalischen Test muss aus der AVI-Dynamik eine messbare Observable `O` folgen, so dass

`O_A(a*) != O_B(a*)`.

Die entscheidende Schwierigkeit liegt in der Definition von `Y`. Globale Topologie, Randbedingungen, baryonische Zustände oder andere Standardinformation dürfen nicht versehentlich aus `Y` herausgelassen und anschließend als AVI-Gedächtnis fehlinterpretiert werden.

## 8. Kontrollregel für den Zustandsbegriff

Vor jedem Test-B-Kandidaten muss explizit festgelegt werden:

- welche Größen zu `Y` gehören;
- welche globalen Randbedingungen fixiert sind;
- welche Freiheitsgrade Standardkosmologie und Astrophysik bereits enthalten;
- welche Information ausschließlich `xi` zugeschrieben wird;
- ob die beiden Historien empirisch und mathematisch zulässig sind;
- welche konkrete Observable `O` den Unterschied messbar machen soll;
- ob alle relevanten Zustände des Beobachtungskanals `C` kontrolliert, modelliert oder marginalisiert wurden;\n- ob Unsicherheit in `Y` selbst als `P(Y | D,M)` marginalisiert wurde, statt sie als zusätzliche ontische Zustandsinformation zu behandeln.

Der kosmische Topologie-Fall dient als methodischer Kontrolltyp für globale Information. Der FRB-Fall ergänzt ihn auf anderer Ebene: unvollständig modellierte baryonische Materieverteilung darf nicht als zusätzliche fundamentale Zustandsinformation missverstanden werden.

## 9. Nächste Ausbaustufe

Die Matrix ist nun strukturell auf die vorgesehenen Felder erweitert. Als nächstes sind `OBS-02` bis `OBS-04` mit konkreten Releases und Datenprodukten zu belegen. Parallel muss der dynamische Closure-Vertrag entscheiden, welche physikalische Observable AVI überhaupt verändert.

Erst wenn die entsprechende AVI-Dynamik diese Observable berechnen kann, beginnt die quantitative Datenphase.

## 10. Leitplanke

Die Testmatrix dient nicht dazu, aktuelle kosmologische Spannungen nachträglich als AVI-Evidenz zu etikettieren. Sie definiert, unter welchen Bedingungen AVI mit unabhängigen Beobachtungskanälen vergleichbar und falsifizierbar wird.


## 11. OBS-09 Orbitaler WEP-Quantentest

Peer-reviewter Nullkanal: 85Rb/87Rb-Atominterferometrie auf der China Space Station, 280 Tage, Testunsicherheit 2.8e-8; Resultat mit keiner WEP-Verletzung vereinbar.

AVI-P: kein T1-T4-Trigger. Der Kanal ist als zukünftiger Constraint relevant, falls eine unabhängig definierte Erweiterung eine kompositions-/isotopenabhängige lokale Gravitationsresponse vorhersagt.

Verbindlich:

> **Precision null channels constrain extensions before they can support them.**

## 12. OBS-10 Károlyházy-/Nicht-Markov-Negativkontrolle

Der peer-reviewte Ausschluss der getesteten generalisierten Károlyházy-Modellklasse (R_K > 4.64 m experimentell versus R_K < 1.98 m aus der modellinternen Lokalisierungsbedingung) ist eine Falsifikationsreferenz.

AVI-P: T3/T4 werden nicht aktiviert, sondern methodisch eingeschränkt.

Verbindlich:

> **Non-Markovianity is not evidence of irreducible AVI retention.**

Eine konkrete Retentions-/Memory-Dynamik muss quantitativ formuliert und experimentell überlebensfähig sein; die bloße Bezeichnung "nicht-Markovsch" trägt keine AVI-Evidenz.
