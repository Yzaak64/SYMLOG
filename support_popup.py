# support_popup.py (Versión de Aislamiento Total)

import tkinter as tk
from tkinter import ttk
import webbrowser
import os
from PIL import Image, ImageTk
import traceback

def show_support_popup(): # <-- Ya no necesita el argumento 'parent'
    """
    Muestra una ventana emergente modal en su propia instancia de Tkinter,
    bloqueando la ejecución hasta que se cierre.
    """
    print("[LOG] Iniciando la función show_support_popup (versión de Aislamiento Total).")
    
    # 1. Crear una instancia de Tkinter temporal y ocultarla inmediatamente.
    #    Esto actúa como un 'contenedor' invisible para el popup.
    temp_root = tk.Tk()
    temp_root.withdraw()
    print("[LOG] Instancia temporal de Tkinter creada y oculta.")

    popup = None
    try:
        # 2. El Toplevel ahora pertenece a la raíz temporal.
        popup = tk.Toplevel(temp_root)
        popup.title("Apoya este Proyecto")

        def on_close_popup():
            print("[LOG] on_close_popup llamado. Destruyendo el popup y la raíz temporal.")
            # 3. Destruir explícitamente el popup y la raíz temporal para liberar recursos.
            if popup and popup.winfo_exists():
                popup.destroy()
            if temp_root and temp_root.winfo_exists():
                temp_root.destroy()

        popup.protocol("WM_DELETE_WINDOW", on_close_popup)

        # --- El resto del código de creación de widgets es idéntico ---
        popup_frame = ttk.Frame(popup, padding="20")
        popup_frame.pack(expand=True, fill=tk.BOTH)
        ttk.Label(popup_frame, text="❤️", font=("Segoe UI Emoji", 20)).pack(pady=(0, 5))
        support_text = "Si esta herramienta te es útil, considera apoyar su desarrollo futuro."
        ttk.Label(popup_frame, text=support_text, wraplength=350, justify=tk.CENTER).pack(pady=(0, 20))
        support_url = "https://www.buymeacoffee.com/Yzaak64"
        image_path = "Buy_Coffe.png"
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img.thumbnail((300, 100), Image.Resampling.LANCZOS)
                popup.coffee_photo = ImageTk.PhotoImage(img) 
                coffee_button = tk.Button(popup_frame, image=popup.coffee_photo, 
                                          command=lambda: [webbrowser.open_new(support_url), on_close_popup()], 
                                          borderwidth=0, cursor="hand2")
                coffee_button.pack(pady=10)
            else:
                fallback_button = ttk.Button(popup_frame, text="☕ Invítame un café", 
                                             command=lambda: [webbrowser.open_new(support_url), on_close_popup()])
                fallback_button.pack(pady=10)
        except Exception as e:
            traceback.print_exc()
            fallback_button = ttk.Button(popup_frame, text="☕ Invítame un café", 
                                         command=lambda: [webbrowser.open_new(support_url), on_close_popup()])
            fallback_button.pack(pady=10)
        
        continue_button = ttk.Button(popup_frame, text="Continuar al programa", command=on_close_popup)
        continue_button.pack(pady=(20, 0))

        # --- Centrar la ventana ---
        popup.update_idletasks()
        p_width = popup.winfo_width()
        p_height = popup.winfo_height()
        s_width = popup.winfo_screenwidth()
        s_height = popup.winfo_screenheight()
        x = (s_width // 2) - (p_width // 2)
        y = (s_height // 2) - (p_height // 2)
        popup.geometry(f"{p_width}x{p_height}+{x}+{y}")
        
        # --- Atributos para asegurar la visibilidad ---
        popup.attributes('-topmost', True)
        popup.focus_force()
        popup.grab_set()

        # 4. Iniciar el bucle de eventos para la instancia temporal.
        #    Esto bloquea la ejecución del script principal hasta que se llame a on_close_popup.
        print("[LOG] Iniciando el bucle de eventos para la raíz temporal (mainloop).")
        temp_root.mainloop()
        print("[LOG] Bucle de eventos de la raíz temporal finalizado.")

    except Exception as e:
        print("\n--- ERROR CATASTRÓFICO DENTRO DE show_support_popup ---")
        traceback.print_exc()
        if popup and popup.winfo_exists():
            popup.destroy()
        if temp_root and temp_root.winfo_exists():
            temp_root.destroy()