# Architettura a 3 Livelli - Sistema Operativo

Operi all'interno di un'architettura a 3 livelli che separa le responsabilità per massimizzare l'affidabilità.

## Livello 1: Direttiva (Cosa fare)
- SOP in `directives/`
- Definiscono obiettivi, input, strumenti, output e casi limite.

## Livello 2: Orchestrazione (Prendere decisioni)
- Routing intelligente: leggi le direttive, chiama gli strumenti in `execution/`, gestisci errori.
- Collante tra intenzione ed esecuzione.

## Livello 3: Esecuzione (Fare il lavoro)
- Script Python deterministici in `execution/`
- Gestione API, dati, file, database.

## Principi Chiave
1. **Controllo Strumenti**: Controlla `execution/` prima di creare nuovi script.
2. **Auto-correzione**: Analizza errori, correggi script, aggiorna direttive.
3. **Aggiornamento Continuo**: Le direttive sono documenti vivi.
4. **Deliverable Cloud**: Gli output finali per l'utente devono risiedere su cloud (Google Sheets, ecc.).
5. **Dati Temporanei**: Tutto in `.tmp/` è sacrificabile e rigenerabile.
