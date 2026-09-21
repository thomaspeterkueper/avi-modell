# AVI — ξ-Ontologie-Screening v0.1

**Stand:** 21. September 2026  
**Status:** kritisches Modell-Screening nach dem Determinismus-Gate  
**Ausgangspunkt:** AVI-B0.1 scheitert am strong Test B, wenn ξ nur ein Filter einer vollständig rekonstruierbaren Standardhistorie ist.

## 1. Prüffrage

Gesucht ist keine neue Bezeichnung für Vergangenheit, sondern eine physikalisch unterscheidbare Zustandsgröße ξ, für die gleichzeitig gelten kann:

    Y_full,A(a*) = Y_full,B(a*)
    ξ_A(a*) != ξ_B(a*)

und die über eine vorab definierte Kopplung eine messbare Observable beeinflusst.

Drei Ontologien werden geprüft:

1. ξ als zusätzlicher lokaler dynamischer Freiheitsgrad;
2. ξ als globale Zustands-/Randinformation;
3. ξ als Zustandsvariable einer physikalisch nicht-Markovschen Dynamik.

## 2. Gemeinsame Mindestbedingungen

Jede Variante muss beantworten:

- Was repräsentiert ξ physikalisch?
- Ist ξ unabhängig von einem vollständigen Standardzustand Y?
- Welche Dynamik oder Randbedingung bestimmt ξ?
- Welche Anfangs-/Randdaten sind erforderlich?
- Wie koppelt ξ an die bereits definierte differentielle Observable?
- Welcher Nullfall reproduziert Standardphysik?
- Welche vorhandenen Präzisions- oder Kosmologiedaten schränken die Variante ein?
- Kann strong Test B prinzipiell bestehen, ohne Y künstlich zu verkleinern?

## 3. O1 — zusätzlicher lokaler dynamischer Freiheitsgrad

Minimal:

    dY/dN = F_std(Y)
    dξ/dN = G(ξ,Y; θξ)

mit unabhängiger Anfangsbedingung ξ_i.

Dann können zwei Lösungen bei gleichem Y* verschiedene ξ* besitzen, weil der vollständige Zustand des erweiterten Modells tatsächlich (Y,ξ) ist.

### Stärke

Diese Variante löst das Determinismusproblem formal sauber. ξ ist nicht aus der Standardhistorie rekonstruiert, sondern Teil eines erweiterten Zustandsraums.

### Preis

Sie verändert den ontologischen Status von AVI erheblich. ξ wäre ein neuer physikalischer Freiheitsgrad. Dann muss geklärt werden, ob er lokal, global oder feldartig ist, welche Energie-/Gravitationswirkung er besitzt und warum er nicht bereits in Präzisionstests sichtbar ist.

Ein räumlich propagierendes Skalarfeld wäre zudem nicht mehr die bisherige enge AVI-Arbeitsdefinition von Φ. Eine solche Theorie darf nicht stillschweigend eingeführt werden.

### Strong Test B

Formal: **möglich**.

Physikalisch: **noch unbegründet**.

### Entscheidung

Nicht verwerfen, aber nicht als bevorzugte Minimalfortsetzung wählen. O1 benötigt den größten neuen ontologischen Einsatz und nähert AVI bekannten Klassen zusätzlicher Felder/Freiheitsgrade an.

## 4. O2 — globale Zustands- oder Randinformation

Hier ist ξ keine zusätzliche lokale Materie- oder Feldvariable, sondern eine wohldefinierte globale Eigenschaft der kosmologischen Lösung, die durch lokale momentane Größen nicht vollständig bestimmt wird.

Schematisch:

    ξ = G_global[M, boundary data, topology, global state]

während Y_local beziehungsweise ein lokaler FLRW-Zustand dieselben Werte besitzen kann.

Beispiele für die **Art** solcher Information sind globale Topologie, globale Randbedingungen oder andere globale Lösungsdaten. Diese Beispiele sind methodische Analogien, keine Behauptung, dass kosmologische Topologie selbst ξ ist.

### Stärke

Diese Variante liegt am nächsten an der ursprünglichen AVI-Idee einer Relation lokaler Prozesse zu einem globalen kosmologischen Referenzzustand. Sie benötigt nicht automatisch ein neues lokal propagierendes Feld.

