# AVI — Core Stress-Test v0.1

**Stand:** 27. September 2026
**Status:** interner Falsifikations-/Validierungstest
**Voraussetzung:** Core Formalization v0.1

## 1. Ziel

Der Core wird absichtlich mit bekannten Fällen konfrontiert, die bei unvollständiger Zustandsbeschreibung wie zusätzliche Historienabhängigkeit aussehen können.

Pass-Kriterium:

    known standard mechanism
      -> correctly absorbed by Ω or M_std
      -> no false Z extension.

Fail-Kriterium:

    known standard mechanism
      -> Core incorrectly requires Z.

## 2. ST-1 — Hysterese und interne Zustandsvariablen

### Scheinbarer AVI-Fall

Zwei Systeme besitzen dieselben äußeren Kontrollparameter u(t*):

    u_A(t*) = u_B(t*)

aber unterschiedliche Historien und unterschiedliche Response:

    H_A != H_B
    O_A != O_B.

### Core-Audit

Der sichtbare Kontrollvektor u ist kein vollständiges Y.

Bei Hysterese existieren interne Zustandsgrößen m, Defektpopulationen, Domänenstruktur, Relaxationsvariablen oder vergleichbare Standardfreiheitsgrade.

Daher:

    Y = (u,m,...)

und im Allgemeinen

    Y_A != Y_B.

### Ergebnis

    apparent history effect -> incomplete Y -> standard closure restored.

**ST-1: PASS.**

Kein Z zulässig.

## 3. ST-2 — offenes nicht-Markovsches Quantensystem

### Scheinbarer AVI-Fall

Zwei reduzierte Systemzustände können zum Zeitpunkt t* gleich erscheinen,

    ρ_S,A(t*) = ρ_S,B(t*)

aber aufgrund verschiedener System-Umwelt-Korrelationen unterschiedliche spätere Dynamik zeigen.

### Core-Audit

ρ_S allein ist nicht zwingend Ω.

Je nach Beschreibung gehören relevante Umweltfreiheitsgrade und Korrelationen zu Y/G beziehungsweise die etablierte Memory-Kernel-Dynamik zu M_std.

Schematisch:

    Ω = (ρ_S, ρ_E, correlations, B, G, C)

oder

    reduced Ω_S + standard non-Markovian evolution law.

Damit darf die Differenz nicht als neues Z klassifiziert werden, solange die etablierte offene-System-Dynamik closure liefert.

### Ergebnis

    reduced-state non-Markovianity
      -> enlarge standard state or standard dynamics
      -> no AVI extension.

**ST-2: PASS.**

Wichtige Präzisierung: A3 muss "present carrier" nicht als ausschließlich lokale momentane Variable verstehen. Der Träger kann in System-Umwelt-Korrelationen oder in einer physikalisch begründeten nicht-Markovschen Dynamik liegen. Core Formalization v0.1 enthält diese Möglichkeit bereits.

## 4. ST-3 — globale/topologische QFT-Kontexte

### Scheinbarer AVI-Fall

Lokale klassische Geometrie und Detektormikrophysik sind gleich, aber lokale Übergangsraten unterscheiden sich bei verschiedener globaler Topologie/Randstruktur.

### Core-Audit

Die globale Information gehört zu G.

    Ω = (Y,B,G,C).

Standard-QFT liefert

    G
      -> quantum state / Wightman correlations
      -> local detector response.

Damit gilt nicht Ω_A ~_Q Ω_B, sobald Q die Detektorresponse umfasst und G_A != G_B.

### Ergebnis

    global context effect -> G + QFT response -> standard closure.

**ST-3: PASS.**

Kein Z zulässig. Dies reproduziert das Ergebnis des QFT Response Gate.

## 5. ST-4 — Standard-Sirenen / Sichtlinienbeschleunigung

Referenz: OTA-SCI-0093-2026-DE / OBS-07.

### Scheinbarer AVI-Fall

