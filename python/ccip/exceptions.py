class DataTransport:
    """
    An example of an object handling exceptinos foo different levels.
    """

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)
        except ConnectionError as e:
            logger.info("connection error detected: %s", e)
            raise
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e)
            raise

    def connect(self):
        for _ in range(self.retry_n_times):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info(
                    "%s: attempting new connection in %is",
                    e,
                    self.retry_threshold
                )
                time.sleep(self.retry_threshold)
            else:
                return self.connection
        raise ConnectionError(
            f"Couldn't connect after {self.retry_n_times} times"
        )

    def send(self, data):
        return self.connection.send(data)
