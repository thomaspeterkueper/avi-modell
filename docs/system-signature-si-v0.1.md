# AVI — Physikalische Systemsignatur S_i v0.1

**Stand:** 15. September 2026  
**Status:** Arbeitsdokument / Grundlagenphase

## 1. Zweck

Dieses Dokument präzisiert den nächsten offenen Baustein der Klasse-B-Ratenkopplung. Nach dem Closure-Vertrag und der Kandidatenanalyse für messbare Ratenverhältnisse ist zu klären, wodurch zwei physikalische Prozesse auf denselben zusätzlichen AVI-Zustand unterschiedlich reagieren könnten.

Die allgemeine Arbeitsform lautet

`C_i = C(S_i, Φ, ξ; θ)`.

`S_i` bezeichnet dabei keine metaphysische Eigenschaft eines Systems. Es soll eine ausschließlich physikalisch operationalisierbare Signatur des betrachteten Prozesses sein.

## 2. Epistemische Trennung

### [R] Etablierte Grundlage

Physikalische Übergänge und Raten reagieren unterschiedlich auf Änderungen etablierter dimensionsloser Kopplungen und Massenverhältnisse. Präzisionsvergleiche verschiedener Atom- und Molekülsysteme nutzen gerade diese unterschiedlichen Sensitivitäten, um mögliche Variationen fundamentaler Konstanten zu begrenzen.

### [H] AVI-Arbeitshypothese

Falls AVI einen zusätzlichen globalen Zustand `ξ` beziehungsweise eine daraus konstruierte Größe `Φ` benötigt und dieser Zustand lokale Raten beeinflusst, muss eine lokal beobachtbare Klasse-B-Wirkung differentiell sein. Zwei Prozesse `i` und `j` müssen dann verschiedene physikalische Sensitivitäten besitzen.

### [I] Heuristische Herkunft

Die Omnizedenz-Philosophie kann die Fragestellung motivieren: Ein Teil wird nicht nur isoliert betrachtet, sondern in Relation zu einem Ganzen und zu seinem Werden. Diese philosophische Perspektive ist weder physikalische Evidenz noch Bestandteil der AVI-Gleichungen. Für AVI wird daraus ausschließlich die prüfbare Frage gewonnen, welche physikalisch definierte Eigenschaft eines Teils seine differentielle Reaktion auf denselben globalen Zustand bestimmen könnte.

## 3. Definition von S_i

In v0.1 wird `S_i` als Vektor dimensionsloser Sensitivitätskoeffizienten aufgefasst:

`S_i = (K_i^α, K_i^μ, K_i^q, K_i^g, ...)`.

Die Einträge stehen schematisch für die Sensitivität der betrachteten Observable gegenüber etablierten dimensionslosen physikalischen Größen oder Sektoren, beispielsweise:

- Feinstrukturkonstante `α`;
- Proton-Elektron-Massenverhältnis beziehungsweise geeignete dimensionslose Massenverhältnisse;
- QCD-/nukleare Sensitivitäten, soweit sauber operationalisierbar;
- gravitative dimensionslose Vergleichsgrößen, soweit ein konkretes Experiment sie definiert.

Die Liste ist nicht als neue AVI-Physik zu verstehen. Sie bildet zunächst nur eine gemeinsame Sprache für bekannte differentielle Sensitivitäten.

## 4. Was S_i ausdrücklich nicht ist

`S_i` ist in dieser Arbeitsfassung keine Größe für

- Bewusstsein,
- biologische Komplexität,
- subjektive Zeit,
- allgemeine „Resonanzfähigkeit“,
- philosophischen Entwicklungsgrad,
- eine nicht operationalisierte Eigenschaft des Ganzen.

Solche Begriffe besitzen derzeit keine geeignete physikalische Messdefinition und würden die Falsifizierbarkeit des Modells schwächen.

## 5. Differentielle Observable

Für zwei Raten gilt weiterhin

`O_ij = Γ_i / Γ_j`.

Schematisch:

`Γ_i,AVI = Γ_i,std · C_i`

und

`Γ_j,AVI = Γ_j,std · C_j`.

Damit folgt

`O_ij,AVI / O_ij,std = C_i / C_j`.

Ist `C_i = C_j`, verschwindet eine universelle gemeinsame Ratenänderung aus diesem lokalen Verhältnis. Eine direkt lokale Klasse-B-Observable verlangt daher eine differentielle Antwort.

## 6. Minimaler Antwortansatz

Noch ohne mikroskopischen Mechanismus kann die Struktur der Antwort lokal um den Nullfall geschrieben werden als

`δ ln Γ_i = Σ_A K_i^A · δq_A + δ_AVI,i`,

wobei `q_A` etablierte dimensionslose Größen bezeichnet. AVI darf `δ_AVI,i` erst dann spezifizieren, wenn klar ist, ob der neue Zustand tatsächlich auf einen etablierten Sektor abgebildet wird oder eine neue Kopplungsstruktur postuliert werden muss.

Für das Verhältnis zweier Prozesse:

`δ ln O_ij = δ ln Γ_i - δ ln Γ_j`.

Damit werden gemeinsame Beiträge automatisch sichtbar beziehungsweise eliminieren sich.

## 7. Drei mögliche Bedeutungen von S_i

### S1 — etablierte Sensitivitätskarte

