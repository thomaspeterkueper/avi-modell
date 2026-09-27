# AVI — State-Completeness Manifest v0.1

**Stand:** 27. September 2026
**Status:** verbindliches Prüfprotokoll vor Strong-History-/Closure-Tests
**Normative Basis:** Core Formalization v0.2

## 1. Zweck

Dieses Manifest ist für jeden zukünftigen AVI-Kandidaten auszufüllen, bevor ein starker Same-State-/History-Claim, ein Closure-Defekt oder eine Erweiterung Ω -> (Ω,Z) diskutiert wird.

Es soll verhindern:

- Gleichsetzung eines reduzierten Makrozustands mit dem vollständigen Standardzustand;
- Ontologisierung von Rekonstruktionsunsicherheit;
- Auslassen globaler oder topologischer Standardinformation;
- Auslassen von Kanal-/Umweltzuständen;
- nachträgliche Definition von Z aus Zielresiduen;
- unprüfbare Behauptungen von Ω_A ≡_std Ω_B.

Ein unvollständiges Manifest blockiert den Strong History Test.

## 2. Identität des Tests

Pflichtfelder:

    manifest_id:
    test_id:
    version:
    date:
    owner:
    status: DRAFT | READY | BLOCKED | RETIRED

    research_question:
    target_observable_family_Q:
    comparison_time_or_epoch:
    standard_model_M_std:
    standard_model_version:
    target_dataset:
    control_dataset:
    preregistration_reference:

## 3. Zustandsdeklaration Ω

Für den Test gilt

    Ω = (Y,B,G,C).

Jede Kategorie erhält eine explizite Komponentenliste.

### 3.1 Y — lokale/interne Standardfreiheitsgrade

Für jede Komponente:

    id:
    physical_meaning:
    role_in_prediction:
    measured | reconstructed | latent | fixed:
    data_source:
    uncertainty_model:
    correlations:
    marginalization_method:
    omission_justification:

Beispiele je nach Test: Materiedichte, Temperatur, Zusammensetzung, interne Populationen, Peculiar Velocity, Feldzustände, Defekt-/Relaxationsvariablen.

### 3.2 B — Rand-/Anfangsbedingungen

Pflichtprüfung:

- räumliche Randbedingungen;
- zeitliche Anfangsbedingungen, soweit nicht bereits in Y/G kodiert;
- asymptotische Bedingungen;
- externe kontrollierte Inputs;
- Simulations-/Modellgrenzen.

Für jede relevante B-Komponente gilt dasselbe Audit-Schema wie für Y.

### 3.3 G — globale Information

Pflichtprüfung:

- globale Geometrie;
- Topologie;
- Quantenzustand und relevante Korrelationen;
- globale Moden;
- globale Constraints/Erhaltungssätze;
- sonstige Standardinformation, die lokal nicht vollständig rekonstruierbar sein muss.

Eine Größe darf nicht als AVI-Historieninformation behandelt werden, nur weil sie global statt lokal ist.

### 3.4 C — Kanal-/Apparat-/Umweltzustand

Pflichtprüfung:

- Instrument-/Kalibrationszustand;
- lokale Umgebung;
- Bewegung/Beschleunigung;
- Selektionsfunktion;
- Populationsmodell;
- Response-/Wellenformmodell;
- Zustandspräparation;
- Messfenster/Schaltfunktion;
- Host-/Foreground-/Background-Beiträge;
- sonstige kanalspezifische Systematik.

OTA-SCI-0093 / OBS-07 ist der Referenzfall für unvollständiges C.

## 4. Rekonstruktionsmanifest

Es muss dokumentiert werden:

    R_M : D_control -> P(Ω | D_control,M_std).

Pflichtfelder:

    inference_method:
    priors:
    likelihood:
    latent_variables:
    nuisance_parameters:
    covariance_model:
    posterior_representation:
    number_of_reconstructions_or_samples:
    convergence_diagnostics:
    posterior_predictive_checks:
    sensitivity_to_priors:
    sensitivity_to_model_variants:

