import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully.")

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (row['first_name'], row['phone']))

    conn.commit()
    cur.close()
    conn.close()
    print("Contacts imported from CSV successfully.")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO phonebook (first_name, phone)
        VALUES (%s, %s);
    """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added successfully.")

def show_all_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id;")
    rows = cur.fetchall()

    print("\n--- ALL CONTACTS ---")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_by_name():
    name = input("Enter name to search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM phonebook
        WHERE first_name ILIKE %s;
    """, ('%' + name + '%',))

    rows = cur.fetchall()

    print("\n--- SEARCH RESULTS ---")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_by_phone_prefix():
    prefix = input("Enter phone prefix: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM phonebook
        WHERE phone LIKE %s;
    """, (prefix + '%',))

    rows = cur.fetchall()

    print("\n--- SEARCH RESULTS ---")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_contact():
    old_name = input("Enter current name of contact to update: ")
    new_name = input("Enter new name (leave blank if no change): ")
    new_phone = input("Enter new phone (leave blank if no change): ")

    conn = connect()
    cur = conn.cursor()

    if new_name and new_phone:
        cur.execute("""
            UPDATE phonebook
            SET first_name = %s, phone = %s
            WHERE first_name = %s;
        """, (new_name, new_phone, old_name))
    elif new_name:
        cur.execute("""
            UPDATE phonebook
            SET first_name = %s
            WHERE first_name = %s;
        """, (new_name, old_name))
    elif new_phone:
        cur.execute("""
            UPDATE phonebook
            SET phone = %s
            WHERE first_name = %s;
        """, (new_phone, old_name))
    else:
        print("Nothing to update.")

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated successfully.")

def delete_contact():
    choice = input("Delete by (1) name or (2) phone? ")

    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
    elif choice == '2':
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
    else:
        print("Invalid choice.")

    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted successfully.")


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert from CSV")
        print("3. Insert from console")
        print("4. Show all contacts")
        print("5. Search by name")
        print("6. Search by phone prefix")
        print("7. Update contact")
        print("8. Delete contact")
        print("9. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            create_table()
        elif choice == '2':
            insert_from_csv("contacts.csv")
        elif choice == '3':
            insert_from_console()
        elif choice == '4':
            show_all_contacts()
        elif choice == '5':
            search_by_name()
        elif choice == '6':
            search_by_phone_prefix()
        elif choice == '7':
            update_contact()
        elif choice == '8':
            delete_contact()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()