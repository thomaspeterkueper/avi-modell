# AVI — Relational Response Selection Gate v0.1

**Stand:** 28. September 2026  
**Status:** Core Gate nach Operator Minimality  
**Pfad:** AVI-R1 / O1–O2 boundary

## 1. Leitfrage

Kann eine globale/relationale AVI-Zustandsstruktur eine lokale dimensionslose Response erzeugen, ohne

(a) vollständig in QFT+GR aufzugehen oder  
(b) zu einer generischen lokalen EFT mit frei wählbaren Kopplungen zu werden?

## 2. Minimaler relationaler Zustandsraum

Wir definieren zunächst keine neue Feldvariable. Der vollständige Kandidatenzustand sei

Z = (Y_std, C, G, R),

mit:
- Y_std: vollständiger lokaler/standardphysikalischer Zustand;
- C: Kanal-, Apparate- und Umgebungszustand;
- G: globale/Rand-/relationale Information, soweit standardphysikalisch definiert;
- R: nur dann zusätzliche AVI-Struktur, wenn sie nicht aus (Y_std,C,G) rekonstruierbar ist.

Eine AVI-spezifische Relation darf nicht dadurch entstehen, dass Y_std oder C unvollständig gewählt werden.

## 3. Response-Kette

Allgemein:

G -> Q_local -> O_i.

Es gibt drei logisch verschiedene Fälle.

### R1-S — Standardrelation

Q_local ist vollständig durch QFT+GR, Feldzustand, Randbedingungen und Apparatezustand bestimmt.

Dann:

O_i = O_i,QFT+GR[Y_std,C,G].

Dies ist das etablierte Nullmodell und kein AVI-Term.

### R1-E — lokale EFT-Erweiterung

Eine zusätzliche lokale Variable/Wechselwirkung erzeugt

O_i = O_i,std × C_i(ξ,g_i,...).

Wenn die g_i unabhängig oder nur durch gewöhnliche EFT-Symmetrien eingeschränkt sind, ist dies generische BSM/EFT-Physik. AVI besitzt keinen eigenständigen Selektionsgewinn.

### R1-R — echte relationale Zusatzregel

Gesucht wäre

R[G,Y_std] -> {δ ln O_i}

mit einer gemeinsamen, vorab definierten Abbildung und weniger Freiheitsgraden als eine generische lokale EFT.

Nur R1-R könnte AVI-R1 bestehen.

## 4. Markov-Embedding-Test

Eine scheinbar nicht-Markovsche/historienabhängige Response ist kein zusätzlicher fundamentaler Zustand, wenn ein erweiterter Standardzustand Y_std' existiert, so dass

