# Excel · Paso a paso

Curso interactivo en español: 32 lecciones, ocho módulos, ejercicios descargables, apuntes y progreso guardado en el navegador.

## Publicar en GitHub Pages

La versión estática lista para publicar está en `docs/`. No requiere servidor ni inicio de sesión de ChatGPT.

En **Settings → Pages**, selecciona **Deploy from a branch**, rama **main**, carpeta **/docs**, y guarda.

Dirección prevista al activar Pages: https://strabagdev.github.io/excel-paso-a-paso/

## Desarrollo y actualización

Requiere Node 22.13 o posterior.

```bash
npm ci
npm run dev:pages
```

Después de editar las lecciones o la interfaz:

```bash
npm run build:pages
git add app lib pages public docs package.json vite.pages.config.ts scripts/build-pages.mjs
git commit -m "Actualizar curso"
git push origin main
```

GitHub Pages publica el contenido de `docs/`. Hay que reconstruirlo antes de subir cambios de código.

## Archivos

- `lib/course.ts`: contenido, ejercicios y soluciones.
- `app/page.tsx` y `app/globals.css`: interfaz compartida.
- `pages/`: entrada independiente para GitHub Pages.
- `public/recursos/`: ocho libros Excel, CSV, JSON y scripts de práctica.
- `docs/`: distribución estática compilada con Vite.

La configuración original de Sites se conserva; `npm run build` utiliza esa configuración. `npm run build:pages` genera la versión independiente.

## Progreso y prácticas

El progreso, apuntes y marcadores se guardan en localStorage y se pueden exportar e importar desde Mi progreso. El progreso del sitio anterior no migra automáticamente: exporta allí e importa aquí.

Los datos son ficticios. La web no revisa automáticamente los libros del alumno ni se conecta a sistemas reales de Opco o Microsoft 365. Las lecciones de integración explican esas conexiones y sus requisitos.
