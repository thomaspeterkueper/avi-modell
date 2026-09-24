# AVI — Residual-Space Gate v0.1

**Stand:** 24. September 2026  
**Status:** kritisches Modellgate nach QFT Response Gate  
**Pfad:** O2 / Class B — globale Kontextseparation

## 1. Gate-Frage

Existiert nach vollständiger Standardmodellierung durch QFT+GR ein logisch sauber definierbarer Raum für eine zusätzliche AVI-Relation, ohne dass das Residuum selbst zur Definition des AVI-Zustands benutzt wird?

Gesucht ist nicht

    Beobachtung - unvollständiges Standardmodell = AVI,

sondern eine vorab definierte Struktur

    unabhängig bestimmtes X_global
      -> präregistrierte AVI-Kopplung
      -> mehrere lokale Observablen,

deren Nullfall exakt QFT+GR reproduziert.

## 2. Ausgangspunkt

Das QFT Response Gate hat gezeigt:

    G_global
      -> field state / correlations
      -> local response

ist bereits Standard-QFT.

Damit kann weder globale Kontextsensitivität noch eine lokale Response auf globale Topologie oder Randbedingungen für sich allein als AVI-Signal gelten.

Für jeden Kanal k gilt deshalb zunächst

    O_k,pred,std = F_k[QFT, GR, geometry, state, boundary data, apparatus, environment].

Erst danach ist ein Residuum definierbar:

    r_k = ln O_k,obs - ln O_k,pred,std.

## 3. Residuum ist keine Zustandsvariable

Ein zentrales Verbot lautet:

> X_global, ξ oder Φ dürfen nicht aus denselben Residuen konstruiert werden, die anschließend durch sie erklärt werden sollen.

Unzulässig wäre beispielsweise

    ξ := weighted mean(r_k)

und danach

    r_k = λ ξ S_k.

Das wäre zirkulär und nicht unabhängig falsifizierbar.

Ein AVI-Zustand oder globaler Prädiktor muss vor Betrachtung der Zielresiduen durch Theorie oder unabhängige Messung definiert sein.

## 4. Drei Residualräume

### RS1 — geschlossener Standardraum

Alle beobachtbaren global-context-abhängigen Response-Effekte sind innerhalb der Messgenauigkeit durch QFT+GR plus Apparate-, Umwelt- und Populationsmodellierung beschrieben.

Dann gilt:

    r_k compatible with 0

und es gibt keinen empirisch benötigten AVI-Term.

**Folge:** O2 bleibt als konzeptionelle Motivation interessant, ist aber als zusätzlicher physikalischer Mechanismus redundant.

### RS2 — gemeinsamer operationaler Residualraum

Nach vollständiger Standardmodellierung verbleibt in mehreren physikalisch verschiedenen Kanälen eine gemeinsame Abhängigkeit von einer **unabhängig bestimmten** globalen Größe X_global.

Minimal:

    r_k = λ f(X_global) S_k + ε_k

mit vorab definierter Funktion f, präregistrierter Signatur S_k und einem gemeinsamen sparsamen Parametersatz.

Dies wäre zunächst eine phänomenologische Erweiterung, kein Nachweis eines fundamentalen AVI-Zustands.

### RS3 — fundamentaler Erweiterungsraum

Die beobachtete oder theoretisch erforderliche Zusatzrelation kann nicht konsistent als effektive Korrelation formuliert werden und verlangt eine Modifikation von QFT/GR oder einen neuen Freiheitsgrad.

Dann muss AVI den minimalistischen O2-Pfad verlassen und eine konkrete fundamentale Theorie mit eigener Dynamik, Erhaltungssätzen und Konsistenzbedingungen formulieren.

## 5. Channel-State-Completeness Gate

Aus `OTA-SCI-0093-2026-DE` folgt eine zusätzliche zwingende Kontrolle.

Für jeden Messkanal wird neben dem kosmologischen/lokalen Zustand Y ein Kanalzustand C_k geführt:

    P(O_k | Y, C_k, QFT+GR).

Zu C_k gehören je nach Experiment beispielsweise:

- Apparate- und Kalibrationszustände;
- lokale Umgebung;
- Bewegung/Beschleunigung;
- Populations- und Selektionsparameter;
- Wellenform-/Response-Modell;
- Zustandspräparation und Randbedingungen.

Ein nicht modellierter C_k-Beitrag darf nicht in r_k als AVI-Residuum weitergereicht werden.

## 6. Mindestanforderungen an RS2

Ein RS2-Kandidat wird nur zugelassen, wenn alle folgenden Bedingungen erfüllt sind:

1. **X_global ist unabhängig definiert.**
   Keine Definition aus den Zielresiduen.

2. **Standard-QFT+GR ist vollständig spezifiziert.**
   Einschließlich Quantenzustand, Geometrie, Randbedingungen und relevanter Response.

3. **Channel-state completeness ist dokumentiert.**
   Relevante C_k sind modelliert, kontrolliert oder marginalisiert.

4. **Mindestens zwei physikalisch verschiedene Kanäle.**
   Ein einzelnes Residuum genügt nicht.