Mehrere Ereignisse können eine kohärent verschobene H0-Inferenz liefern. Zusätzliche Daten reduzieren dabei die statistische Breite, ohne einen nicht modellierten Bias zwingend auszumitteln.

### Core-Audit

Die relevante Sichtlinienbeschleunigung/Umgebung gehört zum Kanalzustand C.

Eine Inferenz nur mit

    P(O|Y)

ist unvollständig.

Erforderlich ist

    P(O|Y,C,M_std)

und anschließend Marginalisierung über C.

### Ergebnis

    apparent cosmological residual -> incomplete C -> standard inference repair.

**ST-4: PASS.**

Kein Z zulässig.

## 6. ST-5 — TRGB-H0 / lokale Feldrekonstruktion

Referenz: OTA-SCI-0094-2026-DE / OBS-08.

### Scheinbarer AVI-Fall

Dieselben Distanzdaten können bei unterschiedlichen zulässigen Rekonstruktionen lokaler Dichte-/Peculiar-Velocity-Felder verschiedene H0-Posterioren erzeugen.

### Core-Audit

Die Rekonstruktionen sind Samples beziehungsweise alternative Realisierungen innerhalb

    P(Ω | D,M_std).

Sie sind keine zusätzlichen ontischen Zustände.

Die korrekte Standardvorhersage marginalisiert über diese Unsicherheit:

    P_std(O|D,M_std)
      = integral dΩ P_std(O|Ω,M_std) P(Ω|D,M_std).

### Ergebnis

    reconstruction spread -> epistemic uncertainty -> posterior predictive propagation.

**ST-5: PASS.**

Kein Z zulässig.

## 7. ST-6 — coarse graining / gleicher Makrozustand

### Scheinbarer AVI-Fall

    M_A(t*) = M_B(t*)
    H_A != H_B
    O_A != O_B.

### Core-Audit

Wenn O von mikroskopischen Freiheitsgraden abhängt, ist M nicht der für Q vollständige Zustand.

Die Äquivalenzrelation des Core verlangt nicht Koordinatengleichheit, sondern

    Ω_A ~_Q Ω_B.

Wenn die Mikrozustände unterschiedliche Q-Prädiktionen erzeugen, sind sie definitionsgemäß nicht Q-äquivalent.

### Ergebnis

**ST-6: PASS.**

Der Core verhindert, dass Gleichheit eines groben Makrozustands als starker Same-State-Test ausgegeben wird.

## 8. ST-7 — irreversibler thermodynamischer Prozess

### Scheinbarer AVI-Fall

Ein System trägt heute Defekte, Gradienten oder Zusammensetzungsunterschiede, die von seiner Herstellung abhängen.

### Core-Audit

Soweit diese Spuren heute die Response beeinflussen, gehören sie zu Y. Sind alle operationalen Spuren verschwunden und erzeugen verschiedene Historien dieselbe Standardprädiktion, dann sind die Historien bezüglich Q nicht unterscheidbar und benötigen kein Z.

### Ergebnis

    retained trace -> Y
    no retained trace -> operationally irrelevant history.

**ST-7: PASS.**

## 9. Adversarial Test — falsche Z-Konstruktion aus Residuen

Setze künstlich

    Z := mean(r_k)

und erkläre anschließend

    r_k = λ Z S_k.

### Core-Audit

Verletzt E3 Independent Definition und A5.

### Ergebnis

**ST-A1: REJECTED AS REQUIRED.**

Der Core blockiert zirkuläre Ontologisierung eines Residuals.

## 10. Adversarial Test — einzelner signifikanter Kanal

Angenommen ein Kanal liefert großes |r_1|, alle anderen sind unauffällig.

### Core-Audit

E2 verlangt Robustheit und E6 sparsame Cross-Channel-Struktur. Zusätzlich müssen C, Ω-Rekonstruktion und Modellmissspezifikation geprüft werden.

### Ergebnis

**ST-A2: NO AUTOMATIC EXTENSION.**

Ein einzelner Ausreißer öffnet Z nicht.

## 11. Adversarial Test — echter hypothetischer Closure-Fehler

