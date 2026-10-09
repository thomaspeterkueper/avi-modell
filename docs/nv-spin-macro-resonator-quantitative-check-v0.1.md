# AVI — NV-Spin-Makroresonator: quantitativer Erstcheck v0.1

**Stand:** 2026-10-09  
**Status:** Parametrischer H0-Check anhand publizierter Eckwerte; **KEINE Rohdatenreproduktion**.

## Provenienz

- Nayak, Kim, Tian, Twamley (2026), *Spin-force from a Nitrogen-Vacancy ensemble drives a 100 mg levitated resonator*, Science Advances, DOI: 10.1126/sciadv.aeh0566; arXiv:2605.17750.
- Archiv + README: https://datadryad.org/dataset/doi:10.5061/dryad.4xgxd25q4 (3,28 GB, veröffentlicht 2026-09-08).
- README: Fig. 2–4 enthalten interferometrische Positions-Zeitreihen (.h5) und Python/Mathematica-Auswertungen; Fig. S8 Frequenzantwort, S10 Abstand/Kraft, S11 Magnetkontrolle; Abtastrate 2,44 kHz.
- Experimentelle Kontrollbedingungen: Magnet entfernt; nicht-spinpolarisierender IR-Laser (vgl. Primärarbeit).

## H0-Rechnung aus gerundeten Literatur-Eckdaten

Parameter (nicht neu gefittet):
- Masse `M=128 mg=1.28e-4 kg`
- Eigenfrequenz `f0=17.6 Hz`
- mechanischer Gütefaktor `Q ≈ 55` (aus Sekundärzusammenfassung; **mit Primärarbeit/Supplement verifizieren**)
- Referenzamplitude `A=100 nm=1e-7 m` (Arbeit berichtet >100 nm)

Einachsiger gedämpfter harmonischer Oszillator:
`M z'' + b z' + k z = F1 cos(omega t)`;
`omega0=2*pi*f0=110.584 rad/s`;
`k=M*omega0^2 = 1.56529 N/m`;
`b=M*omega0/Q`;
`A(omega0)=Q*F1/(M*omega0^2)`;
`F1=k*A/Q = 2.84598e-9 N = 2.846 nN` (**sinusförmige Grundwellen-Kraftamplitude**, nicht ohne Weiteres die publizierte Puls-Kraftdifferenz);
`T=1/f0=0.0568182 s`;
`E=0.5*k*A^2=7.82645e-15 J`.

Bei rechteckigem Laserpuls und Duty Cycle D ist die erste harmonische Komponente einer Kraftdifferenz ΔF proportional zu `(2/pi)*ΔF*sin(pi D)`. Für D=1/2 folgt unter idealen Bedingungen `ΔF=pi/2*F1`; dieser Schritt darf **nicht** ohne Prüfung der Publikationskonventionen und experimentellen Definition der Amplitude zur behaupteten gemessenen Kraft werden.

## Grenzen
- Die Werte stammen aus gerundeten öffentlichen Parametern und einer ungeprüften Q-Angabe: keine Fehlerbalken, keine unabhängige Datenreplikation, keine Signifikanzbehauptung.
- Vollständiges 3,28-GB-Rohdatenarchiv noch nicht heruntergeladen und nicht ausgewertet.
- Keine Aussage über makroskopische Superposition; eine klassisch messbare Antwort auf quantenkontrollierte Spinpolarisation ist H0-kompatibel.
- Kein AVI-spezifischer Driver, kein `Δ^R`, keine Evidenz für zusätzliche Ontologie.

## Nächste Prüfentscheidung
1. Manuskript/Supplement kontrollieren: Q, Amplituden- und Pulskonventionen, Masse, Messunsicherheiten.
2. Gezielte Rohdaten: Fig. S8 (Frequenzantwort) + Fig. S10 (Abstand/Kraft) + Fig. S11 (Magnetkontrolle), statt vorab das ganze Archiv zu spiegeln.
3. Frequenzgang `A(ω)=F1/sqrt((k-Mω²)^2+(bω)^2)` mit Konfidenzintervallen an Messwerte fitten.
4. Blind definierte dimensionslose Residuen und Nullkanäle; keine nachträglich konstruierte AVI-Anomalie.
