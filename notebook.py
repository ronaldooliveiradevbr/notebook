from datetime import datetime

last_id = 0


class Note(object):
    """Represents a Note in the notebook. Match against
    a string in searches and store tags for each note.
    """

    def __init__(self, memo, tags=''):
        """Initializes a note with a memo and optional
        space-separated tags. Automatically set's a creation
        date and a unique id.
        """
        global last_id
        last_id += 1
        self.id = last_id
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.now()

    def match(self, query):
        """Determine if this note matches the query.
        Returns True if it matches, False otherwise.

        Search is case insensitive and matches both memo and tags.
        """
        return query in self.memo or query in self.tags
