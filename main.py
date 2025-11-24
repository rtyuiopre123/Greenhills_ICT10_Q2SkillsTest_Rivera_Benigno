from pyscript import document

clubs = {
    "Chess Club": {
        "Description": "A club for chess players of all skill levels.",
        "Meeting Time": "Wednesday 3:30 - 5:00 PM",
        "Location": "Room 405",
        "Moderator": "Mr. De Guzman",
        "Members": 20
    },
    "Music Club": {
        "Description": "A club for students who enjoy performing and creating music.",
        "Meeting Time": "Friday 4:00 - 5:30 PM",
        "Location": "Music Room",
        "Moderator": "Mr. Ngo",
        "Members": 15
    },
    "Science Club": {
        "Description": "A club for science experiments and discovery.",
        "Meeting Time": "Tuesday 3:00 - 4:30 PM",
        "Location": "Lab 2",
        "Moderator": "Mr. Mergal",
        "Members": 18
    }
}

def show_info(e):
    selected = document.getElementById("clubSelect").value
    club = clubs[selected]

    text = f"""
    <h3 class='club-title'>{selected}</h3>
    <p><strong>Description:</strong> {club["Description"]}</p>
    <p><strong>Meeting Time:</strong> {club["Meeting Time"]}</p>
    <p><strong>Location:</strong> {club["Location"]}</p>
    <p><strong>Moderator:</strong> {club["Moderator"]}</p>
    <p><strong>Number of Members:</strong> {club["Members"]}</p>
    """

    document.getElementById("output").innerHTML = text
