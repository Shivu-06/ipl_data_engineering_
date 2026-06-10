def clean_data(matches, deliveries):

    # Matches cleaning
    matches.drop(columns=['umpire3'],
                 inplace=True,
                 errors='ignore')

    matches['city'].fillna('Unknown',
                           inplace=True)

    matches.drop_duplicates(inplace=True)

    # Deliveries cleaning
    deliveries.drop_duplicates(inplace=True)

    deliveries.fillna(0, inplace=True)

    return matches, deliveries