`S_i` enthält ausschließlich bekannte Sensitivitätskoeffizienten gegenüber dimensionslosen Konstanten. AVI würde dann vorhersagen müssen, wie `ξ` oder `Φ` eine oder mehrere dieser Größen effektiv beeinflusst.

Vorteil: unmittelbar mit Präzisionsexperimenten konfrontierbar.  
Nachteil: bereits sehr stark eingeschränkt.

### S2 — neue sektorielle Kopplung

`S_i` beschreibt die Stärke einer neuen AVI-Kopplung an verschiedene physikalische Sektoren. Diese Variante ist theoretisch weitergehend und benötigt einen eigenständigen Mechanismus sowie Konsistenz mit Äquivalenzprinzip, Lorentz-Symmetrie und bestehenden Präzisionstests.

### S3 — unabhängige kosmologische Referenz

Die lokale Rate wird nicht primär gegen eine zweite lokale Rate, sondern gegen eine unabhängig bestimmte geometrische oder kosmologische Größe verglichen. Dann kann eine gemeinsame lokale Skalierung prinzipiell beobachtbar werden, sofern die Referenz selbst nicht identisch mit skaliert.

Diese Variante verlangt eine besonders klare operationale Definition dessen, was gleichzeitig lokal gemessen und global inferiert wird.

## 8. Priorisierung

Für die nächste Forschungsstufe wird S1 als Kontroll- und Kalibrationsrahmen priorisiert. Das bedeutet nicht, dass AVI eine Variation von `α` oder Massenverhältnissen behauptet. Vielmehr liefern Atom-/Moleküluhren, Molekülspektren und nukleare Systeme bereits bekannte Sensitivitätsmatrizen und harte Nulltests.

S2 bleibt eine mögliche spätere AVI-spezifische Dynamik, darf aber nicht eingeführt werden, nur um vorhandene Grenzen zu umgehen.

S3 bleibt methodisch interessant, weil es dem ursprünglichen AVI-Gedanken einer lokalen Rate relativ zu globalen kosmologischen Referenzparametern nahekommt. Seine Messdefinition muss jedoch unabhängig von einer bloßen Aussage über „schnellere“ oder „langsamere“ Zeit formuliert werden.

## 9. Test B mit Systemsignaturen

Ein scharfer Test-B-Kandidat benötigt nun:

`Y_A(a*) = Y_B(a*)`,

bei kontrollierten Standard-Randbedingungen,

`ξ_A(a*) ≠ ξ_B(a*)`,

und für mindestens zwei geeignete Prozesse

`O_ij,A(a*) ≠ O_ij,B(a*)`.

Dabei müssen `S_i` und `S_j` vor dem Vergleich festgelegt sein. Sie dürfen nicht nach Beobachtung eines Unterschieds angepasst werden.

## 10. Falsifikationsschranke

Die Systemsignatur-Idee verliert ihren wissenschaftlichen Nutzen, wenn mindestens einer der folgenden Fälle eintritt:

1. `S_i` lässt sich nicht unabhängig von der zu erklärenden Anomalie definieren;
2. jede beliebige Rate erhält einen frei wählbaren Kopplungskoeffizienten;
3. alle zulässigen Kopplungen sind common-mode und daher lokal unbeobachtbar;
4. eine postulierte sektorielle Kopplung verletzt bereits etablierte Präzisionsgrenzen;
5. unterschiedliche Historien mit gleichem vollständig definiertem `Y(a*)` können im Modell keinen unterschiedlichen zusätzlichen Zustand erzeugen;
6. `ξ` oder `Φ` beeinflussen keine messbare Observable.

Diese Punkte sind keine Randbedingungen, die AVI umgehen soll, sondern echte Möglichkeiten des Scheiterns.

## 11. Rolle der Omnizedenz bei der Ideenfindung

Die zulässige Richtung ist

`philosophische Intuition → präzise Frage → physikalische Definition → unabhängiger Test`.

Nicht zulässig wäre

`philosophischer Begriff → gleichnamige physikalische Größe → scheinbare Bestätigung`.

Für die aktuelle Arbeit ist insbesondere die Relation Teil/Ganzes heuristisch produktiv. Sie legt nahe, nicht nach einer isolierten absoluten Rate zu fragen, sondern nach einer relationalen Observable zwischen einem lokalen Prozess, seiner physikalischen Signatur und einer unabhängig definierten Referenz.

Der Begriff „Werden“ kann analog die Frage nach Zustandskompression und Historienabhängigkeit motivieren. Ob eine solche zusätzliche Zustandsinformation in der Natur existiert, bleibt vollständig eine empirische Frage.

## 12. Nächster Schritt

Als nächstes ist eine kleine `S_i`-Sensitivitätsmatrix mit realen experimentellen Systemen aufzubauen. Sie soll mindestens enthalten:

- zwei optische/atomare Frequenzvergleiche mit deutlich verschiedenen Sensitivitäten;
- einen molekularen Vergleichskanal;
- einen nuklearen Langzeitkanal;
- einen gravitativen Konsistenzkanal;
- die jeweilige experimentelle Grenze;
- die Frage, welche AVI-Kopplungsvarianten dadurch bereits ausgeschlossen oder stark eingeschränkt wären.

Erst danach soll entschieden werden, ob S1 für eine schmale AVI-Hypothese ausreicht oder ob überhaupt ein wissenschaftlicher Grund für S2 beziehungsweise S3 besteht.
