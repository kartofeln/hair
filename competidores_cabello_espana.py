import pandas as pd
from datetime import datetime

# Lista de competidores principales en el mercado español de cuidado del cabello
competidores = [
    {
        "nombre": "L'Oréal Professionnel",
        "dominio": "lorealprofessionnel.es",
        "categoria": "Profesional",
        "productos": ["Champús", "Acondicionadores", "Mascarillas", "Tratamientos", "Coloración"],
        "segmento": "Premium",
        "presencia": "Nacional",
        "canales": ["Salones", "Distribuidores profesionales", "E-commerce"]
    },
    {
        "nombre": "Kérastase",
        "dominio": "kerastase.es",
        "categoria": "Profesional/Lujo",
        "productos": ["Champús", "Mascarillas", "Serums", "Tratamientos específicos"],
        "segmento": "Lujo",
        "presencia": "Nacional",
        "canales": ["Salones premium", "E-commerce", "Tiendas especializadas"]
    },
    {
        "nombre": "Schwarzkopf Professional",
        "dominio": "schwarzkopf-professional.es",
        "categoria": "Profesional",
        "productos": ["Coloración", "Champús", "Tratamientos", "Styling"],
        "segmento": "Premium",
        "presencia": "Nacional",
        "canales": ["Salones", "Distribuidores profesionales"]
    },
    {
        "nombre": "Wella Professionals",
        "dominio": "wella.com/professional/es-ES",
        "categoria": "Profesional",
        "productos": ["Coloración", "Champús", "Tratamientos", "Styling"],
        "segmento": "Premium",
        "presencia": "Nacional",
        "canales": ["Salones", "Distribuidores profesionales"]
    },
    {
        "nombre": "Salerm Cosmetics",
        "dominio": "salerm.com",
        "categoria": "Profesional",
        "productos": ["Champús", "Tratamientos", "Coloración", "Styling"],
        "segmento": "Medio-Alto",
        "presencia": "Nacional",
        "canales": ["Salones", "Tiendas especializadas", "E-commerce"]
    },
    {
        "nombre": "Montibello",
        "dominio": "montibello.com",
        "categoria": "Profesional",
        "productos": ["Champús", "Tratamientos", "Coloración", "Styling"],
        "segmento": "Medio-Alto",
        "presencia": "Nacional",
        "canales": ["Salones", "Distribuidores profesionales"]
    },
    {
        "nombre": "Revlon Professional",
        "dominio": "revlonprofessional.com",
        "categoria": "Profesional",
        "productos": ["Coloración", "Champús", "Tratamientos", "Styling"],
        "segmento": "Medio-Alto",
        "presencia": "Nacional",
        "canales": ["Salones", "Distribuidores profesionales"]
    },
    {
        "nombre": "TIGI",
        "dominio": "tigi.com",
        "categoria": "Profesional",
        "productos": ["Champús", "Styling", "Tratamientos"],
        "segmento": "Premium",
        "presencia": "Nacional",
        "canales": ["Salones", "Tiendas especializadas"]
    },
    {
        "nombre": "Moroccanoil",
        "dominio": "moroccanoil.com/es",
        "categoria": "Profesional/Consumo",
        "productos": ["Tratamientos", "Champús", "Mascarillas", "Styling"],
        "segmento": "Premium",
        "presencia": "Nacional",
        "canales": ["Salones", "Tiendas especializadas", "E-commerce"]
    },
    {
        "nombre": "Redken",
        "dominio": "redken.es",
        "categoria": "Profesional",
        "productos": ["Champús", "Tratamientos", "Coloración", "Styling"],
        "segmento": "Premium",
        "presencia": "Nacional",
        "canales": ["Salones", "Distribuidores profesionales"]
    }
]

def generar_informe_competidores():
    """Genera un informe detallado de los competidores"""
    
    # Crear DataFrame
    df = pd.DataFrame(competidores)
    
    # Generar archivo CSV
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = f"competidores_cabello_espana_{timestamp}.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8')
    
    # Generar informe de texto
    txt_filename = f"informe_competidores_cabello_{timestamp}.txt"
    
    with open(txt_filename, 'w', encoding='utf-8') as f:
        f.write("ANÁLISIS DE COMPETIDORES EN EL MERCADO ESPAÑOL DE CUIDADO CAPILAR\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        # Análisis por segmento
        f.write("1. DISTRIBUCIÓN POR SEGMENTO DE MERCADO\n")
        f.write("-" * 40 + "\n")
        segmentos = df['segmento'].value_counts()
        for segmento, count in segmentos.items():
            f.write(f"{segmento}: {count} competidores ({count/len(df)*100:.1f}%)\n")
        f.write("\n")
        
        # Análisis por categoría
        f.write("2. DISTRIBUCIÓN POR CATEGORÍA\n")
        f.write("-" * 40 + "\n")
        categorias = df['categoria'].value_counts()
        for categoria, count in categorias.items():
            f.write(f"{categoria}: {count} competidores ({count/len(df)*100:.1f}%)\n")
        f.write("\n")
        
        # Productos más comunes
        f.write("3. PRODUCTOS MÁS COMUNES\n")
        f.write("-" * 40 + "\n")
        productos_count = {}
        for productos_list in df['productos']:
            for producto in productos_list:
                productos_count[producto] = productos_count.get(producto, 0) + 1
        
        for producto, count in sorted(productos_count.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{producto}: {count} competidores ({count/len(df)*100:.1f}%)\n")
        f.write("\n")
        
        # Canales de distribución
        f.write("4. CANALES DE DISTRIBUCIÓN\n")
        f.write("-" * 40 + "\n")
        canales_count = {}
        for canales_list in df['canales']:
            for canal in canales_list:
                canales_count[canal] = canales_count.get(canal, 0) + 1
        
        for canal, count in sorted(canales_count.items(), key=lambda x: x[1], reverse=True):
            f.write(f"{canal}: {count} competidores ({count/len(df)*100:.1f}%)\n")
        f.write("\n")
        
        # Conclusiones y recomendaciones
        f.write("5. CONCLUSIONES Y RECOMENDACIONES\n")
        f.write("-" * 40 + "\n")
        f.write("a) Segmentación del mercado:\n")
        f.write("   - El mercado está dominado por marcas premium y profesionales\n")
        f.write("   - Existe una oportunidad en el segmento medio para diferenciación\n\n")
        
        f.write("b) Productos:\n")
        f.write("   - Los champús y tratamientos son productos base en todas las marcas\n")
        f.write("   - La coloración es un segmento importante en el mercado profesional\n\n")
        
        f.write("c) Canales:\n")
        f.write("   - Los salones profesionales son el canal principal\n")
        f.write("   - El e-commerce está ganando importancia como canal de distribución\n\n")
        
        f.write("d) Recomendaciones estratégicas:\n")
        f.write("   - Desarrollar una línea profesional completa\n")
        f.write("   - Enfocarse en productos de tratamiento específicos\n")
        f.write("   - Establecer una fuerte presencia en salones profesionales\n")
        f.write("   - Implementar una estrategia omnicanal\n")
    
    print(f"Se ha generado el archivo CSV: {csv_filename}")
    print(f"Se ha generado el informe: {txt_filename}")

if __name__ == "__main__":
    generar_informe_competidores() 