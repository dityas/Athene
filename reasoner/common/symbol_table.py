import logging

logger=logging.getLogger(__name__)

class SymbolTable(object):

    def __init__(self):
        logger.debug("Initialised empty symbol table.")
        self.uuid_to_name={}
        self.name_to_uuid={}

    def add_to_table(self,name,uuid):
        '''
            Make a new lookup pair for name:uuid
        '''
        self.uuid_to_name[uuid]=name
        self.name_to_uuid[name]=uuid
        logger.debug(f"Name {name} with UUID {uuid} added to symbol table.")

    def get_name(self,uuid):
        '''
            Get name corrosponding to uuid. returns None if uuid does not
            exist.
        '''
        return self.uuid_to_name.setdefault(uuid)

    def get_uuid(self,name):
        '''
            Get uuid corrosponding to name. None if name does not exit.
        '''
        return self.name_to_uuid.setdefault(name)

    def debug(self):
        print(f"UUID to Name: {self.uuid_to_name}")
        print(f"Name to UUID: {self.name_to_uuid}")