Sie erklärt außerdem, warum lokaler Zustand und globaler Zustand begrifflich getrennt werden müssen.

### Kritische Bedingung

Wenn Y_full in Test B bereits sämtliche globalen Rand- und Topologiedaten enthalten soll, dann darf ξ nicht nochmals dieselbe Information enthalten. Daher muss der Begriff "full" präzisiert werden:

- Y_std,full: vollständiger dynamischer Zustand der gewählten lokalen/Standard-Evolution;
- G_global: separat spezifizierte globale Lösungsdaten.

Strong Test B darf dann nicht behaupten, zwei **vollständig identische Universen** seien verschieden. Er prüft vielmehr, ob identische lokale Standardzustände bei unterschiedlichen zulässigen globalen Zuständen messbar unterschiedliche lokale Raten zeigen.

### Strong Test B

In der bisherigen Formulierung mit "boundary/global controls matched": **nein**, denn unterschiedliche globale Daten würden diese Bedingung verletzen.

Als präzisierter globaler Test:

    Y_std,full,A(a*) = Y_std,full,B(a*)
    G_global,A != G_global,B
    => O_A != O_B

ist die Frage **sinnvoll und nicht durch das Determinismus-Gate trivial ausgeschlossen**.

Das ist allerdings ein anderer Test als der bisherige strong Test B und muss entsprechend benannt werden.

### Entscheidung

**Höchste konzeptionelle Passung zur ursprünglichen AVI-Frage**, aber nur bei sauberer Trennung von lokalem Standardzustand und globalen Lösungsdaten. Keine vorhandene globale Eigenschaft darf ohne Mechanismus zur AVI-Evidenz erklärt werden.

## 5. O3 — physikalisch nicht-Markovsche Dynamik

Hier ist die reduzierte Dynamik tatsächlich von einer vergangenen Trajektorie abhängig:

    dY/dN = F[Y(N), history; θ]

oder äquivalent durch einen Gedächtniskern:

    response(N) = ∫ K(N,N') J(N') dN'.

Ein Hilfszustand ξ kann eine solche Gedächtnisdynamik lokalisieren/komprimieren.

### Stärke

Historienabhängigkeit ist hier nicht nachträglich hinzugefügt, sondern Bestandteil der Dynamik. ξ kann dann als physikalischer Gedächtniszustand sinnvoll sein.

### Kritisches Problem

Viele scheinbar nicht-Markovsche effektive Beschreibungen werden wieder Markovsch, sobald die ausgelassenen Freiheitsgrade in den vollständigen Zustand aufgenommen werden. Dann verschiebt sich das Problem lediglich auf einen größeren Zustandsraum.

AVI müsste daher zeigen, warum die nicht-Markovsche Struktur fundamental relevant ist oder warum die integrierten Freiheitsgrade prinzipiell als effektive Beschreibung genügen.

### Strong Test B

Für einen reduzierten Zustand: **möglich**.

Für einen wirklich vollständigen fundamentalen Zustand: **ungeklärt und möglicherweise wieder ausgeschlossen**.

### Entscheidung

Methodisch interessant, aber als Fundament schwächer als O2, solange kein unabhängiger physikalischer Ursprung des Gedächtniskerns existiert.

## 6. Vergleich

| Kriterium | O1 zusätzlicher Freiheitsgrad | O2 globale Information | O3 nicht-Markov |
|---|---|---|---|
| übersteht Determinismus-Gate formal | ja | ja, für lokalen Standardzustand | ja, reduziert |
| benötigt neue lokale Physik | stark | nicht zwingend | möglicherweise |
| Nähe zur ursprünglichen AVI-Frage | mittel | hoch | hoch |
| Risiko bloßer Umbenennung | mittel | mittel | hoch |
| vorhandene methodische Vergleichsfälle | zusätzliche Felder/Sektoren | Topologie/Randdaten | effektive Gedächtniskerne |
| sofortige quantitative Kopplung vorhanden | nein | nein | nein |
| wichtigste offene Frage | Was ist der neue Freiheitsgrad? | Welche globale Größe koppelt lokal? | Was trägt das physikalische Gedächtnis? |

## 7. Ergebnis

Keine der drei Ontologien ist derzeit physikalisch etabliert.

