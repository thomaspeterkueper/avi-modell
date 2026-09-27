# AVI — Core Invariant Reconstruction Gate v0.1

**Stand:** 27. September 2026  
**Status:** Grundlagenrekonstruktion nach O2-HOLD und O1-HOLD  
**Scope:** ξ-, Φ-, Kernel- und kopplungsfreie Kernfassung

## 1. Zweck

Dieses Gate entfernt vorübergehend alle bislang hypothetischen AVI-Mechanismen:

    ξ
    Φ
    memory kernel W
    X_global as AVI variable
    EFT coupling vector n_a
    λ, κ
    konkrete lokale AVI-Kopplungen.

Gesucht wird der minimale Aussagekern, der nach dieser Entfernung logisch erhalten bleibt.

Das Ziel ist ausdrücklich nicht, AVI zu retten. Das Gate darf ergeben, dass kein eigenständiger physikalischer Kern übrig bleibt.

## 2. Ausgangsfrage

Die reduzierte AVI-Frage lautet:

> Ist ein vollständig spezifizierter physikalischer Gegenwartszustand zusammen mit den geltenden Gesetzen und relevanten Rand-/Globalbedingungen hinreichend, um alle gegenwärtig zugänglichen Observablen festzulegen?

Schematisch sei

    Ω_std(t*) =
      {Y_full(t*), laws, parameters, boundary/global data, channel state}.

Die Standard-Closure-Hypothese lautet:

    Ω_std(t*) -> P(O(t*) | Ω_std)

ist vollständig.

Eine AVI-relevante Lücke existiert nur, falls reproduzierbar zusätzliche Information benötigt wird, die nicht bereits Bestandteil von Ω_std ist.

## 3. Kerninvariante CI-1 — Zustandsvollständigkeit

Keine fehlende Standardinformation darf als neue Physik umetikettiert werden.

Dazu gehören:

- nicht beobachtete Mikrozustände;
- interne Freiheitsgrade;
- Umweltzustände;
- globale/topologische Daten;
- Quantenzustand/Korrelationen;
- Apparate-/Kanalzustände;
- Populations-/Selektionsinformation;
- Unsicherheit über den Standardzustand selbst.

Formal:

    D -> P(Ω_std | D,M_std)

und nicht

    Ω_reconstructed == Ω_true.

**Status:** methodische Kerninvariante.

## 4. Kerninvariante CI-2 — Ontisch/epistemische Trennung

Zwei verschiedene Rekonstruktionen desselben Systems sind nicht zwei verschiedene physikalische Zustände.

    P(Ω_A | D) != P(Ω_B | D)

oder verschiedene Samples aus einem Zustands-Posterior begründen keine zusätzliche Ontologie.

OTA-SCI-0093 und OTA-SCI-0094 liefern hierfür komplementäre Kontrollfälle auf Kanal- beziehungsweise Zustandsrekonstruktionsebene.

**Status:** methodische Kerninvariante.

## 5. Kerninvariante CI-3 — Historie ist nicht automatisch Zustand

Aus

    history_A != history_B

folgt nicht automatisch

    current physical state_A != current physical state_B

und auch nicht automatisch eine heute messbare Historieninformation.

Historische Information kann

- vollständig im Gegenwartszustand enthalten sein;
- in Standard-Mikrozuständen/Korrelationen verborgen sein;
- durch coarse graining praktisch verloren sein;
- global statt lokal kodiert sein;
- operational nicht mehr zugänglich sein.

Daher gilt:

    past difference != present extra state.

**Status:** konzeptionell-methodische Kerninvariante.

## 6. Kerninvariante CI-4 — starker Retentionstest

Eine echte zusätzliche Retention wäre nur dann gegeben, wenn zwei physikalisch zulässige Fälle existieren mit

    Ω_std,A(t*) = Ω_std,B(t*)

aber

    P(O | Ω_std,A) != P(O | Ω_std,B)

für mindestens eine reproduzierbare gegenwärtige Observable.

Falls dies auftritt, ist Ω_std per Definition nicht vollständig. Dann muss die fehlende Information identifiziert werden.

Der entscheidende Punkt:

