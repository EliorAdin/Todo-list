def main_menu():
    while True:
        print("\n--- יומן משימות ---")
        print("1. הוספת משימה")
        print("2. עדכון משימה")
        print("3. מחיקת משימה")
        print("4. הצגת כל המשימות")
        print("5. חיפוש משימות לפי סטטוס")
        print("6. ייצוא משימות כ־JSON")
        print("7. יציאה")

        choice = input("בחר אפשרות: ")

        if choice == '1':
            title = input("כותרת המשימה: ")
            description = input("תיאור המשימה: ")
            start_date = input("תאריך התחלה (YYYY-MM-DD): ")
            end_date = input("תאריך סיום (YYYY-MM-DD): ")
            status = input("סטטוס (open/in_progress/completed): ")
            add_task(title, description, start_date, end_date, status)

        elif choice == '2':
            task_id = int(input("הכנס ID של המשימה לעדכון: "))
            print("מה ברצונך לעדכן?")
            print("1. סטטוס")
            print("2. תיאור")
            print("3. תאריכים")
            update_choice = input("בחר אפשרות: ")
            if update_choice == '1':
                new_status = input("סטטוס חדש: ")
                update_task(task_id, status=new_status)
            elif update_choice == '2':
                new_description = input("תיאור חדש: ")
                update_task(task_id, description=new_description)
            elif update_choice == '3':
                new_start = input("תאריך התחלה חדש (YYYY-MM-DD): ")
                new_end = input("תאריך סיום חדש (YYYY-MM-DD): ")
                update_task(task_id, start_date=new_start, end_date=new_end)
            else:
                print("בחירה לא תקינה.")

        elif choice == '3':
            task_id = int(input("הכנס ID של המשימה למחיקה: "))
            delete_task(task_id)

        elif choice == '4':
            list_tasks()

        elif choice == '5':
            status = input("הכנס סטטוס לחיפוש (open/in_progress/completed): ")
            find_tasks_by_status(status)

        elif choice == '6':
            export_tasks_to_json()

        elif choice == '7':
            print("להתראות!")
            break

        else:
            print("בחירה לא תקינה. נסה שוב.")


if __name__ == "__main__":
    main_menu()
