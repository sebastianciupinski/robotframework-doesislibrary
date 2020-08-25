from robot.libraries.BuiltIn import BuiltIn
import robot.libdocpkg
from robot.libdocpkg.builder import LibraryDocumentation
from robot.libdocpkg.consoleviewer import ConsoleViewer
import sys
import logging


is_kw_map = []
does_kw_map = []
does_not_kw_map = []
is_not_kw_map = []

        


class DoesIsListener:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 2
    
    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self

            
    def _start_suite(self, name, attributes):
        pass
        libs = BuiltIn().get_library_instance(all=True)
      
        for lib_name, library in libs.items():

        
            kw_list = []

            should_be_kw_list = []
            should_not_be_kw_list = []
            should_kw_list = []
            should_not_kw_list = []

            is_kw_list = []
            is_not_kw_list = []
            does_kw_list = []
            does_not_kw_list = []
            
        
            libdoc = LibraryDocumentation(lib_name)
            existing_keywords = KeywordsInformation(libdoc).get_kw_definition()


            for kw_name, kw_args in existing_keywords:
                kw_list.append((lib_name, kw_name, kw_args))


            for item in kw_list:
                if "Should Be" in item[1]:
                    should_be_kw_list.append((item[0], item[1], item[2]))
                    del(item)
                elif "Should Not Be" in item[1]:
                    should_not_be_kw_list.append((item[0], item[1], item[2]))
                    del(item)
                elif "Should Not" in item[1]:
                    should_not_kw_list.append((item[0], item[1], item[2]))
                    del(item)
                    pass
                elif "Should" in item[1]:
                    pass
                    should_kw_list.append((item[0], item[1], item[2]))
                    del(item)


            for libname, kw_name, kw_args in should_be_kw_list:
                old_kw_name = kw_name
                if kw_name.startswith("Should Be"):
                    new_kw_name = kw_name.replace("Should Be", "Is").strip().replace(" ", "_").replace("__", "_").lower()
                    is_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                else:
                    new_kw_name = "is_" + kw_name.replace("Should Be", "").strip().replace(" ", "_").replace("__", "_").lower()
                    is_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                    

            for libname, kw_name, kw_args in should_not_be_kw_list:
                old_kw_name = kw_name
                if kw_name.startswith("Should Not Be"):
                    new_kw_name = kw_name.replace("Should Not Be", "Is not").strip().replace(" ", "_").replace("__", "_").lower()
                    is_not_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                else:
                    new_kw_name = "is_" + kw_name.replace("Should Not Be", "not").strip().replace(" ", "_").replace("__", "_").lower()
                    is_not_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                    

            for libname, kw_name, kw_args in should_kw_list:
                old_kw_name = kw_name
                if kw_name.startswith("Should"):
                    new_kw_name = kw_name.replace("Should", "Does").strip().replace(" ", "_").replace("__", "_").lower()
                    does_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                else:
                    new_kw_name = "does_" + kw_name.replace("Should", "").strip().replace(" ", "_").replace("__", "_").lower()
                    does_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                    
          
            for libname, kw_name, kw_args in should_not_kw_list:
                old_kw_name = kw_name
                if kw_name.startswith("Should"):
                    new_kw_name = kw_name.replace("Should", "Does").strip().replace(" ", "_").replace("__", "_").lower()
                    does_not_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                else:
                    new_kw_name = "does_" + kw_name.replace("Should", "").strip().replace(" ", "_").replace("__", "_").lower()
                    does_not_kw_map.append((libname, new_kw_name, old_kw_name, kw_args))
                    

            def _make_method(name, library):
                def _method(*args):
                    invoked_kw = [tup for tup in is_kw_map if tup[1]==name][0][2]
                    method_name = invoked_kw.replace(" ", "_").lower()
                    arguments_list = [invoked_kw] + [*args]
                    status = BuiltIn().run_keyword_and_return_status(*arguments_list)
                    return status
                return _method
            

            for libname, new_kw_name, old_kw_name, kw_args in is_kw_map:
                if lib_name == libname:
                    _method = _make_method(new_kw_name, library)
                    setattr(library, new_kw_name, _method)
            
            BuiltIn().reload_library(lib_name)
            

    def _snake_to_camel(self, word):
        import re
        return (''.join(x.capitalize() + " " or '_' for x in word.split('_'))).strip()

    def list_is_keywords(self):
        is_kws = is_kw_map + is_not_kw_map
        for libname, new_kw, old_kw, args in is_kws:
            print('%-20s%-50s%-50s%-50s' % (libname, self._snake_to_camel(new_kw), old_kw, args))
        pass

    def list_does_keywords(self):
        does_kws = does_kw_map + does_not_kw_map
        for libname, new_kw, old_kw, args in does_kws:
            print('%-20s%-50s%-50s%-50s' % (libname, self._snake_to_camel(new_kw), old_kw, args))
        pass

class KeywordsInformation(ConsoleViewer):
    def get_kw_definition(self, *patterns):
        kws_def = []
        for kw in self._keywords.search('*%s*' % p for p in patterns):
            kw_info = kw.name, kw.args
            kws_def.append(kw_info)
        return kws_def
    pass