> Der Test beweist zunächst Unvollständigkeit der Zustandsbeschreibung, nicht AVI.

Erst die physikalische Identifikation der fehlenden Information könnte eine neue Theorie motivieren.

**Status:** zentraler Null-/Discovery-Test.

## 7. Kerninvariante CI-5 — Markov-Closure-Test

Für eine vollständige autonome Dynamik

    dΩ/dt = F(Ω)

mit eindeutiger Lösung ist die Zukunft lokal durch Ω festgelegt; bei geeigneter Invertierbarkeit ist auch die relevante Vergangenheit aus dem Zustand plus Dynamik bestimmt.

Ein scheinbarer Historieneffekt bei gleichem reduzierten Zustand verlangt daher zuerst den Test:

    reduced state
      -> enlarge state
      -> does Markov closure return?

Falls ja, lag versteckte Standardzustandsinformation vor.

Falls nein, bleiben als Möglichkeiten unter anderem fundamentale Nicht-Markovianität, nichtlokale Dynamik oder unvollständige Theorie.

**Status:** strukturelle Kernprüfung.

## 8. Kerninvariante CI-6 — relationale Observablen

Wo möglich, werden dimensionslose relationale Observablen bevorzugt:

    O_ij = Γ_i / Γ_j

oder andere dimensionslose Vergleiche.

Dies reduziert Einheitenkonventionen und macht common-mode Beiträge sichtbar.

Es ist keine AVI-Dynamik und keine Behauptung über neue Physik.

**Status:** Messdesign-Prinzip.

## 9. Kerninvariante CI-7 — unabhängige Multi-Channel-Prüfung

Eine zusätzliche Zustands-/Historienbehauptung darf nicht aus einem einzelnen Residuum konstruiert werden.

Erforderlich sind nach Möglichkeit:

- physikalisch verschiedene Kanäle;
- gemeinsames Nullmodell;
- propagierte Zustands-/Kanalunsicherheiten;
- vorab definierte relationale Vorhersage;
- Nullresultate im Datensatz;
- keine kanalweise freie Rettungsparameter.

**Status:** Falsifikationsprinzip.

## 10. Kerninvariante CI-8 — Residuum ist keine Ontologie

Es gilt strikt:

    observation - incomplete model != new state.

Ein Residuum wird erst physikalisch interpretierbar, nachdem Standardmodell, Zustandsunsicherheit und Kanalzustände vollständig genug behandelt sind.

Selbst dann ist

    residual != ξ.

Ein neues Zustandsobjekt benötigt unabhängige Definition, Dynamik und messbare Konsequenzen.

**Status:** epistemische Kerninvariante.

## 11. Was nach der Reduktion nicht übrig bleibt

Nicht zum gegenwärtig gerechtfertigten AVI-Kern gehören:

- ξ als reale Entität;
- Φ als physikalisches Vakuumintegral;
- eine universelle Memory-Funktion;
- eine AVI-spezifische lokale Ratenkopplung;
- ein AVI-spezifisches X_global;
- eine Operatorrichtung n_a;
- eine Erklärung von H0, S8 oder Dunkler Energie;
- die Behauptung, das Universum besitze ein zusätzliches physikalisches Gedächtnis.

Diese Elemente bleiben historische Modellkandidaten beziehungsweise HOLD-Pfade.

## 12. Was tatsächlich übrig bleibt

Nach Entfernung aller hypothetischen Mechanismen bleibt eine kohärente Forschungsarchitektur:

    complete present-state specification
      -> standard predictive closure
      -> controlled comparison across histories/channels
      -> search for irreducible present-state insufficiency
      -> only then ontology extension.

Der eigenständige Fokus liegt auf der **operationalen Prüfung von Zustandsvollständigkeit gegenüber behaupteter Historieninformation**.

## 13. Ist dies bereits eine neue physikalische Theorie?

Nein.

Die Core-Invarianten formulieren derzeit keine neue Bewegungsgleichung, kein neues Feld und keine neue quantitative Naturkonstante.

Mehrere Prinzipien sind etablierte wissenschaftliche Methodik oder folgen aus Standard-Zustandsraumdenken.

