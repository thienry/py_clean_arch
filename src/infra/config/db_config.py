from sqlalchemy import create_engine, Engine


class DBConnectionHandler:
    """
    SQLAlchemy database connection.
    """

    def __int__(self):
        self.__connection_string = "sqlite://storage.db"
        self.session = None

    def get_engine(self) -> Engine:
        """
        Gets connection string.

        :returns: - Engine connection to database.
        """

        return create_engine(self.__connection_string)
