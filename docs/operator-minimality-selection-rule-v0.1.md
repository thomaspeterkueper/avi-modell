# AVI — Operator Minimality Selection Rule v0.1

**Stand:** 27. September 2026  
**Status:** kritisches Struktur-Gate nach Minimal ξ Degree-of-Freedom Gate und CB-1A  
**Pfad:** O1-minimal / Test B-F

## 1. Gate-Frage

Besitzt AVI bereits eine unabhängig motivierte Struktur, die den zulässigen Kopplungs-/Operatorraum enger macht als eine generische EFT mit einem zusätzlichen Freiheitsgrad?

PASS ist nur zulässig, wenn die Restriktion aus AVI vor Wahl einer Anomalie/Observable folgt.

## 2. Vorab feststehende AVI-Aussagen

Aus dem bisherigen Kanon folgen:
- ξ trägt unabhängige Zustandsinformation, falls O1 realisiert wird;
- ξ ist nicht als Funktion des vollständigen Standardzustands definierbar;
- die Schreibweise ξ(a) legt weder Spin noch Lorentzrepräsentation fest;
- Globalität darf lokale Konsistenzbedingungen nicht umgehen;
- ein messbarer Class-B-Effekt muss differentiell sein;
- Standardphysik muss im Entkopplungsgrenzfall exakt zurückkehren.

Nicht festgelegt sind:
- scalar vs pseudoscalar vs vector/tensor;
- P/CP/CPT-Transformation;
- lokale Feldnatur;
- interne Symmetrie oder shift symmetry;
- UV-Ursprung;
- operatorabhängige Ladungen/Selektionsregeln.

## 3. EFT-Basis-Screening

### S0 — echter Lorentz-Skalar

Niedrigdimensionale Portale umfassen schematisch Kopplungen an gauge-invariante Standardoperatoren, z.B. Higgs-, Fermionmassen-, Gauge-kinetische und gluonische Strukturen.

Folge: differentielle Ratenänderungen sind möglich, aber fifth-force-, Äquivalenzprinzip-, varying-constant-, stellar- und cosmological constraints werden unmittelbar relevant.

AVI-spezifische Selektion: **keine vorhanden**.

### P0 — Pseudoskalar

Die bekannte parity-odd Basis enthält insbesondere

χ F_{μν} F_tilde^{μν}

und analoge duale nichtabelsche Gaugeoperatoren sowie derivative Fermionkopplungen.

Eine approximate shift symmetry kann einen leichten pseudoskalaren Zustand technisch schützen, ist aber eine zusätzliche axionartige Modellannahme und folgt nicht aus AVI.

AVI-spezifische Selektion: **keine vorhanden**.

### V/T — Vektor oder Tensor

Solche Zustände benötigen zusätzliche Lorentz-/Gauge-Struktur und erzeugen typischerweise Richtungs-, Polarisations- oder preferred-frame-Signaturen.

AVI liefert derzeit keine Motivation für diese höhere Strukturkosten.

AVI-spezifische Selektion: **keine vorhanden**.

### G — globaler / nichtlokaler Zustand

Dies liegt konzeptionell näher an der ursprünglichen AVI-Idee, erzeugt aber ohne explizite Wirkung keine Operatorselektion. Sobald G lokal messbare Prozesse beeinflusst, ist eine wohldefinierte Response-Abbildung

G_global -> Q_local -> O_i

erforderlich. Wird Q_local durch bekannte QFT-Korrelationen vollständig beschrieben, ist der Effekt Nullmodell; wird ein neuer lokaler Carrier eingeführt, kehrt das EFT-Problem zurück.

AVI-spezifische Selektion: **noch keine konstruktive Regel**.

## 4. Kann Historienabhängigkeit Operatoren selektieren?

Nein, nicht allein.

Eine Zustandsvariable kann historienabhängig sein und dennoch an beliebige symmetrieerlaubte Standardoperatoren koppeln. Memory/Retention bestimmt die Dynamik des Zustands, nicht automatisch dessen Standardmodell-Ladungen oder P/CP-Eigenschaften.

Daher gilt:

history dependence != interaction selection rule.

## 5. Kann Globalität Operatoren selektieren?

Nicht ohne zusätzliche Struktur.

Ein räumlich homogener Zustand kann weiterhin skalar, pseudoskalar oder anderer Natur sein. Homogenität unterdrückt räumliche Gradienten, bestimmt aber nicht die interne Symmetrie der Kopplung.

Daher gilt:

global/homogeneous != scalar/pseudoscalar selection.

## 6. Kann Differentialität Operatoren selektieren?

Nur schwach.

Die Forderung O_ij != common mode schließt rein universelle Multiplikationen aus. Sie wählt jedoch keine eindeutige mikroskopische Operatorfamilie; viele scalar-, pseudoscalar- und andere EFT-Kopplungen erzeugen differentielle Sensitivitäten.

Differentialität ist daher ein **Messbarkeitsfilter**, keine Theorie-Selektionsregel.

## 7. Radiative Stabilität / technische Natürlichkeit

Ein postuliertes Fehlen niedrigerdimensionaler, symmetrieerlaubter Kopplungen ist ohne Schutzsymmetrie nicht stabil begründet. Eine echte AVI-Minimalität müsste deshalb entweder

