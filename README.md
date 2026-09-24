# AVI-Modell

Website zur Vertiefung des kosmologischen Arbeitsmodells **AVI — Axiomatisches Vakuum Integral**.

AVI untersucht als theoretisches Arbeitsmodell, ob und wie lokale Raten oder Zyklen an globale kosmologische beziehungsweise informationelle Referenzparameter gekoppelt sein könnten. Ein Schwerpunkt liegt auf der Frage, ob zwei Systeme mit identischem momentanen kosmologischen Zustand aufgrund unterschiedlicher Historien unterscheidbar sein können und welche zusätzliche Zustandsinformation dafür formal erforderlich wäre.

Der aktuelle Stand ist Grundlagenarbeit. Etablierte Kosmologie, Modellpostulate, mathematische Ableitungen, Interpretationen und falsifizierbare Vorhersagen werden ausdrücklich getrennt geführt. Der globale Arbeitsparameter `Φ(a)` ist dabei kein räumlich propagierendes Feld, sondern ein Kandidat für eine integrierte, historienabhängige Zustandsgröße.

## Aktueller Forschungsstand

Die Beobachtungs-Testmatrix liegt unter [`docs/observational-test-matrix-v0.2.md`](docs/observational-test-matrix-v0.2.md). Sie trennt externe kosmologische Datensätze von AVI-spezifischen Tests und hält insbesondere fest, dass integrierte Expansions- oder Materiehistorien keinen positiven Test B darstellen.

Der [`dynamische Closure-Vertrag v0.1`](docs/dynamical-closure-contract-v0.1.md) definiert die noch fehlende mathematische Brücke von `Z_AVI=(Y,ξ)` über `Φ` und `C` zu tatsächlich berechenbaren Observablen. Er trennt Expansionskopplung, Ratenkopplung und eine kombinierte Variante, ohne bereits eine datenfitgetriebene AVI-Dynamik zu postulieren.

Die [`Kandidatenanalyse für Raten und Observablen v0.1`](docs/rate-observable-candidates-v0.1.md) prüft atomare, nukleare, chemisch-biologische, gravitative und kosmologische Messkanäle. Als erste allgemeine AVI-Observable wird ein dimensionsloses differentielles Ratenverhältnis `O_ij = Γ_i/Γ_j` untersucht; eine konkrete Prozesskopplung wird noch nicht postuliert.

Die [`physikalische Systemsignatur S_i v0.1`](docs/system-signature-si-v0.1.md) präzisiert, wie verschiedene Prozesse differentiell auf denselben zusätzlichen AVI-Zustand reagieren könnten. `S_i` wird als physikalisch operationalisierbare Sensitivitätsstruktur behandelt. Philosophische Intuitionen aus der Omnizedenz dürfen Fragestellungen motivieren, gelten aber weder als Evidenz noch als Bestandteil der AVI-Gleichungen.

Die [`S_i-Sensitivitätsmatrix v0.1`](docs/si-sensitivity-matrix-v0.1.md) verankert diese Signatur erstmals an realen experimentellen Kanälen: optischen Atomuhren, molekularen Übergängen, nuklearen Langzeitdaten und Äquivalenzprinziptests. Sie trennt ausdrücklich Messpräzision, physikalische Parametergrenzen und erst noch abzuleitende AVI-Grenzen und formuliert den nächsten Schritt als vorab festzulegende minimale Kopplungsfamilie.

Die [`minimale differentielle Kopplungsfamilie v0.1`](docs/minimal-differential-coupling-v0.1.md) legt diese erste Class-B-Modellstruktur nun vor dem Datenfit fest: `D=λξn`, mit genau einer lokalen Kopplungsamplitude je präregistrierter Signaturrichtung. Common-mode-Anteile fallen aus lokalen Ratenverhältnissen heraus; die noch offene zentrale Aufgabe ist damit die unabhängige Dynamik und Normierung von `ξ`.

Das [`minimale ξ-Dynamikmodell v0.1`](docs/xi-dynamics-v0.1.md) schließt die Historienseite zunächst phänomenologisch über `dξ/dN = κ(s-ξ)`. Damit wird Test B erstmals konstruktiv von einer unterschiedlichen vergangenen Standard-Treiberhistorie über `Δξ` bis zu einem differentiellen Ratenverhältnis formuliert. Offen bleibt bewusst die physikalisch begründete, vor dem Datenfit festzulegende Wahl des dimensionslosen Treibers `s[Y]`.

Das [`ξ-Treiber-Screening v0.1`](docs/xi-driver-screening-v0.1.md) vergleicht Expansionsrate, Expansionsänderung, Materieanteil, Epochenkontrast, Krümmung und Zustandsraumänderung ohne Anomaliefit. Für die erste explizite Testvariante `AVI-B0.1` wird provisorisch `s=-d ln H_std/dN-3/2` gewählt. Der nächste Gate-Test prüft zuerst, ob damit bei vollständig definiertem Standardzustand überhaupt physikalisch zulässige Historienseparation möglich ist.

