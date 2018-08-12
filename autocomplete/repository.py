import string
import datrie


class AppsRepository:
    def __init__(self, filepath):
        self.trie = datrie.Trie(string.ascii_letters + string.digits + string.whitespace)

        with open(filepath, 'r') as f:
            for line in f:
                # Remove new line and store app names in lower case to allow searching case insensitive
                self.trie[unicode(line.rstrip().lower())] = line.rstrip()

    def __contains__(self, key):
        return unicode(key) in self.trie

    def get(self, prefix):
        """
        Get all apps which names start with given prefix
        :param prefix: prefix
        :return:
        """
        if prefix:
            return self.trie.values(unicode(prefix.lower()))

        return self.trie.values()
