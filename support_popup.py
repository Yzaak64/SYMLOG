# support_popup.py (Versión Final con Scroll y con Imagen)

import tkinter as tk
from tkinter import ttk
import webbrowser
import os
from PIL import Image, ImageTk
import traceback

def show_support_popup():
    """
    Muestra una ventana emergente modal con barras de desplazamiento y la imagen 
    del botón, bloqueando la ejecución hasta que se cierre.
    """
    print("[LOG] Iniciando la función show_support_popup (versión con Scroll e Imagen).")
    
    temp_root = tk.Tk()
    temp_root.withdraw()
    print("[LOG] Instancia temporal de Tkinter creada y oculta.")

    popup = None
    try:
        popup = tk.Toplevel(temp_root)
        popup.title("Apoya este Proyecto")
        popup.minsize(300, 350)

        def on_close_popup():
            print("[LOG] on_close_popup llamado. Destruyendo el popup y la raíz temporal.")
            if popup and popup.winfo_exists():
                popup.destroy()
            if temp_root and temp_root.winfo_exists():
                temp_root.destroy()

        popup.protocol("WM_DELETE_WINDOW", on_close_popup)

        # --- ESTRUCTURA DE SCROLL ---
        main_container = ttk.Frame(popup)
        main_container.pack(expand=True, fill=tk.BOTH)
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        canvas = tk.Canvas(main_container, bd=0, highlightthickness=0)
        canvas.grid(row=0, column=0, sticky='nsew')

        v_scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar = ttk.Scrollbar(main_container, orient="horizontal", command=canvas.xview)
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        scrollable_frame = ttk.Frame(canvas, padding="20")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        def _on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scrollable_frame.bind("<Configure>", _on_frame_configure)
        # --- FIN DE ESTRUCTURA DE SCROLL ---

        # --- Contenido del Pop-up (dentro de 'scrollable_frame') ---
        ttk.Label(scrollable_frame, text="❤️", font=("Segoe UI Emoji", 20)).pack(pady=(0, 5))
        support_text = "Si esta herramienta te es útil, considera apoyar su desarrollo futuro."
        ttk.Label(scrollable_frame, text=support_text, wraplength=350, justify=tk.CENTER).pack(pady=(0, 20))
        
        support_url = "https://www.buymeacoffee.com/Yzaak64"
        image_path = "buy_me_a_coffee.png" # Nombre del archivo de imagen
        
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                img.thumbnail((217, 60), Image.Resampling.LANCZOS) 
                popup.coffee_photo = ImageTk.PhotoImage(img) 
                coffee_button = tk.Button(scrollable_frame, image=popup.coffee_photo, 
                                          command=lambda: [webbrowser.open_new(support_url), on_close_popup()], 
                                          borderwidth=0, cursor="hand2")
                coffee_button.pack(pady=10)
            else:
                # Botón de respaldo si la imagen no se encuentra
                print(f"[ADVERTENCIA] No se encontró la imagen '{image_path}'. Usando botón de texto.")
                fallback_button = ttk.Button(scrollable_frame, text="☕ Buy me a coffee", 
                                             command=lambda: [webbrowser.open_new(support_url), on_close_popup()])
                fallback_button.pack(pady=10)
        except Exception as e:
            traceback.print_exc()
            # Botón de respaldo en caso de cualquier otro error
            print(f"[ERROR] No se pudo cargar la imagen '{image_path}'. Usando botón de texto.")
            fallback_button = ttk.Button(scrollable_frame, text="☕ Buy me a coffee", 
                                         command=lambda: [webbrowser.open_new(support_url), on_close_popup()])
            fallback_button.pack(pady=10)
        
        continue_button = ttk.Button(scrollable_frame, text="Continuar al programa", command=on_close_popup)
        continue_button.pack(pady=(20, 0))

        # --- Centrar la ventana ---
        popup.update_idletasks()
        req_width = scrollable_frame.winfo_reqwidth() + v_scrollbar.winfo_width() + 40
        req_height = scrollable_frame.winfo_reqheight() + h_scrollbar.winfo_height() + 40
        
        s_width = popup.winfo_screenwidth()
        s_height = popup.winfo_screenheight()
        
        p_width = min(req_width, s_width - 50)
        p_height = min(req_height, s_height - 50)

        x = (s_width // 2) - (p_width // 2)
        y = (s_height // 2) - (p_height // 2)
        popup.geometry(f"{p_width}x{p_height}+{x}+{y}")
        
        # --- Atributos para asegurar la visibilidad ---
        popup.attributes('-topmost', True)
        popup.focus_force()
        popup.grab_set()

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