A. eine Symmetrie liefern, die unerwünschte Operatoren verbietet,
B. eine Constraint-/Topologiestruktur liefern, aus der die Kopplung eindeutig folgt,
C. oder zeigen, dass der relevante Zustand gar kein lokaler EFT-Freiheitsgrad ist und dennoch eine konsistente, kausale Response besitzt.

Keine dieser drei Bedingungen ist derzeit erfüllt.

## 8. Backreaction Gate

Ein dynamischer lokaler Zustand besitzt im Allgemeinen Stress-Energie und/oder induziert Standardsektor-Korrekturen. Striktes Class B (lokale differentielle Wirkung bei H = H_std) ist deshalb keine fundamentale Eigenschaft, sondern muss quantitativ als kontrollierter Grenzfall bewiesen werden.

Bis dahin:
- Class B = approximation candidate;
- Class C = mandatory comparison branch.

## 9. Operator-Minimality-Ergebnis

### Gate verdict: FAIL AS DISTINCT OPERATOR THEORY / HOLD FOR AVI

Der gegenwärtige AVI-Kanon **selektiert keine kleinere Operatorbasis als generische EFT**.

Das ist ein negatives, aber produktives Ergebnis:
- O1-minimal bleibt logisch möglich;
- Test B-F bleibt formal definierbar;
- ξ darf nicht als neues Feld mit frei gewählten Kopplungen ausgegeben werden;
- keine beobachtete Anomalie darf zur Auswahl von Spin, Parität oder Portal benutzt werden;
- CB-1B1 bleibt BLOCKED.

## 10. Harte No-Go-Regel

Ab v0.1 gilt:

> Eine AVI-spezifische lokale Kopplung ist nicht kanonisch zulässig, solange ihre Transformations- und Selektionsregel nicht unabhängig aus einer tieferen AVI-Struktur hergeleitet wurde.

Insbesondere unzulässig:
- ξ -> pseudoscalar, weil cosmic birefringence interessant ist;
- ξ -> scalar, weil Atomuhren sensitiv sind;
- ξ -> matter coupling, weil S8/H0 betroffen sein könnten;
- sektorabhängige g_i als freie Fitparameter ohne Selektionsprinzip.

## 11. Verbleibende eigenständige Suchrichtung

Die stärkste noch offene AVI-spezifische Möglichkeit ist **nicht** ein weiterer Standard-EFT-Operator, sondern eine strengere Zustands-/Relationsstruktur:

AVI-R1:
1. fundamentaler zusätzlicher Zustand trägt relationale/global definierte Information;
2. diese Information ist nicht als lokales Standardfeld rekonstruierbar;
3. lokale Wirkung entsteht über eine eindeutig definierte Response-Regel;
4. die Regel besitzt weniger freie Kopplungen als generische EFT;
5. QFT+GR wird im Nullfall exakt reproduziert;
6. Kausalität, Energieerhaltung/Backreaction und Markov-Embedding werden explizit geprüft.

Dies ist noch keine Theorie, aber eine echte Selektionsanforderung.

## 12. Konsequenzen

### CB-1
CB-1 bleibt externer Constraint-/Vergleichskanal. CB-1B0 ist zulässig; CB-1B1 bleibt gesperrt.

### Lokale Raten
Die bestehende S_i-Struktur bleibt phänomenologische Testsprache, darf aber nicht als fundamentale Kopplung interpretiert werden.

### Test B-F
B-F kann erst wieder auf PASS wechseln, wenn AVI-R1 eine unabhängige Zustandsinformation **und** eine nicht-beliebige Response-Abbildung konstruktiv liefert.

### Φ und W
Φ/W bleiben Arbeitsgrößen für globale/Historienstruktur. Ihnen werden durch dieses Gate keine Lorentz-, Paritäts- oder Teilcheneigenschaften zugewiesen.

## 13. Nächster Gate-Test

**Relational Response Selection Gate (AVI-R1).**

Frage:
Kann eine globale/relationale AVI-Zustandsstruktur eine lokale dimensionslose Response erzeugen, ohne entweder
(a) vollständig in QFT+GR aufzugehen oder
(b) zu einer generischen neuen lokalen EFT mit frei wählbaren Kopplungen zu werden?

PASS-Kriterien:
- mathematisch definierter state space;
- eindeutige Response map;
- höchstens sehr kleine präregistrierte Parameterzahl;
- explizite Kausal-/Backreaction-Struktur;
- mindestens eine Nullvorhersage und eine nichttriviale falsifizierbare Relation zwischen mehreren Observablen;
- keine Definition durch bestehende Anomalien.

## 14. Epistemischer Status

- [R] EFT-Operatoren werden durch Feldinhalt und Symmetrien eingeschränkt; zusätzliche Schutzsymmetrien können Operatorräume weiter reduzieren.
- [R] Leichte scalar/pseudoscalar Kopplungen unterliegen Präzisions-, astrophysikalischen und kosmologischen Constraints.
- [D] Historienabhängigkeit, Globalität und Differentialität allein selektieren keine eindeutige Standardmodell-Kopplung.
- [D] AVI besitzt derzeit keine eigenständige Operator-Selektionsregel.
- [OFFEN] Ob AVI-R1 eine relationale Response-Struktur liefert, die weder Standard-QFT+GR noch generische EFT umbenennt.