Konstruiere abstrakt zwei Fälle mit

    Ω_A ~_Q Ω_B

unter vollständig spezifiziertem M_std, aber reproduzierbar

    P_obs(Q|A) != P_obs(Q|B),

wobei der Unterschied über unabhängige Replikationen und Kanäle bestehen bleibt.

### Core-Audit

E1 und E2 könnten damit bestanden werden.

Der Core führt aber nicht automatisch Z ein. Es folgen E3–E8: unabhängige Definition, Dynamik, quantitative Vorhersage, Sparsamkeit, Nullgrenze und Falsifikationsbereich.

### Ergebnis

**ST-A3: DISCOVERY PATH OPENS, AVI NOT CONFIRMED.**

Dies ist das gewünschte Verhalten.

## 12. Gefundene Schwachstelle: Zustandsäquivalenz

Die Definition

    Ω_A ~_Q Ω_B
    iff
    P_std(q|Ω_A)=P_std(q|Ω_B) for all q in Q

ist operational nützlich, aber allein zu schwach, wenn Q zu eng gewählt wird.

Zwei physikalisch verschiedene Standardzustände können für eine kleine Observablenfamilie Q zufällig dieselbe Prädiktion liefern.

Daher muss für starke Same-State-Behauptungen zusätzlich gelten:

    all standard state coordinates relevant to the tested dynamics are matched or marginalized,

nicht nur predictive equivalence auf einer kleinen Zielmenge.

### Patch-Regel

Es werden zwei Begriffe getrennt:

**Q-equivalence**

    Ω_A ~_Q Ω_B

= gleiche Standardprädiktion für die vorab definierte Q-Familie.

**Strong state equivalence**

    Ω_A ≡_std Ω_B

= Gleichheit aller im Standardmodell dynamisch relevanten Zustands-, Rand-, Global- und Kanalinformationen bis auf explizit marginalisierte Unsicherheit.

Ein Strong History Test verlangt ≡_std, nicht nur ~_Q.

## 13. Gesamtresultat

| Test | Mechanismus | Core-Klassifikation | Ergebnis |
|---|---|---|---|
| ST-1 | Hysterese | fehlende interne Y-Komponente | PASS |
| ST-2 | offenes Quantensystem | Umwelt/Korrelation/M_std | PASS |
| ST-3 | globale QFT-Response | G + Standard-QFT | PASS |
| ST-4 | Standard-Sirenen | Kanalzustand C | PASS |
| ST-5 | TRGB-H0 | P(Ω|D,M) | PASS |
| ST-6 | coarse graining | unvollständiger Zustand | PASS |
| ST-7 | Thermodynamik | Y oder operational irrelevant | PASS |
| ST-A1 | Z aus Residuum | E3-Verletzung | REJECT |
| ST-A2 | Einzelkanal-Ausreißer | E2/E6 nicht erfüllt | HOLD |
| ST-A3 | echter Closure-Fehler | E3–E8 werden geöffnet | CORRECT |

## 14. Gate-Ergebnis

**Core Stress-Test v0.1: PASS WITH ONE FORMAL PATCH.**

Der Core erzeugt in den geprüften bekannten Standardfällen keine falsche zusätzliche Ontologie.

Die gefundene Schwachstelle betrifft nicht Ω oder den Closure-Begriff, sondern die Gleichsetzung von Q-bezogener prädiktiver Äquivalenz mit starker physikalischer Zustandsäquivalenz.

Diese muss in Core Formalization v0.2 getrennt werden.

## 15. Konsequenz

Der Core ist robust genug für den nächsten Formalisierungsschritt, aber noch nicht für einen empirischen AVI-Test.

Vor Datenarbeit ist erforderlich:

1. Core Formalization v0.2 mit ~_Q versus ≡_std;
2. Definition eines auditierbaren State-Completeness-Manifests;
3. erst danach Auswahl eines konkreten Testbeds.

Kein ξ-, Φ- oder Z-Modell wird durch diesen Stress-Test reaktiviert.
