class BaseConnector:

    def __init__(self) -> None:
        pass

    def refresh(self):
        # Do a refresh
        pass
    
class ObjectStoreConnector(BaseConnector):

    def __init__(self) -> None:
        super().__init__()

class JDBCConnector(BaseConnector):

    def __init__(self) -> None:
        super().__init__()