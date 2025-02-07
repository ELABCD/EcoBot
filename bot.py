import discord
import random

# Configuración del bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# 🌍 Datos sobre el cambio climático
datos_cambio_climatico = [
    "🌡️ La temperatura global ha aumentado 1.1°C desde la era preindustrial.",
    "🌊 El nivel del mar ha subido aproximadamente 8 cm desde 1993.",
    "🔥 Las olas de calor han aumentado en frecuencia e intensidad.",
    "🌲 La deforestación libera 15% de las emisiones globales de CO2.",
    "💨 Las ciudades generan el 70% de las emisiones de gases de efecto invernadero."
]

# 🔗 Enlaces útiles
enlaces_cambio_climatico = [
    "[ONU - Cambio Climático](https://www.un.org/es/climatechange)",
    "[NASA - Evidencia del Cambio Climático](https://climate.nasa.gov/evidence/)",
    "[WWF - Cambio Climático](https://www.worldwildlife.org/initiatives/climate)"
]

# 🛠 Consejos ecológicos
tips_eco = [
    "♻️ Reduce el uso de plásticos desechables.",
    "🚴 Usa bicicleta o transporte público en lugar de autos.",
    "💡 Ahorra energía apagando luces y usando bombillas LED.",
    "🌱 Come más alimentos de origen vegetal y menos carne.",
    "🚰 Reduce el consumo de agua cerrando el grifo mientras te cepillas los dientes."
]

# 📰 Noticias sobre el cambio climático (se pueden actualizar manualmente)
noticias = [
    "📢 *Un nuevo informe de la ONU advierte sobre el impacto del cambio climático en la biodiversidad.*",
    "📢 *Se registran temperaturas récord en varias partes del mundo.*",
    "📢 *Países acuerdan reducir emisiones en un 30% para 2030.*"
]

# 🌍 Calculadora de impacto ambiental (simplificada)
preguntas_impacto = [
    ("¿Usas transporte público o bicicleta a diario?", 5),
    ("¿Consumes productos locales y de temporada?", 3),
    ("¿Reciclas en tu casa regularmente?", 4),
    ("¿Reduciste tu consumo de carne en el último año?", 5),
    ("¿Tienes paneles solares o energía renovable en casa?", 6)
]

# 🟢 Comando /dato
@tree.command(name="dato", description="Muestra un dato aleatorio sobre el cambio climático.")
async def dato(interaction: discord.Interaction):
    dato_aleatorio = random.choice(datos_cambio_climatico)
    embed = discord.Embed(title="🌍 Dato sobre el Cambio Climático", 
                          description=dato_aleatorio, 
                          color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

# 🔵 Comando /mas
@tree.command(name="mas", description="Muestra enlaces sobre contaminación y cambio climático.")
async def mas(interaction: discord.Interaction):
    embed = discord.Embed(title="🔗 Enlaces sobre el Cambio Climático", 
                          description="Aquí tienes algunos sitios confiables:", 
                          color=discord.Color.blue())
    for enlace in enlaces_cambio_climatico:
        embed.add_field(name="🌱", value=enlace, inline=False)
    await interaction.response.send_message(embed=embed)

# 🌱 Comando /tips
@tree.command(name="tips", description="Muestra consejos para ayudar al medio ambiente.")
async def tips(interaction: discord.Interaction):
    tip_aleatorio = random.choice(tips_eco)
    embed = discord.Embed(title="🌿 Consejo Ecológico", 
                          description=tip_aleatorio, 
                          color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

# 📰 Comando /noticias
@tree.command(name="noticias", description="Muestra una noticia reciente sobre el cambio climático.")
async def noticias_command(interaction: discord.Interaction):
    noticia_aleatoria = random.choice(noticias)
    embed = discord.Embed(title="📰 Noticias sobre el Cambio Climático", 
                          description=noticia_aleatoria, 
                          color=discord.Color.orange())
    await interaction.response.send_message(embed=embed)

# 📊 Comando /impacto (Evalúa tu impacto ambiental)
@tree.command(name="impacto", description="Evalúa tu impacto ambiental con algunas preguntas.")
async def impacto(interaction: discord.Interaction):
    puntos = 0
    respuestas = []
    
    for pregunta, valor in preguntas_impacto:
        respuestas.append(f"✅ {pregunta} (+{valor} puntos)")
        puntos += valor
    
    resultado = "🌱 ¡Estás haciendo un gran trabajo!" if puntos > 15 else "♻️ ¡Puedes mejorar tus hábitos!"
    
    embed = discord.Embed(title="🌍 Evaluación de Impacto Ambiental", 
                          description=f"Tu puntaje: **{puntos}**\n\n" + "\n".join(respuestas) + f"\n\n**{resultado}**", 
                          color=discord.Color.green())
    await interaction.response.send_message(embed=embed)

# Evento cuando el bot está listo
@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user} está listo para ayudar al planeta 🌍")

client.run("TOKEN") 