5. **Gemeinsame sparsame Kopplung.**
   Kein freies λ_k für jeden Kanal, das beliebige Abweichungen absorbieren kann.

6. **Vorzeichen-/Richtungsstruktur vor Datenfit.**
   S_k beziehungsweise ΔS_ij muss unabhängig festgelegt sein.

7. **Nullfall.**

       λ = 0 -> QFT+GR.

8. **Falsifikationsbereich.**
   Es muss mögliche Daten geben, die die gemeinsame AVI-Struktur verwerfen.

## 7. Minimale präregistrierbare Form

Als Arbeitsform, nicht als Naturgesetz:

    ln O_k,pred =
      ln O_k,QFT+GR
      + λ f(X_global) (S_k · n).

Für zwei Kanäle i,j:

    Δr_ij =
      r_i - r_j
      = λ f(X_global) [(S_i-S_j) · n].

Vorteile:

- common-mode Beiträge werden reduziert;
- die Zahl freier Parameter bleibt klein;
- die Systemsignatur ist separat prüfbar;
- Standardphysik bleibt explizites Nullmodell.

Diese Form wird erst datenfähig, wenn X_global physikalisch unabhängig definiert ist.

## 8. Kandidaten für X_global

Derzeit ist **kein AVI-spezifisches X_global etabliert**.

Zulässige Kandidatensuche darf nur Größen betrachten, die:

- global oder kosmologisch wohldefiniert sind;
- unabhängig vom lokalen Zielresiduum messbar oder berechenbar sind;
- nicht bloß eine andere Schreibweise der bereits in QFT+GR enthaltenen Zustandsinformation darstellen;
- eine kausal und mathematisch definierte Verbindung zur lokalen Response besitzen.

Topologie, globale Modendaten oder kosmologische Zustandsgrößen dienen zunächst als Kontrollen. Sie werden nicht automatisch zu AVI-Variablen.

## 9. Verhältnis zu ξ und Φ

Nach diesem Gate gelten vorläufig:

    X_global = unabhängig definierter globaler Prädiktor
    ξ = nur zulässig, falls eine zusätzliche Zustandsvariable wirklich benötigt wird
    Φ = mögliche integrierte Arbeitsgröße, nicht automatisch fundamental

Für RS2 ist ξ nicht zwingend erforderlich. Eine sparsame direkte Relation

    X_global -> residual response

ist methodisch vorzuziehen, solange kein unabhängiger Grund für einen zusätzlichen Zustand existiert.

Damit wird vermieden, ξ allein zur Rettung der bisherigen AVI-Sprache einzuführen.

## 10. Ergebnis des Gates

Das logische Ergebnis lautet:

    RS1: offen und Standard-Default
    RS2: logisch zulässig, aber noch ohne qualifiziertes X_global
    RS3: logisch zulässig, derzeit unbegründet

Damit besteht das Residual-Space Gate **nur konditional**:

> Ein nicht-zirkulärer AVI-Residualraum ist definierbar, aber derzeit existiert weder ein empirischer Bedarf noch ein unabhängig qualifizierter globaler AVI-Prädiktor.

Dies ist kein Scheitern von AVI. Es verschiebt die Forschungsfrage auf den entscheidenden Punkt: Gibt es überhaupt ein X_global, das außerhalb der bereits vollständigen QFT+GR-Zustandsbeschreibung zusätzliche Vorhersagekraft besitzt?

## 11. Konsequenz für Datenfits

Bis ein X_global-Kandidat das Qualifikationsgate besteht:

- keine Fits von λ an kosmologische Spannungen;
- keine Ableitung von ξ aus Residuen;
- keine Kombination heterogener Anomalien zu einem AVI-Signal;
- keine Signifikanzangabe für AVI.

Zulässig sind Standardmodell-Reproduktionen, Nulltests und Sensitivitätsanalysen.

## 12. Nächster Gate-Test — X-global Qualification

Für jeden Kandidaten X_global sind zu prüfen:

1. physikalische Definition;
2. Unabhängigkeit von Zielresiduen;
3. Abgrenzung von QFT+GR-Zustandsdaten;
4. Kausal-/Dynamikpfad zur lokalen Response;
5. Dimensions- und Normierungsdefinition;
6. zeitliche beziehungsweise kosmologische Evolution;
7. mindestens zwei mögliche differentielle Kanäle;
8. Nullfall und Falsifikationskriterium.

Scheitern alle Kandidaten an Punkt 3, ist O2 als eigenständige AVI-Physik redundant.

## 13. Epistemischer Status

- **[R]** QFT+GR liefert bereits global-context-sensitive lokale Response-Kanäle.
- **[D]** Ein Residuum gegenüber einem unvollständigen Standard- oder Kanalmodell ist keine Evidenz für zusätzliche Physik.
- **[D]** Ein aus Zielresiduen definierter AVI-Prädiktor wäre zirkulär.
- **[H]** Eine unabhängig definierte globale Größe könnte eine gemeinsame zusätzliche Residualstruktur tragen.
- **[OFFEN]** Ob eine solche Größe außerhalb der vollständigen Standardbeschreibung existiert.
