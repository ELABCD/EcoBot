# 🌍 EcoBot

EcoBot es un bot de Discord diseñado para educar y concienciar sobre el cambio climático. Ofrece datos informativos, consejos ecológicos, enlaces a recursos y herramientas interactivas para calcular el impacto ambiental.

## 🚀 Características

✅ **/dato** – Muestra un dato aleatorio sobre el cambio climático.  
✅ **/mas** – Proporciona enlaces con información confiable.  
✅ **/tips** – Ofrece consejos prácticos para reducir la contaminación.  
✅ **/noticias** – Muestra noticias recientes sobre el cambio climático.  
✅ **/impacto** – Evalúa qué tan ecológico eres con preguntas simples.  

---

## 🛠 Instalación y configuración

### 1️⃣ Requisitos previos
Antes de ejecutar EcoBot, asegúrate de tener:
- Python 3.12+
- `discord.py` instalado

Para instalar la librería de Discord:
```bash
pip install -U discord.py
```

### 2️⃣ Configurar el bot
1. Crea una aplicación en el [Portal de Desarrolladores de Discord](https://discord.com/developers/applications)
2. Genera un token y reemplázalo en el archivo `bot.py` en la línea:
   ```python
   client.run("TU_TOKEN_AQUI")
   ```
3. Invita el bot a tu servidor con los permisos adecuados.

🔗 **Invita a EcoBot a tu servidor:** [Haz clic aquí](https://discord.com/oauth2/authorize?client_id=1332496650911875225)
## O puedes usar un QR :)

![qr_EcoBot](https://github.com/user-attachments/assets/a5b0ba81-1f21-4f1e-bacd-edf3000c5036)



---

## 🏃‍♂️ Ejecución
Para ejecutar el bot, usa:
```bash
python bot.py
```
---

## 📜 Comandos disponibles

| Comando  | Descripción |
|----------|------------|
| `/dato` | Muestra un dato aleatorio sobre el cambio climático. |
| `/mas` | Muestra enlaces a páginas informativas sobre la contaminación. |
| `/tips` | Proporciona un consejo ecológico aleatorio. |
| `/noticias` | Muestra una noticia reciente sobre el cambio climático. |
| `/impacto` | Evalúa tu impacto ambiental mediante preguntas interactivas. |

---

## 🔥 Dificultades y soluciones
Durante el desarrollo de EcoBot, se presentaron algunos desafíos técnicos:

- **Error con la importación de `discord`**: Inicialmente, el código arrojaba un error `AttributeError: module 'discord' has no attribute 'bot'`. Se solucionó asegurando que `discord.py` estuviera actualizado y cambiando la implementación a `client` en lugar de `bot`.
- **Compatibilidad con versiones de Python**: Algunas funciones de `discord.py` no funcionaban correctamente con versiones antiguas de Python. Se resolvió actualizando el código para soportar Python 3.12+.
- **Problemas con permisos**: El bot no respondía a comandos debido a permisos insuficientes. Se verificaron y ajustaron los permisos en el portal de desarrolladores de Discord.
- **Interrupciones por desconexión**: Hubo problemas con la estabilidad del bot debido a desconexiones imprevistas. Se implementó un manejador de errores para reconectar automáticamente en caso de fallos.

Estos desafíos ayudaron a mejorar la estabilidad y funcionalidad de EcoBot, asegurando un rendimiento más fluido y confiable.

---

## 🔗 Fuentes y referencias
- [ONU - Cambio Climático](https://www.un.org/es/climatechange)
- [NASA - Evidencia del Cambio Climático](https://climate.nasa.gov/evidence/)
- [WWF - Cambio Climático](https://www.worldwildlife.org/initiatives/climate)

---

## 📌 Contribuciones
Si deseas mejorar EcoBot, puedes hacer un fork del repositorio, crear una nueva rama y enviar un pull request.

---

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