Das [`Test-B-Determinismus-Gate v0.1`](docs/test-b-determinism-gate-v0.1.md) führt diese Prüfung durch. Ergebnis: `AVI-B0.1` besteht den **strong Test B** in seiner bisherigen Filterform nicht, wenn `Y` ein vollständiger Markov-Zustand der eindeutig lösbaren Standarddynamik ist. Ein Filter über die dadurch rekonstruierbare Standardhistorie erzeugt keinen unabhängigen physikalischen Zustand. Das Dokument trennt deshalb `Test B-weak` von `Test B-strong` und verlangt für die nächste AVI-Stufe eine physikalische Ontologie von `ξ` als echten zusätzlichen, globalen oder nicht-Markovschen Zustand.

Das [`ξ-Ontologie-Screening v0.1`](docs/xi-ontology-screening-v0.1.md) prüft diese drei Wege. Als primärer Forschungszweig wird globale Zustands-/Randinformation weiter untersucht, ohne sie bereits mit `ξ` oder `Φ` gleichzusetzen; nicht-Markovsche Dynamik bleibt Vergleichspfad, ein neuer lokaler Freiheitsgrad Reservepfad. Zugleich wird Test B in `B-F` (fundamentale Zustandsseparation) und `B-G` (globale Kontextseparation) präzisiert.

Das [`Global-Context Gate v0.1`](docs/global-context-gate-v0.1.md) prüft O2 gegen reale QFT-Referenzarchitekturen. Ergebnis: `PASS (architecture only)`. Globale/boundary Daten können über einen definierten Quantenfeldzustand lokale Erwartungswerte beeinflussen; Casimir-Physik und topologieabhängige Feldmoden liefern dafür den Referenzfall. Für AVI fehlen weiterhin ein spezifisches `G_global`, ein physikalischer Träger `Q` und die Herleitung einer differentiellen Ratenkopplung. Test `B-G` verlangt deshalb nun explizit einen vermittelnden Zustand `Q`.

Das [`Global Carrier Screening v0.1`](docs/global-carrier-screening-v0.1.md) prüft Quantenzustand, Modenspektrum, renormierten Stress-Energie-Tensor, lokale Korrelations-/Response-Struktur und einen hypothetischen neuen AVI-Zustand. Für Class B wird die lokale Korrelations-/Response-Struktur als stärkster Referenzcarrier priorisiert: `G_global -> quantum state/correlations -> local transition response -> rate ratio`. Ein neuer AVI-Freiheitsgrad wird ausdrücklich nicht eingeführt; zuerst folgt ein Response Gate gegen Standard-QFT.

Das [`QFT Response Gate v0.1`](docs/qft-response-gate-v0.1.md) bestätigt diesen Kanal als **Standard-QFT-Referenz**: global unterschiedliche, lokal klassisch gleiche Konfigurationen können über unterschiedliche Wightman-/Korrelationsstrukturen verschiedene lokale Detektorantworten erzeugen. Damit ist `Q4` kein fehlender AVI-Carrier mehr, sondern Teil des zwingenden Nullmodells. AVI muss einen zusätzlichen, präregistrierten Residualbeitrag relativ zu `QFT+GR` vorhersagen; andernfalls ist O2 als AVI-Mechanismus redundant. Nächster Schritt ist das `Residual-Space Gate`.

## Rolle im Ökosystem

AVI-Modell ist Teil des KUEPER-Ökosystems (Ökosystem-Code `AVI`) und die Vertiefung neben dem groben Überblick auf `thomas-kueper.de` (`/grundlagen/avi`). Beide beschreiben dasselbe kosmologische Modell und müssen inhaltlich zusammenpassen.

Details: [`decisions/ECO-ARC-0011-2026-DE.md`](https://github.com/thomaspeterkueper/kueper-ecosystem/blob/main/decisions/ECO-ARC-0011-2026-DE.md) im Repository `kueper-ecosystem`.

## Forschungsleitplanken

- etablierte physikalische Grundlagen werden von AVI-spezifischen Postulaten getrennt;
- Historienabhängigkeit muss formal definiert und prinzipiell testbar sein;
- ein zusätzlicher Zustandsparameter darf nicht nur vergangene Information umbenennen, sondern muss klare Dynamik- und Beobachtungsbedingungen erfüllen;
- Analogien aus Philosophie oder Metaphysik gelten nicht als physikalische Evidenz;
- Forschungsergebnisse werden zunächst als nicht-kanonische Kandidaten behandelt.

Das frühere Repository-Verständnis von AVI als allgemeine Methode „Aufnehmen, Verdichten, Integrieren“ ist mit der Scope-Korrektur vom 28.08.2026 aufgehoben.

## Verbindliche Ökosystem-Regeln

**[`kueper-ecosystem/docs/onboarding-template.md`](https://github.com/thomaspeterkueper/kueper-ecosystem/blob/main/docs/onboarding-template.md)**

Bitte auf diesen Link verweisen statt den Inhalt zu kopieren.

## Cross-Repository-Anforderungen

Änderungswünsche an andere Projekte werden nicht direkt committet, sondern als External Task in `external-tasks/open/` des jeweiligen Ziel-Repositories abgelegt. Anforderungen an AVI-Modell liegen entsprechend hier unter `external-tasks/open/`. Format: [`ECO-ARC-0006`](https://github.com/thomaspeterkueper/kueper-ecosystem/blob/main/decisions/ECO-ARC-0006-2026-DE.md).
