class AssistantMemory:
    """
    A simple memory module for storing and retrieving previous question-response pairs.
    """

    def __init__(self):
        self.memory = {}

    def remember(self, query, response):
        """
        Stores a query-response pair in memory.
        """
        self.memory[query.strip().lower()] = response

    def recall(self, query):
        """
        Retrieves a stored response if the query is already in memory.
        """
        return self.memory.get(query.strip().lower(), None)

    def reset(self):
        """
        Clears the entire memory.
        """
        self.memory.clear()
