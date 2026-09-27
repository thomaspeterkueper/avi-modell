# AVI — State-Completeness Manifest: QFT Global-Context Reference v0.1

**Manifest:** SCM-QFT-GLOBAL-001
**Stand:** 27. September 2026
**Status:** READY-Q / NEGATIVE CONTROL
**Basis:** State-Completeness Manifest v0.1; Core Formalization v0.2; QFT Response Gate v0.1

## 1. Research question

Kann eine lokal gemessene Detektorresponse verschieden sein, obwohl lokale klassische Geometrie, Detektormikrophysik und lokale Trajektorie gleich sind, ohne dass eine zusätzliche AVI-Zustandsvariable Z benötigt wird?

## 2. Q und M_std

    Q = {detector response F(ω), normalized response ratios}
    M_std = QFT in curved/topologically nontrivial spacetime
            + detector model
            + specified field state.

Ziel ist kein Test neuer Physik, sondern ein End-to-End-Negativkontrolltest des AVI-Core.

## 3. Ω = (Y,B,G,C)

### Y

- Detektor-Energielücke;
- lokale Detektormikrophysik;
- lokale klassische Geometrie entlang der Weltlinie;
- lokale Trajektorie.

Status: MATCHED zwischen A/B im Referenzaufbau.

### B

- Feld-Randbedingungen;
- räumliche Identifikationsbedingungen;
- asymptotische beziehungsweise kompakte Randstruktur, soweit nicht unter G geführt.

Status: explizit spezifiziert; bei verschiedenen globalen Kontexten nicht notwendigerweise MATCHED.

### G

- globale Raumzeittopologie/-geometrie;
- globaler Quantenzustand;
- relevante Wightman-/Korrelationsstruktur;
- globale Moden/Nullmoden, falls vorhanden.

Status: **NOT MATCHED by construction.**

    G_A != G_B.

### C

- Detektortrajektorie;
- Schaltfunktion χ;
- Messdauer;
- Kopplungsprotokoll;
- Präparation und Readout.

Status: MATCHED beziehungsweise kontrolliert.

## 4. Standard prediction

Für einen Unruh-DeWitt-artigen Detektor:

    F(ω)
      = integral dτ dτ'
          χ(τ)χ(τ')
          exp[-iω(τ-τ')]
          W(x(τ),x(τ')).

Damit gilt standardtheoretisch:

    G_A != G_B
      -> W_A != W_B
      -> F_A != F_B

in geeigneten bekannten Referenzmodellen.

## 5. Rekonstruktion

Dieser Referenztest ist primär theoretisch/konstruktiv. Ω wird im Modell festgelegt statt aus verrauschten kosmologischen Daten vollständig rekonstruiert.

Für eine reale experimentelle Umsetzung wäre erneut

    P(Ω|D,M_std)

erforderlich.

## 6. Äquivalenzprüfung

Lokale Teilgrößen können gleich sein:

    Y_local,A = Y_local,B
    C_A = C_B.

Auch lokale klassische Geometrie kann gleich sein.

Aber:

    G_A != G_B.

Daher gilt ausdrücklich nicht

    Ω_A ≡_std Ω_B.

Für Q kann ebenfalls im Allgemeinen nicht gelten

    Ω_A ~_Q Ω_B,

da M_std unterschiedliche Detektorresponses vorhersagt.

## 7. History claim

Kein Strong History Test.

Der Unterschied ist ein **gegenwärtiger globaler Standardzustandsunterschied**, keine irreduzible Erinnerung an verschiedene Entstehungshistorien.

    global state != history memory.

## 8. Closure

Die unterschiedliche Response wird durch M_std vorhergesagt.

    Δ_cl compatible with standard closure.

Es existiert daher kein Grund, E1/E2 als Öffnung einer neuen Ontologie zu interpretieren.

## 9. Extension gate

    extension.allowed = false
    E1 = PASS for constructed reference model
    E2 = FAIL / NOT TRIGGERED
    E3-E8 = NOT OPENED.

Z ist weder erforderlich noch zulässig.

## 10. Machine-readable block

    state_completeness:
      manifest_version: "0.1"
      manifest_id: "SCM-QFT-GLOBAL-001"
      omega:
        Y:
          - detector_microphysics
          - local_geometry
          - local_trajectory
        B:
          - field_boundary_conditions
        G:
          - global_spacetime_structure
          - quantum_state
          - correlation_structure
        C:
          - switching_function
          - measurement_duration
          - detector_protocol
      reconstruction:
        posterior: not_required_for_constructed_reference
        point_estimate_only: false
      equivalence:
        q_equivalence: FAIL_AS_EXPECTED
        strong_standard_equivalence: FAIL_AS_EXPECTED
        unresolved_components: []
      closure:
        statistic_preregistered: reference_analytic_prediction
        control_target_separation: NOT_APPLICABLE
        defect_status: NO_UNEXPLAINED_DEFECT
      extension:
        allowed: false
        E1: PASS
        E2: NOT_TRIGGERED
        E3: NOT_OPENED
        E4: NOT_OPENED
        E5: NOT_OPENED
        E6: NOT_OPENED
        E7: NOT_OPENED
        E8: NOT_OPENED

## 11. End-to-End result

**MANIFEST END-TO-END CONTROL: PASS.**

Das Manifest klassifiziert den bekannten Effekt korrekt:

    locally similar setup
      + different G
      -> different standard QFT response
      -> no strong same-state claim
      -> no closure defect
      -> no Z.

Damit besteht das State-Completeness Manifest seinen ersten vollständigen Negativkontrolllauf.

## 12. Konsequenz

Der nächste Referenztest sollte schwieriger sein: ein Fall, in dem A/B in einer reduzierten Beschreibung tatsächlich gleich erscheinen und erst eine versteckte interne Standardvariable oder Rekonstruktionsverteilung die scheinbare Historienabhängigkeit auflöst.

Geeignet ist ein Hysterese-/interner-Zustands-Testbed, bevor ein offenes kosmologisches Testbed gewählt wird.
