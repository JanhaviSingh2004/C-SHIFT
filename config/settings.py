CARBON_THRESHOLD = 400


CHECK_INTERVAL = 30   # seconds (for testing)


WORKLOADS = {
    "critical": ["analytics-job"],     # always run
    "medium": ["backup-job"],          # optional
    "heavy": ["ml-training"]           # stop first
}