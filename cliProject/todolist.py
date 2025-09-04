import argparse
import json
from datetime import datetime

# Initialisation du parser principal
parser = argparse.ArgumentParser(
    prog="MyToDoList",
    description="Programme CLI qui permet de gérer une liste de tâches (add, update, remove, list)."
)


def parsers_initialisation():
    """
    Initialise et configure les sous-commandes disponibles (add, remove, update, list).
    Retourne les arguments parsés de la ligne de commande.
    """
    subparsers = parser.add_subparsers(
        dest="method",
        help="Action à effectuer (add, remove, update, list).",
        required=False
    )

    # Commande: add
    parser_add = subparsers.add_parser("add", help="Ajouter une tâche")
    parser_add.add_argument("description", help="Brève description de la tâche")

    # Commande: remove
    parser_rem = subparsers.add_parser("remove", help="Supprimer une tâche")
    parser_rem.add_argument("id", help="ID de la tâche à supprimer")

    # Commande: update
    parser_upd = subparsers.add_parser("update", help="Mettre à jour une tâche")
    parser_upd.add_argument("id", help="ID de la tâche à mettre à jour")
    parser_upd.add_argument("--description", help="Nouvelle description de la tâche")
    parser_upd.add_argument("--status", help="Nouveau statut de la tâche",
                            choices=["todo", "done", "in-progress"])

    # Commande: list
    parser_list = subparsers.add_parser("list", help="Lister les tâches")
    parser_list.add_argument("--status", help="Filtrer par statut",
                             choices=["todo", "done", "in-progress"])

    return parser.parse_args()


def load_tasks():
    """
    Charge les tâches depuis le fichier JSON.
    Retourne une liste de tâches (vide si le fichier n'existe pas).
    """
    try:
        with open("todolist.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """
    Sauvegarde la liste des tâches dans le fichier JSON.
    """
    with open("todolist.json", "w") as f:
        json.dump(tasks, f, indent=4)


def addTask(args):
    """
    Ajoute une nouvelle tâche à la liste.
    """
    description = args.description
    data = load_tasks()

    # Génération d'un ID unique basé sur le timestamp (µs)
    task_id = int(datetime.now().timestamp() * 1_000_000)

    newTask = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.strftime(datetime.now(), "%d-%m-%Y, %H:%M:%S"),
        "updatedAt": datetime.strftime(datetime.now(), "%d-%m-%Y, %H:%M:%S")
    }

    data.append(newTask)
    save_tasks(data)
    print(f"Task added (ID : {task_id})")


def updateTask(args):
    """
    Met à jour une tâche existante (description et/ou statut).
    """
    task_id = int(args.id)
    data = load_tasks()

    # Recherche de la tâche cible
    cible = next((i for i in data if i["id"] == task_id), None)

    if cible:
        description = args.description if args.description else cible["description"]
        status = args.status if args.status else cible["status"]

        updatedTask = {
            "id": task_id,
            "description": description,
            "status": status,
            "createdAt": cible["createdAt"],
            "updatedAt": datetime.strftime(datetime.now(), "%d-%m-%Y, %H:%M:%S")
        }

        data[data.index(cible)] = updatedTask
        save_tasks(data)
        print(f"Task updated (ID: {cible['id']})")
    else:
        print("Task not found")


def removeTask(args):
    """
    Supprime une tâche de la liste en fonction de son ID.
    """
    task_id = int(args.id)
    data = load_tasks()

    cible = next((i for i in data if i["id"] == task_id), None)

    if cible:
        data.remove(cible)
        save_tasks(data)
        print(f"Task deleted (ID: {cible['id']})")
    else:
        print("Task not found")


def listTask(args):
    """
    Liste les tâches en fonction du statut demandé (ou toutes si non spécifié).
    """
    status = args.status if args.status else "all"
    data = load_tasks()

    # Filtrage par statut
    if status != "all":
        data = [i for i in data if i["status"] == status]

    if not data:
        print("📭 No tasks found.")
        return

    for task in data:
        print(f"ID : {task['id']}")
        print(f"Description : {task['description']}")
        print(f"Status : {task['status']}")
        print(f"Created At : {task['createdAt']}")
        print(f"Updated At : {task['updatedAt']}")
        print("-" * 40)


def updatefile():
    """
    Gère la logique principale en fonction de la méthode appelée par l'utilisateur.
    """
    args = parsers_initialisation()

    if not args.method:
        print("Aucune méthode choisie.\n")
        parser.print_help()
        return

    match args.method:
        case "add":
            addTask(args)
        case "remove":
            removeTask(args)
        case "update":
            updateTask(args)
        case "list":
            listTask(args)


if __name__ == "__main__":
    updatefile()
