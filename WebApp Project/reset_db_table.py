from app import db, app
from app import EventReport  # Adjust the import path according to your project structure


def reset_event_report_table():
    with app.app_context():  # Ensures the function runs with your Flask app's context
        try:
            # Drop the table
            EventReport.__table__.drop(db.engine)
            print("EventReport table dropped.")

            # Recreate the table
            EventReport.__table__.create(db.engine)
            print("EventReport table created.")
        except Exception as e:
            print(f"Error occurred: {e}")


# Call the function
reset_event_report_table()