Das Screening liefert aber eine klare Reihenfolge für die weitere Grundlagenarbeit:

### Primärer Pfad: O2 — globale Information

Nicht weil O2 bereits bestätigt wäre, sondern weil sie die geringste Abweichung von der ursprünglichen AVI-Frage erfordert: lokale Raten werden relativ zu einem globalen kosmologischen Zustand untersucht, ohne sofort ein neues lokales Feld zu postulieren.

### Sekundärer Pfad: O3 — nicht-Markovsche effektive Dynamik

Als mathematischer Vergleichspfad. Er muss beweisen, dass ξ mehr ist als ein Hilfszustand für ausgelassene Standardfreiheitsgrade.

### Reservepfad: O1 — zusätzlicher dynamischer Freiheitsgrad

Nur weiterverfolgen, wenn O2/O3 scheitern oder unabhängige Physik einen neuen Freiheitsgrad motiviert. Er darf nicht allein eingeführt werden, um Test B zu retten.

## 8. Revision von Test B

Die bisherige Form wird in zwei harte Tests aufgeteilt.

### Test B-F — fundamentale Zustandsseparation

    Y_fund,A = Y_fund,B
    ξ_A != ξ_B
    => O_A != O_B

Dieser Test verlangt einen echten zusätzlichen Freiheitsgrad und passt primär zu O1.

### Test B-G — globale Kontextseparation

    Y_std,local,A = Y_std,local,B
    G_global,A != G_global,B
    => O_A != O_B

Dieser Test passt zu O2. Die globalen Unterschiede sind **keine unkontrollierten Confounder**, sondern die explizite unabhängige Variable des Tests. Alle übrigen relevanten Standardparameter müssen kontrolliert werden.

O3 erhält vorläufig keinen eigenen fundamentalen Testnamen, solange nicht geklärt ist, ob seine Gedächtnisvariable fundamental oder nur effektiv ist.

## 9. Konsequenz für Φ und ξ

Für O2 sollte ξ nicht vorschnell mit Φ identifiziert werden.

Saubere vorläufige Rollen:

    G_global = physikalisch definierte globale Information
    ξ = minimaler zusätzlicher Zustandsparameter, falls zur Dynamik/Kopplung nötig
    Φ = mögliche integrierte Arbeitsgröße

Erst eine konkrete Theorie darf Beziehungen wie

    ξ = f(G_global)
    Φ = F[ξ,Y]

festlegen.

Damit wird verhindert, dass drei bisher offene Begriffe durch Namensgleichsetzung scheinbar geschlossen werden.

## 10. Nächster Gate-Test

Der primäre O2-Pfad muss nun eine strengere Frage bestehen:

> Gibt es in etablierter Kosmologie globale Lösungsdaten, die bei lokal identischem Standardzustand verschieden sein können und prinzipiell lokale Observablen beeinflussen, ohne bereits vollständig durch bekannte lokale Physik beschrieben zu sein?

Zu prüfen sind insbesondere:

1. globale räumliche Topologie als methodischer Referenzfall;
2. Randbedingungen/global modes;
3. beobachtbare Konsequenzen solcher globalen Unterschiede;
4. ob irgendein solcher Mechanismus überhaupt zu lokalen dimensionslosen Ratenverhältnissen führen könnte.

Der Zweck ist ausdrücklich nicht, Topologie oder Randbedingungen zu AVI umzubenennen. Der Test soll feststellen, ob O2 eine physikalisch sinnvolle Architektur besitzt oder nur eine philosophisch attraktive Formulierung ist.

## 11. Epistemischer Status

- **[R]** Lokale Dynamik und globale Topologie/Randdaten sind in physikalischen Modellen logisch unterscheidbare Ebenen; effektive nicht-Markovsche Beschreibungen können aus reduzierten Freiheitsgraden entstehen.
- **[D]** Ein ausschließlich aus vollständig determinierter Standardhistorie berechneter ξ-Zustand genügt nicht für Test B-F.
- **[H]** AVI könnte an globale Information oder einen echten zusätzlichen Freiheitsgrad koppeln.
- **[I]** Die Omnizedenz kann die Frage nach Teil/Ganzes und Werden motivieren, entscheidet aber weder für O1, O2 noch O3.
