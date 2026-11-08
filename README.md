# Excel · Paso a paso

Curso web en español con 32 lecciones, ocho módulos y ejemplos ficticios inspirados en oficina técnica. Incluye fundamentos, fórmulas, búsquedas, calidad de datos, tablas dinámicas, Gantt, LET, LAMBDA, Solver, Power Query, Power BI, Office Scripts, VBA y Python.

## Ejecutar

Requiere Node 22.13 o posterior. Instalar con `npm ci` y ejecutar `npm run dev`. El proyecto usa React y Vinext. `npm run build` produce la aplicación para Cloudflare Workers mediante la integración de Sites.

## Contenido

- `lib/course.ts`: lecciones, ejercicios, soluciones y fuentes oficiales.
- `app/page.tsx`: navegación, comprobaciones, apuntes, marcadores y progreso.
- `app/globals.css`: diseño adaptable.
- `public/recursos`: ocho libros XLSX y archivos complementarios.
- `scripts/create-course-workbooks.mjs`: generador de recursos para el runtime de Artifact Tool. No se necesita para ejecutar la web.

## Progreso

Se guarda en localStorage con la clave `excel-paso-a-paso-v1`. No hay sincronización entre dispositivos. Exportar/importar permite trasladar progreso, notas y marcadores. Importar reemplaza el estado actual y valida formato e IDs. Una lección se completa cuando el alumno declara haber realizado la práctica y responde correctamente la comprobación. La web no analiza sus archivos de Excel.

## Alcance

Los datos son ficticios. Los archivos contienen bases para ejercicios; las consultas, tablas dinámicas, macros y gráficos se construyen siguiendo las lecciones. No hay conexión activa con Opco, Microsoft 365, WhatsApp ni Power BI. El JSON es una simulación explícita. La base es Microsoft 365 en español; cada tema avanzado incluye sus requisitos.

## Publicación

Curso publicado: https://excel-paso-a-paso-daniel.dxsilva.chatgpt.site

Repositorio: https://github.com/strabagdev/excel-paso-a-paso

El sitio publicado y este repositorio son copias independientes. Subir cambios a GitHub no despliega automáticamente el sitio.
