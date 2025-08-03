# Decission_Tree-
#  Mushroom Edibility Classifier (Decision Tree + Flask)

This project predicts whether a mushroom is **edible** or **poisonous** based on categorical features like cap shape, odor, gill color, etc., using a **Decision Tree Classifier** wrapped in a **Flask web application**.

---

##  Dataset

- Source: [UCI Mushroom Dataset](https://archive.ics.uci.edu/ml/datasets/Mushroom)
- Filename: `mushroom_data.csv` or `agaricus-lepiota.data`
- Target:  
  - `e` → Edible  
  - `p` → Poisonous

---

##  Features Used in This App

- `cap-shape`
- `cap-surface`
- `cap-color`
- `bruises`
- `odor`

> All features are categorical and encoded using `LabelEncoder`.

---

##  Model

- Model: `DecisionTreeClassifier` from `scikit-learn`
- Preprocessing: Label encoding for categorical features
- Serialized with: `joblib`

# Files generated:
- `mushroom_model.pkl` → Contains the trained model and encoders.

---

##  Web Interface (Flask)

### Structure:
```
mushroom_classifier/
├── app.py
├── mushroom_model.pkl
├── templates/
│ └── result.html
├── static/
│ └── style.css
```


### To Run:

```bash
pip install flask pandas scikit-learn
python app.py]
```
Open in your browser:
http://127.0.0.1:5000/

# What It Does:
```
Takes mushroom characteristics as input.

Predicts and displays: "Edible " or "Poisonous "
```
 # Sample Input Example
 ```
makefile
Copy code
cap-shape: x
cap-surface: s
cap-color: n
bruises: t
odor: a
```
# ScreenShots
![alt text](<Screenshot 2025-08-03 104716.png>)
![alt text](<Screenshot 2025-08-03 104738.png>)
![alt text](<Screenshot 2025-08-03 104905.png>)