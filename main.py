from pyscript import document
 
non_metals = {
    "H": {"name": "Hydrogen", "number": 1, "mass": 1.008},
    "He": {"name": "Helium", "number": 2, "mass": 4.0026},
    "C": {"name": "Carbon", "number": 6, "mass": 12.011},
    "N": {"name": "Nitrogen", "number": 7, "mass": 14.007},
    "O": {"name": "Oxygen", "number": 8, "mass": 15.999},
    "F": {"name": "Fluorine", "number": 9, "mass": 18.998},
    "Ne": {"name": "Neon", "number": 10, "mass": 20.180},
    "P": {"name": "Phosphorus", "number": 15, "mass": 30.974},
    "S": {"name": "Sulfur", "number": 16, "mass": 32.06},
    "Cl": {"name": "Chlorine", "number": 17, "mass": 35.45},
    "Ar": {"name": "Argon", "number": 18, "mass": 39.948},
    "Se": {"name": "Selenium", "number": 34, "mass": 78.971},
    "Br": {"name": "Bromine", "number": 35, "mass": 79.904},
    "Kr": {"name": "Krypton", "number": 36, "mass": 83.798},
    "I": {"name": "Iodine", "number": 53, "mass": 126.90},
    "Xe": {"name": "Xenon", "number": 54, "mass": 131.29},
    "Rn": {"name": "Radon", "number": 86, "mass": 222},
}
 
 
def make_row(label, value):
    """Build one label/value row for the result box."""
    return (
        f'<div class="row"><span class="label">{label}</span>'
        f"<span>{value}</span></div>"
    )
 
 
def check_details(event):
    """Look up the entered symbol and display the element details."""
    symbol = document.querySelector("#symbol").value.strip().capitalize()
    result_box = document.querySelector("#result")
 
    if symbol in non_metals:
        element = non_metals[symbol]
        result_box.className = "result"
        result_box.innerHTML = (
            make_row("Symbol", symbol)
            + make_row("Element", element["name"])
            + make_row("Atomic Number", element["number"])
            + make_row("Atomic Mass", element["mass"])
        )
    else:

        result_box.className = "result error"
        result_box.textContent = (
            "The element does not exist in the non-metals list."
        )
 