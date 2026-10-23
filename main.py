from html import escape

from pyscript import document

# one set per grade level, sets can't have duplicates so we're good
grade_7 = {
    "Ramon Magsaysay", "Ryan Garcia", "Donya Victorina", "Dominic Torreto"
}
grade_8 = {"Peter Parker", "Octavius", "Wolverine"}
grade_9 = {"Yukio", "Wade Wilson", "Finnick"}
grade_10 = {"Kat Stratford", "Patrick Verona", "Lucas Watanabe"}

# union operator (|) mashes all four grades into one master set
members = grade_7 | grade_8 | grade_9 | grade_10

# index 0 = brand new member, index 1 = already in the club
messages = ["Added to the club!", "That person is already in the club."]


def build_output(message):
    """Put together the html for the results box."""
    # sorted() turns the set into a list so it shows up in alphabetical order
    names = "</li><li>".join(sorted(members))
    total = len(members)  # len() on a set = how many members we have

    return (
        f"<p class='fs-5 fw-bold mb-2'>{message}</p>"
        f"<p class='mb-2'>Total members: <strong>{total}</strong></p>"
        "<p class='mb-1'>Full member list:</p>"
        f"<ul class='mb-0'><li>{names}</li></ul>"
    )


def result_checker(event):
    """Runs when the submit button gets clicked."""
    global members  # need this since we're updating the master set

    # grab whatever got typed in the two boxes
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    # split() + join() cleans up extra spaces, title() fixes the capitals
    # escape() keeps weird characters from messing up the page
    full_name = escape(" ".join(f"{first} {last}".split()).title())

    # put the new person in their own set so we can use set operators on it
    new_member = {full_name}

    # & checks if they're already in there (overlap between the two sets)
    # len() of that overlap is 0 or 1, which works as the index for messages
    message = messages[len(members & new_member)]

    # - {""} throws out blank names, |= adds the new member to the master set
    members |= new_member - {""}

    # show everything in the output box
    document.getElementById("output").innerHTML = build_output(message)


# show the starting list as soon as the page loads
document.getElementById("output").innerHTML = build_output("Current club roster")
