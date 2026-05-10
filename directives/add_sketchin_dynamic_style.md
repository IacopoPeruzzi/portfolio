# Direttiva: Dinamismo Fluido (Sketchin-Inspired) (COMPLETATA)

## Obiettivo
Rompere la rigidità della griglia attuale a favore di un layout dinamico e interattivo.

## Layout
- **Staggered Grid**: Alternanza di offset verticali per le card dei progetti.
- **Large Typography**: Titoli di sezione massimalisti che dominano lo spazio.

## Animazioni (Reveal)
- Utilizzare `IntersectionObserver` per attivare classi CSS (`is-visible`) quando gli elementi entrano nel viewport.
- Transizioni: `transform: translateY(50px)` e `opacity: 0` -> `translateY(0)` e `opacity: 1`.

## Effetti Hover
- Card che si espandono leggermente e aumentano il blur dello sfondo (effetto vetro più profondo).

## Strumenti/Script
- `execution/apply_dynamic_layout.py`: Aggiornamento CSS e aggiunta hook di osservazione.