Eine einzelne Best-Fit-Rekonstruktion darf P(Ω|D,M_std) nicht ohne quantitative Begründung ersetzen.

OTA-SCI-0094 / OBS-08 ist der Referenzfall.

## 5. Datenisolation und Zirkularität

Für jedes Datenprodukt ist anzugeben:

    used_for_state_reconstruction:
    used_for_model_calibration:
    used_for_target_test:
    used_for_extension_definition:

Wo dasselbe Datenprodukt mehrere Rollen besitzt, muss die daraus entstehende Abhängigkeit explizit modelliert werden.

Bevorzugt:

    D_control ∩ D_target = empty

soweit experimentell/statistisch sinnvoll.

Wenn Trennung unmöglich ist, muss eine gemeinsame Likelihood oder ein äquivalentes Verfahren Doppelverwendung berücksichtigen.

## 6. Q-bezogene prädiktive Äquivalenz

Für

    Ω_A ~_Q Ω_B

muss dokumentiert werden:

    Q_definition:
    prediction_tolerance:
    distributional_distance_metric:
    covariance_treatment:
    equivalence_threshold:
    robustness_checks:

~_Q darf nur als prädiktive Äquivalenz für Q bezeichnet werden.

Es ist kein Strong-Same-State-Nachweis.

## 7. Starke Standardzustandsäquivalenz

Ein Claim

    Ω_A ≡_std Ω_B

benötigt ein separates Audit.

Für jede dynamisch relevante Komponente von Y,B,G,C ist genau einer der Zustände anzugeben:

    MATCHED
    JOINTLY_MARGINALIZED
    PROVEN_IRRELEVANT_FOR_TESTED_DYNAMICS
    UNRESOLVED.

Strong equivalence ist nur zulässig, wenn kein Eintrag UNRESOLVED verbleibt.

Zusätzlich müssen erfüllt sein:

1. dieselbe Version von M_std;
2. dieselben relevanten Natur-/Modellparameter oder gemeinsam marginalisierte Unsicherheit;
3. identische relevante Rand-/Globalbedingungen oder dokumentierte gemeinsame Marginalisierung;
4. kompatible Kanalzustände;
5. keine bekannte versteckte Standardvariable, die Q unterschiedlich beeinflussen kann;
6. keine bloße Gleichheit ausgewählter Makroparameter als Ersatz.

## 8. History-Separation Manifest

Erst nach bestandener Strong-equivalence-Prüfung darf

    H_A != H_B

als kontrollierte Historienseparation verwendet werden.

Pflichtfelder:

    history_definition:
    history_interval:
    physical_distinction:
    how_histories_are_generated_or_identified:
    evidence_HA_not_equal_HB:
    standard_present_carriers_checked:
    known_non_markovian_dynamics_checked:

Wenn die Historieninformation bereits in Ω kodiert ist, liegt kein Strong History Test vor.

## 9. Standard-Prädiktor

Zu dokumentieren:

    P_std(Q | Ω,M_std)

und posterior-prädiktiv

    P_std(Q | D_control,M_std)
      = integral dΩ P_std(Q|Ω,M_std) P(Ω|D_control,M_std).

Pflichtfelder:

    forward_model:
    numerical_method:
    approximation_regime:
    calibration:
    validation:
    theoretical_uncertainty:
    numerical_uncertainty:
    observational_covariance:

## 10. Closure-Test

Vor Betrachtung des Zielresultats:

    test_statistic_T:
    expected_null_distribution:
    decision_rule:
    multiple_testing_policy:
    look_elsewhere_policy:
    replication_requirement:
    cross_channel_requirement:

Dann

    Δ_cl = T(D_target, P_std(Q|D_control,M_std)).

Ein signifikanter Δ_cl ist ein Audit-Trigger, keine Ontologie.

## 11. Closure-Audit bei Abweichung

Bei auffälligem Δ_cl wird in dieser Reihenfolge geprüft:

    CA1 data integrity
    CA2 calibration / C
    CA3 reconstruction P(Ω|D,M)
    CA4 missing Y
    CA5 missing B
    CA6 missing G
    CA7 covariance / selection / population
    CA8 approximation / numerical error
    CA9 alternative standard dynamics
    CA10 independent replication.

