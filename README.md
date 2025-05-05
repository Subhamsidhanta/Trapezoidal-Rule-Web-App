
# 📐 Trapezoidal Rule Web App

A simple and elegant web application built using **Flask**, **HTML**, **CSS**, and **JavaScript** to solve definite integrals using the **Trapezoidal Rule**.

Supports:
- 📊 Table-based inputs (Type 1)
- 🧮 Function-based inputs (Type 2)

---

## 🔗 Live Preview

*(If hosted, add the link here)*

---

## 🖥️ Features

- ✅ Compute integrals using Trapezoidal Rule
- ✅ Choose between function or tabulated data
- ✅ Clean, professional UI
- ✅ Error handling for invalid inputs
- ✅ Mobile-friendly design

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Subhamsidhanta/trapezoidal-rule-webapp.git
cd trapezoidal-rule-webapp
```

### 2. Install Dependencies

```bash
pip install flask numpy
```

### 3. Run the App

```bash
python app.py
```

### 4. Open in Browser

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📂 Project Structure

```
trapezoidal-rule-webapp/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## ✏️ Usage

### Type 1 (Table Input)

- Input X and Y values as comma-separated lists.
- Ensure equal number of X and Y points.

### Type 2 (Function Input)

- Input the function using Python syntax.
- Use `np` for math functions: `np.sin(x)`, `np.log(x)`, etc.
- Example: `x + 1/x`, `np.sin(x)`, `x**2 + 2*x + 1`

---

## ⚠️ Notes

- Do **not** include `dx` in the function field.
- Avoid invalid math (like division by zero).
- Make sure number of intervals is a positive integer.

---

## 📜 License

This project is open-source and free to use.
