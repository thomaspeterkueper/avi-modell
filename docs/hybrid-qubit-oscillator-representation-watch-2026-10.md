# Hybrid qubit–oscillator quantum simulation — methodological reference
Date: 2026-10-13. Status: WATCH / STANDARD PHYSICS / not AVI evidence.

Primary publication: Crane et al., Physical Review X 16, 041008 (7 Oct 2026), DOI https://doi.org/10.1103/s5bn-z4jq

The proposal combines qubit and bosonic oscillator hardware to encode interacting fermions, bosons and gauge fields. Direct oscillator representation may reduce boson-to-qubit mapping overhead for selected Hamiltonians and target cutoffs. Resource comparisons depend on assumed gate fidelity, cutoff, model, compiler and hardware noise; these are not universal empirical speedups. The paper includes theory, compilation and numerical estimates, not a generic experimental quantum advantage.

AVI relevance: distinguish physical system, Hamiltonian, encoding, measurement channel and noise model. Apparent mismatch caused by an inefficient encoding or omitted hardware noise is not evidence for additional physical state Z. Apply standard-state completeness, covariance and independent-observable gates before stronger claims.

Review checklist: reproduce one small Hamiltonian classically; compare qubit-only versus hybrid logical resource estimates at matched error; document cutoff and fidelity assumptions; distinguish simulated from observed outputs; revisit after independent hardware demonstrations.