Die spezifische AVI-Leistung liegt derzeit in ihrer systematischen Kombination zu einem Forschungsprogramm für die Frage:

    present-state sufficiency
    versus
    irreducible history/state information.

Daher lautet die korrekte Klassifikation momentan:

> **AVI ist in seiner belastbaren Kernfassung ein theoretisches Test- und Modellierungsframework, noch keine eigenständige fundamentale physikalische Theorie.**

## 14. Falsifizierbarkeit des Kernprogramms

Ein Framework ist nicht auf dieselbe Weise falsifizierbar wie eine konkrete Dynamik. Einzelne starke AVI-Hypothesen sind es jedoch.

Die starke Zusatzinformationshypothese wird entkräftet, wenn für alle untersuchten Kandidaten gilt:

    apparent history dependence
      -> standard hidden/internal/global/channel state
      -> complete closure restored.

Dann bleibt keine empirische Motivation für eine zusätzliche AVI-Ontologie.

Umgekehrt wäre ein reproduzierbarer Closure-Fehler nur ein Discovery-Signal. Er würde nicht automatisch AVI bestätigen.

## 15. Minimaler AVI-Core v0.1

Der Kern kann auf fünf Sätze komprimiert werden:

**A1 — Completeness before extension**  
Keine neue Zustandsgröße vor Ausschöpfung der Standardzustandsbeschreibung.

**A2 — Reconstruction is not ontology**  
Unsicherheit oder Mehrdeutigkeit der Rekonstruktion ist keine zusätzliche physikalische Zustandsinformation.

**A3 — History requires a present carrier**  
Eine Vergangenheit ist heute nur physikalisch relevant, soweit ihre Information in einem gegenwärtigen Träger, einer Relation oder einer irreduziblen Dynamik operational wirksam ist.

**A4 — Same-state claims require full-state equality**  
Historienseparation zählt nur, wenn Gleichheit des vollständigen relevanten Gegenwartszustands und der Rand-/Kanalbedingungen gezeigt ist.

**A5 — Extension requires independent predictive closure**  
Jede zusätzliche Ontologie muss unabhängig definiert sein und vor dem Ziel-Datenfit eine neue, falsifizierbare relationale Vorhersage erzeugen.

## 16. Verhältnis zum Namen „Axiomatisches Vakuum Integral“

Die rekonstruierte Kernfassung benötigt derzeit weder ein Vakuumobjekt noch ein Integral.

Damit entsteht eine terminologische Spannung: Der historische Name AVI bezeichnet einen Forschungsweg, dessen belastbarer Kern enger und abstrakter geworden ist als die ursprüngliche Integralidee.

Der Name wird vorläufig aus Kontinuitätsgründen beibehalten. Er darf jedoch nicht als Behauptung verstanden werden, ein physikalisches Vakuumintegral sei bereits etabliert.

## 17. Gate-Ergebnis

**Core Invariant Reconstruction Gate: PASS.**

Aber der Pass ist präzise zu lesen:

    coherent core framework = YES
    independent new dynamics = NO
    additional ontology required = NO
    falsifiable extension criteria = YES
    current evidence for irreducible history state = NO.

Das Gate rettet keine frühere Mechanik. Es trennt erstmals klar den belastbaren AVI-Kern von den hypothetischen Erweiterungen.

## 18. Nächster Schritt — Core Formalization v0.1

Als nächstes sollte der fünfaxiomatische Kern mathematisch als zustandsraumneutraler Vertrag formalisiert werden.

Zu definieren sind:

1. vollständiger Referenzzustand Ω;
2. Beobachtungsdaten D und Rekonstruktionsoperator R;
3. Standard-Prädiktor P_std(O|Ω);
4. Äquivalenzrelation für „gleicher Gegenwartszustand“;
5. Closure-Defekt als statistisch definierte, nicht ontologisch interpretierte Größe;
6. Bedingungen, unter denen eine Erweiterung Ω -> (Ω,Z) überhaupt zugelassen wird.

Erst danach sollte entschieden werden, ob ein neuer physikalischer AVI-Zweig begonnen wird.
