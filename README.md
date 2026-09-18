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
