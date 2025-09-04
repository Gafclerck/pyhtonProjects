````markdown
# 📝 MyToDoList (CLI)

Un gestionnaire de tâches simple en **ligne de commande** écrit en Python.  
Permet d'**ajouter, mettre à jour, supprimer et lister** vos tâches avec persistance en JSON.

---

## 🚀 Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Gafclerck/pyhtonProjects.git
   cd PyhtonProjects/cliProject
````

2. Exécuter le programme avec Python (≥ 3.10 recommandé) :

   ```bash
   python todolist.py.py --help
   ```

---

## ⚡ Utilisation

### ➕ Ajouter une tâche

```bash
python todolist.py add "Acheter du pain"
```

### ✏️ Mettre à jour une tâche

```bash
python todolist.py update 1693769200000 --description "Acheter du pain complet" --status done
```

### 🗑️ Supprimer une tâche

```bash
python todolist.py remove 1693769200000
```

### 📋 Lister toutes les tâches

```bash
python todolist.py list
```

### 📂 Lister uniquement les tâches en cours

```bash
python todolist.py list --status in-progress
```

---

## 📦 Persistance des données

Les tâches sont stockées dans un fichier `todolist.json` au format suivant :

```json
[
    {
        "id": 1693769200000,
        "description": "Acheter du pain",
        "status": "todo",
        "createdAt": "03-09-2025, 18:30:12",
        "updatedAt": "03-09-2025, 18:30:12"
    }
]
```

---

## 👨‍💻 Auteur

Développé par **Amadou Abdoul-Gafar**
Étudiant en Informatique – Génie logiciel, réseaux & systèmes

```

