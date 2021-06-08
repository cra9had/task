json_str = exec_statement("""
       import sys

       # exec_statement only captures stdout. If there are
       # errors, capture them to stdout so they can be displayed to the
       # user. Do this early, in case PyQt5 imports produce stderr
       # output.
       sys.stderr = sys.stdout

       import json
       from %s.QtCore import QLibraryInfo, QCoreApplication

       # QLibraryInfo isn't always valid until a QCoreApplication is
       # instantiated.
       app = QCoreApplication([])
       paths = [x for x in dir(QLibraryInfo) if x.endswith('Path')]
       location = {x: QLibraryInfo.location(getattr(QLibraryInfo, x))
                   for x in paths}
       try:
           version = QLibraryInfo.version().segments()
       except AttributeError:
           version = None
       print(str(json.dumps({
           'isDebugBuild': QLibraryInfo.isDebugBuild(),
           'version': version,
           'location': location,
       })))
   """ % self.namespace)
