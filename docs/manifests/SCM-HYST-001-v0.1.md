# AVI — State-Completeness Manifest: Hysteresis/Internal-State Reference v0.1

**Manifest:** SCM-HYST-001
**Stand:** 27. September 2026
**Status:** READY-Q / NEGATIVE CONTROL
**Basis:** State-Completeness Manifest v0.1; Core Formalization v0.2; Core Stress-Test ST-1

## 1. Research question

Kann ein System bei gleichen äußeren Kontrollgrößen u(t*) aufgrund verschiedener Vorgeschichten unterschiedliche gegenwärtige Response zeigen, ohne dass eine zusätzliche AVI-Ontologie Z benötigt wird?

## 2. Referenzklasse

Kontrollierte Standardfälle sind hysteretische Systeme wie Ferromagnete, ferroelektrische Systeme, plastische/defektreiche Materialien oder andere Systeme mit internen Zustandsvariablen.

Der Test ist klassenbasiert und behauptet kein universelles konkretes Materialmodell.

## 3. Scheinbarer Strong-History-Fall

Reduzierte Beschreibung:

    u_A(t*) = u_B(t*)
    H_A != H_B
    O_A != O_B.

Wenn u fälschlich als vollständiger Gegenwartszustand behandelt wird, scheint die Response Information über die Historie zu benötigen.

## 4. Ω = (Y,B,G,C)

### Y — lokale/interne Standardfreiheitsgrade

Mindestens:

    Y = (u,m,...)

wobei m je nach Referenzsystem beispielsweise Magnetisierungskomponenten, Domänenkonfiguration, Defektpopulation, interne Spannung, Polarisationszustand oder andere etablierte interne Zustandsvariablen repräsentiert.

Für unterschiedliche Hystereseäste gilt im Allgemeinen:

    m_A(t*) != m_B(t*).

Damit:

    Y_A != Y_B.

Status: NOT MATCHED by construction once the relevant internal state is included.

### B

- angelegte Rand-/Kontrollbedingungen;
- Probengeometrie;
- gegebenenfalls thermische/mechanische Randbedingungen.

Status: MATCHED im idealisierten Referenztest.

### G

Keine zusätzliche globale AVI-Information erforderlich.

Systemweite Domänen-/Korrelationsstruktur gehört, soweit dynamisch relevant, bereits zum Standardzustand Y oder G gemäß konkretem Modell.

Status: STANDARD MODEL CONTENT.

### C

- Sensor-/Readoutzustand;
- Kalibration;
- Messprotokoll;
- Messrichtung;
- Temperatur-/Umgebungsbedingungen, soweit nicht Y/B.

Status: MATCHED/kontrolliert im Referenztest.

## 5. Rekonstruktionsmanifest

Der zentrale methodische Punkt ist, dass m häufig nicht vollständig aus den äußeren Kontrollen u rekonstruiert werden kann.

Daher ist korrekt:

    P(m | D_control, u, M_std)

und nicht

    m := function(u) uniquely.

Falls m latent ist, wird es rekonstruiert oder marginalisiert.

Unwissen über m ist epistemische Zustandsunsicherheit, kein Z.

## 6. Äquivalenzprüfung

In der reduzierten Beschreibung:

    u_A = u_B.

Das genügt weder für

    Ω_A ~_Q Ω_B

noch für

    Ω_A ≡_std Ω_B.

Sobald m in Y aufgenommen wird:

    Ω_A != Ω_B.

Die unterschiedliche Standardresponse ist daher zulässig und erwartet.

## 7. History-Separation Audit

    H_A != H_B

ist physikalisch real, aber die relevante Historieninformation besitzt einen gegenwärtigen Standardträger:

    H -> m(t*) -> O(t*).

Damit erfüllt der Fall Core-Axiom A3 ohne Erweiterung.

Es liegt kein Strong History Test vor, weil die vollständigen Standardzustände nicht gleich sind.

## 8. Standard-Prädiktor

Schematisch:

    P_std(O | u,m,B,G,C,M_std).

