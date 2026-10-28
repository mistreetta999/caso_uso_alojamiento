# gestor_templates.py

from pathlib import Path

class GestorTemplates:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)

    def buscar_templates(self):
        return list(self.base_dir.rglob("*.html"))

    def mostrar_templates(self):
        templates = self.buscar_templates()

        print("\n=== TEMPLATES ENCONTRADOS ===\n")

        for tpl in templates:
            print(tpl)

        print(f"\nTotal: {len(templates)} templates")

    def buscar_por_nombre(self, nombre):
        encontrados = list(self.base_dir.rglob(nombre))

        if encontrados:
            print(f"\nTemplate encontrado: {nombre}\n")
            for archivo in encontrados:
                print(archivo)
        else:
            print(f"\nNo existe: {nombre}")

    def detectar_duplicados(self):
        nombres = {}

        for archivo in self.buscar_templates():
            nombres.setdefault(archivo.name, []).append(archivo)

        print("\n=== DUPLICADOS ===\n")

        for nombre, rutas in nombres.items():
            if len(rutas) > 1:
                print(f"\n{nombre}")
                for ruta in rutas:
                    print(f"  {ruta}")

if __name__ == "__main__":
    gestor = GestorTemplates(".")

    gestor.mostrar_templates()
    gestor.detectar_duplicados()
