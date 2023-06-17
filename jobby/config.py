class Config:
    SCHEDULER_API_ENABLED = True

    JOBS = [
        {
            "id": "hello_world_job",
            "func": "jobby:jobs.hello",
            "args": (),
            "trigger": "interval",
            "seconds": 10,
        }
    ]