Wenn m latent ist:

    P_std(O | D_control,M_std)
      = integral dm
          P_std(O | u,m,...)
          P(m | D_control,u,M_std).

Ein Modell nur mit P(O|u) kann einen scheinbaren Closure-Defekt erzeugen; dieser verschwindet nach Zustandsvervollständigung.

## 9. Closure-Test

Reduziertes Fehlmodell:

    M_reduced: O = f(u)

kann liefern

    Δ_cl != 0.

State-complete Standardmodell:

    M_std: O = f(u,m,...)

liefert erwartungsgemäß Closure, sofern das interne Zustandsmodell hinreichend ist.

Damit demonstriert der Test explizit:

    closure defect under reduced state
      !=
    fundamental closure defect.

## 10. Extension gate

    extension.allowed = false.

E1 ist unter der reduzierten Beschreibung FAIL.

Nach Aufnahme/Marginalisierung von m kann E1 erfüllt sein, aber E2 wird durch wiederhergestellte Standard-Closure nicht ausgelöst.

Daher:

    E1_reduced = FAIL
    E1_complete = PASS
    E2 = NOT_TRIGGERED
    E3-E8 = NOT_OPENED.

## 11. Machine-readable block

    state_completeness:
      manifest_version: "0.1"
      manifest_id: "SCM-HYST-001"
      omega:
        Y:
          - external_controls_u
          - internal_state_m
        B:
          - sample_boundary_conditions
        G:
          - standard_systemwide_correlations_if_relevant
        C:
          - readout
          - calibration
          - environment
      reconstruction:
        posterior: required_if_m_latent
        point_estimate_only: false
      equivalence:
        q_equivalence: FAIL_AS_EXPECTED_AFTER_STATE_COMPLETION
        strong_standard_equivalence: FAIL_AS_EXPECTED
        unresolved_components: []
      closure:
        statistic_preregistered: reference_model_comparison
        control_target_separation: MODEL_DEPENDENT
        defect_status: RESOLVED_BY_STANDARD_INTERNAL_STATE
      extension:
        allowed: false
        E1: PASS_AFTER_STATE_COMPLETION
        E2: NOT_TRIGGERED
        E3: NOT_OPENED
        E4: NOT_OPENED
        E5: NOT_OPENED
        E6: NOT_OPENED
        E7: NOT_OPENED
        E8: NOT_OPENED

## 12. End-to-End result

**MANIFEST END-TO-END CONTROL #2: PASS.**

Das Manifest erkennt einen schwierigeren Scheinhistorienfall korrekt:

    same external controls
      + different history
      + different response

wird zu

    different internal standard state m
      -> Ω_A != Ω_B
      -> standard response difference
      -> no strong same-state claim
      -> no Z.

## 13. Vergleich mit QFT-Kontrollfall

SCM-QFT-GLOBAL-001:

    missing distinction was G.

SCM-HYST-001:

    missing distinction is Y.

Damit hat das Manifest zwei qualitativ verschiedene Fehlklassifikationswege erfolgreich abgefangen:

    omitted global standard information
    omitted internal standard information.

## 14. Neue operative Regel

> **Reduced-state equality is not state completeness.**

Gleichheit kontrollierter oder makroskopisch sichtbarer Variablen ist niemals hinreichend für Ω_A ≡_std Ω_B, solange bekannte oder plausible interne Standardfreiheitsgrade die Zielobservable beeinflussen können.

## 15. Nächster Referenztest

Als dritter End-to-End-Test sollte ein Fall folgen, bei dem nicht Y oder G fehlt, sondern die Schwierigkeit rein epistemisch ist:

    same data class
      -> multiple admissible state reconstructions
      -> different inferred target quantity.

Dafür ist OBS-08 / OTA-SCI-0094 (TRGB-H0 mit lokalen Dichte-/Peculiar-Velocity-Rekonstruktionen) geeignet.

Dieser Test prüft erstmals den vollständigen posterior-prädiktiven Pfad P(Ω|D,M), statt nur die korrekte Zuordnung einer bekannten Zustandskomponente.
