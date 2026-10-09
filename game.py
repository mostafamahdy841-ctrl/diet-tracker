import tkinter as tk
from tkinter import messagebox

# 1. إنشاء النافذة الرئيسية للبرنامج
root = tk.Tk()
root.title("برنامج تتبع الدايت والتمارين 🏋️‍♂️🍎")
root.geometry("400x600") # كبرنا الطول شوية عشان الخانات الجديدة
root.configure(bg="#f0f0f0")

# متغيرات لتخزين البيانات (تبدأ بقيم افتراضية)
calories_limit = 2000
total_eaten_calories = 0

# 2. الدوال (Functions)

# دالة لتحديث الهدف اليومي للسعرات
def set_calories_limit():
    global calories_limit
    user_limit = limit_entry.get()
    
    if user_limit == "":
        messagebox.showwarning("خطأ", "اكتب رقم السعرات اللي عاوز تحدده!")
        return
    
    try:
        calories_limit = int(user_limit)
        # تحديث نص العداد تحت فوراً بالهدف الجديد
        status_label.config(text=f"إجمالي السعرات المستهلكة: {total_eaten_calories} / {calories_limit} سعر")
        messagebox.showinfo("تم", f"تم تغيير هدفك اليومي لـ {calories_limit} سعر بنجاح! 🎯")
        limit_entry.delete(0, tk.END) # مسح الخانة بعد الضبط
        
    except ValueError:
        messagebox.showerror("خطأ", "دخل السعرات بالأرقام بس يا بطل!")

# دالة إضافة الوجبة
def add_meal():
    global total_eaten_calories
    meal_name = meal_entry.get()
    meal_cal = cal_entry.get()
    
    if meal_name == "" or meal_cal == "":
        messagebox.showwarning("خطأ", "يا بطل لازم تكتب اسم الوجبة والسعرات!")
        return
    
    try:
        cal = int(meal_cal)
        total_eaten_calories += cal
        
        meals_listbox.insert(tk.END, f"• {meal_name}: {cal} سعر")
        status_label.config(text=f"إجمالي السعرات المستهلكة: {total_eaten_calories} / {calories_limit} سعر")
        
        meal_entry.delete(0, tk.END)
        cal_entry.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("خطأ", "دخل السعرات بالأرقام بس!")

# 3. تصميم واجهة المستخدم (Widgets)

title_label = tk.Label(root, text="متابعة الدايت اليومي", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# --- القسم الجديد: تحديد السعرات بمزاجك ---
frame_limit = tk.LabelFrame(root, text=" حدد هدفك اليومي من السعرات ", bg="#f0f0f0", fg="#00bcd4", font=("bold", 10))
frame_limit.pack(pady=10, padx=10, fill="x")

limit_entry = tk.Entry(frame_limit, width=15, justify="center")
limit_entry.pack(side="right", padx=10, pady=10)

set_limit_btn = tk.Button(frame_limit, text="تعديل الهدف 🎯", command=set_calories_limit, bg="#00bcd4", fg="white")
set_limit_btn.pack(side="left", padx=10, pady=10)
# ----------------------------------------

# خانة إدخال اسم الوجبة
tk.Label(root, text="اسم الوجبة:", bg="#f0f0f0").pack()
meal_entry = tk.Entry(root, width=30, justify="right")
meal_entry.pack(pady=5)

# خانة إدخال السعرات
tk.Label(root, text="السعرات الحرارية للوجبة:", bg="#f0f0f0").pack()
cal_entry = tk.Entry(root, width=30, justify="right")
cal_entry.pack(pady=5)

# زر إضافة الوجبة
add_btn = tk.Button(root, text="إضافة الوجبة 🍽️", command=add_meal, bg="#4CAF50", fg="white", width=20)
add_btn.pack(pady=10)

# قائمة لعرض الوجبات المضافة
tk.Label(root, text="وجبات اليوم:", bg="#f0f0f0", font=("bold", 11)).pack()
meals_listbox = tk.Listbox(root, width=35, height=6, justify="right")
meals_listbox.pack(pady=5)

# نص يوضح إجمالي السعرات
status_label = tk.Label(root, text=f"إجمالي السعرات المستهلكة: {total_eaten_calories} / {calories_limit} سعر", font=("bold", 12), fg="#ff5722", bg="#f0f0f0")
status_label.pack(pady=15)

root.mainloop()
