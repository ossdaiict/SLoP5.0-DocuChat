"""Logger placeholder"""

def get_logger(name=__name__):
    class Dummy:
        def info(self,*a,**k): pass
        def warning(self,*a,**k): pass
        def error(self,*a,**k): pass
    return Dummy()
