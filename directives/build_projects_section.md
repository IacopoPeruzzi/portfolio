# Direttiva: Costruzione Sezione Progetti (COMPLETATA)

## Obiettivo
Creare una griglia di progetti elegante e interattiva per mostrare il lavoro svolto.

## Requisiti di Design
- **Grid**: Layout a 2 o 3 colonne (responsive).
- **Project Card**: Immagine di anteprima, titolo, breve descrizione e tag tecnologici.
- **Interazione**: Effetto hover per sollevare leggermente la card o mostrare un overlay.
- **Dati**: I dati devono essere gestiti tramite un array di oggetti per facilitare l'integrazione futura con un database o Google Sheets.

## Strumenti/Script
- `execution/deploy_projects_section.py`: Genera `src/components/Projects.jsx` e aggiorna `src/App.jsx`.

## Output
- Componente `Projects.jsx` funzionante.
- Stili CSS aggiuntivi in `src/index.css`.