P(O_{t+dt}|history) = P(O_{t+dt}|Y_std'(t),C(t)).

Dann liegt IR-1/IR-2 vor.

AVI-R1 verlangt deshalb:

Es darf kein physikalisch vollständiges Standard-Markov-Embedding geben, das R absorbiert.

Aktueller Befund: **nicht gezeigt**.

## 5. QFT-Completeness-Test

Das QFT Response Gate liefert reale Fälle:

global/boundary data
 -> quantum state / correlation function
 -> local detector response.

Damit sind Casimir-, Topologie-, Vakuumzustands- und verwandte Korrelationsantworten zwingende Nullmodelle.

Eine AVI-R1-Abweichung muss operational als

Δ_i^R = ln O_i - ln O_i,QFT+GR

definiert werden, nachdem Y_std und C marginalisiert/kontrolliert wurden.

Aktueller Befund: **kein etabliertes Δ_i^R**.

## 6. EFT-Reduction-Test

Angenommen eine relationale Regel erzeugt lokal

δ ln O_i = λ R(G) S_i.

Falls dies bei allen zugänglichen Experimenten äquivalent beschrieben werden kann durch lokale effektive Kopplungen

g_i,eff(x) = g_i,0 + δg_i[R(G)],

ohne zusätzliche beobachtbare Konsistenzrelation, dann ist AVI-R1 empirisch nur eine Reparametrisierung einer EFT.

Daher muss AVI mindestens eine Relation liefern, die lokale EFT-Koeffizienten nicht unabhängig reproduzieren können, ohne zusätzliche Fine-Tuning-/Korrelationsannahmen.

Aktueller Befund: **nicht vorhanden**.

## 7. Parameterzählung

Generische EFT:
N relevante Operatoren -> bis zu N unabhängige Wilson-Koeffizienten plus Zustandsparameter.

AVI-R1 muss strenger sein. Minimal zulässig wäre z.B.

δ ln O_i = λ X_R S_i

mit:
- einem unabhängig bestimmten X_R;
- einem gemeinsamen λ;
- präregistriertem S_i;
- keiner kanalweisen Nachjustierung.

Noch stärker wäre eine parameterfreie Ratio-Relation:

Δ_i / Δ_j = S_i / S_j.

Dies wäre eine echte cross-observable prediction.

Derzeit sind weder X_R noch S_i fundamental hergeleitet.

## 8. Causality / no-signalling contract

Eine globale relationale Variable darf nicht als instantan steuerbarer Fernkanal wirken.

Verbindliche Bedingungen:
1. lokale Eingriffe außerhalb des vergangenen Lichtkegels dürfen keine kontrollierbare sofortige Änderung von O_i erzeugen;
2. globale Zustandsinformation muss durch zulässige Zustandspräparation/Dynamik definiert sein;
3. Response-Funktion darf Mikrokausalität nicht umgehen;
4. falls R nichtlokal ist, muss die nichtlokale Dynamik explizit zeigen, warum kein signalling entsteht.

Ohne diesen Vertrag ist R1-R nicht physikalisch vollständig.

## 9. Backreaction / Energie

Zwei Fälle:

A. R verändert lokale Hamiltonian-/Lagrangeparameter.
Dann müssen Energieaustausch, Stress-Energie und Rückwirkung bilanziert werden.

B. R verändert nur relationale Wahrscheinlichkeiten/Constraints ohne lokalen Energiecarrier.
Dann muss eine konsistente Dynamik zeigen, wie Normierung, Unitarität bzw. geeignete Verallgemeinerung und Erhaltungssätze bestehen.

„Global“ ist keine Befreiung von dieser Buchhaltung.

## 10. Nullvorhersage

AVI-R1 muss mindestens eine Klasse von Systemen festlegen, für die

Δ_i^R = 0

obwohl ein globaler Kontext G vorhanden ist.

Ohne Nullkanäle kann jede Abweichung nachträglich als sensitiv erklärt werden.

Derzeit existiert keine fundamental hergeleitete Nullklasse.

## 11. Cross-observable relation

Minimaler Zieltyp:

Δ_i / Δ_j = K_ij

mit K_ij vor Datenkontakt aus derselben relationalen Struktur abgeleitet.

Eine solche Relation wäre stärker als unabhängige g_i und könnte AVI von generischer EFT unterscheiden.

Derzeit existiert kein hergeleitetes K_ij.

## 12. Gate-Matrix

| Test | Ergebnis |
|---|---|
| unabhängige relationale Information | logisch möglich, nicht etabliert |
| Standard-Markov-Embedding ausgeschlossen | FAIL / offen |
| QFT+GR-Nullmodell abgezogen | konzeptionell PASS |
| zusätzlicher Residualterm nachgewiesen | FAIL / nicht etabliert |
| EFT-Reduktion vermieden | FAIL / nicht gezeigt |
| weniger Parameter als generische EFT | Ziel definiert, nicht erreicht |
| Kausal/no-signalling contract | Anforderungen definiert, keine Dynamik |
| Backreaction accounting | Anforderungen definiert, keine Dynamik |
| präregistrierte Nullvorhersage | FAIL |
| cross-observable relation | FAIL |

## 13. Gate-Entscheidung

**AVI-R1 = HOLD, with a strong negative constraint.**

Warum nicht PASS:
Es gibt noch keine konstruktive relationale Response, die Standard-QFT+GR und generische EFT übertrifft.

Warum nicht endgültig FAIL:
Die bisherigen Gates schließen logisch nicht aus, dass eine globale/relationale Constraint-Struktur existiert, die eine kleine gemeinsame Response-Matrix erzwingt. Diese Struktur ist aber derzeit nicht formuliert.

Damit gilt:

> Relationalität ist eine zulässige Suchrichtung, aber noch kein Mechanismus.

## 14. Harte Konsequenz für AVI

Der nächste Fortschritt darf nicht durch Hinzufügen eines weiteren freien Zustands oder Operators erfolgen.

Erforderlich ist stattdessen eine **Response Algebra**: eine mathematische Regel, die aus einer unabhängig definierten relationalen Zustandsstruktur die relativen Sensitivitäten mehrerer Observablen bestimmt.

Ohne diese Algebra konvergiert AVI entweder zu Standard-QFT+GR oder zu generischer EFT.

## 15. Minimal Response Algebra Challenge — MRA-1

Gesucht sind Strukturen der Form

R : G_rel × S_phys -> V_obs

mit:
- G_rel: unabhängig definierter relationaler/globaler Zustand;
- S_phys: standardphysikalisch vollständige lokale Systembeschreibung;
- V_obs: Vektor dimensionsloser Residualresponses.

Die Abbildung muss:
1. kovariant/operational eindeutig sein;
2. keine Zielresiduen zur Definition von G_rel verwenden;
3. höchstens einen gemeinsamen neuen Skalen-/Kopplungsparameter benötigen;
4. mindestens eine Nullrichtung in V_obs besitzen;
5. mindestens eine feste Ratio/Linearrelation zwischen zwei nichtidentischen Kanälen liefern;
6. im Nullfall exakt QFT+GR ergeben;
7. no-signalling und Backreaction-Bedingungen erfüllen.

## 16. Falsifikationssatz

Falls jede konkrete MRA-1-Realisierung entweder

- vollständig als QFT+GR-Zustands-/Korrelationsresponse geschrieben werden kann, oder
- eine Menge unabhängiger lokaler Wilson-Koeffizienten benötigt,

dann besitzt AVI-R1 keine eigenständige physikalische Struktur.

Das wäre ein klarer Grund, O1/O2 als fundamentalen AVI-Mechanismus zu schließen und AVI auf methodische/phenomenologische Rollen zu reduzieren oder neu zu axiomatisieren.

## 17. Konsequenzen für bestehende Pfade

- **CB-1:** bleibt theory-gated; keine AVI-spezifische birefringence prediction.
- **Test B-F:** HOLD.
- **RS2:** logisch offen, empirisch/theoretisch nicht qualifiziert.
- **IR-3:** nicht etabliert.
- **Φ/W:** keine Ontologie; nur Arbeitsgrößen.
- **ξ_AVI:** undefined, solange keine MRA-1-Struktur einen zusätzlichen Zustand verlangt.

## 18. Nächster Schritt

Nicht weitere Datenkanäle sammeln.

Nächster Kernschritt:

**MRA-1 — Minimal Response Algebra Construction Screen.**

Dabei werden zunächst bekannte mathematische Klassen als Kontrollen geprüft:
- lineare Response-/Suszeptibilitätsmatrizen;
- constrained low-rank response;
- symmetry/representation-based selection rules;
- relational/conditional-state maps;
- nonlocal kernels mit kausaler Unterstützung.

Ziel ist nicht, eine passende Formel zu erfinden, sondern festzustellen, ob irgendeine sparsame Struktur die AVI-Kriterien erfüllt, ohne bekannte Physik umzubenennen.

## 19. Epistemischer Status

- [R] Globale/Randinformation kann in QFT lokale Response über Zustände/Korrelationen beeinflussen.
- [R] Nicht-Markovsche reduzierte Dynamik kann durch Erweiterung des Zustandsraums Markov-Struktur zurückgewinnen; dies ist ein zwingendes Kontrollprinzip.
- [D] Relationalität allein ist keine neue Wechselwirkung.
- [D] Eine empirisch eigenständige AVI-Struktur benötigt feste cross-observable constraints, nicht nur zusätzliche freie Kopplungen.
- [OFFEN] Ob eine Minimal Response Algebra existiert, die diese Bedingungen erfüllt.
