import time

from run_ingestion import run


while True:

    print(
        "Starting ingestion..."
    )

    run()

    print(
        "Sleeping for 1 hour..."
    )

    time.sleep(3600)