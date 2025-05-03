# coding: utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, scrolledtext
import json
import pandas as pd
# import io
import os
import sys
# import random
import matplotlib.colors
import matplotlib.pyplot as plt
import numpy as np
import traceback
import datetime
# import threading

# --- DEFINICIONES DE DATOS SYMLOG, TABLA, scale_score ---
# (Sin cambios)
symlog_adjective_items_data = [ {'dimension': 'U',   'item': 'Activo, dominante, habla mucho',         'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'UP',  'item': 'Extrovertido, destaca, positivo',        'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UPF', 'item': 'Un líder democrático orientado a la tarea','weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'UF',  'item': 'Parecido a un ejecutivo asertivo',       'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UNF', 'item': 'Autoritario, controlador, desaprobador', 'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'UN',  'item': 'Arrogante, tenaz, poderoso',             'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UNB', 'item': 'Provocativo, egocéntrico, se pavonea',   'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'UB',  'item': 'Bromista, expresivo, teatrero',          'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UPB', 'item': 'Entretenido, sociable, sonriente, cálido','weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'P',   'item': 'Amistoso, igualitario',                  'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'PF',  'item': 'Trabaja cooperativamente con otros',     'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'F',   'item': 'Analítico, orientado a la tarea, solucionador de problemas', 'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'NF',  'item': 'Legalista, quiere hacer las cosas bien', 'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'N',   'item': 'No amistoso, negativo',                  'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'NB',  'item': 'Irritable, cínico, no cooperativo',      'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'B',   'item': 'Muestra los sentimientos y las emociones','weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'PB',  'item': 'Afectuoso, agradable, le gusta divertirse','weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DP',  'item': 'Considerado con los demás, agradecido, inspira confianza', 'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DPF', 'item': 'Apacible, deseoso de aceptar responsabilidades', 'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'DF',  'item': 'Obediente, trabaja sumisamente',           'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DNF', 'item': 'Se autocastiga, trabaja demasiado duro',   'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'DN',  'item': 'Depresivo, triste, resentido',             'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DNB', 'item': 'Alienado, ausente, ido',                   'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'DB',  'item': 'Miedoso, duda de sus propias capacidades','weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DPB', 'item': 'Se encuentra feliz con los demás',         'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'D',   'item': 'Pasivo, introvertido, habla poco',         'weighted_scores': [0, 6, 12, 18, 24]},]
symlog_value_items_data = [{'dimension': 'U',   'item': 'Exito financiero individual, prominencia y poder personal', 'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'UP',  'item': 'Popularidad y exito social, gustar a otros a ser admirado', 'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UPF', 'item': 'Activo en trabajo de equipo hacia metas comunes, unidad en la organizacion', 'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'UF',  'item': 'Eficiencia, administracion firme e imparcial',   'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UNF', 'item': 'Fortalecer la autoridad y el cumprimento de normas y reglamentos',   'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'UN',  'item': 'Caracter forte, agresivo crescimento personal',              'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UNB', 'item': 'Recio individualismo personal, resistencia a la autoridad',   'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'UB',  'item': 'Divertirse, liberar tension, relajar el control',            'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'UPB', 'item': 'Proteger a los membros menos capazes, dar ajuda quando sea necesario','weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'P',   'item': 'Igualdad, participacion democratica en la toma de decisiones',           'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'PF',  'item': 'Idealismo responsable, trabalho de colaboracion',       'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'F',   'item': 'Formas conservadoras, estabelecidas y "correctas" de hacer las cosas', 'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'NF',  'item': 'Restringir desejos individuais por las metas de la organizacion',   'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'N',   'item': 'Autoproteccion, intereses personales primero, autosuficiencia',                   'weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'NB',  'item': 'Rechazo de los procedimentos estabelecidos',    'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'B',   'item': 'Cambio a nuevos procedimentos, valores diferentes, creatividade','weighted_scores': [0, 6, 12, 18, 24]}, {'dimension': 'PB',  'item': 'Amistad, compatibilidade, recreacion','weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DP',  'item': 'Confianza en la bondad en los demas', 'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DPF', 'item': 'Dedicacion, fidelidade, lealdad a la organizacion', 'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'DF',  'item': 'Obediencia a la linea de mando complaciendo a la autoridad',         'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DNF', 'item': 'Auto-sacrificio si es necesario para alcanzar las metas de la organizacion',   'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'DN',  'item': 'Rechazo a la popularidad, no haciendo las cosas con otros',           'weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DNB', 'item': 'Aceptacion del fracaso, dejar de esforzarse',              'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'DB',  'item': 'Pasividad y falta de cooperacion con la autoridad','weighted_scores': [0, 3, 6, 9, 12]}, {'dimension': 'DPB', 'item': 'Tranquilo, satisfecho, llevar la vida con calma',       'weighted_scores': [0, 2, 4, 6, 8]}, {'dimension': 'D',   'item': 'Has dejado a un lado necessidades y deseos personales, pasividad',         'weighted_scores': [0, 6, 12, 18, 24]},]
all_scales_data = { "Adjetivos": symlog_adjective_items_data, "Valores": symlog_value_items_data }
scaling_table = [ (8,1),(14,2),(20,3),(25,4),(31,5),(37,6),(43,7),(49,8),(54,9),(60,10),(66,11),(72,12),(77,13),(83,14),(89,15),(95,16),(101,17),(104,18) ]

# --- CONSTANTES DE TAMAÑO ---
BASE_SIZE = 4500
SCALE_FACTOR = 400
MIN_MARKER_SIZE = 60
# --- DIVISOR VISUAL PARA MATPLOTLIB ---
PLOT_SIZE_DIVISOR = 2
# ------------------------------------

# --- FUNCIONES AUXILIARES SYMLOG ---
# (Sin cambios)
def scale_score(raw_score, table):
    if raw_score == 0: return 0
    abs_score = abs(raw_score); sv = table[-1][1]
    for limit, unit in table:
        if abs_score <= limit: sv = unit; break
    return sv if raw_score > 0 else -sv
def calculate_from_manual_scores(pname, sname, scores_dict, stable):
    items = all_scales_data.get(sname)
    if not items: return None, False, f"Err: Escala '{sname}' no encontrada."
    rs = {'U': 0, 'D': 0, 'P': 0, 'N': 0, 'F': 0, 'B': 0}; ok = True; msgs = []
    for idata in items:
        item, code, sc = idata['item'], idata['dimension'], idata['weighted_scores']
        idx = scores_dict.get(item, 0)
        try:
            if not (0 <= idx < len(sc)): raise IndexError(f"Índice {idx} fuera rango '{item[:20]}...'")
            ws = sc[idx]
            for char in code:
                 if char in rs: rs[char] += ws
                 else: msgs.append(f"Warn: Dim '{char}' inv '{code}' en '{item[:20]}...'.")
        except IndexError as e: msgs.append(f"Error: {e}. Usando 0."); ok = False
        except Exception as e: msgs.append(f"Error calc '{item[:20]}...': {e}"); ok = False
    if ok:
        ud, pn, fb = rs['U'] - rs['D'], rs['P'] - rs['N'], rs['F'] - rs['B']
        uds, pns, fbs = scale_score(ud, stable), scale_score(pn, stable), scale_score(fb, stable)
        res = {'name': pname, 'scale': sname, 'ud': uds, 'pn': pns, 'fb': fbs, 'raw_ud': ud, 'raw_pn': pn, 'raw_fb': fb}
        final_msg = "\n".join(msgs) if msgs else "Cálculo manual OK."
        return res, True, final_msg
    else: msgs.append("Cálculo manual fallido por errores críticos."); return None, False, "\n".join(msgs)
def calculate_participant_scores_by_position(pname, pscores, items, stable, sname):
    rs = {'U': 0, 'D': 0, 'P': 0, 'N': 0, 'F': 0, 'B': 0}
    warns = []; calculation_possible = True; n_items = len(items)
    if len(pscores) != n_items: warns.append(f"Error Crítico: Scores({len(pscores)}) != Ítems({n_items})."); return None, warns
    for i, info in enumerate(items):
        code, s_opts, idbg = info['dimension'], info['weighted_scores'], info.get('item', f'Item {i+1}')
        raw_score = pscores.iloc[i]; idx = 0
        if pd.isna(raw_score) or raw_score is None: warns.append(f"Warn: NaN/Nulo f{i+1} ('{idbg}'). Usando 0."); idx = 0
        else:
            try:
                temp_idx = int(raw_score)
                if not (0 <= temp_idx <= 4): warns.append(f"Warn: '{raw_score}' (f{i+1}) fuera rango '{idbg}'. Usando 0."); idx = 0
                else: idx = temp_idx
            except (ValueError, TypeError): warns.append(f"Warn: '{raw_score}' (f{i+1}) no número '{idbg}'. Usando 0."); idx = 0
        try:
            if not s_opts or len(s_opts) != 5: warns.append(f"Err Int: Pesos inv '{idbg}' (f{i+1}). Omitiendo."); calculation_possible = False; continue
            if not (0 <= idx < len(s_opts)): warns.append(f"Err Int: Índice {idx} inv pesos '{idbg}' (f{i+1}). Omitiendo."); calculation_possible = False; continue
            ws = s_opts[idx]
            for char in code:
                if char in rs: rs[char] += ws
                else: warns.append(f"Warn: Dim '{char}' inv en '{code}' (f{i+1}, '{idbg}').")
        except Exception as e: warns.append(f"Err inesperado pesos '{idbg}' (f{i+1}): {e}"); calculation_possible = False; continue
    if not calculation_possible: warns.append("Cálculo no posible por errores críticos."); return None, warns
    ud, pn, fb = rs['U'] - rs['D'], rs['P'] - rs['N'], rs['F'] - rs['B']
    uds, pns, fbs = scale_score(ud, stable), scale_score(pn, stable), scale_score(fb, stable)
    res = {'name': pname, 'scale': sname, 'ud': uds, 'pn': pns, 'fb': fbs, 'raw_ud': ud, 'raw_pn': pn, 'raw_fb': fb}
    return res, warns
def calculate_marker_size(ud_score):
    if not isinstance(ud_score, (int, float)): ud_score = 0
    marker_size = BASE_SIZE + ud_score * SCALE_FACTOR
    return max(MIN_MARKER_SIZE, marker_size)

# --- CLASE PRINCIPAL DE LA APLICACIÓN TKINTER ---
class SymlogApp:
    def __init__(self, master):
        self.master=master; master.title("Interfaz SYMLOG Tkinter v1.3.18"); master.geometry("800x600")
        self.current_action=tk.StringVar(master); self.selected_scale_name=tk.StringVar(master); self.selected_excel_file=tk.StringVar(master); self.selected_json_file_plot=tk.StringVar(master); self.results_filename=tk.StringVar(master,value="resultados_symlog.json"); self.results_by_scale={}; self.manual_item_widgets={}
        self.manual_entry_order = []
        style=ttk.Style(); style.theme_use('clam')
        main_frame=ttk.Frame(master,padding="10"); main_frame.pack(fill=tk.BOTH,expand=True)
        top_frame=ttk.Frame(main_frame); top_frame.pack(fill=tk.X,pady=5,side=tk.TOP)
        ttk.Label(top_frame,text="Acción:").pack(side=tk.LEFT,padx=5); action_options=['Por favor, selecciona...','1. Generar Plantilla Excel','2. Ingresar Datos Manualmente','3. Procesar Archivo Excel Subido','4. Generar Gráfico desde JSON']; self.action_combo=ttk.Combobox(top_frame,textvariable=self.current_action,values=action_options,state='readonly',width=30); self.action_combo.pack(side=tk.LEFT,padx=5); self.action_combo.current(0); self.action_combo.bind('<<ComboboxSelected>>',self._on_action_change)
        ttk.Label(top_frame,text="Escala SYMLOG:").pack(side=tk.LEFT,padx=5); scale_options=['Adjetivos','Valores']; self.scale_combo=ttk.Combobox(top_frame,textvariable=self.selected_scale_name,values=scale_options,state='disabled',width=15); self.scale_combo.pack(side=tk.LEFT,padx=5); self.scale_combo.bind('<<ComboboxSelected>>',self._on_scale_change)
        self.action_panel_container=ttk.Frame(main_frame); self.action_panel_container.pack(fill=tk.BOTH,expand=True,pady=5,side=tk.TOP,after=top_frame)
        self.action_panels={}; self.action_panels['1. Generar Plantilla Excel']=self._create_template_panel(self.action_panel_container); self.action_panels['2. Ingresar Datos Manualmente']=self._create_manual_panel(self.action_panel_container); self.action_panels['3. Procesar Archivo Excel Subido']=self._create_excel_panel(self.action_panel_container); self.action_panels['4. Generar Gráfico desde JSON']=self._create_json_plot_panel(self.action_panel_container)
        output_frame_container=ttk.LabelFrame(main_frame,text="Salida y Mensajes"); output_frame_container.pack(fill=tk.X,pady=5,side=tk.BOTTOM,expand=False); self.output_text=scrolledtext.ScrolledText(output_frame_container,wrap=tk.WORD,height=10,state='disabled'); self.output_text.pack(fill=tk.BOTH,expand=True)
        self.results_frame=ttk.Frame(main_frame);
        ttk.Label(self.results_frame,text="Guardar JSON como:").grid(row=0,column=0,padx=5,pady=5,sticky="w"); self.results_entry=ttk.Entry(self.results_frame,textvariable=self.results_filename,width=40); self.results_entry.grid(row=0,column=1,padx=5,pady=5,sticky="ew"); self.save_button=ttk.Button(self.results_frame,text="Guardar Resultados",command=self._save_results,state='disabled'); self.save_button.grid(row=1,column=0,padx=5,pady=5); self.clear_button=ttk.Button(self.results_frame,text="Limpiar Resultados",command=self._clear_all,state='disabled',style='Danger.TButton'); self.clear_button.grid(row=1,column=1,padx=5,pady=5); style.configure('Danger.TButton',foreground='white',background='red')
        self._update_action_panels(); self._update_widget_states(); self._log("Interfaz SYMLOG iniciada.")

    # --- Crear Paneles ---
    # (Sin cambios funcionales)
    def _create_template_panel(self, parent): frame=ttk.Frame(parent,padding="10"); ttk.Label(frame,text="Selecciona escala y clic para generar plantilla Excel (.xlsx).").pack(pady=5,anchor="w"); ttk.Button(frame,text="Generar y Guardar Plantilla",command=self._generate_template).pack(pady=10); return frame
    def _create_manual_panel(self, parent): frame=ttk.Frame(parent,padding="10"); nf=ttk.Frame(frame); nf.pack(fill=tk.X, pady=5); ttk.Label(nf,text="Nombre Participante:").pack(side=tk.LEFT,padx=5); self.manual_participant_name_entry=ttk.Entry(nf,width=40); self.manual_participant_name_entry.pack(side=tk.LEFT,padx=5,fill=tk.X,expand=True); icf=ttk.LabelFrame(frame,text="Puntajes(0-4)"); icf.pack(fill=tk.BOTH,expand=True, pady=5); self.mic=tk.Canvas(icf,bd=0,highlightthickness=0,bg="#ffffff"); self.mif=ttk.Frame(self.mic,padding="5"); vsb=ttk.Scrollbar(icf,orient="vertical",command=self.mic.yview); self.mic.configure(yscrollcommand=vsb.set); vsb.pack(side="right",fill="y"); self.mic.pack(side="left",fill="both",expand=True); self.micw=self.mic.create_window((0,0),window=self.mif,anchor="nw",tags="self.mif"); self.mif.bind("<Configure>", self._on_manual_items_frame_configure); self.mic.bind_all("<MouseWheel>", self._on_mousewheel, add='+'); self.mic.bind_all("<Button-4>", self._on_mousewheel, add='+'); self.mic.bind_all("<Button-5>", self._on_mousewheel, add='+'); self.manual_add_button=ttk.Button(frame,text="Calcular y Añadir",command=self._add_manual,state='disabled'); self.manual_add_button.pack(pady=10); return frame
    def _create_excel_panel(self, parent): frame=ttk.Frame(parent,padding="10"); ttk.Label(frame,text="Selecciona escala, elige Excel y procesa.").pack(pady=5,anchor="w"); ttk.Label(frame,text="Nota: Cálculo depende del ORDEN de filas.").pack(pady=2,anchor="w"); fsf=ttk.Frame(frame); fsf.pack(fill=tk.X,pady=5); ttk.Button(fsf,text="Seleccionar Excel",command=self._select_excel).pack(side=tk.LEFT,padx=5); self.excel_file_label=ttk.Label(fsf,text="Ninguno",foreground="grey",width=40,anchor='w'); self.excel_file_label.pack(side=tk.LEFT,padx=5,fill=tk.X,expand=True); self.excel_process_button=ttk.Button(frame,text="Procesar Excel",command=self._process_excel,state='disabled'); self.excel_process_button.pack(pady=10); return frame
    def _create_json_plot_panel(self, parent): frame=ttk.Frame(parent,padding="10"); ttk.Label(frame,text="Selecciona JSON y clic para generar y guardar gráfico.").pack(pady=5,anchor="w"); fsf=ttk.Frame(frame); fsf.pack(fill=tk.X,pady=5); ttk.Button(fsf,text="Seleccionar JSON",command=self._select_json_plot).pack(side=tk.LEFT,padx=5); self.json_plot_file_label=ttk.Label(fsf,text="Ninguno",foreground="grey",width=40,anchor='w'); self.json_plot_file_label.pack(side=tk.LEFT,padx=5,fill=tk.X,expand=True); self.json_plot_button=ttk.Button(frame,text="Generar y Guardar Gráfico",command=self._generate_and_save_plot,state='disabled'); self.json_plot_button.pack(pady=10); return frame

    # --- Ayuda y Lógica UI ---
    # (Sin cambios funcionales)
    def _log(self, msg): now=datetime.datetime.now().strftime("%H:%M:%S"); self.output_text.config(state='normal'); self.output_text.insert(tk.END,f"[{now}] {msg}\n"); self.output_text.config(state='disabled'); self.output_text.see(tk.END)
    def _clear_log(self): self.output_text.config(state='normal'); self.output_text.delete('1.0', tk.END); self.output_text.config(state='disabled')
    def _update_action_panels(self):
        sel=self.current_action.get();
        for pan in self.action_panels.values():
            if isinstance(pan, tk.Widget) and pan.winfo_ismapped(): pan.pack_forget()
        if sel in self.action_panels:
             panel = self.action_panels[sel]
             if isinstance(panel, tk.Widget): panel.pack(in_=self.action_panel_container,fill=tk.BOTH,expand=True,pady=5)
        if self._has_any_results():
            if not self.results_frame.winfo_ismapped(): self.results_frame.pack(fill=tk.X, pady=5, side=tk.BOTTOM, before=self.output_text.master)
        else:
            if self.results_frame.winfo_ismapped(): self.results_frame.pack_forget()
        self.save_button.config(state='normal' if self._has_any_results() else 'disabled')
        self.clear_button.config(state='normal' if self._has_any_results() else 'disabled')
    def _update_widget_states(self):
        act=self.current_action.get(); sc=self.selected_scale_name.get(); hs=bool(sc); hx=bool(self.selected_excel_file.get()); hj=bool(self.selected_json_file_plot.get()); hr=self._has_any_results()
        is_data_act = act in ['1. Generar Plantilla Excel','2. Ingresar Datos Manualmente','3. Procesar Archivo Excel Subido']
        self.scale_combo.config(state='readonly' if is_data_act else 'disabled')
        if is_data_act and not hs and self.scale_combo.cget('values'): self.selected_scale_name.set(self.scale_combo['values'][0]); hs = True
        if hasattr(self,'manual_add_button'): self.manual_add_button.config(state='normal' if act=='2. Ingresar Datos Manualmente' and hs else 'disabled')
        if hasattr(self,'excel_process_button'): self.excel_process_button.config(state='normal' if act=='3. Procesar Archivo Excel Subido' and hs and hx else 'disabled')
        if hasattr(self,'json_plot_button'): self.json_plot_button.config(state='normal' if act=='4. Generar Gráfico desde JSON' and hj else 'disabled')
        self.save_button.config(state='normal' if hr else 'disabled')
        self.clear_button.config(state='normal' if hr else 'disabled')

    def _on_action_change(self, event=None):
        self._clear_log();
        act = self.current_action.get();
        scale_auto_set = False
        previous_scale = self.selected_scale_name.get()

        if act == 'Por favor, selecciona...':
            self._log("Selecciona una acción.");
            self.scale_combo.config(state='disabled');
            self.selected_scale_name.set("")
        else:
            self._log(f"Acción: {act}")
            is_data_act = act in ['1. Generar Plantilla Excel', '2. Ingresar Datos Manualmente', '3. Procesar Archivo Excel Subido']
            if is_data_act:
                self.scale_combo.config(state='readonly')
                if not previous_scale and self.scale_combo.cget('values'):
                    self.selected_scale_name.set(self.scale_combo['values'][0])
                    scale_auto_set = True
            else:
                self.scale_combo.config(state='disabled')
                self.selected_scale_name.set("")

        self._update_action_panels();
        self.action_panel_container.update_idletasks()

        self.selected_excel_file.set("");
        if hasattr(self, 'excel_file_label'): self.excel_file_label.config(text="Ninguno", foreground="grey")
        self.selected_json_file_plot.set("");
        if hasattr(self, 'json_plot_file_label'): self.json_plot_file_label.config(text="Ninguno", foreground="grey")

        # Actualizar ítems manuales SI la acción es manual y hay escala
        if act == '2. Ingresar Datos Manualmente':
            if self.selected_scale_name.get():
                self._update_manual_input_items()

        self._update_widget_states(); # Actualizar estados después de actualizar items

        # Si se puso escala para OTRA acción, llamar a on_scale_change
        if scale_auto_set and act != '2. Ingresar Datos Manualmente':
             self._on_scale_change()

    def _on_scale_change(self, event=None):
        sc=self.selected_scale_name.get();
        if not sc: return;
        self._log(f"Escala: {sc}"); act=self.current_action.get()
        if act=='2. Ingresar Datos Manualmente':
            self._update_manual_input_items()
        self._update_widget_states()

    def _on_manual_items_frame_configure(self, event):
        bbox = self.mic.bbox("all")
        if bbox: self.mic.configure(scrollregion=bbox)
        self.mic.itemconfig(self.micw, width=event.width)

    def _on_mousewheel(self, event):
        widget = self.master.winfo_containing(event.x_root, event.y_root); is_over = False; curr = widget
        while curr is not None:
            if curr == self.mic: is_over = True; break
            curr = curr.master
        if not is_over: return
        if sys.platform == "win32" or sys.platform == "darwin": delta = -1 * int(event.delta / (120 if sys.platform == "win32" else 1))
        else: # Linux
            if event.num == 4: delta = -1
            elif event.num == 5: delta = 1
            else: delta = 0
        self.mic.yview_scroll(delta, "units")

    # --- Lógica Botones ---
    def _generate_template(self):
        sname = self.selected_scale_name.get();
        if not sname: messagebox.showerror("Error","Selecciona escala."); return
        items = all_scales_data.get(sname);
        if not items: self._log(f"Err Int: No items '{sname}'."); messagebox.showerror("Error",f"No ítems '{sname}'."); return
        sugg = f"plantilla_symlog_{sname.lower().replace(' ', '_')}.xlsx"; fname = filedialog.asksaveasfilename(defaultextension=".xlsx",initialfile=sugg,filetypes=[("Excel","*.xlsx"),("Todos","*.*")])
        if not fname: self._log("Gen plantilla cancelada."); return
        self._log(f"Generando plantilla '{sname}' en '{os.path.basename(fname)}'...")
        try:
            item_col="Item SYMLOG (No modificar)"; p_cols=["P1","P2"]; texts=[i['item'] for i in items]; data={item_col:texts};
            for pc in p_cols: data[pc] = [0]*len(texts)
            df=pd.DataFrame(data);
            with pd.ExcelWriter(fname, engine='openpyxl') as w:
                 df.to_excel(w, index=False, sheet_name='SYMLOG_Data'); ws = w.sheets['SYMLOG_Data']
                 max_l = max(len(str(t)) for t in texts) if texts else 20; ws.column_dimensions[ws.cell(1,1).column_letter].width = max(20, max_l + 5)
                 for i, cn in enumerate(p_cols, 2): ws.column_dimensions[ws.cell(1,i).column_letter].width = max(15, len(cn) + 5)
            self._log(f"Plantilla '{os.path.basename(fname)}' guardada!"); messagebox.showinfo("Éxito",f"Guardada:\n{fname}");
        except ImportError: self._log("ERR: Falta 'openpyxl'."); messagebox.showerror("Error Dep", "Requiere 'openpyxl'.\npip install openpyxl");
        except Exception as e: self._log(f"ERR gen plantilla: {e}\n{traceback.format_exc()}"); messagebox.showerror("Error Crítico",f"Error plantilla:\n{e}")

    def _update_manual_input_items(self):
        for widget in self.mif.winfo_children(): widget.destroy()
        self.manual_item_widgets={}
        self.manual_entry_order = []

        scale_name = self.selected_scale_name.get()
        items_list = all_scales_data.get(scale_name) if scale_name else None

        if not items_list:
            ttk.Label(self.mif, text="Selecciona una escala.").pack(pady=10)
        else:
            self._log(f"Cargando {len(items_list)} ítems manuales ({scale_name})...");
            validate_cmd = (self.master.register(self._validate_manual_score), '%P')
            try:
                for i, item_data in enumerate(items_list):
                    item_frame = ttk.Frame(self.mif); item_frame.pack(fill=tk.X, pady=2, anchor='nw')
                    item_label = ttk.Label(item_frame, text=f"{i+1}. ({item_data['dimension']}) {item_data['item']}", wraplength=550, justify=tk.LEFT, anchor='w'); item_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
                    score_var = tk.StringVar(value='0');
                    score_entry = ttk.Entry(item_frame, textvariable=score_var, width=4, justify=tk.CENTER, validate='key', validatecommand=validate_cmd);
                    score_entry.pack(side=tk.RIGHT, padx=5)
                    self.manual_item_widgets[item_data['item']] = (score_var, score_entry)
                    self.manual_entry_order.append(score_entry)
                    score_entry.bind("<Return>", self._focus_next_entry)
            except Exception as e:
                self._log(f"ERR CRIT creando widgets manuales: {e}\n{traceback.format_exc()}"); messagebox.showerror("Error UI", f"Error creando campos:\n{e}"); self._clear_manual_widgets(); return

        self.master.after_idle(self._configure_manual_scroll)

    def _configure_manual_scroll(self):
        try:
             self.mif.update_idletasks()
             bbox = self.mic.bbox("all")
             if bbox:
                 self.mic.configure(scrollregion=bbox)
                 canvas_width = self.mic.winfo_width()
                 if canvas_width > 1:
                     required_width = bbox[2]
                     self.mic.itemconfig(self.micw, width=max(required_width, canvas_width))
             else:
                 self.mic.configure(scrollregion=(0,0,1,1))
             self.mic.yview_moveto(0)
        except tk.TclError as e:
             self._log(f"Advertencia: Error Tcl config scroll: {e}")

    def _clear_manual_widgets(self):
        for w in self.mif.winfo_children(): w.destroy()
        self.manual_item_widgets = {}
        self.manual_entry_order = []
        ttk.Label(self.mif, text="Error al cargar ítems.").pack()
        self.master.after_idle(self._configure_manual_scroll_after_clear)

    def _configure_manual_scroll_after_clear(self):
        try:
            self.mif.update_idletasks()
            self.mic.configure(scrollregion=(0,0,1,1)); self.mic.yview_moveto(0)
        except tk.TclError as e:
             self._log(f"Advertencia: Error Tcl config scroll (clear): {e}")

    def _validate_manual_score(self, v): return v == "" or (v.isdigit() and 0 <= int(v) <= 4)

    def _focus_next_entry(self, event):
        try:
            current_entry = event.widget
            current_index = self.manual_entry_order.index(current_entry)
            next_index = current_index + 1
            if next_index < len(self.manual_entry_order):
                next_entry = self.manual_entry_order[next_index]
                next_entry.focus_set()
                next_entry.selection_range(0, tk.END)
            else:
                if hasattr(self, 'manual_add_button'):
                    self.manual_add_button.focus_set()
            return "break"
        except ValueError: return None
        except Exception as e: self._log(f"Error moviendo foco: {e}"); return None

    def _add_manual(self):
        pname = self.manual_participant_name_entry.get().strip(); sname = self.selected_scale_name.get()
        if not pname: messagebox.showerror("Requerido","Nombre?"); return
        if not sname: messagebox.showerror("Requerido","Escala?"); return
        if not self.manual_item_widgets: messagebox.showerror("Error Int","No ítems."); return
        self._log(f"Proc manual '{pname}' ({sname})..."); scores = {}; warns = 0
        for item, (svar, _) in self.manual_item_widgets.items():
            v = svar.get().strip(); score = 0
            if v == "": svar.set('0')
            else:
                try:
                    score = int(v)
                    if not (0 <= score <= 4): self._log(f"Warn: '{v}' rango '{item[:30]}...'.->0"); svar.set('0'); score=0; warns+=1
                except ValueError: self._log(f"Warn: '{v}' inv '{item[:30]}...'.->0"); svar.set('0'); score=0; warns+=1
            scores[item] = score
        if warns > 0: self._log(f"{warns} warns (->0).")
        res, ok, msg = calculate_from_manual_scores(pname, sname, scores, scaling_table)
        if msg and msg != "Cálculo manual OK.": self._log(f"Msgs cálc: {msg}")

        if res:
            self.results_by_scale.setdefault(sname, {'manual': [], 'excel': []}); mlist = self.results_by_scale[sname].get('manual', [])
            idx = next((i for i, r in enumerate(mlist) if r.get('name','').strip().lower() == pname.strip().lower()), -1)
            add=True
            if idx != -1:
                if messagebox.askyesno("Confirmar", f"'{pname}' existe.\nSobrescribir?"): self._log(f"** Sobrescribiendo '{pname}' ({sname}). **"); mlist[idx] = res
                else: self._log(f"Cancelado '{pname}'."); add=False
            else: mlist.append(res)

            if add:
                self.results_by_scale[sname]['manual'] = mlist
                self._log(f"'{pname}' añadido/actualizado OK.")
                self._log(f" Punts: UD={res['ud']}, PN={res['pn']}, FB={res['fb']}")
                self.manual_participant_name_entry.delete(0, tk.END); [sv.set('0') for sv, en in self.manual_item_widgets.values()]
                self.manual_participant_name_entry.focus(); messagebox.showinfo("Éxito", f"'{pname}' añadido/actualizado.")
                self._update_action_panels()
                self._update_widget_states()
        else:
            messagebox.showerror("Error Cálculo", f"No se pudo calcular para '{pname}'.\nRevise msgs.")
            self._update_widget_states()

    def _select_excel(self):
        fpath = filedialog.askopenfilename(title="Seleccionar Excel", filetypes=[("Excel","*.xlsx *.xls"),("Todos","*.*")])
        if fpath: self.selected_excel_file.set(fpath); self.excel_file_label.config(text=os.path.basename(fpath), foreground="black"); self._log(f"Excel: {os.path.basename(fpath)}")
        else: self.selected_excel_file.set(""); self.excel_file_label.config(text="Ninguno", foreground="grey"); self._log("Sel Excel cancelada.")
        self._update_widget_states()

    def _process_excel(self):
        sname = self.selected_scale_name.get(); fpath = self.selected_excel_file.get()
        if not sname: messagebox.showerror("Error","Escala?"); return
        if not fpath: messagebox.showerror("Error","Excel?"); return
        self._log(f"Proc '{os.path.basename(fpath)}' para '{sname}'..."); self._log("Nota: Reemplaza Excel previos."); self._log("WARN: Cálculo por ORDEN.")
        items = all_scales_data.get(sname);
        if not items: self._log(f"ERR CRIT: No ítems '{sname}'."); messagebox.showerror("Error Int",f"No ítems '{sname}'."); return;
        n_items = len(items);
        processed_results = []
        warns = 0; n_proc = 0; warn_msgs = [];
        try:
            df = pd.read_excel(fpath, engine='openpyxl');
            if df.empty: self._log("ERR: Excel vacío."); messagebox.showerror("Error Archivo","Excel vacío."); return;
            if df.shape[1] < 2: self._log("ERR: Excel sin cols parts."); messagebox.showerror("Error Formato","Excel >= 2 cols."); return;
            if df.shape[0] != n_items: self._log(f"ERR: Filas({df.shape[0]}) != Ítems({n_items}) '{sname}'."); messagebox.showerror("Error Formato", f"Filas != Ítems.\nEsp:{n_items}\nEnc:{df.shape[0]}"); return;
            p_cols = df.columns[1:]; self._log(f"Detectados {len(p_cols)} participantes.");

            for p_col in p_cols:
                p_name = str(p_col).strip();
                if not p_name: self._log(f"Warn: Omitiendo col nombre vacío: '{p_col}'"); continue;
                n_proc += 1; p_scores = df[p_col];
                res, ws = calculate_participant_scores_by_position(p_name, p_scores, items, scaling_table, sname)
                if ws: warns += len(ws); warn_msgs.extend([f"  [{p_name}] {w}" for w in ws]);
                if res: processed_results.append(res);
                else: self._log(f"No se pudo calcular '{p_name}'. Omitido.")

            self.results_by_scale.setdefault(sname, {'manual': [], 'excel': []})['excel'] = processed_results;

            self._log(f"--- Proc Excel Fin ---"); self._log(f"Procesados: {n_proc}. Válidos: {len(processed_results)}.");
            if warns > 0:
                self._log(f"{warns} warns:"); max_w=15;
                for i, m in enumerate(warn_msgs):
                    if i < max_w: self._log(m)
                    elif i == max_w: self._log(f" ... ({warns - max_w} más)"); break
                messagebox.showwarning("Advertencias", f"Excel procesado.\nRes:{len(processed_results)}.\nWarns:{warns} (ver salida).")
            elif len(processed_results) > 0: messagebox.showinfo("Éxito", f"Excel procesado.\nResultados: {len(processed_results)}.")
            else: messagebox.showinfo("Info", f"Excel procesado, sin resultados válidos.")

        except ImportError as e: lib = 'openpyxl' if 'openpyxl' in str(e) else 'xlrd' if 'xlrd' in str(e) else '?'; self._log(f"ERR: Falta '{lib}'."); messagebox.showerror("Error Dep", f"Requiere '{lib}'.\npip install {lib}")
        except FileNotFoundError: self._log(f"ERR: No encontrado: {fpath}"); messagebox.showerror("Error Archivo", f"No encontrado:\n{fpath}")
        except ValueError as e: self._log(f"ERR: Valor inv Excel: {e}. Verificar 0-4."); self._log(f"Traceback:\n{traceback.format_exc()}"); messagebox.showerror("Error Datos Excel", f"Error leyendo vals:\n{e}\nAsegurar 0-4.")
        except Exception as e: self._log(f"ERR INESPERADO Excel: {e}\n{traceback.format_exc()}"); messagebox.showerror("Error Crítico", f"Error inesperado Excel:\n{e}")
        finally:
            self._update_action_panels()
            self._update_widget_states()

    def _select_json_plot(self):
        fpath = filedialog.askopenfilename(title="Seleccionar JSON", filetypes=[("JSON","*.json"),("Todos","*.*")]);
        if fpath: self.selected_json_file_plot.set(fpath); self.json_plot_file_label.config(text=os.path.basename(fpath), foreground="black"); self._log(f"JSON graf: {os.path.basename(fpath)}");
        else: self.selected_json_file_plot.set(""); self.json_plot_file_label.config(text="Ninguno", foreground="grey"); self._log("Sel JSON cancelada.");
        self._update_widget_states()

    def _generate_and_save_plot(self):
        fname = self.selected_json_file_plot.get();
        if not fname: messagebox.showerror("Error", "Selecciona JSON."); return;
        self._log(f"Generando gráfico desde: '{os.path.basename(fname)}'");
        fig = None; ax = None
        try:
            with open(fname, 'r', encoding='utf-8') as f: data = json.load(f);
            if not isinstance(data, dict): self._log("Err: JSON no dict."); messagebox.showerror("Error Formato", "JSON debe ser dict."); return;
            if not data: self._log("Warn: JSON vacío."); messagebox.showwarning("Vacío", "JSON vacío."); return;
            scales = list(data.keys())
            if not scales: self._log("Err: JSON sin escalas."); messagebox.showerror("Error Formato", "JSON sin escalas."); return;
            scale = scales[0]
            if len(scales) > 1:
                 sel = self._ask_scale_selection(scales)
                 if sel: scale = sel
                 else: self._log("Sel escala cancelada."); return
            p_list = data.get(scale);
            if not isinstance(p_list, list): self._log(f"Err: Datos '{scale}' no lista."); messagebox.showerror("Error Formato", f"Contenido '{scale}' no es lista."); return;
            if not p_list: self._log(f"Warn: No parts en '{scale}'."); messagebox.showwarning("Sin Datos", f"No parts para graficar '{scale}'."); return;
            self._log(f"Generando gráfico '{scale}' ({len(p_list)} parts)...");
            fig, ax = plt.subplots(figsize=(11, 8.5));
            ok = self._draw_symlog_plot(fig, ax, p_list, scale);
            if not ok: self._log(f"No datos válidos dibujados '{scale}'."); messagebox.showwarning("Sin Datos", f"No se pudieron dibujar parts '{scale}'."); return;
            def_fname = f"symlog_plot_{scale.lower().replace(' ', '_')}.png";
            fpath = filedialog.asksaveasfilename(title="Guardar Gráfico", initialfile=def_fname, defaultextension=".png", filetypes=[("PNG","*.png"),("PDF","*.pdf"),("SVG","*.svg"),("JPEG","*.jpg"),("Todos","*.*")]);
            if not fpath: self._log("Guardado gráfico cancelado."); return;
            self._log(f"Guardando gráfico '{os.path.basename(fpath)}'..."); fig.savefig(fpath, dpi=300, bbox_inches='tight');
            self._log("¡Gráfico guardado!"); messagebox.showinfo("Éxito", f"Gráfico guardado:\n{fpath}");
        except FileNotFoundError: self._log(f"ERR: No encontrado: {fname}"); messagebox.showerror("Error Archivo", f"No encontrado:\n{fname}");
        except json.JSONDecodeError as e: self._log(f"ERR JSON inv:{e}"); messagebox.showerror("Error Formato JSON", f"JSON inválido:\n{e}");
        except IOError as e: self._log(f"ERR E/S JSON:{e}"); messagebox.showerror("Error Archivo", f"Err leer:\n{e}");
        except Exception as e: self._log(f"ERR INESPERADO G/G gráfico: {e}\n{traceback.format_exc()}"); messagebox.showerror("Error Crítico", f"Error:\n{e}")
        finally:
            if fig is not None: plt.close(fig)

    def _ask_scale_selection(self, scales):
        dialog = tk.Toplevel(self.master); dialog.title("Seleccionar Escala"); dialog.geometry("300x150"); dialog.resizable(False, False); dialog.transient(self.master); dialog.grab_set();
        tk.Label(dialog, text="Selecciona la escala a graficar:").pack(pady=(10, 5))
        sel_var = tk.StringVar(dialog); sel_var.set(scales[0]);
        combo = ttk.Combobox(dialog, textvariable=sel_var, values=scales, state="readonly"); combo.pack(pady=5, padx=20, fill=tk.X)
        res = None
        def ok(): nonlocal res; res = sel_var.get(); dialog.destroy()
        def cancel(): dialog.destroy()
        btn_frame = ttk.Frame(dialog); btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Aceptar", command=ok, style='Accent.TButton').pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="Cancelar", command=cancel).pack(side=tk.LEFT, padx=10)
        try: style = ttk.Style(); style.configure('Accent.TButton', foreground='white', background='#0078D4')
        except tk.TclError: pass
        dialog.wait_window(); return res

    # *** MÉTODO CORREGIDO CON LEYENDA MANUAL MÁS COMPACTA Y POSICIÓN FIJA ***
    def _draw_symlog_plot(self, fig, ax, participants_data, scale_name="General"):
        ax.set_title(f"Diagrama de Campo SYMLOG ({scale_name})", fontsize=14, pad=20);
        limit = 20; ax.set_xlim(-limit, limit); ax.set_ylim(-limit, limit);
        ax.set_aspect('equal', adjustable='box'); ax.grid(True, linestyle='--', alpha=0.6);
        ax.spines['left'].set_position('zero'); ax.spines['right'].set_color('none');
        ax.spines['bottom'].set_position('zero'); ax.spines['top'].set_color('none');
        ax.xaxis.set_ticks_position('bottom'); ax.yaxis.set_ticks_position('left');
        tick_step = 4; ax.set_xticks(np.arange(-limit + tick_step, limit, tick_step));
        ax.set_yticks(np.arange(-limit + tick_step, limit, tick_step));
        ax.tick_params(axis='both', which='major', labelsize=8)
        l_off = limit * 0.85; q_props = dict(ha='center', va='center', fontsize=9, color='darkgrey', style='italic');
        ax.text(l_off, l_off, "PF", **q_props); ax.text(-l_off, l_off, "NF", **q_props); ax.text(l_off, -l_off, "PB", **q_props); ax.text(-l_off, -l_off, "NB", **q_props);
        ax_l_off = limit * 0.98; ax_props = dict(ha='center', va='center', fontsize=10, color='black', weight='bold');
        ax.text(ax_l_off, 0, "P", **ax_props); ax.text(-ax_l_off, 0, "N", **ax_props); ax.text(0, ax_l_off, "F", **ax_props); ax.text(0, -ax_l_off, "B", **ax_props);
        # U y D eliminadas

        n_parts = len(participants_data);
        if n_parts <= 10: cmap = plt.get_cmap('tab10')
        elif n_parts <= 20: cmap = plt.get_cmap('tab20')
        else: cmap = plt.get_cmap('viridis')
        if n_parts <= 20 and isinstance(cmap, matplotlib.colors.ListedColormap): colors = list(cmap.colors)
        else: colors = [cmap(i / max(1,n_parts)) for i in range(n_parts)]
        plotted = []; c_idx = 0; has_data = False;
        size_divisor = PLOT_SIZE_DIVISOR

        for pdat in participants_data:
             if (isinstance(pdat, dict) and all(k in pdat for k in ['name','pn','fb','ud']) and all(isinstance(pdat.get(k), (int, float)) for k in ['pn','fb','ud'])):
                 pn, fb, ud = pdat['pn'], pdat['fb'], pdat['ud']; name = str(pdat.get('name', f'P_{c_idx+1}'))
                 clr = colors[c_idx % len(colors)];
                 size_raw = calculate_marker_size(ud); size_disp = max(10, size_raw / size_divisor)
                 props = dict(s=size_disp, label=name, alpha=0.8, edgecolors='black', linewidth=0.5, zorder=5, c=[clr])
                 ax.scatter(pn, fb, **props);
                 try:
                     x_off, y_off = (ax.get_xlim()[1]-ax.get_xlim()[0])*0.01, (ax.get_ylim()[1]-ax.get_ylim()[0])*0.01
                     ax.text(pn + x_off, fb + y_off, name, fontsize=7, zorder=6, bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.6, ec='none'))
                 except Exception as e: self._log(f"Warn etiqueta '{name}': {e}");
                 plotted.append({'name': name, 'color': clr}); c_idx += 1; has_data = True;
             else:
                 missing = [k for k in ['name','pn','fb','ud'] if k not in pdat]; non_num = [k for k in ['pn','fb','ud'] if k in pdat and not isinstance(pdat.get(k),(int,float))]
                 reason = [];
                 if not isinstance(pdat, dict): reason.append("no dict")
                 if missing: reason.append(f"faltan:{','.join(missing)}")
                 if non_num: reason.append(f"no num:{','.join(non_num)}")
                 self._log(f"Warn: Omitiendo part inv ({'; '.join(reason)}): {pdat}")

        if has_data:
             max_leg = 15
             if len(plotted) <= max_leg:
                 handles = [plt.scatter([], [], s=60, color=p['color'], edgecolors='black', alpha=0.75, label=p['name']) for p in plotted]
                 try:
                     leg1 = ax.legend(handles=handles, title="Participantes", bbox_to_anchor=(1.02, 1.0), loc='upper left', borderaxespad=0.5, fontsize='small', title_fontsize='small')
                 except Exception as e: self._log(f"Warn leg parts: {e}")
             else: self._log(f"Nota: {len(plotted)} parts, omitiendo leyenda detallada.")

             # --- Leyenda de Referencia MANUAL (con posiciones Y absolutas) ---
             ref_ud_scores = [18, 0, -18]
             ref_labels = [f"U/D = {s}" for s in ref_ud_scores]
             ref_sizes = [max(10, calculate_marker_size(s) / size_divisor) for s in ref_ud_scores]

             ref_x = limit + 3.5 # Posición X fija a la derecha

             # *** Definir posiciones Y absolutas para cada elemento ***
             # Ajusta estos valores finamente para que coincidan con tu referencia
             title_y_pos = -1        # Y del título
             circle_y_18 = -5         # Y del círculo U/D=18
             text_y_18   = -8.5         # Y del texto U/D=18 (debajo del círculo)
             circle_y_0  = -12        # Y del círculo U/D=0 (debajo del texto anterior)
             text_y_0    = -14.5      # Y del texto U/D=0
             circle_y_m18 = -16       # Y del círculo U/D=-18
             text_y_m18   = -17       # Y del texto U/D=-18

             ref_y_circles = [circle_y_18, circle_y_0, circle_y_m18]
             ref_y_texts   = [text_y_18, text_y_0, text_y_m18]
             # **********************************************************

             # Título manual
             ax.text(ref_x, title_y_pos, "Ref. Tamaño (U/D):",
                     ha='center', va='center', fontsize='small', weight='bold')

             # Dibujar círculos y texto en posiciones absolutas
             for i, score in enumerate(ref_ud_scores):
                 y_circle = ref_y_circles[i]
                 y_text = ref_y_texts[i]
                 size = ref_sizes[i]
                 label = ref_labels[i]

                 ax.scatter([ref_x], [y_circle], s=size, c='grey', alpha=0.6, edgecolors='black', zorder=4, clip_on=False)
                 ax.text(ref_x, y_text, label, ha='center', va='top', fontsize='small', zorder=5)

             # Ajustar márgenes (right=0.78 probablemente esté bien)
             fig.subplots_adjust(left=0.08, bottom=0.08, right=0.78, top=0.90)

        return has_data
    # *****************************************************************

    def _save_results(self):
        sugg = self.results_filename.get();
        if not self._has_any_results(): self._log("No resultados."); messagebox.showwarning("Sin Datos", "No resultados."); return;
        fname = filedialog.asksaveasfilename(defaultextension=".json", initialfile=sugg, filetypes=[("JSON","*.json"),("Todos","*.*")]);
        if not fname: self._log("Guardado cancelado."); return;
        data = {}; n_total = 0; scales_sum = [];
        for sname in list(self.results_by_scale.keys()):
            sdata = self.results_by_scale[sname]; mlist = sdata.get('manual', []); elist = sdata.get('excel', []);
            combined = mlist + elist;
            if combined:
                 combined.sort(key=lambda x: x.get('name', '').lower()); data[sname] = combined;
                 count = len(combined); n_total += count; scales_sum.append(f"{sname}({len(mlist)}m,{len(elist)}x)")
        if not data: self._log("Err: No datos para guardar."); messagebox.showerror("Error", "No datos."); return
        self._log(f"Guardando {n_total} res en '{os.path.basename(fname)}'. Escalas: {'; '.join(scales_sum) or 'Ninguna'}");
        try:
            with open(fname, 'w', encoding='utf-8') as f: json.dump(data, f, indent=4, ensure_ascii=False);
            self._log(f"¡Resultados guardados '{os.path.basename(fname)}'!"); messagebox.showinfo("Éxito", f"Guardado:\n{fname}");
            self.results_filename.set(os.path.basename(fname));
        except IOError as e: self._log(f"Err E/S guardando: {e}"); messagebox.showerror("Error Guardado", f"No escribir:\n{e}");
        except Exception as e: self._log(f"Err inesperado guardando: {e}\n{traceback.format_exc()}"); messagebox.showerror("Error Crítico", f"Error guardar:\n{e}")

    def _clear_all(self):
        if not self._has_any_results(): messagebox.showinfo("Info", "No resultados para limpiar."); return
        if messagebox.askyesno("Confirmar", "¿Borrar TODOS los resultados?"):
             self.results_by_scale = {}; self._clear_log(); self._log("Resultados eliminados.");
             if self.current_action.get() == '2. Ingresar Datos Manualmente':
                 if hasattr(self, 'manual_participant_name_entry'): self.manual_participant_name_entry.delete(0, tk.END)
                 if hasattr(self, 'manual_item_widgets'): [v.set('0') for v, e in self.manual_item_widgets.values()]
                 self.manual_entry_order = []
                 self._log("Campos manuales reiniciados.")
             self.selected_excel_file.set("");
             if hasattr(self, 'excel_file_label'): self.excel_file_label.config(text="Ninguno", foreground="grey")
             self.selected_json_file_plot.set("");
             if hasattr(self, 'json_plot_file_label'): self.json_plot_file_label.config(text="Ninguno", foreground="grey")
             self._update_action_panels();
             self._update_widget_states();
             messagebox.showinfo("Limpieza Completa", "Resultados eliminados.")
        else: self._log("Limpieza cancelada.")

    def _has_any_results(self):
         return any(d.get('manual') or d.get('excel') for d in self.results_by_scale.values())

# --- Punto de Entrada Principal ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SymlogApp(root)
    root.mainloop()