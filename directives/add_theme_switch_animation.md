# Direttiva: Animazione Switch Tematico (Dark/Light) (COMPLETATA)

## Obiettivo
Creare una transizione cromatica fluida tra le sezioni nere e bianche durante lo scrolling.

## Sistema CSS
- **Body Transition**: `transition: background-color 0.8s ease, color 0.8s ease`.
- **Global Theme Classes**:
    - `.is-light`: Forza lo sfondo a bianco e il testo a nero.
    - `.is-dark`: Forza lo sfondo a nero e il testo a bianco.

## Logica JS
- Utilizzare `IntersectionObserver` con una `threshold` di circa 0.4 per rilevare il passaggio tra sezioni di colore diverso.
- Iniettare la classe corrispondente nell'elemento `<body>`.

## Strumenti/Script
- `execution/apply_theme_engine.py`: Aggiornamento CSS, creazione Hook e aggiornamento App.jsx.