Vor Abschluss CA1–CA10 bleibt jeder Z-Claim BLOCKED.

## 12. Extension Gate

Erst nach dokumentiertem E1/E2-Pass darf ein Z-Vorschlag angelegt werden.

Pflichtfelder:

    Z_name:
    independent_definition:
    independent_measurement_or_theory_basis:
    dynamics:
    preregistered_prediction:
    affected_channels:
    shared_parameter_structure:
    null_embedding:
    falsification_region:
    distinction_from_existing_standard_variables:

Danach sind E3–E8 einzeln als PASS/FAIL/HOLD zu bewerten.

## 13. Verbotene Abkürzungen

Automatisch BLOCKED sind:

    same H0 -> same Ω
    same scale factor -> same Ω
    same local geometry -> same Ω
    same macrostate -> same Ω
    same best fit -> same Ω
    different reconstruction -> different ontology
    residual -> Z
    global information -> AVI memory
    integrated observable -> fundamental memory
    historical correlation -> causal history state.

Jeder dieser Schlüsse benötigt zusätzliche physikalische Begründung.

## 14. Machine-readable Minimalblock

Jeder konkrete Test soll zusätzlich einen strukturierten Block führen:

    state_completeness:
      manifest_version: "0.1"
      omega:
        Y: []
        B: []
        G: []
        C: []
      reconstruction:
        posterior: required
        point_estimate_only: false
      equivalence:
        q_equivalence: UNTESTED
        strong_standard_equivalence: UNTESTED
        unresolved_components: []
      closure:
        statistic_preregistered: false
        control_target_separation: UNTESTED
        defect_status: UNTESTED
      extension:
        allowed: false
        E1: UNTESTED
        E2: UNTESTED
        E3: UNTESTED
        E4: UNTESTED
        E5: UNTESTED
        E6: UNTESTED
        E7: UNTESTED
        E8: UNTESTED

Default ist konservativ:

    extension.allowed = false.

## 15. Statuslogik

**DRAFT** — Manifest wird aufgebaut.

**BLOCKED** — mindestens eine zwingende Zustands-/Rekonstruktions-/Closure-Frage ist ungelöst.

**READY-Q** — ~_Q kann geprüft werden; kein Strong-History-Claim.

**READY-STRONG** — alle Voraussetzungen für ≡_std und kontrollierte Historienseparation sind dokumentiert.

**CLOSURE-AUDIT** — auffälliger Δ_cl; CA1–CA10 laufen.

**EXTENSION-ELIGIBLE** — E1 und E2 bestanden; Z darf formuliert, aber nicht bestätigt werden.

Kein Status heißt "AVI bestätigt".

## 16. Anwendung auf bestehende Beobachtungsmatrix

OBS-07 Standard-Sirenen:

    primary_manifest_risk = C
    strong_equivalence = not established
    extension = blocked.

OBS-08 TRGB-H0:

    primary_manifest_risk = reconstruction P(Ω|D,M)
    strong_equivalence = not established
    extension = blocked.

Die bestehenden Fälle dienen damit als negative Kalibrierung des Manifests.

## 17. Gate-Ergebnis

**State-Completeness Manifest v0.1: READY FOR USE.**

Es ist ab jetzt die operative Vorbedingung für neue Strong-History-/Closure-Tests im AVI-Modell.

Ein Test ohne ausgefülltes Manifest darf als Exploration dokumentiert werden, aber nicht als starker AVI-Test oder Evidenz für zusätzliche Ontologie klassifiziert werden.

## 18. Nächster Schritt

Als nächstes sollte ein konkretes Testbed gewählt und das Manifest vollständig ausgefüllt werden.

Die beste erste Wahl ist nicht die H0-Spannung, sondern ein kontrollierter Referenzfall, bei dem der korrekte Ausgang bereits aus Standardphysik bekannt ist. Damit kann geprüft werden, ob das Manifest praktisch funktioniert, bevor es auf offene kosmologische Fragen angewendet wird.
