from datetime import datetime

import pandas as pd


def summarize_attendees(df):
    # Remove the last two rows
    df = df.iloc[:-2]

    total_attendees = len(df)
    total_paid = df['Order total'].sum()

    section_counts = df['Section'].value_counts().to_dict()
    total_players = sum(section_counts.values())
    section_order = ['Open', 'Section 1', 'Section 2', 'Section 3', 'Section 4', 'Section 5', 'Section 6']
    sorted_section_counts = sorted(section_counts.items(), key=lambda item: section_order.index(item[0]))
    section_data = {section: f"{count} ({count / total_players * 100:.1f}%)" for section, count in sorted_section_counts}

    junior_count = df['Ticket type'].value_counts().get('SquashVIC Junior Member', 0)
    adult_count = df['Ticket type'].value_counts().get('SquashVIC Adult Member', 0)

    # Prepare data for registration timeline line chart
    registration_counts = df['Registered on'].value_counts().sort_index()
    registration_df = pd.DataFrame({'Date': registration_counts.index, 'Count': registration_counts.values})

    # Prepare data for ticket type distribution bar chart
    ticket_type_counts = df['Ticket type'].value_counts().to_dict()
    ticket_type_df = pd.DataFrame(list(ticket_type_counts.items()), columns=["Ticket Type", "Count"])

    ages = []
    for dob_str in df['Date of birth']:
        try:
            if isinstance(dob_str, str) and dob_str:
                dob = datetime.strptime(dob_str, '%Y-%m-%d')
                today = datetime.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                ages.append(age)
        except ValueError:
            pass

    average_age = sum(ages) / len(ages) if ages else 0

    # Prepare data for age distribution bar chart
    age_counts = {}
    for age in ages:
        age_group = f"{age // 10 * 10}-{age // 10 * 10 + 9}"
        age_counts[age_group] = age_counts.get(age_group, 0) + 1
    age_df = pd.DataFrame(list(age_counts.items()), columns=["Age Group", "Count"])

    return {
        "total_attendees": total_attendees,
        "total_paid": total_paid,
        "section_data": section_data,
        "junior_count": junior_count,
        "adult_count": adult_count,
        "average_age": average_age,
        "age_df": age_df,
        "ticket_type_df": ticket_type_df,
        "registration_df": registration_df
    }