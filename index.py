import datetime
import re

# Fonction pour lire le fichier readme
def read_readme_file():
    with open('./readme', 'r') as file:
        return file.read()

# Fonction pour mettre à jour l'identificateur dans le readme
def update_identifier(identifier, replace_text, readme_row):
    identifier_index = find_identifier_index(readme_row, identifier)
    if identifier_index == -1:
        return
    readme_row[identifier_index] = readme_row[identifier_index].replace(f'<#{identifier}>', replace_text)

# Fonction pour trouver l'index de l'identificateur dans les lignes du readme
def find_identifier_index(rows, identifier):
    for i, r in enumerate(rows):
        if re.search(f'<#{identifier}>', r, re.IGNORECASE):
            return i
    return -1

# Fonction pour obtenir la signature de Bicko
def get_bicko_signing():
    mood_by_day = {
        1: 'hate',
        2: 'wickedness',
        3: 'pleasure',
        4: 'wickedness',
        5: 'cruelty',
        6: 'horror',
        7: 'love',
    }
    mood = mood_by_day[today.weekday() + 1]
    return f'🤖 This README.md is updated with {mood}, by Bicko ❤️'

# Fonction pour obtenir la date d'aujourd'hui
def get_today_date():
    return today.strftime('%a %b %d %Y')

# Fonction pour obtenir la prochaine année
def get_next_year():
    today = datetime.today()
    next_year = today.year + 1
    return next_year

# Fonction pour obtenir la description de soi-même
def get_myself():
    return 'penguin 🐧' if today.day % 2 == 0 else 'penguin bear 🐧🐻'

# Fonction pour obtenir la phrase avant le nouvel an
def get_dbnw_sentence():
    next_year = today.year + 1
    next_year_date = datetime.date(next_year, 1, 1)
    time_until_new_year = next_year_date - today
    day_until_new_year = time_until_new_year.days
    return f'**{day_until_new_year} day before {next_year} ⏱**'

# Fonction pour écrire dans le fichier README.md
def update_readme_file(text):
    with open('./README.md', 'w') as file:
        file.write(text)

# Fonction principale
def main():
    global today
    today = datetime.date.today()
    readme = read_readme_file()
    readme_row = readme.split('\n')

    identifier_to_update = {
        'day_before_new_years': get_dbnw_sentence(),
        'today_date': get_today_date(),
        'bicko_signing': get_bicko_signing(),
        'next_year': get_next_year(),
    }

    for key, value in identifier_to_update.items():
        update_identifier(key, value, readme_row)

    updated_readme = '\n'.join(readme_row)
    print(updated_readme)
    update_readme_file(updated_readme)

if __name__ == "__main__":
    main()
