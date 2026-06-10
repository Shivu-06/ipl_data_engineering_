from sqlalchemy import create_engine
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_to_mysql(matches, deliveries):

    engine = create_engine(
        "mysql+pymysql://shiva:1234@localhost/ipl_project"
    )

    try:

        matches.to_sql(
            "matches",
            con=engine,
            if_exists="replace",
            index=False
        )

        deliveries.to_sql(
            "deliveries",
            con=engine,
            if_exists="replace",
            index=False
        )

        logging.info(
            "Both tables loaded successfully!"
        )

    except Exception as e:

        logging.error(
            f"Error while loading data: {e}"
        )